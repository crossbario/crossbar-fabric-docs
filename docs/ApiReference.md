# Crossbar.io Fabric Center API Reference

Crossbar.io Fabric Center (CFC) exposes a rich set of APIs to user management tools and applications.

Clients connect to CFC under one óf two realms:

1. the global users realm (com.crossbario.fabric)
2. a specific user management realm

The former allows users to create new management realms, pair nodes with such realms and manage their user profiles.

The latter actually are for managing user nodes. Both Crossbar.io Fabric nodes and user management tools and apps connect to previously created management realms in regular operation.


## Global Users Realm API

The global users realm (`com.crossbario.fabric`) on CFC exposes the following API:

1. [cfc.get_status](#cfcget_status)
1. [cfc.get_management_realms](#cfcget_management_realms)
1. [cfc.get_management_realm](#cfcget_management_realm)
1. [cfc.create_management_realm](#cfccreate_management_realm)
1. [cfc.delete_management_realm](#cfcdelete_management_realm)
1. [cfc.get_nodes](#cfcget_nodes)
1. [cfc.get_node](#cfcget_node)
1. [cfc.pair_node](#cfcpair_node)
1. [cfc.unpair_node](#cfcunpair_node)


## User Management Realms

User management realms are created by users. CFC will then automatically start a backend dedicated to the user's management realm.

CFC exposes the following three APIs for :

* **Global API**: management realm wide operations
* **Remote Meta API**: remote access to CF nodes WAMP meta API
* **Remote Management API**: remote access to CF nodes management API

CFC clients can use all three APIs at the same time, and use the functionality provided over whole sets of CF nodes in the management realm.

This single point of entry allows you to create complex automatic application management functions using standard programming patterns, and very little user code to write.


**Global API**

* [cfc.get_status](#cfcget_status)
* [cfc.get_nodes](#cfcget_nodes)
* [cfc.get_node](#cfcget_node)

**Remote Meta API**

* [cfc.remote.router.meta.*](#cfcremoteroutermeta)

**Remote Management API**

1. [Nodes](#nodes)
   1. [cfc.remote.node.get_status](#cfcremotenodeget_status)
   1. [cfc.remote.node.shutdown](#cfcremotenodeshutdown)
   1. [cfc.remote.node.get_workers](#cfcremotenodeget_workers)
   1. [cfc.remote.node.get_worker](#cfcremotenodeget_worker)
   1. [cfc.remote.node.start_worker](#cfcremotenodestart_worker)
   1. [cfc.remote.node.stop_worker](#cfcremotenodestop_worker)
1. [Workers](#workers)
    1. [cfc.remote.worker.shutdown](#cfcremoteworkershutdown)
    1. [cfc.remote.worker.get_status](#cfcremoteworkerget_status)
    1. [cfc.remote.worker.get_pythonpath](#cfcremoteworkerget_pythonpath)
    1. [cfc.remote.worker.add_pythonpath](#cfcremoteworkeradd_pythonpath)
    1. [cfc.remote.worker.get_worker_log](#cfcremoteworkerget_worker_log)
    1. [cfc.remote.worker.get_cpu_affinity](#cfcremoteworkerget_cpu_affinity)
    1. [cfc.remote.worker.set_cpu_affinity](#cfcremoteworkerset_cpu_affinity)
    1. [cfc.remote.worker.get_profilers](#cfcremoteworkerget_profilers)
    1. [cfc.remote.worker.start_profiler](#cfcremoteworkerstart_profiler)
    1. [cfc.remote.worker.get_profile](#cfcremoteworkerget_profile)
1. [Routers](#routers)
    1. [Router Realms](#routerrealms)
        1. [cfc.remote.router.get_router_realms](#cfcremoterouterget_router_realms)
        1. [cfc.remote.router.get_router_realm](#cfcremoterouterget_router_realm)
        1. [cfc.remote.router.start_router_realm](#cfcremoterouterstart_router_realm)
        1. [cfc.remote.router.stop_router_realm](#cfcremoterouterstop_router_realm)
    1. [Realm Roles](Realm Roles)
        1. [cfc.remote.router.get_realm_roles](#cfcremoterouterget_realm_roles)
        1. [cfc.remote.router.get_realm_role](#cfcremoterouterget_realm_role)
        1. [cfc.remote.router.start_realm_role](#cfcremoterouterstart_realm_role)
        1. [cfc.remote.router.stop_realm_role](#cfcremoterouterstop_realm_role)
    1. [Router Transports](#routertransports):
        1. [cfc.remote.router.get_router_transports](#cfcremoterouterget_router_transports)
        1. [cfc.remote.router.get_router_transport](#cfcremoterouterget_router_transport)
        1. [cfc.remote.router.start_router_transport](#cfcremoterouterstart_router_transport)
        1. [cfc.remote.router.stop_router_transport](#cfcremoterouterstop_router_transport)
    1. [Transport Paths](#transportpaths):
        1. [cfc.remote.router.get_transport_paths](#cfcremoterouterget_transport_paths)
        1. [cfc.remote.router.get_transport_path](#cfcremoterouterget_transport_path)
        1. [cfc.remote.router.start_transport_path](#cfcremoterouterstart_transport_path)
        1. [cfc.remote.router.stop_transport_path](#cfcremoterouterstop_transport_path)
    1. [Router Components](#routercomponents):
        1. [cfc.remote.router.get_router_components](#cfcremoterouterget_router_components)
        1. [cfc.remote.router.get_router_component](#cfcremoterouterget_router_component)
        1. [cfc.remote.router.start_router_component](#cfcremoterouterstart_router_component)
        1. [cfc.remote.router.stop_router_component](#cfcremoterouterstop_router_component)
1. [Containers*](#containers)
    1. [cfc.remote.container.get_container_components](#cfcremotecontainerget_container_components)
    1. [cfc.remote.container.get_container_component](#cfcremotecontainerget_container_component)
    1. [cfc.remote.container.start_container_component](#cfcremotecontainerstart_container_component)
    1. [cfc.remote.container.stop_container_component](#cfcremotecontainerstop_container_component)
1. [Proxies](#proxies)
    1. [cfc.remote.proxy.get_proxy_transports](#cfcremoteproxyget_proxy_transports)
    1. [cfc.remote.proxy.get_proxy_transport](#cfcremoteproxyget_proxy_transport)
    1. [cfc.remote.proxy.start_proxy_transport](#cfcremoteproxystart_proxy_transport)
    1. [cfc.remote.proxy.stop_proxy_transport](#cfcremoteproxystop_proxy_transport)
1. [Tracing](#tracing)
    1. [cfc.remote.tracing.get_router_traces](#cfcremotetracingget_router_traces)
    1. [cfc.remote.tracing.get_router_trace](#cfcremotetracingget_router_trace)
    1. [cfc.remote.tracing.start_router_trace](#cfcremotetracingstart_router_trace)
    1. [cfc.remote.tracing.stop_router_trace](#cfcremotetracingstop_router_trace)
    1. [cfc.remote.tracing.get_router_trace_data](#cfcremotetracingget_router_trace_data)
1. [Docker](#docker)
    1. [cfc.remote.docker.get_docker_status](#cfcremotedockerget_docker_status)
    1. [cfc.remote.docker.get_docker_containers](#cfcremotedockerget_docker_containers)
    1. [cfc.remote.docker.get_docker_container](#cfcremotedockerget_docker_container)
    1. [cfc.remote.docker.start_docker_container](#cfcremotedockerstart_docker_container)
    1. [cfc.remote.docker.stop_docker_container](#cfcremotedockerstop_docker_container)
    1. [cfc.remote.docker.get_docker_images](#cfcremotedockerget_docker_images)
    1. [cfc.remote.docker.get_docker_image](#cfcremotedockerget_docker_image)
    1. [cfc.remote.docker.update_docker_image](#cfcremotedockerupdate_docker_image)
    1. [cfc.remote.docker.remove_docker_image](#cfcremotedockerremove_docker_image)

---


## Global

**Namespace:**

* **cfc.**


### cfc.get_status

Return management realm status information.

* **get_status** () -> status

where

* **status** (dict): status information object

---


### cfc.get_nodes

Return list of IDs of nodes in the management realm.

* **get_nodes ()** -> [node_id]

> The order of IDs within the list returned is unspecified, but stable.

---


### cfc.get_node

Return detailed information about a node in the management realm.

* **get_node** (node_id) -> node

where

* **node_id** (string): ID of the node to retrieve information for

and

* **node** (dict): node information object

---


## Nodes

Nodes are instances of Crossbar.io (Fabric) running on host systems, and running from a node directory. Most of the time, nodes run within Docker containers or confined as snaps.

**Namespace:**

* **cfc.remote.node.**

---


### cfc.remote.node.get_status

Retrieve status information (directly) from a node.

* **get_status** (node_id) -> status

where

* **node_id** (string): ID of the node to retrieve status from

and

* **status** (dict): Node status information object.

---


### cfc.remote.node.shutdown

Orderly shutdown a node (from within the node).

* **shutdown** (node_id) -> node_shutdown

where

* **node_id** (string): ID of the node to shut down

and

* **node_shutdown** (dict): Node (final) shutdown information object.

---


### cfc.remote.node.get_workers

Get list of IDs of workers in node.

* **get_workers** (node_id) -> [worker_id]

where

* **node_id** (string): ID of the node to get workers for

> The order of IDs within the list returned is unspecified, but stable.

---


### cfc.remote.node.get_worker


* **get_worker** (node_id, worker_id)


### cfc.remote.node.start_worker

* **start_worker** (node_id, worker_id, config)


### cfc.remote.node.stop_worker

* **stop_worker** (node_id, worker_id)


## Native Workers

**Namespace:**

* **cfc.remote.worker.**

---

### cfc.remote.worker.get_status

* **get_status** (node_id, worker_id)

---

### cfc.remote.worker.shutdown

* **shutdown** (node_id, worker_id)

---

### cfc.remote.worker.

* **get_worker_log** (node_id, worker_id)

---

### cfc.remote.worker.get_pythonpath

* **get_pythonpath** (node_id, worker_id)

---

### cfc.remote.worker.add_pythonpath

* **add_pythonpath** (node_id, worker_id)

---

### cfc.remote.worker.get_cpu_affinity

* **get_cpu_affinity** (node_id, worker_id)

---

### cfc.remote.worker.set_cpu_affinity

* **set_cpu_affinity** (node_id, worker_id)

---

### cfc.remote.worker.get_profilers

* **get_profilers** (node_id, worker_id)

---

### cfc.remote.worker.start_profiler

* **start_profiler** (node_id, worker_id)

---

### cfc.remote.worker.get_profile

* **get_profile** (node_id, worker_id)


## Router Workers

Routers are the core of Crossbar.io. They are native worker processes that run the routing code of Crossbar.io as well as endpoint listeners, Web services and other transports.

The API here allows for remote and dynamic management of router workers.

**Namespace:**

* **cfc.remote.router.**


### Realms

All routing of messages in Crossbar.io is isolated in different routing confinements called realms.

Realms, at the same time, also provide namespace isolation, as URIs as always interpreted with respect to the realm within they occur. URIs portable accross realms - if required - needs to be arranged for by the user.


### cfc.remote.router.get_router_realms

Return a list of IDs of realms in the given router worker.

* **get_router_realms** (node_id, worker_id) -> [realm_id]

> The order of IDs within the list returned is unspecified, but stable.


### cfc.remote.router.get_router_realm

Return detailed information about the given realm.

* **get_router_realm** (node_id, worker_id, realm_id) -> realm


### cfc.remote.router.start_router_realm

Start a new realm on the given router worker.

* **start_router_realm** (node_id, worker_id, realm_id, realm_config) -> realm_started

The call does not return until the realm has completely started.

When the new realm *is starting*, an event

* **on_router_realm_starting** (node_id, worker_id, realm_id, realm_starting)

is fired.

When the new realm *is completely started*, an event

* **on_router_realm_started** (node_id, worker_id, realm_id, realm_started)

is fired.


### cfc.remote.router.stop_router_realm

Stop a realm currently running in the given router worker.

* **stop_router_realm** (node_id, worker_id, realm_id) -> realm_stopped


### Roles

Roles are bundles of permissions defined on a realm. When a client connects to the router and authenticates successfully, it is assigned a **role**.

This role will then determine the actual permissions the client is granted by the router.

The management of roles on realms and the permissions associated with roles can be dynamically managed using the API in the following.


### cfc.remote.router.get_router_realm_roles

Return a list of IDs of roles in the given realm.

* **get_router_realm_roles** (node_id, worker_id, realm_id) -> [role_id]

> The order of IDs within the list returned is unspecified, but stable.


### cfc.remote.router.get_router_realm_role

Return detailed information about the given role.

* **get_router_realm_role* (node_id, worker_id, realm_id, role_id) -> role


### cfc.remote.router.start_router_realm_role

Start a new role on the given router worker and realm.

* **start_router_realm_role** (node_id, worker_id, realm_id, role_id, role_config) -> role_created


### cfc.remote.router.stop_router_realm_role

Stop a role currently running in a realm in a router worker.

* **stop_router_realm_role** (node_id, worker_id, realm_id, role_id) -> role_stopped


### Router Transports

Routers will want to listen for incoming client connections on so-called listening endpoints. The API here allows the dynamic startup and shutdown of router liensting endpoints in the form of transports.

### cfc.remote.router.get_router_transports

* **get_router_transports** (node_id, worker_id) -> [transport_id]


### cfc.remote.router.get_router_transport

* **get_router_transport** (node_id, worker_id, transport_id) -> transport


### cfc.remote.router.start_router_transport

* **start_router_transport** (node_id, worker_id, transport_id, transport_config) -> transport_started


### cfc.remote.router.stop_router_transport

* **stop_router_transport** (node_id, worker_id, transport_id) -> transport_stopped


### cfc.remote.router.get_router_transport_paths

* **get_router_transport_paths** (node_id, worker_id, transport_id) -> [path_id]


### cfc.remote.router.get_router_transport_path

* **get_router_transport_path** (node_id, worker_id, transport_id, path_id) -> path


### cfc.remote.router.start_router_transport_path

* **start_router_transport_path** (node_id, worker_id, transport_id, path_id, transport_path_config) -> path_started


### cfc.remote.router.stop_router_transport_path

* **stop_router_transport_path** (node_id, worker_id, transport_id, path_id) -> path_stopped


### Router Components

Router workers are native Crossbar.io processes that can host Python user components.

> Restrictions: The user components must be written using AutobahnPython and Twisted, and run under the same Python Crossbar.io runs under. Further, running user components in the same OS process as Crossbar.io routing code can lead to instability, and provides less security isolation. Router components should only be used very selectively for small amounts of code, such as dynamic authenticators or authorizors.


### cfc.remote.router.get_router_components

Return list of IDs of components in this router worker.

* **get_router_components** (node_id, worker_id) -> [component_id]


### cfc.remote.router.get_router_component

Return detailed information about the given router component.

* **get_router_component** (node_id, worker_id, component_id) -> component


### cfc.remote.router.start_router_component

Start a new (native Python) user component in this router worker.

* **start_router_component** (node_id, worker_id, component_id, component_config) -> component_started


### cfc.remote.router.stop_router_component

Stop a user component running in this router worker.

* **stop_router_component** (node_id, worker_id) -> component_stopped


## Container Workers

**Namespace:**

* **cfc.remote.container.**

Container workers are native Crossbar.io processes that can host Python user components.

> Restrictions: The user components must be written using AutobahnPython and Twisted, and run under the same Python Crossbar.io runs under.

---


### cfc.remote.container.get_container_components

Return list of IDs of (native Python) components in container.

* **get_container_components** (node_id, worker_id) -> [component_id]


### cfc.remote.container.get_container_component

Return detailed information about container component.

* **get_container_component** (node_id, worker_id, component_id) -> component


### cfc.remote.container.start_container_component

Start a new (native Python) component in container.

* **start_container_component** (node_id, worker_id, component_config) -> component_started


### cfc.remote.container.stop_container_component

Stop a component running in the container.

* **stop_container_component** (node_id, worker_id, component_id) -> component_stopped


## Proxy Workers

**Namespace:**

* **cfc.remote.proxy.**

---

### cfc.remote.proxy.get_proxy_transports

Return list of IDs of proxy worker transport in a proxy worker.

* **get_proxy_transports** (node_id, worker_id) -> [transport_id]


### cfc.remote.proxy.get_proxy_transport

Return detailed information about proxy worker transport in a proxy worker.

* **get_proxy_transport** (node_id, worker_id, transport_id) -> transport


### cfc.remote.proxy.start_proxy_transport

Start a new proxy worker transport in this proxy worker.

* **start_proxy_transport** (node_id, worker_id, transport_id, transport_config) -> transport_started


### cfc.remote.proxy.stop_proxy_transport

Stop a proxy worker transport running in a proxy worker.

* **stop_proxy_transport** (node_id, worker_id, transport_id) -> transport_stopped


## Message Tracing

Tap into the message flow of Crossbar.io Fabric nodes. Monitor and trace real-time message traffic and routing down to the single message level.

**Namespace:**

* **cfc.remote.tracing.**

---


### cfc.remote.tracing.get_router_traces

Return list of IDs of traces on a router worker.

* **get_router_traces** (node_id, worker_id) -> [trace_id]

where

* **node_id** (string): the ID of the node to get traces from
* **worker_id** (string): the ID of the worker to get traces from

---


### cfc.remote.tracing.get_router_trace

Return detailed information about a trace on a router worker.

* **get_router_trace (node_id, worker_id, trace_id) -> trace

where

* **node_id** (string): the ID of the node to get trace from
* **worker_id** (string): the ID of the worker to get trace from
* **trace_id** (string): the ID of the trace to get

and

* **trace** (dict): trace information object

---


### cfc.remote.tracing.start_router_trace

Starts a new trace on a router worker.

* **start_router_trace** (node_id, worker_id, trace_id, trace_config) -> trace_started

where

* **node_id** (string): the ID of the node to start the trace on
* **worker_id** (string): the ID of the worker to start the trace on
* **trace_id** (string or null): optional ID of the trace to start. when not given, auto-assign

and

* **trace_started** (dict): trace startup information object

---


### cfc.remote.tracing.stop_router_trace

Stops a running trace on a router worker.

* **stop_router_trace** (node_id, worker_id, trace_id) -> trace_stopped

where

* **node_id** (string): the ID of the node to stop the trace on
* **worker_id** (string): the ID of the worker to stop the trace on
* **trace_id** (string or null): the ID of the trace to stop

and

* **trace_stopped** (dict): trace stop information object

---


### cfc.remote.tracing.get_router_trace_data

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


## Docker Control

Remotely control the Docker daemons of hosts running Crossbar.io Fabric nodes.

**Namespace:**

* **cfc.remote.docker.**

---


### cfc.remote.docker.get_docker_status

Get status information from Docker on host system.

* **get_docker_status** (node_id) -> status

where

* **node_id** (string): the ID of the node to get Docker status from

and

* **status** (dict): Docker status information object

---


### cfc.remote.docker.get_docker_containers

Get list of IDs of Docker containers running on host system

* **get_docker_containers** (node_id) -> [container_id]

where

* **node_id** (string): the ID of the node to get Docker containers for

---


### cfc.remote.docker.get_docker_container

Get detailed information for Docker container on host system.

* **get_docker_container** (node_id, container_id) -> container

where

* **node_id** (string): the ID of the node to get the Docker container
* **container_id** (string): the ID of the Docker container

and

* **container** (dict): Docker container information object

---


### cfc.remote.docker.start_docker_container

Start a Docker container on a host system.

* **start_docker_container** (node_id, container_id, container_config) -> container_started

where

* **node_id** (string): the ID of the node to get the Docker container
* **container_id** (string or null): optional ID of the Docker container. when not given, auto-generated
* **container_config** (dict): container configuration object

and

* **container_started** (dict): container started information object


### cfc.remote.docker.stop_docker_container

Stop a Docker container running on a host system.

* **stop_docker_container** (node_id, container_id) -> container_stopped

where

* **node_id** (string): the ID of the node with the Docker container (on the host) to stop
* **container_id** (string): the ID of the Docker container to stop

and

* **container_stopped** (dict): container stopped information object


### cfc.remote.docker.get_docker_images

Get list of IDs of Docker image on a host system.

* **get_docker_images** (node_id) -> [image_id]

where

* **node_id** (string): the ID of the node with the image (on the host) to get

> The order of IDs within the list returned is unspecified, but stable.

---


### cfc.remote.docker.get_docker_image

Get detailed information about a Docker image on a host system.

* **get_docker_image** (node_id, image_id) -> image

where

* **node_id** (string): the ID of the node with the image (on the host) to get
* **image_id** (string): the ID of the Docker image to get

and

* **image** (dict): image information object

---


### cfc.remote.docker.update_docker_image

Update a Docker image on a host system.

* **update_docker_image** (node_id, image_id) -> image_updated

where

* **node_id** (string): the ID of the node to update the image (on the host)
* **image_id** (string): the ID of the Docker image to remove

and

* **image_update** (dict): image update information object

---


### cfc.remote.docker.remove_docker_image

Remove a Docker image from a host system.

* **remove_docker_image** (node_id, image_id) -> image_removed

where

* **node_id** (string): the ID of the node to remove the image (from the host)
* **image_id** (string): the ID of the Docker image to remove

and

* **image_removed** (dict): image removal information object

---
