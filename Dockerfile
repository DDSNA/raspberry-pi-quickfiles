FROM apache/airflow:2.9.0
ENV AIRFLOW_VERSION = 2.9.0

USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         vim \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

USER airflow

RUN pip install --no-cache-dir 'apache-airflow==${AIFLOW-VERSION}' lxml
RUN pip install --no-cache-dir 'apache-airflow==${AIFLOW-VERSION}' apache-airflow-providers-apache-spark
