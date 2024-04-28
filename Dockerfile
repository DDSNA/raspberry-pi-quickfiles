FROM apache/airflow:2.9.0

ARG AIRFLOW_VERSION="2.9.0"
ENV AIRFLOW_VERSION="2.9.0"

USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         vim \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

USER airflow

RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' lxml
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-apache-spark
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-databricks
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-airbyte
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-alibaba
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-amazon
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-apache-beam
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-apache-cassandra
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-apache-drill
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-apache-druid
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-apache-flink
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-apache-hdfs
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-apache-hive
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-apache-impala
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-apache-kafka
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-apache-kylin
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-apache-livy
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-apache-pig
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-apache-pinot
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-apache-spark
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-apprise
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-arangodb
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-asana
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-atlassian-jira
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-celery
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-cloudant
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-cncf-kubernetes
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-cohere
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-common-io
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-common-sql
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-databricks
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-datadog
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-dbt-cloud
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-dingding
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-discord
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-docker
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-elasticsearch
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-exasol
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-fab
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-facebook
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-ftp
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-github
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-google
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-grpc
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-hashicorp
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-http
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-imap
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-influxdb
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-jdbc
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-jenkins
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-microsoft-azure
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-microsoft-mssql
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-microsoft-psrp
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-microsoft-winrm
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-mongo
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-mysql
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-neo4j
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-odbc
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-openai
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-openfaas
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-openlineage
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-opensearch
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-opsgenie
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-oracle
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-pagerduty
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-papermill
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-pgvector
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-pinecone
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-postgres
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-presto
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-qdrant
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-redis
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-salesforce
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-samba
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-segment
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-sendgrid
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-sftp
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-singularity
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-slack
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-smtp
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-snowflake
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-sqlite
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-ssh
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-tableau
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-tabular
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-telegram
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-teradata
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-trino
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-vertica
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-weaviate
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-yandex
RUN pip install --no-cache-dir 'apache-airflow==${AIRFLOW_VERSION}' apache-airflow-providers-zendesk
