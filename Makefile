teardown:
	echo "Tearing down"
	sudo docker compose down
	sudo chown -R 1001 dags
	sudo chown -R 1001 plugins
	sudo chown -R 1001 logs