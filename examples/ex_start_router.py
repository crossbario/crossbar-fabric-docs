# Copyright (c) Crossbar.io Technologies GmbH, licensed under The MIT License (MIT)

import asyncio

from crossbarfabricshell import client

WORKER_ID = u'my-worker1'

REALM_ID = u'my-realm1'

REALM_CONFIG = {
    u'name': u'realm1'
}

ROLE_ID = u'my-role1'

ROLE_CONFIG = {
    u"name": u"anonymous",
    u"permissions": [
        {
            u"uri": u"",
            u"match": u"prefix",
            u"allow": {
                u"call": True,
                u"register": True,
                u"publish": True,
                u"subscribe": True,
            },
            u"disclose": {
                u"caller": False,
                u"publisher": False
            },
            u"cache": True
        }
    ]
}

TRANSPORT_ID = u'my-transport1'

TRANSPORT_CONFIG = {
    u'type': u'websocket',
    u'endpoint': {
        u'type': u'tcp',
        u'port': 8000
    }
}

async def main(session):
    """
    Start a router worker on each node, with a realm and a role. Then stop everything again.
    """
    try:
        # remember (router) workers we started
        workers_started = []

        nodes = await session.call(u'crossbarfabriccenter.mrealm.get_nodes', status=u'online')
        for node_id in nodes:

            workers = await session.call(u'crossbarfabriccenter.remote.node.get_workers', node_id)
            if WORKER_ID in workers:
                worker_stopped = await session.call(u'crossbarfabriccenter.remote.worker.shutdown', node_id, WORKER_ID)
                #worker_stopped = await session.call(u'crossbarfabriccenter.remote.node.stop_worker', node_id, WORKER_ID)
                session.log.info('Worker {worker_id} stopped: {worker_stopped}', worker_id=WORKER_ID, worker_stopped=worker_stopped)

            worker_started = await session.call(u'crossbarfabriccenter.remote.node.start_worker',
                                                node_id, WORKER_ID, u'router')

            workers_started.append((node_id, WORKER_ID))

            session.log.info('Node "{node_id}" / Worker "{worker_id}" started: {worker_started}', node_id=node_id, worker_id=WORKER_ID, worker_started=worker_started)

            realm_started = await session.call(u'crossbarfabriccenter.remote.router.start_router_realm', node_id, WORKER_ID, REALM_ID, REALM_CONFIG)

            session.log.info('Realm started: {realm_started}', realm_started=realm_started)

            role_started = await session.call(u'crossbarfabriccenter.remote.router.start_router_realm_role', node_id, WORKER_ID, REALM_ID, ROLE_ID, ROLE_CONFIG)
            session.log.info('Role started: {role_started}', role_started=role_started)

            transport_started = await session.call(u'crossbarfabriccenter.remote.router.start_router_transport', node_id, WORKER_ID, TRANSPORT_ID, TRANSPORT_CONFIG)
            session.log.info('Transport started: {transport_started}', transport_started=transport_started)

            TRANSPORT_CONFIG[u'endpoint'][u'port'] += 1

        session.log.info('sleeping ..')
        await asyncio.sleep(5)

        # stop all the router transports we started
        for node_id, worker_id in workers_started:

            role_stopped = await session.call(u'crossbarfabriccenter.remote.router.stop_router_realm_role', node_id, WORKER_ID, REALM_ID, ROLE_ID)
            session.log.info('Role stopped: {role_stopped}', role_stopped=role_stopped)

            realm_stopped = await session.call(u'crossbarfabriccenter.remote.router.stop_router_realm', node_id, WORKER_ID, REALM_ID)
            session.log.info('Realm stopped: {realm_stopped}', realm_stopped=realm_stopped)

            transport_stopped = await session.call(u'crossbarfabriccenter.remote.router.stop_router_transport', node_id, worker_id, TRANSPORT_ID)
            session.log.info('Transport {transport_id} on worker {worker_id} ({node_id}) stopped: {transport_stopped}', transport_stopped=transport_stopped, node_id=node_id, worker_id=worker_id, transport_id=TRANSPORT_ID)

            worker_stopped = await session.call(u'crossbarfabriccenter.remote.worker.shutdown', node_id, worker_id)
            session.log.info('Worker {worker_id} stopped: {worker_stopped}', worker_stopped=worker_stopped, worker_id=worker_id)

    except Exception as e:
        print('fatal: {}'.format(e))


if __name__ == '__main__':
    client.run(main)
