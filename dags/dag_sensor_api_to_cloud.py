from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.datasets import Dataset
from airflow.sensors.http_sensor import HttpSensor

from airflow.providers.google.cloud.hooks.gcs import GCSHook
from airflow.providers.http.operators.http import SimpleHttpOperator

from datetime import datetime

import requests
import pandas as pd
import numpy as np


import os
import logging
import requests
import pandas as pd
import numpy as np

gcp_csv_dataset = Dataset("gcp-dan://simple-bucket-ddsna/testing/dataset.csv")

def download_dataset(type: str):
    url = "http://eve.danserban.ro/call-fuzz"
    if type == "csv":
        response = requests.get(url)
        logging.debug(response.status_code)
        logging.debug(response.text)
        print(response.status_code)
        df = pd.DataFrame(response.json())
        df.to_csv("dataset.csv", index=False)
        
    elif type == "parquet":
        response = requests.get(url)
        logging.debug(response.status_code)
        df = pd.DataFrame(response.json())
        for col in df.columns:
            if df[col].dtype == 'object':  # Check if the column is of object type (strings)
                try:
                    df[col] = pd.to_numeric(df[col], errors='coerce')  # Attempt to convert to numeric, coercing errors
                except ValueError:
                    print(f"Failed to convert {col} to numeric.")
        df.to_parquet("dataset.parquet")


def upload_dataset():
    import logging
    logger = logging.getLogger(__name__)
    logger.info("This is a log message")
    try:
        gcs_hook = GCSHook(gcp_conn_id="gcp-dan")
        gcs_hook.upload(
            bucket_name="simple-bucket-ddsna",
            object_name="testing/dataset.csv",
            filename="dataset.csv")
        os.remove("dataset.csv")
    except Exception as e:
        print(e)
        logging.error(e)
        gcs_hook = GCSHook(gcp_conn_id="gcp-dan")
        gcs_hook.upload(
            bucket_name="simple-bucket-ddsna",
            object_name="testing/dataset.parquet",
            filename="dataset.parquet")
        os.remove("dataset.parquet")

with DAG(
    dag_id="Dan_cloud_sensor_plus_saver",
    start_date=datetime(2024, 1, 1),
    schedule_interval="3 * * * *",
    tags=["gcp","sensor","dan"],
    catchup=False
) as dag:
    
    get_dataset = PythonOperator(
        task_id="get_dataset",
        python_callable=download_dataset,
        op_args=["parquet"]
    )

    upload_dataset = PythonOperator(
        task_id="upload_dataset",
        python_callable=upload_dataset,
        outlets=[gcp_csv_dataset]
    )

get_dataset >> upload_dataset