ex: ex_status ex_list_workers ex_trace_10s

ex_status:
	python -u examples/ex_status.py --url ws://localhost:9000/ws --realm test1 --keyfile ${HOME}/.cbf/default.priv

ex_list_workers:
	python -u examples/ex_list_workers.py --url ws://localhost:9000/ws --realm test1 --keyfile ${HOME}/.cbf/default.priv

ex_trace_10s:
	python -u examples/ex_trace_10s.py --url ws://localhost:9000/ws --realm test1 --keyfile ${HOME}/.cbf/default.priv
