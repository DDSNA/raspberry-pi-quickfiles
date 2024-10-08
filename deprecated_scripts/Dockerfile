FROM python:latest

RUN pip install pandas
RUN pip install apache-airflow-providers-apache-spark

WORKDIR /app

COPY pipeline.py pipeline.py

ENTRYPOINT [ "python","pipeline.py" ]
