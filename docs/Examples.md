title: Examples
toc: [Documentation, Examples]

# Crossbar.io Fabric Examples

This repository contains example code for programming against the Crossbar.io Fabric Center (CFC) API to remotely manage and monitor your Crossbar.io Fabric (CF) nodes connected to CFC.

## Status

This example demonstrates how  to connect to CFC and retrieve status. That's it. It is the "most basic example".

* [ex_status.py](../examples/ex_status.py)

The APIs covered:

* [crossbarfabriccenter.mrealm.get_status](Management-API.md#crossbarfabriccentermrealmget_status)


## Listing workers

This example demonstrates how to iterate over the (currently connected) CF nodes, and on each node, iterate over the currently running workers to retrieve worker information.

* [ex_list_workers.py](../examples/ex_list_workers.py)

The APIs covered:

* [crossbarfabriccenter.mrealm.get_nodes](Management-API.md#crossbarfabriccentermrealmget_nodes)
* [crossbarfabriccenter.remote.node.get_workers](Management-API.md#crossbarfabriccenterremotenodeget_workers)
* [crossbarfabriccenter.remote.node.get_worker](Management-API.md#crossbarfabriccenterremotenodeget_worker)


## Listing Sessions

The APIs covered:

* `crossbarfabriccenter.remote.root.*`


## Tracing

Crossbar.io Fabric has an message tracing extensions built into the routing core of Crossbar.io.

This allows to tap into the feeds of WAMP messages flowing through the routing core - in real-time.

The example will iterate over all router workers on all CF nodes, stop all traces (if any), and start a new trace on each router worker. It will run the trace for 10s, stop the traces and retrieve tracing data collected during the trace.

* [ex_trace_10s.py](../examples/ex_trace_10s.py)

The APIs covered:

* `crossbarfabriccenter.remote.get_router_traces`
* `crossbarfabriccenter.remote.get_router_trace`
* `crossbarfabriccenter.remote.start_router_trace`
* `crossbarfabriccenter.remote.stop_router_trace`
* `crossbarfabriccenter.remote.get_router_trace_data`
