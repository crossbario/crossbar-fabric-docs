# Copyright (c) Crossbar.io Technologies GmbH, licensed under The MIT License (MIT)

import pprint

from twisted.internet.defer import inlineCallbacks

import client

GET_NODES = u'crossbarfabriccenter.get_nodes'

GET_WORKERS = u'crossbarfabriccenter.remote.get_workers'
GET_WORKER = u'crossbarfabriccenter.remote.get_worker'
GET_ROUTER_REALMS = u'crossbarfabriccenter.remote.get_router_realms'

GET_SESSIONS = u'crossbarfabriccenter.node.{node_id}.worker.{worker_id}.realm.{realm}.wamp.session.list'
GET_SESSION = u'crossbarfabriccenter.node.{node_id}.worker.{worker_id}.realm.{realm}.wamp.session.get'


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
                    sessions = yield session.call(GET_SESSIONS.format(node_id=node_id, worker_id=worker_id, realm=realm))
                    print('node "{}" / router "{}" / realm "{}" has currently {} sessions connected: {}'.format(realm, node_id, worker_id, len(sessions), sessions))
                    for session_id in sessions:
                        session_info = yield session.call(GET_SESSION.format(node_id=node_id, worker_id=worker_id, realm=realm), session_id)
                        if verbose:
                            pprint.pprint(session_info)


if __name__ == '__main__':
    client.run(main)
