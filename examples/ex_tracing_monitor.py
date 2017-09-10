# Copyright (c) Crossbar.io Technologies GmbH, licensed under The MIT License (MIT)

import pprint
import asyncio

from crossbarfabricshell import client


async def main(session):
    """
    Subscribe to all tracing related topics to monitor tracing on any node/worker.
    """
    def on_trace_started(node_id, worker_id, trace_id, trace_started):
        session.log.info('Trace "{trace_id}" started on node "{node_id}" / worker "{worker_id}":\n{trace_started}',
                         node_id=node_id, worker_id=worker_id, trace_id=trace_id,
                         trace_started=pprint.pformat(trace_started))

    await session.subscribe(on_trace_started, u'crossbarfabriccenter.remote.tracing.on_trace_started',)

    def on_trace_stopped(node_id, worker_id, trace_id, trace_stopped):
        session.log.info('Trace "{trace_id}" stopped on node "{node_id}" / worker "{worker_id}":\n{trace_stopped}',
                         node_id=node_id, worker_id=worker_id, trace_id=trace_id,
                         trace_stopped=pprint.pformat(trace_stopped))

    await session.subscribe(on_trace_stopped, u'crossbarfabriccenter.remote.tracing.on_trace_stopped',)

    monitor_time = 600
    session.log.info('ok, subscribed to tracing events - now sleeping for {monitor_time} secs ..',
                     monitor_time=monitor_time)
    await asyncio.sleep(monitor_time)


if __name__ == '__main__':
    client.run(main)
