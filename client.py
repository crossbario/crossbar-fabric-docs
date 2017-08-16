# Copyright (c) Crossbar.io Technologies GmbH, licensed under The MIT License (MIT)

import six
import sys
import os
import argparse
import binascii
import pprint

import txaio
txaio.use_twisted()

from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
from twisted.internet.error import ReactorNotRunning

from autobahn.twisted.wamp import ApplicationSession
from autobahn.twisted.wamp import ApplicationRunner
from autobahn.twisted.util import sleep
from autobahn.wamp import cryptosign


class ManagementClientSession(ApplicationSession):

    def __init__(self, config=None):
        ApplicationSession.__init__(self, config)
        self._key = self.config.extra[u'key']

    def onConnect(self):
        self.log.info("connected to router")

        # authentication extra information for wamp-cryptosign
        extra = {
            # forward the client pubkey: this allows us to omit authid as
            # the router can identify us with the pubkey already
            u'pubkey': self._key.public_key(),
            u'trustroot': None,
            u'challenge': None,

            u'channel_binding': u'tls-unique'
        }

        # now request to join ..
        self.join(self.config.realm,
                  authmethods=[u'cryptosign'],
                  authid=self.config.extra.get(u'authid', None),
                  authrole=self.config.extra.get(u'authrole', None),
                  authextra=extra)

    def onChallenge(self, challenge):
        # sign the challenge with our private key.
        signed_challenge = self._key.sign_challenge(self, challenge)

        # send back the signed challenge for verification
        return signed_challenge

    @inlineCallbacks
    def onJoin(self, details):
        self.log.info("CFC session joined: {details}", details=details)
        try:
            main = self.config.extra.get(u'main', None)
            if main:
                return_code = yield main(self)
                self.config.extra[u'return_code'] = return_code
        except:
            # something bad happened: investigate your side or pls file an issue;)
            self.log.failure()
        finally:
            # in any case, shutdown orderly
            if not self._goodbye_sent:
                self.leave()

    def onLeave(self, details):
        self.log.info("CFC session closed: {details}", details=details)
        self.disconnect()

    def onDisconnect(self):
        try:
            reactor.stop()
        except ReactorNotRunning:
            pass


def run(main=None):
    # parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', dest='debug', action='store_true', default=False, help='Enable logging at level "debug".')
    parser.add_argument('--url', dest='url', type=six.text_type, default=u'wss://fabric.crossbario.com', help='The Crossbar.io Fabric Center (CFC) WebSocket URL (default: wss://fabric.crossbario.com')
    parser.add_argument('--realm', dest='realm', type=six.text_type, help='The management realm to join on CFC')
    parser.add_argument('--keyfile', dest='keyfile', type=six.text_type, default=u'~/.cbf/default.priv', help='The private client key file to use for authentication.')
    args = parser.parse_args()

    if args.debug:
        txaio.start_logging(level='debug')
    else:
        txaio.start_logging(level='info')

    # for authenticating the management client, we need a Ed25519 public/private key pair
    # here, we are reusing the user key - so this needs to exist before
    privkey_file = os.path.expanduser(args.keyfile)
    privkey_hex = None

    if not os.path.exists(privkey_file):
        raise Exception('private key file {} does not exist'.format(privkey_file))
    else:
        with open(privkey_file, 'r') as f:
            data = f.read()
            for line in data.splitlines():
                if line.startswith('private-key-ed25519'):
                    privkey_hex = line.split(':')[1].strip()

    if privkey_hex is None:
        raise Exception('no private key found in keyfile!')

    key = cryptosign.SigningKey.from_key_bytes(binascii.a2b_hex(privkey_hex))

    extra = {
        u'key': key,
        u'authid': u'tobias.oberstein@gmail.com',
        u'authrole': None,
        u'main': main,
        u'return_code': None
    }

    runner = ApplicationRunner(url=args.url, realm=args.realm, extra=extra)
    runner.run(ManagementClientSession)

    return_code = extra[u'return_code']
    if type(return_code) in six.integer_types and return_code != 0:
        sys.exit(return_code)


if __name__ == '__main__':
    run()
