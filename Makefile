examples: \
	ex_status \
	ex_list_workers \
	ex_list_sessions \
	ex_list_subs_regs \
	ex_cpu_affinity \
	ex_process_stats \
	ex_tracing

ex_status:
	python -u examples/ex_status.py --url ws://localhost:9000/ws --realm test1 --keyfile ${HOME}/.cbf/default.priv

ex_list_workers:
	python -u examples/ex_list_workers.py --url ws://localhost:9000/ws --realm test1 --keyfile ${HOME}/.cbf/default.priv

ex_list_sessions:
	python -u examples/ex_list_sessions.py --url ws://localhost:9000/ws --realm test1 --keyfile ${HOME}/.cbf/default.priv

ex_list_subs_regs:
	python -u examples/ex_list_subs_regs.py --url ws://localhost:9000/ws --realm test1 --keyfile ${HOME}/.cbf/default.priv

ex_tracing:
	python -u examples/ex_tracing.py --url ws://localhost:9000/ws --realm test1 --keyfile ${HOME}/.cbf/default.priv

ex_cpu_affinity:
	python -u examples/ex_cpu_affinity.py --url ws://localhost:9000/ws --realm test1 --keyfile ${HOME}/.cbf/default.priv

ex_worker_log:
	python -u examples/ex_worker_log.py --url ws://localhost:9000/ws --realm test1 --keyfile ${HOME}/.cbf/default.priv

ex_process_stats:
	python -u examples/ex_process_stats.py --url ws://localhost:9000/ws --realm test1 --keyfile ${HOME}/.cbf/default.priv
