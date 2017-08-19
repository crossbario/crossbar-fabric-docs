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


## Container Workers

Prefix: **crossbarfabriccenter.remote.container.**

* **get_container_components** (node_id, worker_id)

* **get_container_component** (node_id, worker_id, component_id)

* **start_container_component** (node_id, worker_id, component_id, config)

* **stop_container_component** (node_id, worker_id, component_id)


## Proxy Workers

Preifx: **crossbarfabriccenter.remote.proxy.**

* **get_proxy_transports** (node_id, worker_id)

* **get_proxy_transport** (node_id, worker_id, transport_id)

* **start_proxy_transport** (node_id, worker_id, transport_id, config)

* **stop_proxy_transport** (node_id, worker_id, transport_id)


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
