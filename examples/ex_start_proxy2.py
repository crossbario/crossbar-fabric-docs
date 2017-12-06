# Copyright (c) Crossbar.io Technologies GmbH, licensed under The MIT License (MIT)

import asyncio
from os.path import expanduser

from autobahn.wamp.exception import ApplicationError
from autobahn.wamp import types
from autobahn.asyncio.component import Component

from crossbarfabricshell import client

def _load_privkey():
    with open(expanduser('~/.cbf/default.priv'), 'r') as f:
        for line in f.readlines():
            if ':' in line:
                (tag, val) = line.split(':', 1)
                if tag.strip() == 'private-key-ed25519':
                    return val.strip()
    return None
privkey_hex = _load_privkey()


PROXY_ID = u'my-proxy{}'

PROXY_OPTIONS = {
    # worker level options
}

TRANSPORT_ID = u'my-proxy{}-transport{}'

TRANSPORT_CONFIG = {
    u"type": u"websocket",
    u"endpoint": {
        u"type": u"tcp",
        u"port": None,  # replaced by code
    },
    # XXX hmm, I need auth: cryptosign here for some reason, but it's
    # not 'really' used?!
    u"auth": {
        "cryptosign": {
            "type": u"static",
            "principals": {
            },
#            "type": u"dynamic",
#            "authenticator": u"com.example.authenticate",
#            "authenticator-realm": u"realm-auth"
        }
    }
}


async def _test(reactor, session):
    print("transport_tester: joined: {}".format(session))
    await asyncio.sleep(1)

    def event(*args, **kw):
        print("transport_tester: got event {} {}".format(args, kw))
    sub = await session.subscribe(
        event, u"com.foo",
        options=types.SubscribeOptions(details_arg='details'),
    )
    print("transport_tester: sub {}".format(sub))
    await asyncio.sleep(1)

    pub = session.publish(
        u"com.foo", 1, 2, three=4,
        options=types.PublishOptions(exclude_me=False),
    )
    print("transport_tester: pub {}".format(pub))
    await asyncio.sleep(1)
    print("transport_tester: done sleeping, leaving")
    await session.leave()


async def test_proxy(session, node_id, proxy_id, port):
    print("\n\nTesting node '{}' proxy '{}' on port {}\n".format(node_id, proxy_id, port))
    transport_tester = Component(
        transports=u"ws://localhost:{}/ws".format(port),
        #realm=u"test2",
        realm=u"testrealm0",
        main=_test,
        authentication={
            u"ticket": {
                #u"ticket": "a secret ticket that's wrong",
                u"ticket": "a secret ticket",
            }
            # "cryptosign": {
            #     u"authid": u"meejah@gmail.com",
            #     u"authrole": u"owner",
            #     u"privkey": privkey_hex,
            # }
        }
    )
    try:
        await transport_tester.start()
    except Exception as e:
        print("\nTest failed: {}\n".format(e))
    else:
        # only can get here if our component "succeeded"; ran to the
        # end of on-join
        print("Successful connection to new transport")


async def main(session):
    # remember (container) workers we started
    workers_started = []
    proxy_transport_port = [8084]

    nodes = await session.call(u'crossbarfabriccenter.mrealm.get_nodes', status=u'online')
    if not nodes:
        print("No nodes")
        return

    for node_id in nodes:
        print("Starting proxies on '{}'".format(node_id))

        workers = await session.call(u'crossbarfabriccenter.remote.node.get_workers', node_id)
        for proxy_id in [PROXY_ID.format(i) for i in range(2)]:

            # stop any worker running with our worker ID
            if proxy_id in workers:
                print("Stopping '{}' on '{}'".format(proxy_id, node_id))
                worker_stopped = await session.call(
                    u'crossbarfabriccenter.remote.node.stop_worker',
                    node_id,
                    proxy_id,
                )
                session.log.info('Worker {worker_id} stopped: {worker_stopped}',
                                  worker_id=proxy_id, worker_stopped=worker_stopped)

            # now actually start a new proxy worker
            worker_started = await session.call(
                u'crossbarfabriccenter.remote.node.start_worker',
                node_id,
                proxy_id,
                u'proxy',
                PROXY_OPTIONS,
            )

            from copy import copy
            cfg = copy(TRANSPORT_CONFIG)
            cfg['endpoint']['port'] = proxy_transport_port[0]
            transport_started = await session.call(
                u"crossbarfabriccenter.node.{}.worker.{}.start_proxy_transport".format(node_id, proxy_id),
                TRANSPORT_ID.format(proxy_id, 0),
                cfg,
            )
            print("transport: {}".format(transport_started))
            proxy_transport_port[0] += 1

            backend_started = await session.call(
                u"crossbarfabriccenter.node.{}.worker.{}.start_proxy_backend".format(node_id, proxy_id),
                u"backend0",
                {
                    u"type": u"class",
                    u"classname": u"myapp.MySession2",
                    u"realm": u"realm1",
                    u"transport": {
                        u"type": u"rawsocket",
                        u"serializer": [u"cbor"],
                        u"endpoint": {
                            u"type": u"tcp",
                            u"host": u"localhost",
                            u"port": 9999
                        },
                        u"auth": {
                            u"cryptosign": {
                                u"authid": u"meejah@gmail.com",
                                u"authrole": u"testrealm0",
                                u"privkey": privkey_hex
                            },
                            u"ticket": {
                                u"type": u"static",
                                u"principals": {
                                    u"meejah@gmail.com": {
                                        u"ticket": "a secret ticket",
                                        u"role": u"testrealm0",
                                    }
                                }
                            }
                        }
                    }
                }
            )
            print("backend: {}".format(backend_started))
            workers_started.append((node_id, proxy_id))

            session.log.info('Node "{node_id}" / Worker "{worker_id}" started: {worker_started}',
                             node_id=node_id, worker_id=proxy_id, worker_started=worker_started)

    session.log.info('sleeping ..')
    base = 8084
    for i, (node_id, proxy_id) in enumerate(workers_started):
        await test_proxy(session, node_id, proxy_id, base + i)
    await asyncio.sleep(5)

    # stop everything ..
    if True:
        for node_id, worker_id in workers_started:

            # .. stopping the whole worker
            try:
                worker_stopped = await session.call(u'crossbarfabriccenter.remote.worker.shutdown',
                                                    node_id,
                                                    worker_id)

            # FIXME: remove this once the respective CF bug is fixed
            except ApplicationError as e:
                if e.error == u'wamp.error.canceled':
                    worker_stopped = None
                else:
                    raise

            session.log.info('Worker {worker_id} stopped: {worker_stopped}',
                             worker_stopped=worker_stopped, worker_id=worker_id)


if __name__ == '__main__':
    client.run(main)
