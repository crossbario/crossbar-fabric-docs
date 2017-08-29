#
# Examples
#

examples: \
	ex_status \
	ex_list_nodes \
	ex_list_workers \
	ex_start_router \
	ex_start_container \
	ex_start_guest \
	ex_list_sessions \
	ex_list_subs_regs \
	ex_cpu_affinity \
	ex_process_stats \
	ex_worker_log \
	ex_tracing \
	ex_docker

ex_status:
	python -u examples/ex_status.py --url ws://localhost:9000/ws --realm test1 --keyfile ${HOME}/.cbf/default.priv

ex_list_nodes:
	python -u examples/ex_list_nodes.py --url ws://localhost:9000/ws --realm test1 --keyfile ${HOME}/.cbf/default.priv

ex_list_workers:
	python -u examples/ex_list_workers.py --url ws://localhost:9000/ws --realm test1 --keyfile ${HOME}/.cbf/default.priv

ex_start_router:
	python -u examples/ex_start_router.py --url ws://localhost:9000/ws --realm test1 --keyfile ${HOME}/.cbf/default.priv

ex_start_container:
	python -u examples/ex_start_container.py --url ws://localhost:9000/ws --realm test1 --keyfile ${HOME}/.cbf/default.priv

ex_start_guest:
	python -u examples/ex_start_guest.py --url ws://localhost:9000/ws --realm test1 --keyfile ${HOME}/.cbf/default.priv

ex_list_sessions:
	python -u examples/ex_list_sessions.py --url ws://localhost:9000/ws --realm test1 --keyfile ${HOME}/.cbf/default.priv

ex_list_subs_regs:
	python -u examples/ex_list_subs_regs.py --url ws://localhost:9000/ws --realm test1 --keyfile ${HOME}/.cbf/default.priv

ex_cpu_affinity:
	python -u examples/ex_cpu_affinity.py --url ws://localhost:9000/ws --realm test1 --keyfile ${HOME}/.cbf/default.priv

ex_process_stats:
	python -u examples/ex_process_stats.py --url ws://localhost:9000/ws --realm test1 --keyfile ${HOME}/.cbf/default.priv

ex_worker_log:
	python -u examples/ex_worker_log.py --url ws://localhost:9000/ws --realm test1 --keyfile ${HOME}/.cbf/default.priv

ex_tracing:
	python -u examples/ex_tracing.py --url ws://localhost:9000/ws --realm test1 --keyfile ${HOME}/.cbf/default.priv

ex_docker:
	python -u examples/ex_docker.py --url ws://localhost:9000/ws --realm test1 --keyfile ${HOME}/.cbf/default.priv


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
