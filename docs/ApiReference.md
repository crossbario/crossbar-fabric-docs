# Crossbar.io Fabric Center API Reference


## Global

Prefix: **crossbarfabriccenter.**

* **get_status** ()

* **get_nodes** ()

* **get_node** ()


## Nodes

Prefix: **crossbarfabriccenter.remote.node.**

* **get_status** (node_id)

* **shutdown** (node_id)

* **get_workers** (node_id)

* **get_worker** (node_id, worker_id)

* **start_worker** (node_id, worker_id, config)

* **stop_worker** (node_id, worker_id)


## Native Workers

Prefix: **crossbarfabriccenter.remote.worker.**

* **get_status** (node_id, worker_id)

* **shutdown** (node_id, worker_id)

* **get_worker_log** (node_id, worker_id)

* **get_pythonpath** (node_id, worker_id)

* **add_pythonpath** (node_id, worker_id)

* **get_cpu_affinity** (node_id, worker_id)

* **set_cpu_affinity** (node_id, worker_id)

* **get_profilers** (node_id, worker_id)

* **start_profiler** (node_id, worker_id)

* **get_profile** (node_id, worker_id)


## Router Workers

Prefix: **crossbarfabriccenter.remote.router.**

* **get_router_realms** (node_id, worker_id)

* **get_router_realm** (node_id, worker_id)

* **start_router_realm** (node_id, worker_id)

* **stop_router_realm** (node_id, worker_id)

* **get_router_realm_roles** (node_id, worker_id)

* **get_router_realm_role** (node_id, worker_id)

* **start_router_realm_role** (node_id, worker_id)

* **stop_router_realm_role** (node_id, worker_id)

* **get_router_transports** (node_id, worker_id)

* **get_router_transport** (node_id, worker_id)

* **start_router_transport** (node_id, worker_id)

* **stop_router_transport** (node_id, worker_id)

* **get_router_transport_paths** (node_id, worker_id)

* **get_router_transport_path** (node_id, worker_id)

* **start_router_transport_path** (node_id, worker_id)

* **stop_router_transport_path** (node_id, worker_id)

* **get_router_components** (node_id, worker_id)

* **get_router_component** (node_id, worker_id)

* **start_router_component** (node_id, worker_id)

* **stop_router_component** (node_id, worker_id)


## crossbarfabriccenter.remote.container


### get_container_components

*Return list of IDs of (native Python) components in container.*

* **get_container_components** (node_id, worker_id) -> [component_id]


### get_container_component

*Return detailed information about container component.*

* **get_container_component** (node_id, worker_id, component_id) -> {container_component}


### start_container_component

*Start a new (native Python) component in container.*

* **start_container_component** (node_id, worker_id, component_id, config) -> {on_container_started}


### stop_container_component

*Stop a component running in the container.*

* **stop_container_component** (node_id, worker_id, component_id) -> {on_container_stopped}


## crossbarfabriccenter.remote.proxy.

### get_proxy_transports

*Return list of IDs of proxy worker transport in a proxy worker.*

* **get_proxy_transports** (node_id, worker_id) -> [transport_id]


### get_proxy_transport

*Return detailed information about proxy worker transport in a proxy worker.*

* **get_proxy_transport** (node_id, worker_id, transport_id) -> {proxy_transport}


### start_proxy_transport

*Start a new proxy worker transport in this proxy worker.*

* **start_proxy_transport** (node_id, worker_id, transport_id, config) -> {on_proxy_transport_started}


### stop_proxy_transport

*Stop a proxy worker transport running in a proxy worker.*

* **stop_proxy_transport** (node_id, worker_id, transport_id) -> {on_proxy_transport_stopped}


## Message Tracing

Prefix: **crossbarfabriccenter.remote.tracing.**

* **get_router_traces** (node_id, worker_id)

* **get_router_trace** (node_id, worker_id, trace_id)

* **start_router_trace** (node_id, worker_id, trace_id, config)

* **stop_router_trace** (node_id, worker_id, trace_id)

* **get_router_trace_data** (node_id, worker_id, trace_id, from_seq_ to_seq)


## Docker Control

Prefix: **crossbarfabriccenter.remote.docker.**

* **get_docker_status** (node_id)

* **get_docker_containers** (node_id)

* **get_docker_container** (node_id, docker_container_id)

* **start_docker_container** (node_id, docker_container_id, config)

* **stop_docker_container** (node_id, docker_container_id)

* **get_docker_images** (node_id)

* **get_docker_image** (node_id, image_id)

* **update_docker_image** (node_id, image_id)

* **remove_docker_image** (node_id, image_id)
