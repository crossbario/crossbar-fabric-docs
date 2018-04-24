# Copyright (c) Crossbar.io Technologies GmbH, licensed under The MIT License (MIT)

from pprint import pformat

from cbsh import client

CLUSTER_ID = u'cluster1'
CLUSTER_NODES = ['cf1', 'cf2', 'cf3']


async def main(session):
    clusters = await session.call(u'crossbarfabriccenter.mrealm.clustering.wsrp.list')
    if CLUSTER_ID not in clusters:
        cluster_created = await session.call(u'crossbarfabriccenter.mrealm.clustering.wsrp.create', CLUSTER_ID, {})
        session.log.info('cluster "{cluster_id}" created: {cluster_created}',
                         cluster_id=CLUSTER_ID,
                         cluster_created=cluster_created)
    else:
        session.log.info('cluster "{cluster_id}" already existing',
                         cluster_id=CLUSTER_ID)

    cluster = await session.call(u'crossbarfabriccenter.mrealm.clustering.wsrp.get', CLUSTER_ID)
    print(cluster)

    nodes_online = await session.call(u'crossbarfabriccenter.mrealm.get_nodes', status=u'online')
    for node_id in CLUSTER_NODES:
        if node_id in nodes_online:
            session.log.info('node "{node_id}" is part of cluster and is online.',
                             node_id=node_id)

            frontend_id = u'{}-{}'.format(CLUSTER_ID, node_id)
            frontend_config = {}
            if frontend_id not in cluster[u'frontends']:
                session.log.info('frontend "{frontend_id}" does not exist - addin!',
                                 frontend_id=frontend_id)

                frontend_added = await session.call(u'crossbarfabriccenter.mrealm.clustering.wsrp.add_frontend',
                                                    CLUSTER_ID,
                                                    frontend_id,
                                                    frontend_config)
            else:
                session.log.info('frontend "{frontend_id}" already exists - skipping',
                                 frontend_id=frontend_id)

        else:
            session.log.warn('node "{node_id}" is part of cluster but is NOT online!',
                             node_id=node_id)

    frontend = await session.call(u'crossbarfabriccenter.mrealm.clustering.wsrp.deploy_changes',
                                  CLUSTER_ID)


if __name__ == '__main__':
    client.run(main)
