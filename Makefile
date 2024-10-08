teardown-admin:
	echo "Tearing down"
	sudo docker compose down
	sudo chown -R 1000 dags
	sudo chown -R 1000 plugins
	sudo chown -R 1000 logs
	sudo chown -R 1000 ./dags/
	sudo chown -R 1000 dags/

teardown-dev:
	echo "Tearing down"
	sudo docker compose down
	sudo chown -R 1001 dags
	sudo chown -R 1001 plugins
	sudo chown -R 1001 logs
	sudo chown -R 1001 ./dags/
	sudo chown -R 1001 dags/

compose-up:
	echo "Starting up"
	sudo docker compose up -d

build:
	docker compose build

build-nc:
	docker compose build --no-cache

build-progress:
	docker compose build --no-cache --progress=plain