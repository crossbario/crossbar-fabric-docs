title: Examples
toc: [Documentation, Examples]

# Crossbar.io Fabric Examples

This repository contains example code for programming against the Crossbar.io Fabric Center (CFC) API to remotely manage and monitor your Crossbar.io Fabric (CF) nodes connected to CFC.

**Examples:**

* [Get Status](#get-status)
* [Listing Workers](#listing-workers)
* [Starting Routers](#starting-routers)
* [Listing Sessions](#listing-sessions)
* [Listing Registrations and Subscriptions](#listing-registrations-and-subscriptions)
* [Worker CPU Affinity](#worker-cpu-affinity)
* [Process Statistics](#process-statistics)
* [Worker Logs](#worker-logs)
* [Message Tracing](#message-tracing)

---


## Get Status

This example demonstrates how  to connect to CFC and retrieve status. That's it. It is the "most basic example".

* [ex_status.py](../examples/ex_status.py)

APIs covered:

* [crossbarfabriccenter.mrealm.get_status](Management-API.md#crossbarfabriccentermrealmget_status)

---


## Listing workers

This example demonstrates how to iterate over the (currently connected) CF nodes, and on each node, iterate over the currently running workers to retrieve worker information.

* [ex_list_workers.py](../examples/ex_list_workers.py)

APIs covered:

* [crossbarfabriccenter.mrealm.get_nodes](Management-API.md#crossbarfabriccentermrealmget_nodes)
* [crossbarfabriccenter.remote.node.get_workers](Management-API.md#crossbarfabriccenterremotenodeget_workers)
* [crossbarfabriccenter.remote.node.get_worker](Management-API.md#crossbarfabriccenterremotenodeget_worker)

---


## Starting Routers

This example demonstrates how to dynamically start a new router worker on a node, start a realm and a role on the router and finally start a listening transport so the router will accept incoming WAMP connections.

* [ex_start_router.py](../examples/ex_start_router.py)

APIs covered:

* [crossbarfabriccenter.remote.worker.shutdown](Management-API.md#crossbarfabriccenterremoteworkershutdown)
* [crossbarfabriccenter.remote.node.start_worker](Management-API.md#crossbarfabriccenterremotenodestart_worker)
* [crossbarfabriccenter.remote.node.stop_worker](Management-API.md#crossbarfabriccenterremotenodestop_worker)
* [crossbarfabriccenter.remote.router.start_router_realm](Management-API.md#crossbarfabriccenterremoterouterstart_router_realm)
* [crossbarfabriccenter.remote.router.stop_router_realm](Management-API.md#crossbarfabriccenterremoterouterstop_router_realm)
* [crossbarfabriccenter.remote.router.start_router_realm_role](Management-API.md#crossbarfabriccenterremoterouterstart_router_realm_role)
* [crossbarfabriccenter.remote.router.stop_router_realm_role](Management-API.md#crossbarfabriccenterremoterouterstop_router_realm_role)
* [crossbarfabriccenter.remote.router.start_router_transport](Management-API.md#crossbarfabriccenterremoterouterstart_router_transport)
* [crossbarfabriccenter.remote.router.stop_router_transport](Management-API.md#crossbarfabriccenterremoterouterstop_router_transport)

---


## Listing Sessions

The example demonstrates listing of WAMP sessions currently joined on router realms running on CF nodes connected to CFC.

* [ex_list_sessions.py](../examples/ex_list_sessions.py)

This is using the [Remote Realm WAMP meta API](Management-API.md#remote-realm-wamp-meta-api)

The APIs covered:

* [crossbarfabriccenter.remote.realm.meta.*](Management-API.md#crossbarfabriccenterremoterealmmeta)

---


## Listing Registrations and Subscriptions

The example demonstrates listing of WAMP subscriptions and registrations currently active for WAMP sessions on router realms running on CF nodes connected to CFC.

* [ex_list_subs_regs.py](../examples/ex_list_subs_regs.py)

This is using the [Remote Realm WAMP meta API](Management-API.md#remote-realm-wamp-meta-api)

The APIs covered:

* [crossbarfabriccenter.remote.realm.meta.*](Management-API.md#crossbarfabriccenterremoterealmmeta)

---


## Worker CPU Affinity

Demonstrates getting/setting the CPU affinity set of CF workers.

* [ex_cpu_affinity.py](../examples/ex_cpu_affinity.py)

APIs covered:

* [crossbarfabriccenter.remote.node.get_cpu_count](Management-API.md#crossbarfabriccenterremotenodeget_cpu_count)
* [crossbarfabriccenter.remote.node.get_cpu_affinity](Management-API.md#crossbarfabriccenterremotenodeget_cpu_affinity)
* [crossbarfabriccenter.remote.worker.get_cpu_affinity](Management-API.md#crossbarfabriccenterremoteworkerget_cpu_affinity)
* [crossbarfabriccenter.remote.worker.set_cpu_affinity](Management-API.md#crossbarfabriccenterremoteworkerset_cpu_affinity)

---


## Process Statistics

This example demonstrates how to retrieve OS process statistics for Crossbar.io Fabric node controller and worker processes.

* [ex_process_stats.py](../examples/ex_process_stats.py)

APIs covered:

* [crossbarfabriccenter.remote.node.get_process_stats](Management-API.md#crossbarfabriccenterremotenodeget_process_stats)
* [crossbarfabriccenter.remote.worker.get_process_stats](Management-API.md#crossbarfabriccenterremoteworkerget_process_stats)

---


## Worker Logs

This example demonstrates how to remotely retrieve the log output from a worker running on a node, and how to receive a live feed for such a worker log.

* [ex_worker_log.py](../examples/ex_worker_log.py)

APIs covered:

* [crossbarfabriccenter.remote.node.get_worker_log](Management-API.md#crossbarfabriccenterremotenodeget_worker_log)

---


## Message Tracing

Crossbar.io Fabric has an message tracing extensions built into the routing core of Crossbar.io.

This allows to tap into the feeds of WAMP messages flowing through the routing core - in real-time.

The example will iterate over all router workers on all CF nodes, stop all traces (if any), and start a new trace on each router worker. It will run the trace for 10s, stop the traces and retrieve tracing data collected during the trace.

* [ex_tracing.py](../examples/ex_tracing.py)

The APIs covered:

* [crossbarfabriccenter.remote.tracing.get_traces](Management-API.md#crossbarfabriccenterremotetracingget_traces)
* [crossbarfabriccenter.remote.tracing.get_trace](Management-API.md#crossbarfabriccenterremotetracingget_trace)
* [crossbarfabriccenter.remote.tracing.start_trace](Management-API.md#crossbarfabriccenterremotetracingstart_trace)
* [crossbarfabriccenter.remote.tracing.stop_trace](Management-API.md#crossbarfabriccenterremotetracingstop_trace)
* [crossbarfabriccenter.remote.tracing.get_trace_data](Management-API.md#crossbarfabriccenterremotetracingget_trace_data)

---
