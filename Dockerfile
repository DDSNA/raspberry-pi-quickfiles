FROM apache/airflow:2.9.0

USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         vim \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

USER airflow

RUN pip install --no-cache-dir 'apache-airflow==2.9.0' lxml
RUN pip install --no-cache-dir 'apache-airflow==2.9.0' apache-airflow-providers-apache-spark
