# Copyright (c) Crossbar.io Technologies GmbH, licensed under The MIT License (MIT)

from crossbarfabricshell import client


async def main(session):
    """
    Connect to CFC, get status and exit.

    This is about the most basic example possible. You can copy this
    example and add your CFC calls, reuse the example driver (client.py)
    and get started super quickly.
    """
    status = await session.call(u'crossbarfabriccenter.mrealm.get_status')
    session.log.info('CFC status: {status}', status=status)


if __name__ == '__main__':
    client.run(main)
