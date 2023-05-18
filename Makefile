.PHONY: init start stop

init:
	mkdir -p db
	initdb -D db/postgres

start:
	pg_ctl -D db/postgres -l db/server.log start

stop:
	pg_ctl -D db/postgres stop

