FROM apache/airflow:2.9.0-python3.12

ENV AIRFLOW_VERSION="2.9.0"
ARG AIRFLOW_VERSION="2.9.0"
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
        build-essential \
        python3-dev \
        libffi-dev \
        libssl-dev \
        vim \
        # needed for hdfs
        libkrb5-dev \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

USER airflow
RUN pip install --no-cache-dir grpcio-tools
# Disclaimer: I am planning to test as many of these connectors as possible to increase my knowhow of how various platforms work. There's also some redundant ones.
# This is by design. The build time on a raspberry pi goes to almost an hour. I recommend asking for my private repository image rather than waiting for that long
# Seriously, ask me for it. Some of these providers have incredibly slow downloads for Europe.
RUN pip install --no-cache-dir "apache-airflow==2.9.0" lxml
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-apache-spark
# Databricks disable during this iteration due to associated costs
# RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-databricks
# RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-airbyte
# No plan to use this one due to lack of ecommerce business
# RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-alibaba
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-amazon
# warn: considering dropping beam due to lack of arm architecture support via docker images (as well as alternatives below)
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-apache-beam
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-apache-cassandra
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-apache-drill
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-apache-druid
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-apache-flink
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-apache-hdfs
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-apache-hive
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-apache-impala
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-apache-kafka
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-apache-kylin
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-apache-livy
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-apache-pig
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-apache-pinot
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-apache-spark
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-apprise
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-arangodb
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-asana
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-atlassian-jira
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-celery
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-cloudant
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-cncf-kubernetes
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-cohere
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-common-io
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-common-sql
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-databricks
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-datadog
# I tried dbt locally but will not try with paid cloud services
# RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-dbt-cloud
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-dingding
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-discord
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-docker
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-elasticsearch
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-exasol
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-fab
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-facebook
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-ftp
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-github
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-google
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-grpc
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-hashicorp
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-http
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-imap
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-influxdb
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-jdbc
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-jenkins
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-microsoft-azure
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-microsoft-mssql
# I don't plan to use windows related stuff or mongo yet
# RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-microsoft-psrp
# RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-microsoft-winrm
# RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-mongo
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-mysql
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-neo4j
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-odbc
# I don't have an openai api key
# RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-openai
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-openfaas
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-openlineage
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-opensearch
# I don't have a way to test atlassian products
# RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-opsgenie
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-oracle
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-pagerduty
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-papermill
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-pgvector
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-pinecone
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-postgres
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-presto
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-qdrant
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-redis
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-salesforce
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-samba
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-segment
# RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-sendgrid
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-sftp
# RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-singularity
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-slack
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-smtp
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-snowflake
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-sqlite
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-ssh
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-tableau
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-tabular
RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-telegram
# RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-teradata
# RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-trino
# RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-vertica
# RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-weaviate
# RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-yandex
# RUN pip install --no-cache-dir "apache-airflow==2.9.0" apache-airflow-providers-zendesk
RUN pip install pyspark utils

# Removing conflicts, at the moment typing seems to have a few issues with some connectors and from my investigation of forums, even with airflow itself

RUN pip uninstall typing -y

# I am aware that slamming api keys in any public repo/file that can be read online is a very bad idea - this one is free to use and has no strings attached.
ENV AIRFLOW_VAR_stock_market_source_api_key=041470e6cc7b4fa:tgn6gznxxxfudur