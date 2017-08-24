title: Management API
toc: [Documentation, API Reference, Management API]

# Management API

Each user created **management realm** (eg `com.example.my-mgmt-realm1`) on Crossbar.io Fabric Center (CFC) exposes the following APIs to clients:

* **[Management Realm API](#management-realm-api)**: management realm wide operations
* **[Remote Realm WAMP Meta API](#remote-realm-wamp-meta-api)**: remote access to CF nodes WAMP meta API
* **[Remote Node Management API](#remote-node-management-api)**: remote access to CF nodes management API

CFC clients can use all three APIs at the same time, and use the functionality provided over whole sets of CF nodes in the management realm.

This single point of entry allows you to create complex automatic application management functions using standard programming patterns, and very little user code to write.

---


## Management Realm API

Prefix: `crossbarfabriccenter.mrealm.`

Status: **alpha**

Provides management realm wide procedures.

* [ ] [crossbarfabriccenter.mrealm.get_status](#crossbarfabriccentermrealmget_status)
* [ ] [crossbarfabriccenter.mrealm.get_nodes](#crossbarfabriccentermrealmget_nodes)
* [ ] [crossbarfabriccenter.mrealm.get_node](#crossbarfabriccentermrealmget_node)


## Remote Realm WAMP Meta API

Prefix: `crossbarfabriccenterremote.realm.meta.`

Status: **alpha**

Provides remote access to the WAMP meta API of routing realms on Crossbar.io Fabric nodes currently connected.

* [ ] [crossbarfabriccenter.remote.realm.meta.*](#crossbarfabriccenterremoterealmmeta)


## Remote Node Management API

Provides remote access to the node management API of Crossbar.io Fabric nodes currently connected.


### Nodes

Prefix: `crossbarfabriccenter.remote.node.`

Status: **alpha**

Nodes are instances of Crossbar.io (Fabric) running on host systems, and running from a node directory. Most of the time, nodes run within Docker containers or confined as snaps.

* [ ] [crossbarfabriccenter.remote.node.get_status](#crossbarfabriccenterremotenodeget_status)
* [ ] [crossbarfabriccenter.remote.node.shutdown](#crossbarfabriccenterremotenodeshutdown)
* [ ] [crossbarfabriccenter.remote.node.get_workers](#crossbarfabriccenterremotenodeget_workers)
* [ ] [crossbarfabriccenter.remote.node.get_worker](#crossbarfabriccenterremotenodeget_worker)
* [ ] [crossbarfabriccenter.remote.node.start_worker](#crossbarfabriccenterremotenodestart_worker)
* [ ] [crossbarfabriccenter.remote.node.stop_worker](#crossbarfabriccenterremotenodestop_worker)


### Native Workers

Prefix: `crossbarfabriccenter.remote.worker.`)

Status: **alpha**

Native workers are node worker processes of the types **router**, **container** and **proxy**. The API here allows to retrieve worker logs, control the worker CPU affinity and run code profilers in a live running system.

* [ ] [crossbarfabriccenter.remote.worker.get_status](#crossbarfabriccenterremoteworkerget_status)
* [ ] [crossbarfabriccenter.remote.worker.shutdown](#crossbarfabriccenterremoteworkershutdown)
* [ ] [crossbarfabriccenter.remote.worker.get_worker_log](#crossbarfabriccenterremoteworkerget_worker_log)
* [ ] [crossbarfabriccenter.remote.worker.get_pythonpath](#crossbarfabriccenterremoteworkerget_pythonpath)
* [ ] [crossbarfabriccenter.remote.worker.add_pythonpath](#crossbarfabriccenterremoteworkeradd_pythonpath)
* [ ] [crossbarfabriccenter.remote.worker.get_cpu_count](#crossbarfabriccenterremoteworkerget_cpu_count)
* [ ] [crossbarfabriccenter.remote.worker.get_cpu_affinity](#crossbarfabriccenterremoteworkerget_cpu_affinity)
* [ ] [crossbarfabriccenter.remote.worker.set_cpu_affinity](#crossbarfabriccenterremoteworkerset_cpu_affinity)
* [ ] [crossbarfabriccenter.remote.worker.get_profilers](#crossbarfabriccenterremoteworkerget_profilers)
* [ ] [crossbarfabriccenter.remote.worker.start_profiler](#crossbarfabriccenterremoteworkerstart_profiler)
* [ ] [crossbarfabriccenter.remote.worker.get_profile](#crossbarfabriccenterremoteworkerget_profile)


### Router Workers

Prefix: `crossbarfabriccenter.remote.router.`

Routers are the core of Crossbar.io. They are native worker processes that run the routing code of Crossbar.io as well as endpoint listeners, Web services and other transports. The API here allows for remote and dynamic management of router workers.


#### Router Realms

Status: **alpha**

All routing of messages in Crossbar.io is isolated in different routing confinements called realms. Realms, at the same time, also provide namespace isolation, as URIs as always interpreted with respect to the realm within they occur. URIs portable accross realms - if required - needs to be arranged for by the user.

* [ ] [crossbarfabriccenter.remote.router.get_realms](#crossbarfabriccenterremoterouterget_realms)
* [ ] [crossbarfabriccenter.remote.router.get_realm](#crossbarfabriccenterremoterouterget_realm)
* [ ] [crossbarfabriccenter.remote.router.start_realm](#crossbarfabriccenterremoterouterstart_realm)
* [ ] [crossbarfabriccenter.remote.router.stop_realm](#crossbarfabriccenterremoterouterstop_realm)


#### Realm Roles

Status: **alpha**

Roles are bundles of permissions defined on a realm. When a client connects to the router and authenticates successfully, it is assigned a **role**. This role will then determine the actual permissions the client is granted by the router.

* [ ] [crossbarfabriccenter.remote.router.get_realm_roles](#crossbarfabriccenterremoterouterget_realm_roles)
* [ ] [crossbarfabriccenter.remote.router.get_realm_role](#crossbarfabriccenterremoterouterget_realm_role)
* [ ] [crossbarfabriccenter.remote.router.start_realm_role](#crossbarfabriccenterremoterouterstart_realm_role)
* [ ] [crossbarfabriccenter.remote.router.stop_realm_role](#crossbarfabriccenterremoterouterstop_realm_role)


#### Role Permissions

Status: **planned**

Permissions specific which WAMP actions is allowed on which URI (pattern) for the pair realm-role.

* [ ] [crossbarfabriccenter.remote.router.get_role_permissions](#crossbarfabriccenterremoterouterget_role_permissions)
* [ ] [crossbarfabriccenter.remote.router.get_role_permission](#crossbarfabriccenterremoterouterget_role_permission)
* [ ] [crossbarfabriccenter.remote.router.start_role_permission](#crossbarfabriccenterremoterouterstart_ŕole_permission)
* [ ] [crossbarfabriccenter.remote.router.stop_role_permission](#crossbarfabriccenterremoterouterstop_role_permission)


#### Router Transports

Status: **alpha**

Routers will want to listen for incoming client connections on so-called listening endpoints. The API here allows the dynamic startup and shutdown of router liensting endpoints in the form of transports.

* [ ] [crossbarfabriccenter.remote.router.get_transports](#crossbarfabriccenterremoterouterget_transports)
* [ ] [crossbarfabriccenter.remote.router.get_transport](#crossbarfabriccenterremoterouterget_transport)
* [ ] [crossbarfabriccenter.remote.router.start_transport](#crossbarfabriccenterremoterouterstart_transport)
* [ ] [crossbarfabriccenter.remote.router.stop_transport](#crossbarfabriccenterremoterouterstop_transport)


#### Transport Services

Status: **planned**

Some router transports, such as Web transports, allow to configure *transport services* attached to URL parts in a Web resource tree. The API here allows to dynamically configure Web services, such as a static Web or file download service on dynamic URL part in the Web resource tree of Web transports.

* [ ] [crossbarfabriccenter.remote.router.get_transport_services](#crossbarfabriccenterremoterouterget_transport_services)
* [ ] [crossbarfabriccenter.remote.router.get_transport_service](#crossbarfabriccenterremoterouterget_transport_service)
* [ ] [crossbarfabriccenter.remote.router.start_transport_service](#crossbarfabriccenterremoterouterstart_transport_service)
* [ ] [crossbarfabriccenter.remote.router.stop_transport_service](#crossbarfabriccenterremoterouterstop_transport_service)


#### Router Components

Status: **alpha**

Router workers are native Crossbar.io processes that can host Python user components. Restrictions: The user components must be written using AutobahnPython and Twisted, and run under the same Python Crossbar.io runs under. Further, running user components in the same OS process as Crossbar.io routing code can lead to instability, and provides less security isolation. Router components should only be used very selectively for small amounts of code, such as dynamic authenticators or authorizers.

* [ ] [crossbarfabriccenter.remote.router.get_components](#crossbarfabriccenterremoterouterget_components)
* [ ] [crossbarfabriccenter.remote.router.get_component](#crossbarfabriccenterremoterouterget_component)
* [ ] [crossbarfabriccenter.remote.router.start_component](#crossbarfabriccenterremoterouterstart_component)
* [ ] [crossbarfabriccenter.remote.router.stop_component](#crossbarfabriccenterremoterouterstop_component)


### Container Workers

Prefix: `crossbarfabriccenter.remote.container.`

Status: **alpha**

Container workers are native Crossbar.io processes that can host Python user components. Restrictions: The user components must be written using AutobahnPython and Twisted, and run under the same Python Crossbar.io runs under.

* [ ] [crossbarfabriccenter.remote.container.get_components](#crossbarfabriccenterremotecontainerget_components)
* [ ] [crossbarfabriccenter.remote.container.get_component](#crossbarfabriccenterremotecontainerget_component)
* [ ] [crossbarfabriccenter.remote.container.start_component](#crossbarfabriccenterremotecontainerstart_component)
* [ ] [crossbarfabriccenter.remote.container.stop_component](#crossbarfabriccenterremotecontainerstop_component)


### Proxy Workers

Prefix: `crossbarfabriccenter.remote.proxy.`

Status: **under development**

Proxy workers are native worker processes of Crossbar.io Fabric that can proxy and authenticate frontend WAMP connections, normalize and scrub WAMP messages, and forward to backend router workers in an optimized way. This allows to scale up and scale out the WAMP frontend connection handling layer.

* [ ] [crossbarfabriccenter.remote.proxy.get_transports](#crossbarfabriccenterremoteproxyget_transports)
* [ ] [crossbarfabriccenter.remote.proxy.get_transport](#crossbarfabriccenterremoteproxyget_transport)
* [ ] [crossbarfabriccenter.remote.proxy.start_transport](#crossbarfabriccenterremoteproxystart_transport)
* [ ] [crossbarfabriccenter.remote.proxy.stop_transport](#crossbarfabriccenterremoteproxystop_transport)


### Message Tracing

Prefix: `crossbarfabriccenter.remote.tracing.`

Status: **alpha**

Tap into the message flow of Crossbar.io Fabric nodes. Monitor and trace real-time message traffic and routing down to the single WAMP message level.

* [ ] [crossbarfabriccenter.remote.tracing.get_traces](#crossbarfabriccenterremotetracingget_traces)
* [ ] [crossbarfabriccenter.remote.tracing.get_trace](#crossbarfabriccenterremotetracingget_trace)
* [ ] [crossbarfabriccenter.remote.tracing.start_trace](#crossbarfabriccenterremotetracingstart_trace)
* [ ] [crossbarfabriccenter.remote.tracing.stop_trace](#crossbarfabriccenterremotetracingstop_trace)
* [ ] [crossbarfabriccenter.remote.tracing.get_trace_data](#crossbarfabriccenterremotetracingget_trace_data)


### Docker Control

Prefix: `crossbarfabriccenter.remote.docker.`

Status: **under development**

Remotely control the Docker daemons of hosts running Crossbar.io Fabric nodes.

* [ ] [crossbarfabriccenter.remote.docker.get_status](#crossbarfabriccenterremotedockerget_status)
* [ ] [crossbarfabriccenter.remote.docker.get_containers](#crossbarfabriccenterremotedockerget_containers)
* [ ] [crossbarfabriccenter.remote.docker.get_container](#crossbarfabriccenterremotedockerget_container)
* [ ] [crossbarfabriccenter.remote.docker.start_container](#crossbarfabriccenterremotedockerstart_container)
* [ ] [crossbarfabriccenter.remote.docker.stop_container](#crossbarfabriccenterremotedockerstop_container)
* [ ] [crossbarfabriccenter.remote.docker.get_images](#crossbarfabriccenterremotedockerget_images)
* [ ] [crossbarfabriccenter.remote.docker.get_image](#crossbarfabriccenterremotedockerget_image)
* [ ] [crossbarfabriccenter.remote.docker.update_image](#crossbarfabriccenterremotedockerupdate_image)
* [ ] [crossbarfabriccenter.remote.docker.remove_image](#crossbarfabriccenterremotedockerremove_image)

---


## Procedures Reference

Signature and descriptions of API procedures.

---


### crossbarfabriccenter.mrealm.get_status

Return management realm status information.

* **get_status** () -> status

where

* **status** (dict): status information object

is returned:

```javascript
{
   // FIXME
}
```

---


### crossbarfabriccenter.mrealm.get_nodes

Return list of IDs of nodes in the management realm.

* **get_nodes ()** -> [node_id]

where

* **node_id** (string): ID of a node (that is paired with the management realm)

is returned:

```javascript
["node1", "node2"]
```

> The order of IDs within the list returned is unspecified, but stable.

---


### crossbarfabriccenter.mrealm.get_node

Return detailed information about a node in the management realm.

* **get_node** (node_id) -> node

where

* **node_id** (string): ID of the node to retrieve information for

and

* **node** (dict): node information object

is returned:

```javascript
{
   // FIXME
}
```

---


### crossbarfabriccenter.remote.realm.meta.*

Crossbar.io implements the WAMP meta API at the app router level:

* [Session Meta Events and Procedures](http://crossbar.io/docs/Session-Metaevents-and-Procedures/)
* [Subscription Meta Events and Procedures](http://crossbar.io/docs/Subscription-Meta-Events-and-Procedures/)
* [Registration Meta-Events and Procedures](http://crossbar.io/docs/Registration-Meta-Events-and-Procedures/)

Exposing the WAMP meta API at the app router level is enabled by default, but can be disabled by setting `enable_meta_api: false` in the [realms options](https://github.com/crossbario/crossbar/blob/master/docs/pages/administration/router/Router-Realms.md#realm-options).

Exposing the WAMP meta API to CFC however is disabled by default, and **needs to be enabled by setting `bridge_meta_api: true`** in the router options.

If the bridging of the WAMP meta API is enabled, all above procedures and topics will be available prefixed with an additional `crossbarfabriccenter.remote.realm.meta.`.

So, for example, the WAMP meta API procedure

* `wamp.session.list ()`

that returns a list of WAMP session IDs of session currently joined on the realm is exposed via CFC under

* `crossbarfabriccenter.remote.realm.meta.wamp.session.list (node_id, worker_id, realm_id)`

Since the CFC exposed procedure needs to know the realm on which to actually call into the WAMP meta API of that realm, the CFC procedure has additional (positional) parameters prepended, notably, node_id, worker_id and realm_id.

In this case, the original procedure did not take any parameters, and hence the CFC flavor of the procedure has exactly the three mentioned additional parameters. Had the original procedure already a positional argument, that would appear _after_ the extra parameters required by CFC (recap that the latter are always _prepended_ to any already existing procedure parameters).

The translation works pattern based (note the `*` at the end of the URI `crossbarfabriccenter.remote.realm.meta.*`), this allows CFC clients to remotely call into any WAMP meta API procedure of any of the CF nodes connected, which can be a very powerful vector into the guts of your application - live and in production.

WAMP meta events are translated similar. That is, events destined for topic

* `wamp.session.on_join (session_id, session_details)`

can be subscribed under

* `crossbarfabriccenter.remote.realm.meta.wamp.session.on_join (node_id, worker_id, realm_id, session_id, session_details)`

The WAMP meta API defines (meta) topics for various events like a session joining or leaving, registering a procedure or subscribing to a topic and so on. Making this functionality available remotely, and to many nodes, but from a single point of entry for the CFC client, this allows to cover a lot of scenarios.

> Caution: Depending on the application, many subscribes to topics could happen per second, and exposing all these WAMP meta events not only on the (local) app router, but also remotely to CFC can generate a lot of traffic.

---


### crossbarfabriccenter.remote.node.get_status

Retrieve status information (directly) from a node.

* **get_status** (node_id) -> status

where

* **node_id** (string): ID of the node to retrieve status from

and

* **status** (dict): Node status information object

is returned:

```javascript
{
   // FIXME
}
```

---


### crossbarfabriccenter.remote.node.shutdown

Orderly shutdown a node (from within the node).

* **shutdown** (node_id) -> node_shutdown

where

* **node_id** (string): ID of the node to shut down

and

* **node_shutdown** (dict): Node (final) shutdown information object

is returned:

```javascript
{
   // FIXME
}
```

When the node is shut down, a (last) event

* **on_shutdown** (node_shutdown)

is fired.

---


### crossbarfabriccenter.remote.node.get_workers

Get list of IDs of workers in node.

* **get_workers** (node_id) -> [worker_id]

where

* **node_id** (string): ID of the node to get workers for

and

* **worker_id** (string): worker ID

is returned:

```javascript
["router1", "proxy1", "proxy2"]
```

> The order of IDs within the list returned is unspecified, but stable.

---


### crossbarfabriccenter.remote.node.get_worker

Return detailed information about worker.

* **get_worker** (node_id, worker_id) -> worker

where

* **node_id** (string): ID of the node to get worker for
* **worker_id** (string): ID of the worker to get

and

* **worker** (dict): worker information object

is returned:

```javscript
{
    // FIXME
}
```

---


### crossbarfabriccenter.remote.node.start_worker

Start a new worker on a node.

* **start_worker** (node_id, worker_id, worker_config) -> worker_started

where

* **node_id** (string): ID of the node to start the worker on
* **worker_id** (string): optional ID for the worker. when not given, auto-generated
* **worker_config** (dict): worker configuration object

and

* **worker_started** (dict): worker startup information object

is returned:

```javascript
{
   // FIXME
}
```

The call does not return until the worker has been completely started.

When the new worker *is starting*, an event

* **on_worker_starting** (node_id, worker_id)

is fired.

When the new worker *has been started*, an event

* **on_worker_started** (node_id, worker_id, worker_started)

is fired.

---


### crossbarfabriccenter.remote.node.stop_worker

Stop a worker currently running on a node.

* **stop_worker** (node_id, worker_id) -> worker_stopped

* **node_id** (string): ID of the node to stop the worker on
* **worker_id** (string): ID of the worker to stop

and

* **worker_stopped** (dict): worker stopped information object

is returned:

```javascript
{
   // FIXME
}
```

The call does not return until the worker has been completely stopped.

When the worker *is stopping*, an event

* **on_worker_stopping** (node_id, worker_id)

is fired.

When the worker *has been stopped*, an event

* **on_worker_stopped** (node_id, worker_id, worker_stopped)

is fired.

---


### crossbarfabriccenter.remote.worker.get_status

Get status of native worker (from inside the worker).

* **get_status** (node_id, worker_id) -> status

where

* **node_id** (string): ID of node running the worker to get status for
* **worker_id** (string): ID of the worker to get status for

and

* **status** (dict): worker status information object

is returned:

```javascript
{
   // FIXME
}
```

---


### crossbarfabriccenter.remote.worker.shutdown

Orderly shutdown the worker (from inside).

* **shutdown** (node_id, worker_id) -> worker_shutdown

where

* **node_id** (string): ID of node running the worker to shut down
* **worker_id** (string): ID of the worker to shut down

and

* **worker_shutdown** (dict): worker shutdown information object

is returned:

```javascript
{
   // FIXME
}
```

---


### crossbarfabriccenter.remote.worker.get_worker_log

Retrieve log output from node workers.

* **get_worker_log** (node_id, worker_id, limit) -> [log_record]

where

* **node_id** (string): ID of node running the worker to get logs for
* **worker_id** (string): ID of the worker to get logs for
* **limit** (int): maximum number of log lines to return (default: 100)

and

* **log_record** (dict or string): when the worker support rich logging, a structured log record. when the worker only supports plain logging, a non-structured plain string (the line that was logged)

is returned:

```javascript
{
   // FIXME
}
```

---


### crossbarfabriccenter.remote.worker.get_pythonpath

Returns the current Python module search paths in the (native) worker.

* **get_pythonpath** (node_id, worker_id) -> [path]

where

* **node_id** (string): ID of node running the worker to get Python search paths for
* **worker_id** (string): ID of the worker to get Python search paths for

and

* **path** (string): a Python search path (a directory)

is returned:

```javascript
[".", "/usr/local/lib/python3.6/site-packages"]
```

---


### crossbarfabriccenter.remote.worker.add_pythonpath

* **add_pythonpath** (node_id, worker_id, paths, prepend) -> path_added

where

* **node_id** (string): ID of node running the worker to add Python search p
* **worker_id** (string): ID of the worker to add Python search paths to
* **prepend** (boolean): if True, prepend the search paths to the current list, else append at the end

and

* **path_added** (dict): Python search paths added information object

is returned:

```javascript
{
   // FIXME
}
```

---


### crossbarfabriccenter.remote.worker.get_cpu_count

Returns the CPU core count on the machine this worker (process) is running on.

> Given `CPU_COUNT`, valid CPU (core) IDs then are `[0, CPU_COUNT[`.

* **get_cpu_count** (node_id, worker_id) -> int

where

* **node_id** (string): ID of node running the worker to get CPU count for
* **worker_id** (string): ID of the worker to get CPU count for

and the CPU (core) count is returned:

```javascript
4
```

---


### crossbarfabriccenter.remote.worker.get_cpu_affinity

Get current CPU affinity of this worker (process) returning a list of CPU IDs. CPU (cores) are numbered beginning with 0.

* **get_cpu_affinity** (node_id, worker_id) -> [int]

where

* **node_id** (string): ID of node running the worker to get CPU affinity for
* **worker_id** (string): ID of the worker to get CPU affinity for

and the CPU affinity is returned:

```javascript
[0, 1, 2, 3]
```

---


### crossbarfabriccenter.remote.worker.set_cpu_affinity

Set current CPU affinity of this worker (process).

CPU (cores) are numbered beginning with 0, and `cpus` must be a list of IDs given the CPUs eligible to run this worker.

* **set_cpu_affinity** (node_id, worker_id, cpus) -> [int]

where

* **node_id** (string): ID of node running the worker to set CPU affinity for
* **worker_id** (string): ID of the worker to set CPU affinity for
* **cpus** (list of int): the CPU (core) IDs to set the affinity to

and the new CPU affinity is returned:

```javascript
[1]
```

---


### crossbarfabriccenter.remote.worker.get_profilers

Return the Python profilers available in the (native) worker.

> Currently, the only profiler available is [vmprof](https://vmprof.readthedocs.io/).

* **get_profilers** (node_id, worker_id) -> [profiler]

where

* **node_id** (string): ID of node running the worker to get available profilers for
* **worker_id** (string): ID of the worker to get available profilers for

and

* **profiler** (dict): profiler information object.

is returned:

```javascript
{
   // FIXME
}
```

---


### crossbarfabriccenter.remote.worker.start_profiler

* **start_profiler** (node_id, worker_id, profiler, runtime, async) -> profile_started or [profile_record]

where

* **node_id** (string): ID of node running the worker to profile
* **worker_id** (string): ID of the worker to profile
* **profiler** (string): the profiler to use (default: vmprof)
* **runtime** (float): profiling run-time in seconds (default: 10)
* **async** (boolean): if True, start profile asynchronously and immediately return `profile_started`. if False, wait for the profile to finish before returning from the call (with `profile_result`)

and call result

* **profile_started** (dict): profile started information object

```javascript
{
   // FIXME
}
```

or

* **profile_record** (dict): profile result record

```javascript
{
   // FIXME
}
```

is returned.

---


### crossbarfabriccenter.remote.worker.get_profile

Return the profile of a previously run worker profiling run.

* **get_profile** (node_id, worker_id, profile_id) -> [profile_record]

where

* **node_id** (string): ID of node running the worker on which the profile was run
* **worker_id** (string): ID of the worker on which the profile was run
* **profile_id** (string): ID of the profiling run to retrieve profile for

and

* **profile_record** (dict): profile result record

is returned:

```javascript
{
   // FIXME
}
```

---


### crossbarfabriccenter.remote.router.get_realms

Return a list of IDs of realms in the given router worker.

* **get_realms** (node_id, worker_id) -> [realm_id]

where

* **node_id** (string): ID of node running the worker to get realms for
* **worker_id** (string): ID of the worker to get realms for

and

* **realm_id** (string): realm ID

is returned:

```javascript
["-my-realm-1", "my-realm-2"]
```

> The order of IDs within the list returned is unspecified, but stable.

---


### crossbarfabriccenter.remote.router.get_realm

Return detailed information about the given realm.

* **get_realm** (node_id, worker_id, realm_id) -> realm

where

* **node_id** (string): ID of node running the (router) worker with the realm to to get information for
* **worker_id** (string): ID of the (router) worker with the realm to get informatin for
* **realm_id** (string): ID of the realm to get information for

and

* **realm** (dict): realm information object

is returned:

```javascript
{
   // FIXME
}
```

---


### crossbarfabriccenter.remote.router.start_realm

Start a new realm on the given router worker.

* **start_realm** (node_id, worker_id, realm_id, realm_config) -> realm_started

where

* **node_id** (string): ID of node running the (router) worker to start the realm on
* **worker_id** (string): ID of the (router) worker to start the realm on
* **realm_id** (string): optional ID of the realm to start. if not provided, auto-generated.

and

* **realm_started** (dict): realm started information object

is returned:

```javascript
{
   // FIXME
}
```

The call does not return until the realm has completely started.

When the new realm *is starting*, an event

* **on_realm_starting** (node_id, worker_id, realm_id)

is fired.

When the new realm *is completely started*, an event

* **on_realm_started** (node_id, worker_id, realm_id, realm_started)

is fired.

---


### crossbarfabriccenter.remote.router.stop_realm

Stop a realm currently running in the given router worker.

* **stop_realm** (node_id, worker_id, realm_id) -> realm_stopped

where

* **node_id** (string): ID of node running the (router) worker with the realm to stop
* **worker_id** (string): ID of the (router) worker with the realm to stop
* **realm_id** (string): ID of the realm to stop

and

* **realm_stopped** (dict): realm stopped information object

is returned

```javascript
{
   // FIXME
}
```

The call does not return until the realm has completely stopped.

When the realm *is stopping*, an event

* **on_realm_stopping** (node_id, worker_id, realm_id)

is fired.

When the realm *is completely stopped*, an event

* **on_realm_stopped** (node_id, worker_id, realm_id, realm_stopped)

is fired.

---


### crossbarfabriccenter.remote.router.get_realm_roles

Return a list of IDs of roles in the given realm.

* **get_realm_roles** (node_id, worker_id, realm_id) -> [role_id]

where

* **node_id** (string): ID of node running the (router) worker to get roles for
* **worker_id** (string): ID of the (router) worker to get roles for
* **realm_id** (string): ID of the realm to get roles for

and

* **role_id** (string): role ID

is returned:

```javascript
["role1", "role2", "role3"]
```

> The order of IDs within the list returned is unspecified, but stable.

---


### crossbarfabriccenter.remote.router.get_realm_role

Return detailed information about the given role.

* **get_realm_role* (node_id, worker_id, realm_id, role_id) -> role

where

* **node_id** (string): ID of node running the (router) worker with the role to get information for
* **worker_id** (string): ID of the (router) worker with the role to get informationn for
* **realm_id** (string): ID of the realm with the role to get information for
* **role_id** (string): ID of the role to get information for

and

* **role** (dict): role information object

is returned:

```javascript
{
   // FIXME
}
```

---


### crossbarfabriccenter.remote.router.start_realm_role

Start a new role on the given router worker and realm.

* **start_realm_role** (node_id, worker_id, realm_id, role_id, role_config) -> role_started

where

* **node_id** (string): ID of node running the (router) worker to start the role on
* **worker_id** (string): ID of the (router) worker to start the role on
* **realm_id** (string): ID of the realm to start the role on
* **realm_id** (string): optional ID of the role to start. if not provided, auto-generated.

and

* **role_started** (dict): role started information object

is returned:

```javascript
{
   // FIXME
}
```

When the new role *is started*, an event

* **on_router_role_started** (node_id, worker_id, realm_id, role_id, role_started)

is fired.

---


### crossbarfabriccenter.remote.router.stop_realm_role

Stop a role currently running in a realm in a router worker.

* **stop_realm_role** (node_id, worker_id, realm_id, role_id) -> role_stopped

where

* **node_id** (string): ID of node running the (router) worker to stop the role on
* **worker_id** (string): ID of the (router) worker to stop the role on
* **realm_id** (string): ID of the realm to stop the role on
* **realm_id** (string): ID of the role to stop.

and

* **role_stopped** (dict): role stopped information object

is returned:

```javascript
{
   // FIXME
}
```

The call does not return until the role has completely stopped.

When the role *is stopped*, an event

* **on_router_role_stopped** (node_id, worker_id, realm_id, role_id, role_stopped)

is fired.

---

### crossbarfabriccenter.remote.router.get_role_permissions

Return a list of IDs of permissions on the given role.

* **get_role_permissions** (node_id, worker_id, realm_id, role_id) -> [permission_id]

where

* **node_id** (string): ID of node running the (router) worker to get permissions for
* **worker_id** (string): ID of the (router) worker to get permissions for
* **realm_id** (string): ID of the realm to get permissions for
* **role_id** (string): ID of the role to get permissions for

and

* **permission_id** (string): permission ID

is returned:

```javascript
["perm1", "perm2", "perm3", "perm4", "perm5"]
```

> The order of IDs within the list returned is unspecified, but stable.

---


### crossbarfabriccenter.remote.router.get_role_permission

Return detailed information about the given permission.

* **get_role_permission** (node_id, worker_id, realm_id, role_id, permission_id) -> permission

where

* **node_id** (string): ID of node running the (router) worker with the permission to get information for
* **worker_id** (string): ID of the (router) worker with the permission to get informationn for
* **realm_id** (string): ID of the realm with the permission to get information for
* **role_id** (string): ID of the role with the permission to get information for
* **permission_id** (string): ID of the permission to get information for

and

* **permission** (dict): permission information object

is returned:

```javascript
{
   // FIXME
}
```

---


### crossbarfabriccenter.remote.router.start_role_permission

Start a new permission on the given router worker/realm/role.

* **start_role_permission** (node_id, worker_id, realm_id, role_id, permission_id, permission_config) -> permission_started

where

* **node_id** (string): ID of node running the (router) worker to start the permission on
* **worker_id** (string): ID of the (router) worker to start the permission on
* **realm_id** (string): ID of the realm to start the permission on
* **role_id** (string): ID of the role to start the permission on
* **permission_id** (string): optional ID of the permission to start. if not provided, auto-generated.
* **permission_config** (dict): permission configuration

and

* **permission_started** (dict): permission started information object

is returned:

```javascript
{
   // FIXME
}
```

The call does not return until the permission has completely started.

When the new permission *is started*, an event

* **on_role_permission_started** (node_id, worker_id, realm_id, role_id, permission_id, permission_started)

is fired.

---


### crossbarfabriccenter.remote.router.stop_permission_role

Stop a permission currently running in a role on a realm in a router worker.

* **stop_role_permission** (node_id, worker_id, realm_id, role_id, permission_id) -> permission_stopped

where

* **node_id** (string): ID of node running the (router) worker to stop the permission on
* **worker_id** (string): ID of the (router) worker to stop the permission on
* **realm_id** (string): ID of the realm to stop the permission on
* **role_id** (string): ID of the role to stop the permission on
* **realm_id** (string): ID of the permission to stop.

and

* **permission_stopped** (dict): permission stopped information object

is returned:

```javascript
{
   // FIXME
}
```

The call does not return until the permission has completely stopped.

When the permission *is stopped*, an event

* **on_role_permission_stopped** (node_id, worker_id, realm_id, role_id, permission_id, permission_stopped)

is fired.

---


### crossbarfabriccenter.remote.router.get_transports

Return a list of IDs of transports for the given router.

* **get_transports** (node_id, worker_id) -> [transport_id]

where

* **node_id** (string): ID of node running the router to get transports for
* **worker_id** (string): ID of the (router) worker to get transports for

and

* **transport_id** (string): transport ID

is returned:

```javascript
["transport1", "transport2"]
```

> The order of IDs within the list returned is unspecified, but stable.

---


### crossbarfabriccenter.remote.router.get_transport

Return detailed information about the given router transport.

* **get_transport** (node_id, worker_id, transport_id) -> transport

where

* **node_id** (string): ID of node running the router with the transport to get information for
* **worker_id** (string): ID of the (router) worker with the transport to get information for
* **transport_id** (string): ID of the (router) transport to get information for

where

* **transport** (dict): router transport information object

is returned:

```javascript
{
   // FIXME
}
```

---


### crossbarfabriccenter.remote.router.start_transport

Start a new router transport on the given (router) worker.

* **start_transport** (node_id, worker_id, transport_id, transport_config) -> transport_started

where

* **node_id** (string): ID of node running the router to start the transport on
* **worker_id** (string): ID of the (router) worker to start the transport on
* **transport_id** (string): optional ID of the (router) transport to start. when not given, auto-generated
* **transport_config** (dict): configuration of the transport to start

and

* **transport_started** (dict): transport started information

is returned:

```javascript
{
   // FIXME
}
```

The call does not return until the transport has completely started.

When the new transport *is starting*, an event

* **on_transport_starting** (node_id, worker_id, transport_id)

is fired.

When the new transport *is completely started*, an event

* **on_transport_started** (node_id, worker_id, transport_id, transport_started)

is fired.

---


### crossbarfabriccenter.remote.router.stop_transport

Stop a router transport currently running in the given (router) worker.

* **stop_transport** (node_id, worker_id, transport_id) -> transport_stopped

where

* **node_id** (string): ID of node running the router to stop the transport on
* **worker_id** (string): ID of the (router) worker to stop the transport on
* **transport_id** (string): ID of the (router) transport to stop

where

* **transport_stopped** (dict): transport stopped information

is returned:

```javascript
{
   // FIXME
}
```

The call does not return until the transport has completely stopped.

When the transport *is stopping*, an event

* **on_transport_stopping** (node_id, worker_id, transport_id)

is fired.

When the transport *is completely stopped*, an event

* **on_transport_stopped** (node_id, worker_id, transport_id, transport_stopped)

is fired.

---


### crossbarfabriccenter.remote.router.get_transport_services

* **get_transport_services** (node_id, worker_id, transport_id) -> [path_id]

---


### crossbarfabriccenter.remote.router.get_transport_service

* **get_transport_service** (node_id, worker_id, transport_id, path_id) -> path

---


### crossbarfabriccenter.remote.router.start_transport_service

* **start_transport_service** (node_id, worker_id, transport_id, path_id, transport_service_config) -> path_started

---


### crossbarfabriccenter.remote.router.stop_transport_service

* **stop_transport_service** (node_id, worker_id, transport_id, path_id) -> path_stopped

---


### crossbarfabriccenter.remote.router.get_components

Return list of IDs of components in this router worker.

* **get_components** (node_id, worker_id) -> [component_id]

where

* **node_id** (string): ID of node running the router to get transports for
* **worker_id** (string): ID of the (router) worker to get transports for

and

* **component_id** (string): component ID

is returned:

```javascript
["component1", "component2"]
```

> The order of IDs within the list returned is unspecified, but stable.

---


### crossbarfabriccenter.remote.router.get_component

Return detailed information about the given router component.

* **get_component** (node_id, worker_id, component_id) -> component

where

* **node_id** (string): ID of node running the router to get the component for
* **worker_id** (string): ID of the (router) worker to get the component for
* **component_id** (string): ID of the component to get information for

and

* **component** (dict): component information object

is returned:

```javascript
{
   // FIXME
}
```

---

### crossbarfabriccenter.remote.router.start_component

Start a new (native Python) user component in this router worker.

* **start_component** (node_id, worker_id, component_id, component_config) -> component_started

where

* **node_id** (string): ID of node running the router to start the component on
* **worker_id** (string): ID of the (router) worker to start the component on
* **component_id** (string): optional ID of the (router) component to start. when not given, auto-generated
* **component_config** (dict): configuration of the component to start

and

* **component_started** (dict): component started information

is returned:

```javascript
{
   // FIXME
}
```

The call does not return until the component has completely started.

When the new component *is starting*, an event

* **on_transport_component** (node_id, worker_id, component_id)

is fired.

When the new component *is completely started*, an event

* **on_component_started** (node_id, worker_id, component_id, component_started)

is fired.

---


### crossbarfabriccenter.remote.router.stop_component

Stop a user component running in this router worker.

* **stop_component** (node_id, worker_id) -> component_stopped

where

* **node_id** (string): ID of node running the router to stop the component on
* **worker_id** (string): ID of the (router) worker to stop the component on
* **component_id** (string): ID of the (router) component to stop

where

* **component_stopped** (dict): component stopped information

is returned:

```javascript
{
   // FIXME
}
```

The call does not return until the component has completely stopped.

When the component *is stopping*, an event

* **on_component_stopping** (node_id, worker_id, component_id)

is fired.

When the component *is completely stopped*, an event

* **on_component_stopped** (node_id, worker_id, component_id, component_stopped)

is fired.

---


## Container Workers

**Namespace:**

* **crossbarfabriccenter.remote.container.**

Container workers are native Crossbar.io processes that can host Python user components.

> Restrictions: The user components must be written using AutobahnPython and Twisted, and run under the same Python Crossbar.io runs under.

---


### crossbarfabriccenter.remote.container.get_components

Return list of IDs of (native Python) components in container.

* **get_components** (node_id, worker_id) -> [component_id]


### crossbarfabriccenter.remote.container.get_component

Return detailed information about container component.

* **get_component** (node_id, worker_id, component_id) -> component


### crossbarfabriccenter.remote.container.start_component

Start a new (native Python) component in container.

* **start_component** (node_id, worker_id, component_config) -> component_started


### crossbarfabriccenter.remote.container.stop_component

Stop a component running in the container.

* **stop_component** (node_id, worker_id, component_id) -> component_stopped


## Proxy Workers

**Namespace:**

* **crossbarfabriccenter.remote.proxy.**

---

### crossbarfabriccenter.remote.proxy.get_transports

Return list of IDs of proxy worker transport in a proxy worker.

* **get_transports** (node_id, worker_id) -> [transport_id]


### crossbarfabriccenter.remote.proxy.get_transport

Return detailed information about proxy worker transport in a proxy worker.

* **get_transport** (node_id, worker_id, transport_id) -> transport


### crossbarfabriccenter.remote.proxy.start_transport

Start a new proxy worker transport in this proxy worker.

* **start_transport** (node_id, worker_id, transport_id, transport_config) -> transport_started


### crossbarfabriccenter.remote.proxy.stop_transport

Stop a proxy worker transport running in a proxy worker.

* **stop_transport** (node_id, worker_id, transport_id) -> transport_stopped

---


### crossbarfabriccenter.remote.tracing.get_traces

Return list of IDs of traces on a _router_ worker.

* **get_traces** (node_id, worker_id) -> [trace_id]

where

* **node_id** (string): the ID of the node to get traces from
* **worker_id** (string): the ID of the _router_ worker to get traces from

and

* **trace_id** (string): ID of traces

is returned

```javascript
["trace1", "trace2"]
```

> The order of IDs within the list returned is unspecified, but stable.

---


### crossbarfabriccenter.remote.tracing.get_trace

Return detailed information about a trace on a _router_ worker.

* **get_trace** (node_id, worker_id, trace_id) -> trace

where

* **node_id** (string): the ID of the node to get trace from
* **worker_id** (string): the ID of the _router_ worker to get trace from
* **trace_id** (string): the ID of the trace to get

and

* **trace** (dict): trace information object

is returned:

```javascript
{
   // FIXME
}
```

---


### crossbarfabriccenter.remote.tracing.start_trace

Starts a new trace on a _router_ worker.

* **start_trace** (node_id, worker_id, trace_id, trace_config) -> trace_started

where

* **node_id** (string): the ID of the node to start the trace on
* **worker_id** (string): the ID of the _router_ worker to start the trace on
* **trace_id** (string or null): optional ID of the trace to start. when not given, auto-assign

and

* **trace_started** (dict): trace startup information object

is returned:

```javascript
{
   // FIXME
}
```

When the trace *has been started*, an event

* **on_trace_started** (node_id, worker_id, trace_id, trace_started)

is fired.

---


### crossbarfabriccenter.remote.tracing.stop_trace

Stops a running trace on a _router_ worker.

This procedure explicitly stops a previously started trace. A trace may also be started with a defined run-time, in which case this procedure can still be used to stop the trace prematurely even before the defined run-time has been reached.

* **stop_trace** (node_id, worker_id, trace_id) -> trace_stopped

where

* **node_id** (string): the ID of the node to stop the trace on
* **worker_id** (string): the ID of the _router_ worker to stop the trace on
* **trace_id** (string or null): the ID of the trace to stop

and

* **trace_stopped** (dict): trace stop information object

is returned

```javascript
{
   // FIXME
}
```

When the trace *has been stopped*, an event

* **on_trace_stopped** (node_id, worker_id, trace_id, trace_stopped)

is fired.

> Note that **on_trace_stopped** can also fire without **stop_trace** being ever called, namely when the trace has been started with a defined run-time. In this case, the trace will automatically stop, and the **on_trace_stopped** event automatically fire as well.

---


### crossbarfabriccenter.remote.tracing.get_trace_data

Return trace records from a trace on a _router_ worker.

* **get_trace_data** (node_id, worker_id, trace_id, from_seq, to_seq, limit) -> [trace_record]

where

* **node_id** (string): the ID of the node to get trace records from
* **worker_id** (string): the ID of the _router_ worker to get trace records from
* **trace_id** (string or null): the ID of the trace to get trace records from
* **from_seq** (int): optional "from" sequence number for filtering records to be returned (default: to_seq - limit)
* **to_seq** (int): optional "up to" sequence number for filtering records to be returned (default: last trace record)
* **limit** (int): optional maximum of records to return (default: 100)

and

* **[trace_record]** (list of dict): list of trace records retrieved, with sequence number starting at "from_seq" up to "to_seq", that is, records are returned in ascending sequence number order, with no gaps in between sequence numbers. and at most "limit" records are returned

```javascript
{
    // the sequence number in the trace of messages stored for this trace
    'seq': 4,

    // timestamp when the message was originally traced
    'ts': 1502829396.5978456,

    // performance counter when the message was originally traced
    'pc': 129852.050601509,

    // the direction of the WAMP message flow: Crossbar.io "received" (rx) a message in this case
    'direction': 'rx',

    // the WAMP message type of the message
    'msg_type': 'Publish',

    // the realm, session ID, authid, authrole of the sender of
    // this WAMP message (the publisher in this case)
    'realm': 'realm1',
    'session_id': 1457801355183687,
    'authid': 'E4MW-VYUX-KY3S-Y6US-J5X5-KAUQ',
    'authrole': 'anonymous',

    // message correlation ID: all WAMP messages traced for a given WAMP action
    // like a RPC have identical correlation
    'correlation': 'd5d9bcec-a3eb-4f0e-875b-6933680bb546',

    // the URI for the WAMP action, the same URI for all messages of a given action
    'uri': 'com.example.oncounter',

    // for outgoing messages, a map of serializions to byte length
    // (note: currently missing for incoming messages)
    'serializations': {},

    // actual raw WAMP message right before serialization
    // (note: only if payload_tracing=true when trace was started)
    'msg': [16,
            46,
            {'acknowledge': True, 'exclude_me': False},
            'com.example.oncounter',
            [21, 'E4MW-VYUX-KY3S-Y6US-J5X5-KAUQ', 'Python']],
}
```

---


### crossbarfabriccenter.remote.docker.get_status

Get status information from Docker on host system.

* **get_status** (node_id) -> status

where

* **node_id** (string): the ID of the node to get Docker status from

and

* **status** (dict): Docker status information object

is returned:

```javascript
{
   // FIXME
}
```

---


### crossbarfabriccenter.remote.docker.get_containers

Get list of IDs of Docker containers running on host system

* **get_containers** (node_id) -> [container_id]

where

* **node_id** (string): the ID of the node to get Docker containers for

and

* **container_id** (string): container ID

is returned:

```javascript
["container1", "container2"]
```

---


### crossbarfabriccenter.remote.docker.get_container

Get detailed information for Docker container on host system.

* **get_container** (node_id, container_id) -> container

where

* **node_id** (string): the ID of the node to get the Docker container
* **container_id** (string): the ID of the Docker container

and

* **container** (dict): Docker container information object

is returned:

```javascript
{
   // FIXME
}
```

---


### crossbarfabriccenter.remote.docker.start_container

Start a Docker container on a host system.

* **start_container** (node_id, container_id, container_config) -> container_started

where

* **node_id** (string): the ID of the node to get the Docker container
* **container_id** (string or null): optional ID of the Docker container. when not given, auto-generated
* **container_config** (dict): container configuration object

and

* **container_started** (dict): container started information object

is returned:

```javascript
{
   // FIXME
}
```

---


### crossbarfabriccenter.remote.docker.stop_container

Stop a Docker container running on a host system.

* **stop_container** (node_id, container_id) -> container_stopped

where

* **node_id** (string): the ID of the node with the Docker container (on the host) to stop
* **container_id** (string): the ID of the Docker container to stop

and

* **container_stopped** (dict): container stopped information object

is returned:

```javascript
{
   // FIXME
}
```

---


### crossbarfabriccenter.remote.docker.get_images

Get list of IDs of Docker image on a host system.

* **get_images** (node_id) -> [image_id]

where

* **node_id** (string): the ID of the node with the image (on the host) to get

and

* **image_id** (string): image ID

is returned:

```javascript
["crossbario/crossbar:latest"]
```

> The order of IDs within the list returned is unspecified, but stable.

---


### crossbarfabriccenter.remote.docker.get_image

Get detailed information about a Docker image on a host system.

* **get_image** (node_id, image_id) -> image

where

* **node_id** (string): the ID of the node with the image (on the host) to get
* **image_id** (string): the ID of the Docker image to get

and

* **image** (dict): image information object

is returned:

```javascript
{
   // FIXME
}
```

---


### crossbarfabriccenter.remote.docker.update_image

Update a Docker image on a host system.

* **update_image** (node_id, image_id) -> image_updated

where

* **node_id** (string): the ID of the node to update the image (on the host)
* **image_id** (string): the ID of the Docker image to remove

and

* **image_update** (dict): image update information object

is returned:

```javascript
{
   // FIXME
}
```

---


### crossbarfabriccenter.remote.docker.remove_image

Remove a Docker image from a host system.

* **remove_image** (node_id, image_id) -> image_removed

where

* **node_id** (string): the ID of the node to remove the image (from the host)
* **image_id** (string): the ID of the Docker image to remove

and

* **image_removed** (dict): image removal information object

is returned:

```javascript
{
   // FIXME
}
```

---
