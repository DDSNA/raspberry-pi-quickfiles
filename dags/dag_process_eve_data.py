from airflow import DAG
from airflow.datasets import Dataset
from airflow.operators.python import PythonOperator
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
def load_dataset() -> pd.DataFrame:
    try:
        gcs_hook = GCSHook(gcp_conn_id="gcp-dan")
        gcs_hook.download(
            bucket_name="simple-bucket-ddsna",
            object_name="testing/dataset.csv",
            filename="dataset.csv")
        print("Dataset downloaded")
        logging.info("Dataset loaded")
        df = pd.read_csv("dataset.csv")
        os.remove("dataset.csv")
        return df
        
    except Exception as e:
        print("Error loading dataset: ", e)
        logging.error(e)



with DAG(
    dag_id="Dan_cloud_eve_processor",
    start_date=datetime(2024, 1, 1),
    schedule=[gcp_csv_dataset],
    tags=["gcp","sensor","dan"],
    catchup=False
) as dag:

    load_dataset = PythonOperator(
        task_id="load_dataset",
        python_callable=load_dataset
    )

load_dataset