# Management Realms API

Each user created **management realm** (eg `com.example.my-mgmt-realm1`) on Crossbar.io Fabric Center (CFC) exposes the following APIs to clients:

* **[Global API](#global-api)**: management realm wide operations
* **[Remote Meta API](#remote-meta-api)**: remote access to CF nodes WAMP meta API
* **[Remote Management API](#remote-management-api)**: remote access to CF nodes management API

CFC clients can use all three APIs at the same time, and use the functionality provided over whole sets of CF nodes in the management realm.

This single point of entry allows you to create complex automatic application management functions using standard programming patterns, and very little user code to write.

---


## Global API

* [crossbarfabriccenter.get_status](#crossbarfabriccenterget_status)
* [crossbarfabriccenter.get_nodes](#crossbarfabriccenterget_nodes)
* [crossbarfabriccenter.get_node](#crossbarfabriccenterget_node)


## Remote Meta API

* [crossbarfabriccenter.remote.router.meta.*](#crossbarfabriccenterremoteroutermeta)


## Remote Management API

* **Nodes** (crossbarfabriccenter.remote.node.)
  Nodes are instances of Crossbar.io (Fabric) running on host systems, and running from a node directory. Most of the time, nodes run within Docker containers or confined as snaps.

   * [crossbarfabriccenter.remote.node.get_status](#crossbarfabriccenterremotenodeget_status)
   * [crossbarfabriccenter.remote.node.shutdown](#crossbarfabriccenterremotenodeshutdown)
   * [crossbarfabriccenter.remote.node.get_workers](#crossbarfabriccenterremotenodeget_workers)
   * [crossbarfabriccenter.remote.node.get_worker](#crossbarfabriccenterremotenodeget_worker)
   * [crossbarfabriccenter.remote.node.start_worker](#crossbarfabriccenterremotenodestart_worker)
   * [crossbarfabriccenter.remote.node.stop_worker](#crossbarfabriccenterremotenodestop_worker)

* **Native Workers** (crossbarfabriccenter.remote.worker.)
  Native workers are node worker processes of the types **router**, **container** and **proxy**. The API here allows to retrieve worker logs, control the worker CPU affinity and run code profilers in a live running system.

    * [crossbarfabriccenter.remote.worker.shutdown](#crossbarfabriccenterremoteworkershutdown)
    * [crossbarfabriccenter.remote.worker.get_status](#crossbarfabriccenterremoteworkerget_status)
    * [crossbarfabriccenter.remote.worker.get_pythonpath](#crossbarfabriccenterremoteworkerget_pythonpath)
    * [crossbarfabriccenter.remote.worker.add_pythonpath](#crossbarfabriccenterremoteworkeradd_pythonpath)
    * [crossbarfabriccenter.remote.worker.get_worker_log](#crossbarfabriccenterremoteworkerget_worker_log)
    * [crossbarfabriccenter.remote.worker.get_cpu_count](#crossbarfabriccenterremoteworkerget_cpu_count)
    * [crossbarfabriccenter.remote.worker.get_cpu_affinity](#crossbarfabriccenterremoteworkerget_cpu_affinity)
    * [crossbarfabriccenter.remote.worker.set_cpu_affinity](#crossbarfabriccenterremoteworkerset_cpu_affinity)
    * [crossbarfabriccenter.remote.worker.get_profilers](#crossbarfabriccenterremoteworkerget_profilers)
    * [crossbarfabriccenter.remote.worker.start_profiler](#crossbarfabriccenterremoteworkerstart_profiler)
    * [crossbarfabriccenter.remote.worker.get_profile](#crossbarfabriccenterremoteworkerget_profile)

* **Router Workers** (crossbarfabriccenter.remote.router.)
  Routers are the core of Crossbar.io. They are native worker processes that run the routing code of Crossbar.io as well as endpoint listeners, Web services and other transports. The API here allows for remote and dynamic management of router workers.

    * **Router Realms**
      All routing of messages in Crossbar.io is isolated in different routing confinements called realms. Realms, at the same time, also provide namespace isolation, as URIs as always interpreted with respect to the realm within they occur. URIs portable accross realms - if required - needs to be arranged for by the user.

        * [crossbarfabriccenter.remote.router.get_router_realms](#crossbarfabriccenterremoterouterget_router_realms)
        * [crossbarfabriccenter.remote.router.get_router_realm](#crossbarfabriccenterremoterouterget_router_realm)
        * [crossbarfabriccenter.remote.router.start_router_realm](#crossbarfabriccenterremoterouterstart_router_realm)
        * [crossbarfabriccenter.remote.router.stop_router_realm](#crossbarfabriccenterremoterouterstop_router_realm)

    * **Realm Roles**
      Roles are bundles of permissions defined on a realm. When a client connects to the router and authenticates successfully, it is assigned a **role**. This role will then determine the actual permissions the client is granted by the router.

        * [crossbarfabriccenter.remote.router.get_realm_roles](#crossbarfabriccenterremoterouterget_realm_roles)
        * [crossbarfabriccenter.remote.router.get_realm_role](#crossbarfabriccenterremoterouterget_realm_role)
        * [crossbarfabriccenter.remote.router.start_realm_role](#crossbarfabriccenterremoterouterstart_realm_role)
        * [crossbarfabriccenter.remote.router.stop_realm_role](#crossbarfabriccenterremoterouterstop_realm_role)

    * **Router Transports**
      Routers will want to listen for incoming client connections on so-called listening endpoints. The API here allows the dynamic startup and shutdown of router liensting endpoints in the form of transports.

        * [crossbarfabriccenter.remote.router.get_router_transports](#crossbarfabriccenterremoterouterget_router_transports)
        * [crossbarfabriccenter.remote.router.get_router_transport](#crossbarfabriccenterremoterouterget_router_transport)
        * [crossbarfabriccenter.remote.router.start_router_transport](#crossbarfabriccenterremoterouterstart_router_transport)
        * [crossbarfabriccenter.remote.router.stop_router_transport](#crossbarfabriccenterremoterouterstop_router_transport)

    * **Transport Paths**
      Some router transports, such as Web transports, allow to configure *path services* attached to URL parts in a Web resource tree. The API here allows to dynamically configure Web services, such as a static Web or file download service on dynamic URL part in the Web resource tree of Web transports.

        * [crossbarfabriccenter.remote.router.get_transport_paths](#crossbarfabriccenterremoterouterget_transport_paths)
        * [crossbarfabriccenter.remote.router.get_transport_path](#crossbarfabriccenterremoterouterget_transport_path)
        * [crossbarfabriccenter.remote.router.start_transport_path](#crossbarfabriccenterremoterouterstart_transport_path)
        * [crossbarfabriccenter.remote.router.stop_transport_path](#crossbarfabriccenterremoterouterstop_transport_path)

    * **Router Components**
      Router workers are native Crossbar.io processes that can host Python user components. Restrictions: The user components must be written using AutobahnPython and Twisted, and run under the same Python Crossbar.io runs under. Further, running user components in the same OS process as Crossbar.io routing code can lead to instability, and provides less security isolation. Router components should only be used very selectively for small amounts of code, such as dynamic authenticators or authorizers.

        * [crossbarfabriccenter.remote.router.get_router_components](#crossbarfabriccenterremoterouterget_router_components)
        * [crossbarfabriccenter.remote.router.get_router_component](#crossbarfabriccenterremoterouterget_router_component)
        * [crossbarfabriccenter.remote.router.start_router_component](#crossbarfabriccenterremoterouterstart_router_component)
        * [crossbarfabriccenter.remote.router.stop_router_component](#crossbarfabriccenterremoterouterstop_router_component)

* **Container Workers**

    * [crossbarfabriccenter.remote.container.get_container_components](#crossbarfabriccenterremotecontainerget_container_components)
    * [crossbarfabriccenter.remote.container.get_container_component](#crossbarfabriccenterremotecontainerget_container_component)
    * [crossbarfabriccenter.remote.container.start_container_component](#crossbarfabriccenterremotecontainerstart_container_component)
    * [crossbarfabriccenter.remote.container.stop_container_component](#crossbarfabriccenterremotecontainerstop_container_component)

* **Proxy Workers**

    * [crossbarfabriccenter.remote.proxy.get_proxy_transports](#crossbarfabriccenterremoteproxyget_proxy_transports)
    * [crossbarfabriccenter.remote.proxy.get_proxy_transport](#crossbarfabriccenterremoteproxyget_proxy_transport)
    * [crossbarfabriccenter.remote.proxy.start_proxy_transport](#crossbarfabriccenterremoteproxystart_proxy_transport)
    * [crossbarfabriccenter.remote.proxy.stop_proxy_transport](#crossbarfabriccenterremoteproxystop_proxy_transport)

* **Message Tracing** (crossbarfabriccenter.remote.tracing.)
  Tap into the message flow of Crossbar.io Fabric nodes. Monitor and trace real-time message traffic and routing down to the single message level.

    * [crossbarfabriccenter.remote.tracing.get_router_traces](#crossbarfabriccenterremotetracingget_router_traces)
    * [crossbarfabriccenter.remote.tracing.get_router_trace](#crossbarfabriccenterremotetracingget_router_trace)
    * [crossbarfabriccenter.remote.tracing.start_router_trace](#crossbarfabriccenterremotetracingstart_router_trace)
    * [crossbarfabriccenter.remote.tracing.stop_router_trace](#crossbarfabriccenterremotetracingstop_router_trace)
    * [crossbarfabriccenter.remote.tracing.get_router_trace_data](#crossbarfabriccenterremotetracingget_router_trace_data)

* **Docker Control** (crossbarfabriccenter.remote.docker.)
  Remotely control the Docker daemons of hosts running Crossbar.io Fabric nodes.


    * [crossbarfabriccenter.remote.docker.get_docker_status](#crossbarfabriccenterremotedockerget_docker_status)
    * [crossbarfabriccenter.remote.docker.get_docker_containers](#crossbarfabriccenterremotedockerget_docker_containers)
    * [crossbarfabriccenter.remote.docker.get_docker_container](#crossbarfabriccenterremotedockerget_docker_container)
    * [crossbarfabriccenter.remote.docker.start_docker_container](#crossbarfabriccenterremotedockerstart_docker_container)
    * [crossbarfabriccenter.remote.docker.stop_docker_container](#crossbarfabriccenterremotedockerstop_docker_container)
    * [crossbarfabriccenter.remote.docker.get_docker_images](#crossbarfabriccenterremotedockerget_docker_images)
    * [crossbarfabriccenter.remote.docker.get_docker_image](#crossbarfabriccenterremotedockerget_docker_image)
    * [crossbarfabriccenter.remote.docker.update_docker_image](#crossbarfabriccenterremotedockerupdate_docker_image)
    * [crossbarfabriccenter.remote.docker.remove_docker_image](#crossbarfabriccenterremotedockerremove_docker_image)

---


## Procedures Reference

Signature and descriptions of API procedures.

---


### crossbarfabriccenter.get_status

Return management realm status information.

* **get_status** () -> status

where

* **status** (dict): status information object

---


### crossbarfabriccenter.get_nodes

Return list of IDs of nodes in the management realm.

* **get_nodes ()** -> [node_id]

> The order of IDs within the list returned is unspecified, but stable.

---


### crossbarfabriccenter.get_node

Return detailed information about a node in the management realm.

* **get_node** (node_id) -> node

where

* **node_id** (string): ID of the node to retrieve information for

and

* **node** (dict): node information object

---

### crossbarfabriccenter.remote.meta.*

Crossbar.io implements the WAMP meta API at the app router level:

* [Session Meta Events and Procedures](http://crossbar.io/docs/Session-Metaevents-and-Procedures/)
* [Subscription Meta Events and Procedures](http://crossbar.io/docs/Subscription-Meta-Events-and-Procedures/)
* [Registration Meta-Events and Procedures](http://crossbar.io/docs/Registration-Meta-Events-and-Procedures/)

Exposing the WAMP meta API at the app router level is enabled by default, but can be disabled by setting `enable_meta_api: false` in the [realms options](https://github.com/crossbario/crossbar/blob/master/docs/pages/administration/router/Router-Realms.md#realm-options).

Exposing the WAMP meta API to CFC however is disabled by default, and needs to be enabled by setting `bridge_meta_api: true` in the router options.

If the bridging of the WAMP meta API is enabled, all above procedures and topics will be available prefixed with an additional `crossbarfabriccenter.remote.meta.`.

So, for example, the WAMP meta API procedure

* `wamp.session.list ()`

that returns a list of WAMP session IDs of session currently joined on the realm is exposed via CFC under

* `crossbarfabriccenter.remote.meta.wamp.session.list (node_id, worker_id, realm_id)`

This allows CFC clients to remotely call into the WAMP meta API of any of the CF nodes connected.

WAMP meta events are translated similar. That is, events destined for topic

* `wamp.session.on_join (session_id, session_details)`

can be subscribed under

* `crossbarfabriccenter.remote.meta.wamp.session.on_join (node_id, worker_id, realm_id, session_id, session_details)`

---


### crossbarfabriccenter.remote.node.get_status

Retrieve status information (directly) from a node.

* **get_status** (node_id) -> status

where

* **node_id** (string): ID of the node to retrieve status from

and

* **status** (dict): Node status information object.

---


### crossbarfabriccenter.remote.node.shutdown

Orderly shutdown a node (from within the node).

* **shutdown** (node_id) -> node_shutdown

where

* **node_id** (string): ID of the node to shut down

and

* **node_shutdown** (dict): Node (final) shutdown information object.

---


### crossbarfabriccenter.remote.node.get_workers

Get list of IDs of workers in node.

* **get_workers** (node_id) -> [worker_id]

where

* **node_id** (string): ID of the node to get workers for

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

---


### crossbarfabriccenter.remote.node.stop_worker

Stop a worker currently running on a node.

* **stop_worker** (node_id, worker_id) -> worker_stopped

* **node_id** (string): ID of the node to stop the worker on
* **worker_id** (string): ID of the worker to stop

and

* **worker_stopped** (dict): worker stopped information object

---


### crossbarfabriccenter.remote.worker.get_status

Get status of native worker (from inside the worker).

* **get_status** (node_id, worker_id) -> status

where

* **node_id** (string): ID of node running the worker to get status for
* **worker_id** (string): ID of the worker to get status for

and

* **status** (dict): worker status information object

---


### crossbarfabriccenter.remote.worker.shutdown

Orderly shutdown the worker (from inside).

* **shutdown** (node_id, worker_id) -> worker_shutdown

where

* **node_id** (string): ID of node running the worker to shut down
* **worker_id** (string): ID of the worker to shut down

and

* **worker_shutdown** (dict): worker shutdown information object

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

---


### crossbarfabriccenter.remote.worker.get_pythonpath

Returns the current Python module search paths in the (native) worker.

* **get_pythonpath** (node_id, worker_id) -> [string]

where

* **node_id** (string): ID of node running the worker to get Python search paths for
* **worker_id** (string): ID of the worker to get Python search paths for

---


### crossbarfabriccenter.remote.worker.add_pythonpath

* **add_pythonpath** (node_id, worker_id, paths, prepend) -> path_added

where

* **node_id** (string): ID of node running the worker to add Python search p
* **worker_id** (string): ID of the worker to add Python search paths to
* **prepend** (boolean): if True, prepend the search paths to the current list, else append at the end

and

* **path_added** (dict): Python search paths added information object

---


### crossbarfabriccenter.remote.worker.get_cpu_count

Returns the CPU core count on the machine this worker (process) is running on.

> Given `CPU_COUNT`, valid CPU (core) IDs then are `[0, CPU_COUNT[`.

* **get_cpu_count** (node_id, worker_id) -> int

where

* **node_id** (string): ID of node running the worker to get CPU count for
* **worker_id** (string): ID of the worker to get CPU count for

---


### crossbarfabriccenter.remote.worker.get_cpu_affinity

Get current CPU affinity of this worker (process) returning a list of CPU IDs. CPU (cores) are numbered beginning with 0.

* **get_cpu_affinity** (node_id, worker_id) -> [int]

where

* **node_id** (string): ID of node running the worker to get CPU affinity for
* **worker_id** (string): ID of the worker to get CPU affinity for

---


### crossbarfabriccenter.remote.worker.set_cpu_affinity

Set current CPU affinity of this worker (process).

CPU (cores) are numbered beginning with 0, and `cpus` must be a list of IDs given the CPUs eligible to run this worker.

* **set_cpu_affinity** (node_id, worker_id, cpus) -> cpu_affinity_set

where

* **node_id** (string): ID of node running the worker to set CPU affinity for
* **worker_id** (string): ID of the worker to set CPU affinity for
* **cpus** (list of int): the CPU (core) IDs to set the affinity to

and

* **cpu_affinity_set** (dict): CPU affinity set information object

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

or

* **profile_record** (dict): profile result record

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

---


### crossbarfabriccenter.remote.router.get_router_realms

Return a list of IDs of realms in the given router worker.

* **get_router_realms** (node_id, worker_id) -> [realm_id]

where

* **node_id** (string): ID of node running the worker to get realms for
* **worker_id** (string): ID of the worker to get realms for

> The order of IDs within the list returned is unspecified, but stable.

---


### crossbarfabriccenter.remote.router.get_router_realm

Return detailed information about the given realm.

* **get_router_realm** (node_id, worker_id, realm_id) -> realm

where

* **node_id** (string): ID of node running the (router) worker with the realm to to get information for
* **worker_id** (string): ID of the (router) worker with the realm to get informatin for
* **realm_id** (string): ID of the realm to get information for

and

* **realm** (dict): realm information object

---


### crossbarfabriccenter.remote.router.start_router_realm

Start a new realm on the given router worker.

* **start_router_realm** (node_id, worker_id, realm_id, realm_config) -> realm_started

where

* **node_id** (string): ID of node running the (router) worker to start the realm on
* **worker_id** (string): ID of the (router) worker to start the realm on
* **realm_id** (string): optional ID of the realm to start. if not provided, auto-generated.

and

* **realm_started** (dict): realm started information object

The call does not return until the realm has completely started.

When the new realm *is starting*, an event

* **on_router_realm_starting** (node_id, worker_id, realm_id, realm_starting)

is fired.

When the new realm *is completely started*, an event

* **on_router_realm_started** (node_id, worker_id, realm_id, realm_started)

is fired.

---


### crossbarfabriccenter.remote.router.stop_router_realm

Stop a realm currently running in the given router worker.

* **stop_router_realm** (node_id, worker_id, realm_id) -> realm_stopped

where

* **node_id** (string): ID of node running the (router) worker with the realm to stop
* **worker_id** (string): ID of the (router) worker with the realm to stop
* **realm_id** (string): ID of the realm to stop

and

* **realm_stopped** (dict): realm stopped information object

The call does not return until the realm has completely stopped.

When the realm *is stopping*, an event

* **on_router_realm_stopping** (node_id, worker_id, realm_id, realm_stopping)

is fired.

When the realm *is completely stopped*, an event

* **on_router_realm_stopped** (node_id, worker_id, realm_id, realm_stopped)

is fired.

---


### crossbarfabriccenter.remote.router.get_realm_roles

Return a list of IDs of roles in the given realm.

* **get_realm_roles** (node_id, worker_id, realm_id) -> [role_id]

where

* **node_id** (string): ID of node running the (router) worker to get roles for
* **worker_id** (string): ID of the (router) worker to get roles for
* **realm_id** (string): ID of the realm to get roles for

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

The call does not return until the role has completely started.

When the new role *is starting*, an event

* **on_realm_role_starting** (node_id, worker_id, realm_id, role_id, role_starting)

is fired.

When the new role *is completely started*, an event

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

The call does not return until the role has completely stopped.

When the role *is stopping*, an event

* **on_realm_role_stopping** (node_id, worker_id, realm_id, role_id, role_stopping)

is fired.

When the role *is completely stopped*, an event

* **on_router_role_stopped** (node_id, worker_id, realm_id, role_id, role_stopped)

is fired.

---


### crossbarfabriccenter.remote.router.get_router_transports

Return a list of IDs of transports for the given router.

* **get_router_transports** (node_id, worker_id) -> [transport_id]

where

* **node_id** (string): ID of node running the router to get transports for
* **worker_id** (string): ID of the (router) worker to get transports for

> The order of IDs within the list returned is unspecified, but stable.

---


### crossbarfabriccenter.remote.router.get_router_transport

Return detailed information about the given router transport.

* **get_router_transport** (node_id, worker_id, transport_id) -> transport

where

* **node_id** (string): ID of node running the router with the transport to get information for
* **worker_id** (string): ID of the (router) worker with the transport to get information for
* **transport_id** (string): ID of the (router) transport to get information for

where

* **transport** (dict): router transport information object

---


### crossbarfabriccenter.remote.router.start_router_transport

Start a new router transport on the given (router) worker.

* **start_router_transport** (node_id, worker_id, transport_id, transport_config) -> transport_started

where

* **node_id** (string): ID of node running the router to start the transport on
* **worker_id** (string): ID of the (router) worker to start the transport on
* **transport_id** (string): optional ID of the (router) transport to start. when not given, auto-generated
* **transport_config** (dict): configuration of the transport to start

and

* **transport_started** (dict): transport started information

The call does not return until the transport has completely started.

When the new transport *is starting*, an event

* **on_router_transport_starting** (node_id, worker_id, transport_id, transport_starting)

is fired.

When the new transport *is completely started*, an event

* **on_router_transport_started** (node_id, worker_id, transport_id, transport_started)

is fired.

---


### crossbarfabriccenter.remote.router.stop_router_transport

Stop a router transport currently running in the given (router) worker.

* **stop_router_transport** (node_id, worker_id, transport_id) -> transport_stopped

where

* **node_id** (string): ID of node running the router to stop the transport on
* **worker_id** (string): ID of the (router) worker to stop the transport on
* **transport_id** (string): ID of the (router) transport to stop

where

* **transport_stopped** (dict): transport stopped information

The call does not return until the transport has completely stopped.

When the transport *is stopping*, an event

* **on_router_transport_stopping** (node_id, worker_id, transport_id, transport_stopping)

is fired.

When the transport *is completely stopped*, an event

* **on_router_transport_stopped** (node_id, worker_id, transport_id, transport_stopped)

is fired.

---


### crossbarfabriccenter.remote.router.get_transport_paths

* **get_transport_paths** (node_id, worker_id, transport_id) -> [path_id]


### crossbarfabriccenter.remote.router.get_transport_path

* **get_transport_path** (node_id, worker_id, transport_id, path_id) -> path


### crossbarfabriccenter.remote.router.start_transport_path

* **start_transport_path** (node_id, worker_id, transport_id, path_id, transport_path_config) -> path_started


### crossbarfabriccenter.remote.router.stop_transport_path

* **stop_transport_path** (node_id, worker_id, transport_id, path_id) -> path_stopped


### crossbarfabriccenter.remote.router.get_router_components

Return list of IDs of components in this router worker.

* **get_router_components** (node_id, worker_id) -> [component_id]


### crossbarfabriccenter.remote.router.get_router_component

Return detailed information about the given router component.

* **get_router_component** (node_id, worker_id, component_id) -> component


### crossbarfabriccenter.remote.router.start_router_component

Start a new (native Python) user component in this router worker.

* **start_router_component** (node_id, worker_id, component_id, component_config) -> component_started


### crossbarfabriccenter.remote.router.stop_router_component

Stop a user component running in this router worker.

* **stop_router_component** (node_id, worker_id) -> component_stopped


## Container Workers

**Namespace:**

* **crossbarfabriccenter.remote.container.**

Container workers are native Crossbar.io processes that can host Python user components.

> Restrictions: The user components must be written using AutobahnPython and Twisted, and run under the same Python Crossbar.io runs under.

---


### crossbarfabriccenter.remote.container.get_container_components

Return list of IDs of (native Python) components in container.

* **get_container_components** (node_id, worker_id) -> [component_id]


### crossbarfabriccenter.remote.container.get_container_component

Return detailed information about container component.

* **get_container_component** (node_id, worker_id, component_id) -> component


### crossbarfabriccenter.remote.container.start_container_component

Start a new (native Python) component in container.

* **start_container_component** (node_id, worker_id, component_config) -> component_started


### crossbarfabriccenter.remote.container.stop_container_component

Stop a component running in the container.

* **stop_container_component** (node_id, worker_id, component_id) -> component_stopped


## Proxy Workers

**Namespace:**

* **crossbarfabriccenter.remote.proxy.**

---

### crossbarfabriccenter.remote.proxy.get_proxy_transports

Return list of IDs of proxy worker transport in a proxy worker.

* **get_proxy_transports** (node_id, worker_id) -> [transport_id]


### crossbarfabriccenter.remote.proxy.get_proxy_transport

Return detailed information about proxy worker transport in a proxy worker.

* **get_proxy_transport** (node_id, worker_id, transport_id) -> transport


### crossbarfabriccenter.remote.proxy.start_proxy_transport

Start a new proxy worker transport in this proxy worker.

* **start_proxy_transport** (node_id, worker_id, transport_id, transport_config) -> transport_started


### crossbarfabriccenter.remote.proxy.stop_proxy_transport

Stop a proxy worker transport running in a proxy worker.

* **stop_proxy_transport** (node_id, worker_id, transport_id) -> transport_stopped

---


### crossbarfabriccenter.remote.tracing.get_router_traces

Return list of IDs of traces on a router worker.

* **get_router_traces** (node_id, worker_id) -> [trace_id]

where

* **node_id** (string): the ID of the node to get traces from
* **worker_id** (string): the ID of the worker to get traces from

> The order of IDs within the list returned is unspecified, but stable.

---


### crossbarfabriccenter.remote.tracing.get_router_trace

Return detailed information about a trace on a router worker.

* **get_router_trace (node_id, worker_id, trace_id) -> trace

where

* **node_id** (string): the ID of the node to get trace from
* **worker_id** (string): the ID of the worker to get trace from
* **trace_id** (string): the ID of the trace to get

and

* **trace** (dict): trace information object

---


### crossbarfabriccenter.remote.tracing.start_router_trace

Starts a new trace on a router worker.

* **start_router_trace** (node_id, worker_id, trace_id, trace_config) -> trace_started

where

* **node_id** (string): the ID of the node to start the trace on
* **worker_id** (string): the ID of the worker to start the trace on
* **trace_id** (string or null): optional ID of the trace to start. when not given, auto-assign

and

* **trace_started** (dict): trace startup information object

---


### crossbarfabriccenter.remote.tracing.stop_router_trace

Stops a running trace on a router worker.

* **stop_router_trace** (node_id, worker_id, trace_id) -> trace_stopped

where

* **node_id** (string): the ID of the node to stop the trace on
* **worker_id** (string): the ID of the worker to stop the trace on
* **trace_id** (string or null): the ID of the trace to stop

and

* **trace_stopped** (dict): trace stop information object

---


### crossbarfabriccenter.remote.tracing.get_router_trace_data

Return trace records from a trace on a router worker.

* **get_router_trace_data** (node_id, worker_id, trace_id, from_seq_ to_seq, limit) -> [trace_record]

where

* **node_id** (string): the ID of the node to get trace records from
* **worker_id** (string): the ID of the worker to get trace records from
* **trace_id** (string or null): the ID of the trace to get trace records from
* **from_seq** (int):
* **to_seq** (int):
* **limit** (int):

and

* **[trace_record]** (list of dict): list of trace records retrieved

---


### crossbarfabriccenter.remote.docker.get_docker_status

Get status information from Docker on host system.

* **get_docker_status** (node_id) -> status

where

* **node_id** (string): the ID of the node to get Docker status from

and

* **status** (dict): Docker status information object

---


### crossbarfabriccenter.remote.docker.get_docker_containers

Get list of IDs of Docker containers running on host system

* **get_docker_containers** (node_id) -> [container_id]

where

* **node_id** (string): the ID of the node to get Docker containers for

---


### crossbarfabriccenter.remote.docker.get_docker_container

Get detailed information for Docker container on host system.

* **get_docker_container** (node_id, container_id) -> container

where

* **node_id** (string): the ID of the node to get the Docker container
* **container_id** (string): the ID of the Docker container

and

* **container** (dict): Docker container information object

---


### crossbarfabriccenter.remote.docker.start_docker_container

Start a Docker container on a host system.

* **start_docker_container** (node_id, container_id, container_config) -> container_started

where

* **node_id** (string): the ID of the node to get the Docker container
* **container_id** (string or null): optional ID of the Docker container. when not given, auto-generated
* **container_config** (dict): container configuration object

and

* **container_started** (dict): container started information object


### crossbarfabriccenter.remote.docker.stop_docker_container

Stop a Docker container running on a host system.

* **stop_docker_container** (node_id, container_id) -> container_stopped

where

* **node_id** (string): the ID of the node with the Docker container (on the host) to stop
* **container_id** (string): the ID of the Docker container to stop

and

* **container_stopped** (dict): container stopped information object


### crossbarfabriccenter.remote.docker.get_docker_images

Get list of IDs of Docker image on a host system.

* **get_docker_images** (node_id) -> [image_id]

where

* **node_id** (string): the ID of the node with the image (on the host) to get

> The order of IDs within the list returned is unspecified, but stable.

---


### crossbarfabriccenter.remote.docker.get_docker_image

Get detailed information about a Docker image on a host system.

* **get_docker_image** (node_id, image_id) -> image

where

* **node_id** (string): the ID of the node with the image (on the host) to get
* **image_id** (string): the ID of the Docker image to get

and

* **image** (dict): image information object

---


### crossbarfabriccenter.remote.docker.update_docker_image

Update a Docker image on a host system.

* **update_docker_image** (node_id, image_id) -> image_updated

where

* **node_id** (string): the ID of the node to update the image (on the host)
* **image_id** (string): the ID of the Docker image to remove

and

* **image_update** (dict): image update information object

---


### crossbarfabriccenter.remote.docker.remove_docker_image

Remove a Docker image from a host system.

* **remove_docker_image** (node_id, image_id) -> image_removed

where

* **node_id** (string): the ID of the node to remove the image (from the host)
* **image_id** (string): the ID of the Docker image to remove

and

* **image_removed** (dict): image removal information object

---
