# Data Engineering Project

### Airflow usage with cloud and on prem services integration

## Scope

Portofolio of projects aimed to demonstrate general usage of Airflow run locally with various integrations relevant to the current technologies market.

## Project structure

### Folders

1. dags
   - **Usage**: Contains Directed Acyclic Graphs (DAGs) which define the workflow of tasks.
2. data
   - **Usage**: Directory for storing datasets and other data files used in the projects.
3. deprecated_scripts
   - **Usage**: Contains various scripts for data processing, automation, and other utilities that were previously used in various dags or setups of scripts. May contain old information from Alexey Grigorovich's classes.
4. spark-images
   - **Usage**: Directory containing the spark dockerfile currently used in conjunction with airflow.

### Files

1. .env
   - **Usage**: Mock file used to store environment variables that would normally not be stored on a file accessible to code/repository viewers for security and privacy reasons.
2. .gitignore
   - **Usage**: File used for git instructions to declutter the repository from image usage artefacts.
3. config_local.py
   - **Usage**: File used for PgAdmin 4 configuration. Used in docker-compose.yaml for various customization and replication of objects for quick setup/recovery.
4. docker-compose.yaml
   - **Usage**: File used by Docker to quickly build up custom containers and instructions for their interaction/networking capabilities.
5. Dockerfile
   - **Usage**: File used by Docker to build an image based on the instructions within. Contains customized Airflow installation with multiple community connectors added for functionality extension. Uses Airflow 2.9.0 as a base image from [docker hub repository](https://hub.docker.com/layers/apache/airflow/2.9.0-python3.12/images/sha256-2cc3cc965f2d2ab1603d655a30769ed59b45506aec1dbaedb761e998fa54ae2d?context=explore)
6. Makefile
   - **Usage**: Make file used to create custom commands for easier setup/deconstruction of containers/images. Handy given some limitations

### Running it

#### Contents

1. Full Airflow setup including initializer, scheduler, triggerer, worker and server. (default user)
2. Airflow support software such as a Redis database and a Postgresql database
3. Independent Postgresql database for sandboxing purposes
4. PgAdmin dependent on the Postgresql database mentioned above
5. (Optional) Spark image that can be built locally and enabled to connect with the Airflow system

Prerequisites: Docker, Make (optional)

Getting the docker image:

1. Build from the Dockerfile by downloading the Dockerfile as well as docker-compose.yaml locally and running `docker compose build` or `make build-nc`
2. ~~Pull it from the image provided here~~

Running the docker compose file:
1. `docker compose up` is always a good option but for this particular situation `make compose-up` is also a good alternative

### Notes

1. Due to the dynamic nature of my contexts sometimes I need to be able to jump between developing locally and developing on a more portable Raspberry Pi 4. Personal laptop repairs are quite pricey it seems. Thus, software used in these images is based on ARM64 architecture and thus the nature of the repository is somewhat chaotic the further down the tree one goes.
2. The repository also contains a custom spark docker image for easier deployment of applications.
3. Technically this repository is part of a larger structure of folders that uses the software here as a part of a machine. The entire ecosystem contains an nginx server for reverse proxying and networking study, synapse server for streaming/communication study, kafka for apache projects exploration and various sql/nosql databases for studying.
4. For simplicity I generally reserve address xxx.168.0.38 for the device running this
