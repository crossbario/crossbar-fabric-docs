# Copyright (c) Crossbar.io Technologies GmbH, licensed under The MIT License (MIT)

import pprint

from twisted.internet.defer import inlineCallbacks, returnValue

from autobahn.twisted.util import sleep

import client


@inlineCallbacks
def main(session):
    """
    Connect to CFC, get status and exit.

    This is about the most basic example possible. You can copy this
    example and add your CFC calls, reuse the example driver (client.py)
    and get started super quickly.
    """
    session.log.info('running main() ...')
    return_code = 0
    try:
        status = yield session.call(u'crossbarfabriccenter.get_status')
        session.log.info('CFC status: {status}', status=status)
    except:
        # something bad happened: investigate your side or pls file an issue;)
        return_code = -1
        session.log.failure()
    finally:
        # in any case, shutdown orderly
        session.leave()

    returnValue(return_code)


if __name__ == '__main__':
    client.run(main)
