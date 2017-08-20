# Copyright (c) Crossbar.io Technologies GmbH, licensed under The MIT License (MIT)

import pprint

import client

GET_NODES = u'crossbarfabriccenter.get_nodes'

GET_WORKERS = u'crossbarfabriccenter.remote.node.get_workers'
GET_WORKER = u'crossbarfabriccenter.remote.node.get_worker'
GET_ROUTER_REALMS = u'crossbarfabriccenter.remote.router.get_router_realms'

# the following requires options.bridge_meta_api=true in the options
# of the Crossbar.io router realm called into. it might also require elevated
# rights on CFC for authorization on the URIs
#
# these URIs access the WAMP meta API within Crossbar.io router realms and behave
# exactly the same as a WAMP client locally attached to the respective app router
# would see.
#


def _remote_root(uri):
    s = u'crossbarfabriccenter.node.{{node_id}}.worker.{{worker_id}}.realm.{{realm}}.root.{uri}'.format(uri=uri)

    def _fun(node_id, worker_id, realm):
        return s.format(node_id=node_id, worker_id=worker_id, realm=realm)
    return _fun

GET_SESSIONS = _remote_root(u'wamp.session.list')
GET_SESSION = _remote_root(u'wamp.session.get')


#GET_SESSIONS = u'crossbarfabriccenter.remote.realm.wamp.session.list'
#GET_SESSION = u'crossbarfabriccenter.remote.realm.wamp.session.get'


# ideal for an embedded router component: thin layer of API transformation:
#
#
# prefix registration on "crossbarfabriccenter.remote.realm." that translates as this:
#
#  - crossbarfabriccenter.remote.realm.{uri:string}(node_id, worker_id, realm_id, *args, details=None, **kwargs)
#      =>
#  - crossbarfabriccenter.node.{node_id:string}.worker.{worker_id:string}.realm.{realm_id:string}.root.{uri:string}(*args, **kwargs)
#
#
# prefix subscription to "crossbarfabriccenter.node." that translates as this:
#
#  - crossbarfabriccenter.node.{node_id:string}.worker.{worker_id:string}.realm.{realm_id:string}.root.{uri:string}(*args, **kwargs)
#     =>
#  - crossbarfabricenter.remote.realm.{uri:string}(node_id, worker_id, realm_id, *args, **kwargs)


async def main(session):
    """
    Iterate over all nodes, and all workers on each nodes to retrieve and
    print worker information. then exit.
    """
    verbose = True
    nodes = await session.call(GET_NODES)
    for node_id in nodes:
        workers = await session.call(GET_WORKERS, node_id)
        for worker_id in workers:
            worker = await session.call(GET_WORKER, node_id, worker_id)
            if worker[u'type'] == u'router':
                realms = await session.call(GET_ROUTER_REALMS, node_id, worker_id)
                for realm in realms:
                    sessions = await session.call(GET_SESSIONS(node_id, worker_id, realm))
                    print('node "{}" / router "{}" / realm "{}" has currently {} sessions connected: {}'.format(realm, node_id, worker_id, len(sessions), sessions))
                    for session_id in sessions:
                        session_info = await session.call(GET_SESSION(node_id, worker_id, realm), session_id)
                        if verbose:
                            pprint.pprint(session_info)


if __name__ == '__main__':
    client.run(main)
