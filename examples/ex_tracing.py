# Copyright (c) Crossbar.io Technologies GmbH, licensed under The MIT License (MIT)

import pprint
import asyncio

from crossbarfabricshell import client


async def main(session):
    """
    Iterate over all nodes, and all workers on each nodes to retrieve and
    print worker information. then exit.
    """
    # stop currently running traces upon startup ?
    stop_running = True
    started_traces = []

    # iterate over nodes, over (router) workers, and traces:
    nodes = await session.call(u'crossbarfabriccenter.mrealm.get_nodes')
    for node_id in nodes:
        workers = await session.call(u'crossbarfabriccenter.remote.node.get_workers', node_id)
        session.log.info('Node "{node_id}" is running these workers: {workers}', node_id=node_id,
                         workers=workers)

        # iterate over workers on node
        for worker_id in workers:
            worker = await session.call(u'crossbarfabriccenter.remote.node.get_worker', node_id,
                                        worker_id)
            session.log.info('Worker "{worker_id}": {worker}', worker_id=worker_id, worker=worker)

            # if this is a router worker, ..
            if worker[u'type'] == u'router':
                # get traces currently running on node/worker ...
                traces = await session.call(
                    u'crossbarfabriccenter.remote.tracing.get_router_traces', node_id, worker_id)
                session.log.info('Worker "{worker_id}" is running these traces: {traces}',
                                 worker_id=worker_id, traces=traces)

                # .. and iterate over traces
                for trace_id in traces:
                    trace = await session.call(
                        u'crossbarfabriccenter.remote.tracing.get_router_trace', node_id,
                        worker_id, trace_id)
                    session.log.info('Trace "{trace_id}": {trace}', trace_id=trace_id, trace=trace)

                    # if asked to stop running traces, stop the trace!
                    if stop_running and trace[u'status'] == u'running':
                        # stop the trace
                        stopped = await session.call(
                            u'crossbarfabriccenter.remote.tracing.stop_router_trace', node_id,
                            worker_id, trace_id)

                # start a new trace ..
                trace_id = u'trace-001'
                trace_options = {}
                trace = await session.call(
                    u'crossbarfabriccenter.remote.tracing.start_router_trace', node_id, worker_id,
                    trace_id, trace_options=trace_options)
                started_traces.append((node_id, worker_id, trace_id))
                session.log.info(
                    'Trace "{trace_id} on node "{node_id}" / worker "{worker_id}" started with options: {trace_options}"',
                    node_id=node_id, worker_id=worker_id, trace_id=trace_id,
                    trace_options=trace_options)

    trace_time = 2
    session.log.info('Ok, traces started: {started_traces}\nNow tracing for {trace_time} secs ..',
                     started_traces=started_traces, trace_time=trace_time)
    await asyncio.sleep(trace_time)

    # stop traces and print traced data ..
    for node_id, worker_id, trace_id in started_traces:
        trace_data = await session.call(
            u'crossbarfabriccenter.remote.tracing.get_router_trace_data', node_id, worker_id,
            trace_id, 0)
        stopped = await session.call(u'crossbarfabriccenter.remote.tracing.stop_router_trace',
                                     node_id, worker_id, trace_id)
        session.log.info('Trace data for "{trace_id}" on "{node_id}/{worker_id}":\n{trace_data}',
                         node_id=node_id, worker_id=worker_id, trace_id=trace_id,
                         trace_data=pprint.pformat(trace_data))


if __name__ == '__main__':
    client.run(main)
