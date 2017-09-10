#
# Examples
#

# eg: make examples realm=oberstet
realm := $(or ${realm},${realm},"test1")
url := $(or ${url},${url},"wss://fabric.crossbario.com/ws")

examples: \
	ex_global_api \
	ex_status \
	ex_list_nodes \
	ex_list_workers \
	ex_start_router \
	ex_start_proxy \
	ex_start_container \
	ex_start_guest \
	ex_list_sessions \
	ex_list_subs_regs \
	ex_cpu_affinity \
	ex_process_stats \
	ex_worker_log \
	ex_tracing \
	ex_docker

#
# this example demonstrates some functions on the CFC global users realm
#
ex_global_api:
	python3 -u examples/ex_global_api.py --url ${url} --realm "com.crossbario.fabric" --keyfile ${HOME}/.cbf/default.priv


#
# the following examples all work on a user management realm on CFC
#
ex_status:
	python3 -u examples/ex_status.py --url ${url} --realm ${realm} --keyfile ${HOME}/.cbf/default.priv

ex_list_nodes:
	python3 -u examples/ex_list_nodes.py --url ${url} --realm ${realm} --keyfile ${HOME}/.cbf/default.priv

ex_list_workers:
	python3 -u examples/ex_list_workers.py --url ${url} --realm ${realm} --keyfile ${HOME}/.cbf/default.priv

ex_start_router:
	python3 -u examples/ex_start_router.py --url ${url} --realm ${realm} --keyfile ${HOME}/.cbf/default.priv

ex_start_proxy:
	python3 -u examples/ex_start_proxy.py --url ${url} --realm ${realm} --keyfile ${HOME}/.cbf/default.priv

ex_start_container:
	python3 -u examples/ex_start_container.py --url ${url} --realm ${realm} --keyfile ${HOME}/.cbf/default.priv

ex_start_guest:
	python3 -u examples/ex_start_guest.py --url ${url} --realm ${realm} --keyfile ${HOME}/.cbf/default.priv

ex_list_sessions:
	python3 -u examples/ex_list_sessions.py --url ${url} --realm ${realm} --keyfile ${HOME}/.cbf/default.priv

ex_monitor_sessions:
	python3 -u examples/ex_monitor_sessions.py --url ${url} --realm ${realm} --keyfile ${HOME}/.cbf/default.priv

ex_list_subs_regs:
	python3 -u examples/ex_list_subs_regs.py --url ${url} --realm ${realm} --keyfile ${HOME}/.cbf/default.priv

ex_cpu_affinity:
	python3 -u examples/ex_cpu_affinity.py --url ${url} --realm ${realm} --keyfile ${HOME}/.cbf/default.priv

ex_process_stats:
	python3 -u examples/ex_process_stats.py --url ${url} --realm ${realm} --keyfile ${HOME}/.cbf/default.priv

ex_worker_log:
	python3 -u examples/ex_worker_log.py --url ${url} --realm ${realm} --keyfile ${HOME}/.cbf/default.priv

ex_tracing:
	python3 -u examples/ex_tracing.py --url ${url} --realm ${realm} --keyfile ${HOME}/.cbf/default.priv

ex_tracing_monitor:
	python3 -u examples/ex_tracing_monitor.py --url ${url} --realm ${realm} --keyfile ${HOME}/.cbf/default.priv

ex_docker:
	python3 -u examples/ex_docker.py --url ${url} --realm ${realm} --keyfile ${HOME}/.cbf/default.priv


#
# Docker CF nodes / app containers for testing
#

# start 2x Crossbar.io Fabric (CF) node
run_cf:
	docker-compose up cf1 cf2

# start 4x app components connecting to the 2 CF nodes
run_app:
	docker-compose up app1a app1b app1c app1d

# start everything
run:
	docker-compose up

#
# Local testing (these targets are for CB developers only)
#

run_local_cf1:
	crossbar start --personality fabric --cbdir test/cf1/.crossbar/

run_local_cf2:
	crossbar start --personality fabric --cbdir test/cf2/.crossbar/


run_local_app1a:
	python -u test/app1/client.py --url=ws://localhost:8080/ws --realm realm1 --service=service1

run_local_app1b:
	python -u test/app1/client.py --url=ws://localhost:8080/ws --realm realm1 --service=service2

run_local_app1c:
	python -u test/app1/client.py --url=ws://localhost:8081/ws --realm realm1 --service=service3

run_local_app1d:
	python -u test/app1/client.py --url=ws://localhost:8081/ws --realm realm1 --service=service4
