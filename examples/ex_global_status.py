# Copyright (c) Crossbar.io Technologies GmbH, licensed under The MIT License (MIT)

from pprint import pformat
import asyncio

from crossbarfabricshell import client


async def main(session):
    """
    Connect to CFC, get system status and exit.
    """
    status = await session.call(u'crossbarfabriccenter.system.get_status')
    session.log.info('CFC system status:\n{status}', status=pformat(status))


if __name__ == '__main__':
    client.run(main)
