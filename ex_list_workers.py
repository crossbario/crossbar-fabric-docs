# Copyright (c) Crossbar.io Technologies GmbH, licensed under The MIT License (MIT)

from twisted.internet.defer import inlineCallbacks, returnValue

import client


@inlineCallbacks
def main(session):
    """
    Iterate over all nodes, and all workers on each nodes to retrieve and
    print worker information. then exit.
    """
    nodes = yield session.call(u'crossbarfabriccenter.get_nodes')
    for node_id in nodes:
        workers = yield session.call(u'crossbarfabriccenter.remote.get_workers', node_id)
        for worker_id in workers:
            worker = yield session.call(u'crossbarfabriccenter.remote.get_worker', node_id, worker_id)
            session.log.info('Node "{node_id}" / Worker "{worker_id}": {worker}', node_id=node_id, worker_id=worker_id, worker=worker)


if __name__ == '__main__':
    client.run(main)
