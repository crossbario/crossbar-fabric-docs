# Crossbar.io Fabric Center API Reference

**Overview:**

1. [crossbarfabriccenter.get_status](#crossbarfabriccenterget_status)
1. [crossbarfabriccenter.get_nodes](#crossbarfabriccenterget_nodes)
1. [crossbarfabriccenter.get_node](#crossbarfabriccenterget_node)
1. [crossbarfabriccenter.remote.node.get_status](#crossbarfabriccenterremotenodeget_status)
1. [crossbarfabriccenter.remote.node.shutdown](#crossbarfabriccenterremotenodeshutdown)
1. [crossbarfabriccenter.remote.node.get_workers](#crossbarfabriccenterremotenodeget_workers)
1. [crossbarfabriccenter.remote.node.get_worker](#crossbarfabriccenterremotenodeget_worker)
1. [crossbarfabriccenter.remote.node.start_worker](#crossbarfabriccenterremotenodestart_worker)
1. [crossbarfabriccenter.remote.node.stop_worker](#crossbarfabriccenterremotenodestop_worker)
1. [crossbarfabriccenter.remote.worker.shutdown](#crossbarfabriccenterremoteworkershutdown)
1. [crossbarfabriccenter.remote.worker.get_status](#crossbarfabriccenterremoteworkerget_status)
1. [crossbarfabriccenter.remote.worker.get_pythonpath](#crossbarfabriccenterremoteworkerget_pythonpath)
1. [crossbarfabriccenter.remote.worker.add_pythonpath](#crossbarfabriccenterremoteworkeradd_pythonpath)
1. [crossbarfabriccenter.remote.worker.get_worker_log](#crossbarfabriccenterremoteworkerget_worker_log)
1. [crossbarfabriccenter.remote.worker.get_cpu_affinity](#crossbarfabriccenterremoteworkerget_cpu_affinity)
1. [crossbarfabriccenter.remote.worker.set_cpu_affinity](#crossbarfabriccenterremoteworkerset_cpu_affinity)
1. [crossbarfabriccenter.remote.worker.get_profilers](#crossbarfabriccenterremoteworkerget_profilers)
1. [crossbarfabriccenter.remote.worker.start_profiler](#crossbarfabriccenterremoteworkerstart_profiler)
1. [crossbarfabriccenter.remote.worker.get_profile](#crossbarfabriccenterremoteworkerget_profile)
1. [crossbarfabriccenter.remote.router.get_router_realms](#crossbarfabriccenterremoterouterget_router_realms)
1. [crossbarfabriccenter.remote.router.get_router_realm](#crossbarfabriccenterremoterouterget_router_realm)
1. [crossbarfabriccenter.remote.router.start_router_realm](#crossbarfabriccenterremoterouterstart_router_realm)
1. [crossbarfabriccenter.remote.router.stop_router_realm](#crossbarfabriccenterremoterouterstop_router_realm)
1. [crossbarfabriccenter.remote.router.get_router_realm_roles](#crossbarfabriccenterremoterouterget_router_realm_roles)
1. [crossbarfabriccenter.remote.router.get_router_realm_role](#crossbarfabriccenterremoterouterget_router_realm_role)
1. [crossbarfabriccenter.remote.router.start_router_realm_role](#crossbarfabriccenterremoterouterstart_router_realm_role)
1. [crossbarfabriccenter.remote.router.stop_router_realm_role](#crossbarfabriccenterremoterouterstop_router_realm_role)
1. [crossbarfabriccenter.remote.router.get_router_transports](#crossbarfabriccenterremoterouterget_router_transports)
1. [crossbarfabriccenter.remote.router.get_router_transport](#crossbarfabriccenterremoterouterget_router_transport)
1. [crossbarfabriccenter.remote.router.start_router_transport](#crossbarfabriccenterremoterouterstart_router_transport)
1. [crossbarfabriccenter.remote.router.stop_router_transport](#crossbarfabriccenterremoterouterstop_router_transport)
1. [crossbarfabriccenter.remote.router.get_router_transport_paths](#crossbarfabriccenterremoterouterget_router_transport_paths)
1. [crossbarfabriccenter.remote.router.get_router_transport_path](#crossbarfabriccenterremoterouterget_router_transport_path)
1. [crossbarfabriccenter.remote.router.start_router_transport_path](#crossbarfabriccenterremoterouterstart_router_transport_path)
1. [crossbarfabriccenter.remote.router.stop_router_transport_path](#crossbarfabriccenterremoterouterstop_router_transport_path)
1. [crossbarfabriccenter.remote.router.get_router_components](#crossbarfabriccenterremoterouterget_router_components)
1. [crossbarfabriccenter.remote.router.get_router_component](#crossbarfabriccenterremoterouterget_router_component)
1. [crossbarfabriccenter.remote.router.start_router_component](#crossbarfabriccenterremoterouterstart_router_component)
1. [crossbarfabriccenter.remote.router.stop_router_component](#crossbarfabriccenterremoterouterstop_router_component)
1. [crossbarfabriccenter.remote.container.get_container_components](#crossbarfabriccenterremotecontainerget_container_components)
1. [crossbarfabriccenter.remote.container.get_container_component](#crossbarfabriccenterremotecontainerget_container_component)
1. [crossbarfabriccenter.remote.container.start_container_component](#crossbarfabriccenterremotecontainerstart_container_component)
1. [crossbarfabriccenter.remote.container.stop_container_component](#crossbarfabriccenterremotecontainerstop_container_component)
1. [crossbarfabriccenter.remote.proxy.get_proxy_transports](#crossbarfabriccenterremoteproxyget_proxy_transports)
1. [crossbarfabriccenter.remote.proxy.get_proxy_transport](#crossbarfabriccenterremoteproxyget_proxy_transport)
1. [crossbarfabriccenter.remote.proxy.start_proxy_transport](#crossbarfabriccenterremoteproxystart_proxy_transport)
1. [crossbarfabriccenter.remote.proxy.stop_proxy_transport](#crossbarfabriccenterremoteproxystop_proxy_transport)
1. [crossbarfabriccenter.remote.tracing.get_router_traces](#crossbarfabriccenterremotetracingget_router_traces)
1. [crossbarfabriccenter.remote.tracing.get_router_trace](#crossbarfabriccenterremotetracingget_router_trace)
1. [crossbarfabriccenter.remote.tracing.start_router_trace](#crossbarfabriccenterremotetracingstart_router_trace)
1. [crossbarfabriccenter.remote.tracing.stop_router_trace](#crossbarfabriccenterremotetracingstop_router_trace)
1. [crossbarfabriccenter.remote.tracing.get_router_trace_data](#crossbarfabriccenterremotetracingget_router_trace_data)
1. [crossbarfabriccenter.remote.docker.get_docker_status](#crossbarfabriccenterremotedockerget_docker_status)
1. [crossbarfabriccenter.remote.docker.get_docker_containers](#crossbarfabriccenterremotedockerget_docker_containers)
1. [crossbarfabriccenter.remote.docker.get_docker_container](#crossbarfabriccenterremotedockerget_docker_container)
1. [crossbarfabriccenter.remote.docker.start_docker_container](#crossbarfabriccenterremotedockerstart_docker_container)
1. [crossbarfabriccenter.remote.docker.stop_docker_container](#crossbarfabriccenterremotedockerstop_docker_container)
1. [crossbarfabriccenter.remote.docker.get_docker_images](#crossbarfabriccenterremotedockerget_docker_images)
1. [crossbarfabriccenter.remote.docker.get_docker_image](#crossbarfabriccenterremotedockerget_docker_image)
1. [crossbarfabriccenter.remote.docker.update_docker_image](#crossbarfabriccenterremotedockerupdate_docker_image)
1. [crossbarfabriccenter.remote.docker.remove_docker_image](#crossbarfabriccenterremotedockerremove_docker_image)

---

## Global

**crossbarfabriccenter.**

---

* **get_status ()

* **get_nodes ()

* **get_node ()


## Nodes

**crossbarfabriccenter.remote.node.**

---

* **get_status (node_id)

* **shutdown (node_id)

* **get_workers (node_id)

* **get_worker (node_id, worker_id)

* **start_worker (node_id, worker_id, config)

* **stop_worker (node_id, worker_id)


## Native Workers

**crossbarfabriccenter.remote.worker.**

---

* **get_status (node_id, worker_id)

* **shutdown (node_id, worker_id)

* **get_worker_log (node_id, worker_id)

* **get_pythonpath (node_id, worker_id)

* **add_pythonpath (node_id, worker_id)

* **get_cpu_affinity (node_id, worker_id)

* **set_cpu_affinity (node_id, worker_id)

* **get_profilers (node_id, worker_id)

* **start_profiler (node_id, worker_id)

* **get_profile (node_id, worker_id)


## Router Workers

### Router Realms

#### crossbarfabriccenter.remote.router.get_router_realms

Return a list of IDs of realms in the given router worker.

* **get_router_realms (node_id, worker_id) -> [realm_id]**

> The order of IDs within the list returned is unspecified, but stable.


#### crossbarfabriccenter.remote.router.get_router_realm

Return detailed information about the given realm.

* **get_router_realm (node_id, worker_id, realm_id) -> {realm}**


#### crossbarfabriccenter.remote.router.start_router_realm

Start a new realm on the given router worker.

* **start_router_realm**(node_id, worker_id, realm_id|null, realm_config) -> {realm_started}

The call does not return until the realm has completely started.

When the new realm *is starting*, an event

* **on_router_realm_starting(node_id, worker_id, realm_id, {realm_starting})**

is fired.

When the new realm *is completely started*, an event

* **on_router_realm_started(node_id, worker_id, realm_id, {realm_started})**

is fired.


#### crossbarfabriccenter.remote.router.stop_router_realm

Stop a realm currently running in the given router worker.

* **stop_router_realm (node_id, worker_id, realm_id) -> {realm_stopped}**


### Router Realm Roles

#### crossbarfabriccenter.remote.router.get_router_realm_roles

Return a list of IDs of roles in the given realm.

* **get_router_realm_roles (node_id, worker_id, realm_id) -> [role_id]**

> The order of IDs within the list returned is unspecified, but stable.


#### crossbarfabriccenter.remote.router.get_router_realm_role

Return detailed information about the given role.

* **get_router_realm_role (node_id, worker_id, realm_id, role_id) -> {realm_role}**


#### crossbarfabriccenter.remote.router.start_router_realm_role

Start a new role on the given router worker and realm.

* **start_router_realm_role (node_id, worker_id, realm_id, role_id|null, realm_role_config) -> {realm_role_created}**


#### crossbarfabriccenter.remote.router.stop_router_realm_role

Stop a role currently running in a realm in a router worker.

* **stop_router_realm_role (node_id, worker_id, realm_id, role_id) -> {realm_role_stopped}**


### Router Transports

#### crossbarfabriccenter.remote.router.get_router_transports

* **get_router_transports (node_id, worker_id) -> [transport_id]**


#### crossbarfabriccenter.remote.router.get_router_transport

* **get_router_transport (node_id, worker_id, transport_id) -> {transport}**


#### crossbarfabriccenter.remote.router.start_router_transport

* **start_router_transport (node_id, worker_id, transport_id|null, transport_config) -> {transport_started}**


#### crossbarfabriccenter.remote.router.stop_router_transport

* **stop_router_transport (node_id, worker_id, transport_id) -> {transport_stopped}**


### Router Transport Paths

#### crossbarfabriccenter.remote.router.get_router_transport_paths

* **get_router_transport_paths (node_id, worker_id, transport_id) -> [path_id]**


#### crossbarfabriccenter.remote.router.get_router_transport_path

* **get_router_transport_path (node_id, worker_id, transport_id, path_id) -> {path}**


#### crossbarfabriccenter.remote.router.start_router_transport_path

* **start_router_transport_path (node_id, worker_id, transport_id, path_id|null, transport_path_config) -> {transport_path_started}**


#### crossbarfabriccenter.remote.router.stop_router_transport_path

* **stop_router_transport_path (node_id, worker_id, transport_id, path_id) -> {transport_path_stopped}**


### Router Components

Router workers are native Crossbar.io processes that can host Python user components.

> Restrictions: The user components must be written using AutobahnPython and Twisted, and run under the same Python Crossbar.io runs under. Further, running user components in the same OS process as Crossbar.io routing code can lead to instability, and provides less security isolation. Router components should only be used very selectively for small amounts of code, such as dynamic authenticators or authorizors.


#### crossbarfabriccenter.remote.router.get_router_components

Return list of IDs of components in this router worker.

* **get_router_components (node_id, worker_id) -> [component_id]**


#### crossbarfabriccenter.remote.router.get_router_component

Return detailed information about the given router component.

* **get_router_component (node_id, worker_id, component_id) -> {router_component}**


#### crossbarfabriccenter.remote.router.start_router_component

Start a new (native Python) user component in this router worker.

* **start_router_component (node_id, worker_id, component_id|null, component_config) -> {router_component_started}**


#### crossbarfabriccenter.remote.router.stop_router_component

Stop a user component running in this router worker.

* **stop_router_component (node_id, worker_id) -> {router_component_stopped}**


## Container Workers

**crossbarfabriccenter.remote.container.**

Container workers are native Crossbar.io processes that can host Python user components.

> Restrictions: The user components must be written using AutobahnPython and Twisted, and run under the same Python Crossbar.io runs under.

---


### get_container_components

Return list of IDs of (native Python) components in container.

* **get_container_components (node_id, worker_id) -> [component_id]**


### get_container_component

Return detailed information about container component.

* **get_container_component (node_id, worker_id, component_id) -> {container_component}**


### start_container_component

Start a new (native Python) component in container.

* **start_container_component (node_id, worker_id, component_config) -> {container_component_started}**


### stop_container_component

Stop a component running in the container.

* **stop_container_component (node_id, worker_id, component_id) -> {container_component_stopped}**


## Proxy Workers

**crossbarfabriccenter.remote.proxy.**

---

### get_proxy_transports

*Return list of IDs of proxy worker transport in a proxy worker.*

* **get_proxy_transports (node_id, worker_id) -> [transport_id]**


### get_proxy_transport

*Return detailed information about proxy worker transport in a proxy worker.*

* **get_proxy_transport (node_id, worker_id, transport_id) -> {proxy_transport}**


### start_proxy_transport

*Start a new proxy worker transport in this proxy worker.*

* **start_proxy_transport (node_id, worker_id, transport_id|null, config) -> {on_proxy_transport_started}


### stop_proxy_transport

*Stop a proxy worker transport running in a proxy worker.*

* **stop_proxy_transport (node_id, worker_id, transport_id) -> {on_proxy_transport_stopped}


## Message Tracing

**crossbarfabriccenter.remote.tracing.**

---


### get_router_traces

* **get_router_traces (node_id, worker_id) -> [trace_id]


### get_router_trace

* **get_router_trace (node_id, worker_id, trace_id) -> {trace}


### start_router_trace

* **start_router_trace (node_id, worker_id, trace_id|null, config) -> {on_trace_started}


### stop_router_trace

* **stop_router_trace (node_id, worker_id, trace_id) -> {on_trace_stopped}


### get_router_trace_data

* **get_router_trace_data (node_id, worker_id, trace_id, from_seq_ to_seq) -> [{trace_record}]


## Docker Control

**crossbarfabriccenter.remote.docker.**

---


### get_docker_status

* **get_docker_status (node_id)


### get_docker_containers

* **get_docker_containers (node_id)


### get_docker_container

* **get_docker_container (node_id, docker_container_id)


### start_docker_container

* **start_docker_container (node_id, docker_container_id, config)


### stop_docker_container

* **stop_docker_container (node_id, docker_container_id)


### get_docker_images

* **get_docker_images (node_id)


### get_docker_image

* **get_docker_image (node_id, image_id)


### update_docker_image

* **update_docker_image (node_id, image_id)


### remove_docker_image

* **remove_docker_image (node_id, image_id)
