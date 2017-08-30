title: Examples
toc: [Documentation, Examples]

# Examples

This repository contains example code for programming against the Crossbar.io Fabric Center (CFC) API to remotely manage and monitor your Crossbar.io Fabric (CF) nodes connected to CFC.

**Examples:**

* [Get Status](#get-status)
* [Listing Nodes](#listing-nodes)
* [Listing Workers](#listing-workers)
* [Starting Routers](#starting-routers)
* [Starting Guests](#starting-guests)
* [Listing Sessions](#listing-sessions)
* [Listing Registrations and Subscriptions](#listing-registrations-and-subscriptions)
* [Worker CPU Affinity](#worker-cpu-affinity)
* [Process Statistics](#process-statistics)
* [Worker Logs](#worker-logs)
* [Message Tracing](#message-tracing)
* [Manage Docker](#manage-docker)

---


## Get Status

This example demonstrates how  to connect to CFC and retrieve status. That's it. It is the "most basic example".

* [ex_status.py](https://github.com/crossbario/crossbar-fabric-public/blob/master/examples/ex_status.py)

APIs covered:

* [crossbarfabriccenter.mrealm.get_status](api/Management-API.md#crossbarfabriccentermrealmget_status)

---


## Listing nodes

This example demonstrates how to iterate over the CF nodes in a management realm and retrieve detailed node status from nodes which are online.

* [ex_list_workers.py](https://github.com/crossbario/crossbar-fabric-public/blob/master/examples/ex_list_nodes.py)

APIs covered:

* [crossbarfabriccenter.mrealm.get_nodes](api/Management-API.md#crossbarfabriccentermrealmget_nodes)
* [crossbarfabriccenter.mrealm.get_node](api/Management-API.md#crossbarfabriccentermrealmget_node)
* [crossbarfabriccenter.remote.node.get_status](api/Management-API.md#crossbarfabriccenterremotenodeget_status)

---


## Listing workers

This example demonstrates how to iterate over the (currently connected) CF nodes, and on each node, iterate over the currently running workers to retrieve worker information.

* [ex_list_workers.py](https://github.com/crossbario/crossbar-fabric-public/blob/master/examples/ex_list_workers.py)

APIs covered:

* [crossbarfabriccenter.mrealm.get_nodes](api/Management-API.md#crossbarfabriccentermrealmget_nodes)
* [crossbarfabriccenter.remote.node.get_workers](api/Management-API.md#crossbarfabriccenterremotenodeget_workers)
* [crossbarfabriccenter.remote.node.get_worker](api/Management-API.md#crossbarfabriccenterremotenodeget_worker)

---


## Starting Routers

This example demonstrates how to dynamically start a new router worker on a node, start a realm and a role on the router and finally start a listening transport so the router will accept incoming WAMP connections.

* [ex_start_router.py](https://github.com/crossbario/crossbar-fabric-public/blob/master/examples/ex_start_router.py)

APIs covered:

* [crossbarfabriccenter.remote.worker.shutdown](api/Management-API.md#crossbarfabriccenterremoteworkershutdown)
* [crossbarfabriccenter.remote.node.start_worker](api/Management-API.md#crossbarfabriccenterremotenodestart_worker)
* [crossbarfabriccenter.remote.node.stop_worker](api/Management-API.md#crossbarfabriccenterremotenodestop_worker)
* [crossbarfabriccenter.remote.router.start_router_realm](api/Management-API.md#crossbarfabriccenterremoterouterstart_router_realm)
* [crossbarfabriccenter.remote.router.stop_router_realm](api/Management-API.md#crossbarfabriccenterremoterouterstop_router_realm)
* [crossbarfabriccenter.remote.router.start_router_realm_role](api/Management-API.md#crossbarfabriccenterremoterouterstart_router_realm_role)
* [crossbarfabriccenter.remote.router.stop_router_realm_role](api/Management-API.md#crossbarfabriccenterremoterouterstop_router_realm_role)
* [crossbarfabriccenter.remote.router.start_router_transport](api/Management-API.md#crossbarfabriccenterremoterouterstart_router_transport)
* [crossbarfabriccenter.remote.router.stop_router_transport](api/Management-API.md#crossbarfabriccenterremoterouterstop_router_transport)

---


## Starting Guests

This example demonstrates how to dynamically start and stop guest workers on a node.

* [ex_start_guest.py](https://github.com/crossbario/crossbar-fabric-public/blob/master/examples/ex_start_guest.py)

APIs covered:

* [crossbarfabriccenter.mrealm.get_nodes](api/Management-API.md#crossbarfabriccentermrealmget_nodes)
* [crossbarfabriccenter.remote.node.get_workers](api/Management-API.md#crossbarfabriccenterremotenodeget_workers)
* [crossbarfabriccenter.remote.node.start_worker](api/Management-API.md#crossbarfabriccenterremotenodestart_worker)
* [crossbarfabriccenter.remote.node.stop_worker](api/Management-API.md#crossbarfabriccenterremotenodestop_worker)

---


## Listing Sessions

The example demonstrates listing of WAMP sessions currently joined on router realms running on CF nodes connected to CFC.

* [ex_list_sessions.py](https://github.com/crossbario/crossbar-fabric-public/blob/master/examples/ex_list_sessions.py)

This is using the [Remote Realm WAMP meta API](api/Management-API.md#remote-realm-wamp-meta-api)

The APIs covered:

* [crossbarfabriccenter.remote.realm.meta.*](api/Management-API.md#crossbarfabriccenterremoterealmmeta)

---


## Listing Registrations and Subscriptions

The example demonstrates listing of WAMP subscriptions and registrations currently active for WAMP sessions on router realms running on CF nodes connected to CFC.

* [ex_list_subs_regs.py](https://github.com/crossbario/crossbar-fabric-public/blob/master/examples/ex_list_subs_regs.py)

This is using the [Remote Realm WAMP meta API](api/Management-API.md#remote-realm-wamp-meta-api)

The APIs covered:

* [crossbarfabriccenter.remote.realm.meta.*](api/Management-API.md#crossbarfabriccenterremoterealmmeta)

---


## Worker CPU Affinity

Demonstrates getting/setting the CPU affinity set of CF workers.

* [ex_cpu_affinity.py](https://github.com/crossbario/crossbar-fabric-public/blob/master/examples/ex_cpu_affinity.py)

APIs covered:

* [crossbarfabriccenter.remote.node.get_cpu_count](api/Management-API.md#crossbarfabriccenterremotenodeget_cpu_count)
* [crossbarfabriccenter.remote.node.get_cpu_affinity](api/Management-API.md#crossbarfabriccenterremotenodeget_cpu_affinity)
* [crossbarfabriccenter.remote.worker.get_cpu_affinity](api/Management-API.md#crossbarfabriccenterremoteworkerget_cpu_affinity)
* [crossbarfabriccenter.remote.worker.set_cpu_affinity](api/Management-API.md#crossbarfabriccenterremoteworkerset_cpu_affinity)

---


## Process Statistics

This example demonstrates how to retrieve OS process statistics for Crossbar.io Fabric node controller and worker processes.

* [ex_process_stats.py](https://github.com/crossbario/crossbar-fabric-public/blob/master/examples/ex_process_stats.py)

APIs covered:

* [crossbarfabriccenter.remote.node.get_process_stats](api/Management-API.md#crossbarfabriccenterremotenodeget_process_stats)
* [crossbarfabriccenter.remote.worker.get_process_stats](api/Management-API.md#crossbarfabriccenterremoteworkerget_process_stats)

---


## Worker Logs

This example demonstrates how to remotely retrieve the log output from a worker running on a node, and how to receive a live feed for such a worker log.

* [ex_worker_log.py](https://github.com/crossbario/crossbar-fabric-public/blob/master/examples/ex_worker_log.py)

APIs covered:

* [crossbarfabriccenter.remote.node.get_worker_log](api/Management-API.md#crossbarfabriccenterremotenodeget_worker_log)

---


## Message Tracing

Crossbar.io Fabric has an message tracing extensions built into the routing core of Crossbar.io.

This allows to tap into the feeds of WAMP messages flowing through the routing core - in real-time.

The example will iterate over all router workers on all CF nodes, stop all traces (if any), and start a new trace on each router worker. It will run the trace for 10s, stop the traces and retrieve tracing data collected during the trace.

* [ex_tracing.py](https://github.com/crossbario/crossbar-fabric-public/blob/master/examples/ex_tracing.py)

The APIs covered:

* [crossbarfabriccenter.remote.tracing.get_traces](api/Management-API.md#crossbarfabriccenterremotetracingget_traces)
* [crossbarfabriccenter.remote.tracing.get_trace](api/Management-API.md#crossbarfabriccenterremotetracingget_trace)
* [crossbarfabriccenter.remote.tracing.start_trace](api/Management-API.md#crossbarfabriccenterremotetracingstart_trace)
* [crossbarfabriccenter.remote.tracing.stop_trace](api/Management-API.md#crossbarfabriccenterremotetracingstop_trace)
* [crossbarfabriccenter.remote.tracing.get_trace_data](api/Management-API.md#crossbarfabriccenterremotetracingget_trace_data)

---


## Manage Docker

**This is under development and not yet working.**

Crossbar.io Fabric allows to remotely manage a Docker daemon running on the host the Crossbar.io Fabric node is deployed on.

This allows to dynamically provision, deploy and manage application components wrapped in Docker containers on CF nodes.

* [ex_docker.py](https://github.com/crossbario/crossbar-fabric-public/blob/master/examples/ex_docker.py)

The APIs covered:

* [crossbarfabriccenter.mrealm.get_nodes](api/Management-API.md#crossbarfabriccentermrealmget_nodes)
* [crossbarfabriccenter.remote.node.get_status](api/Management-API.md#crossbarfabriccenterremotenodeget_status)
* [crossbarfabriccenter.remote.docker.get_status](api/Management-API.md#crossbarfabriccenterremotedockerget_status)
* [crossbarfabriccenter.remote.docker.get_containers](api/Management-API.md#crossbarfabriccenterremotedockerget_containers)
* [crossbarfabriccenter.remote.docker.get_container](api/Management-API.md#crossbarfabriccenterremotedockerget_container)
* [crossbarfabriccenter.remote.docker.start_container](api/Management-API.md#crossbarfabriccenterremotedockerstart_container)
* [crossbarfabriccenter.remote.docker.stop_container](api/Management-API.md#crossbarfabriccenterremotedockerstop_container)
* [crossbarfabriccenter.remote.docker.get_images](api/Management-API.md#crossbarfabriccenterremotedockerget_images)
* [crossbarfabriccenter.remote.docker.get_image](api/Management-API.md#crossbarfabriccenterremotedockerget_image)
* [crossbarfabriccenter.remote.docker.update_image](api/Management-API.md#crossbarfabriccenterremotedockerupdate_image)
* [crossbarfabriccenter.remote.docker.remove_image](api/Management-API.md#crossbarfabriccenterremotedockerremove_image)

---
