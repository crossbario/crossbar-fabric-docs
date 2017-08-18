# Copyright (c) Crossbar.io Technologies GmbH, licensed under The MIT License (MIT)

import pprint
import itertools

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
def _remote_root(uri):
    s = u'crossbarfabriccenter.node.{{node_id}}.worker.{{worker_id}}.realm.{{realm}}.root.{uri}'.format(uri=uri)
    def _fun(node_id, worker_id, realm):
        return s.format(node_id=node_id, worker_id=worker_id, realm=realm)
    return _fun

GET_SESSIONS = _remote_root(u'wamp.session.list')
GET_SESSION = _remote_root(u'wamp.session.get')

GET_SUBSCRIPTIONS = _remote_root(u'wamp.subscription.list')
GET_SUBSCRIPTION = _remote_root(u'wamp.subscription.get')


GET_REGISTRATIONS = _remote_root(u'wamp.registration.list')
GET_REGISTRATION = _remote_root(u'wamp.registration.get')

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

@inlineCallbacks
def main(session):
    """
    Iterate over all nodes, and all workers on each nodes to retrieve and
    print worker information. then exit.
    """
    verbose = True

    regs_out = {}
    subs_out = {}

    nodes = yield session.call(GET_NODES)
    print('nodes: {}'.format(nodes))
    for node_id in nodes:
        workers = yield session.call(GET_WORKERS, node_id)
        print('  workers on node {}: {}'.format(node_id, workers))
        for worker_id in workers:
            worker = yield session.call(GET_WORKER, node_id, worker_id)
            if worker[u'type'] == u'router':
                realms = yield session.call(GET_ROUTER_REALMS, node_id, worker_id)
                print('    realms on worker {}: {}'.format(worker_id, realms))
                for realm in realms:
                    sessions = yield session.call(GET_SESSIONS(node_id, worker_id, realm))
                    print('        sessions on realm {}: {}'.format(realm, sessions))
                    for session_id in sessions:

                        subscriptions = yield session.call(GET_SUBSCRIPTIONS(node_id, worker_id, realm), session_id)
                        sub_ids = list(itertools.chain(*subscriptions.values()))
                        print('          subscriptions on session {}: {}'.format(session_id, sub_ids))

                        if verbose:
                            for sub_type, sub_ids in subscriptions.items():
                                for sub_id in sub_ids:
                                    if sub_id not in subs_out:
                                        sub = yield session.call(GET_SUBSCRIPTION(node_id, worker_id, realm), sub_id)
                                        subs_out[sub_id] = sub

                        registrations = yield session.call(GET_REGISTRATIONS(node_id, worker_id, realm), session_id)
                        reg_ids = list(itertools.chain(*registrations.values()))
                        print('          registrations on session {}: {}'.format(session_id, reg_ids))

                        if verbose:
                            for reg_type, reg_ids in registrations.items():
                                for reg_id in reg_ids:
                                    if reg_id not in regs_out:
                                        reg = yield session.call(GET_REGISTRATION(node_id, worker_id, realm), reg_id)
                                        regs_out[reg_id] = reg

    if verbose:
        print('\nsubscriptions retrieved:\n')
        for sub in subs_out.values():
            pprint.pprint(sub)

        print('\nregistrations retrieved:\n')
        for reg in regs_out.values():
            pprint.pprint(reg)


if __name__ == '__main__':
    client.run(main)
