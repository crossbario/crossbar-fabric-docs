# Copyright (c) Crossbar.io Technologies GmbH, licensed under The MIT License (MIT)

import pprint

from twisted.internet.defer import inlineCallbacks

import client

GET_NODES = u'crossbarfabriccenter.get_nodes'

GET_WORKERS = u'crossbarfabriccenter.remote.get_workers'
GET_WORKER = u'crossbarfabriccenter.remote.get_worker'
GET_ROUTER_REALMS = u'crossbarfabriccenter.remote.get_router_realms'

# the following requires options.bridge_meta_api=true in the options
# of the Crossbar.io router realm called into. it might also require elevated
# rights on CFC for authorization on the URIs
#
# these URIs access the WAMP meta API within Crossbar.io router realms and behave
# exactly the same as a WAMP client locally attached to the respective app router
# would see.
#
def _remote(uri):
    s = u'crossbarfabriccenter.node.{{node_id}}.worker.{{worker_id}}.realm.{{realm}}.root.{uri}'.format(uri=uri)
    def _fun(node_id, worker_id, realm):
        return s.format(node_id=node_id, worker_id=worker_id, realm=realm)
    return _fun

GET_SESSIONS = _remote(u'wamp.session.list')
GET_SESSION = _remote(u'wamp.session.get')


@inlineCallbacks
def main(session):
    """
    Iterate over all nodes, and all workers on each nodes to retrieve and
    print worker information. then exit.
    """
    verbose = True
    nodes = yield session.call(GET_NODES)
    for node_id in nodes:
        workers = yield session.call(GET_WORKERS, node_id)
        for worker_id in workers:
            worker = yield session.call(GET_WORKER, node_id, worker_id)
            if worker[u'type'] == u'router':
                realms = yield session.call(GET_ROUTER_REALMS, node_id, worker_id)
                for realm in realms:
                    sessions = yield session.call(GET_SESSIONS(node_id, worker_id, realm))
                    print('node "{}" / router "{}" / realm "{}" has currently {} sessions connected: {}'.format(realm, node_id, worker_id, len(sessions), sessions))
                    for session_id in sessions:
                        session_info = yield session.call(GET_SESSION(node_id, worker_id, realm), session_id)
                        if verbose:
                            pprint.pprint(session_info)


if __name__ == '__main__':
    client.run(main)
