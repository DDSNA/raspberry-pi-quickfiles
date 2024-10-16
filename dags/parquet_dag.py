import pandas as pd
import psycopg2
import os

from datetime import datetime
from sqlalchemy import create_engine, select

from airflow import DAG, Dataset
from airflow.providers.google.cloud.hooks.gcs import GCSHook
from airflow.decorators import dag, task

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 3, 29, 7, 30),
    "retries": 5,
    "catchup":"False"
}

sqlalchemy_db = os.getenv("SQLALCHEMY_DB")
sqlalchemy_db_jdbc = os.getenv("SQLALCHEMY_DB_JDBC")
sqlalchemy_username = os.getenv("SQLALCHEMY_USERNAME")
sqlalchemy_password = os.getenv("SQLALCHEMY_PASSWORD")
sqlalchemy_host_address = os.getenv("SQLALCHEMY_HOST_ADDRESS")
sqlalchemy_host_port = os.getenv("SQLALCHEMY_HOST_PORT")
# this is railway not data analytics
sqlalchemy_host_database = os.getenv("SQLALCHEMY_HOST_DATABASE")

# datasets
csv_file = Dataset(
    "gcp-dan://testing/dataset.parquet"
)

# handling
def task_failure_discord_alert(context):
    import requests
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    print(context)
    message = f"Alert: {context['task_instance_key_str']} failed."
    payload = {
        "content": message,
        "username": "Airflow",

    }
    requests.post(webhook_url, json=payload)
    return message

@dag(
    dag_id="Orders_Backup",
    description="DAG for backing up orders data",
    start_date=datetime(2024, 3, 28, 7, 30),
    schedule= "@weekly",
    tags=["dan", "parquet"],
    catchup=False,
    on_failure_callback=task_failure_discord_alert
    )
def dag_orders():
    engine = create_engine(f"{sqlalchemy_db}+{sqlalchemy_db_jdbc}://{sqlalchemy_username}:{sqlalchemy_password}@{sqlalchemy_host_address}:{sqlalchemy_host_port}/{sqlalchemy_host_database}")
    
    @task()
    def get_orders():
        stmt = """
                SELECT * FROM prun_data.temporary_df_hold_orders
                """
        result = engine.connect().execute(stmt)
        orders = result.fetchall()
        return orders
    @task()
    def save_orders_parquet(orders: list, cloud: bool):
        df = pd.DataFrame(orders)
        parquet_file = df.to_parquet("orders.parquet")
        return parquet_file
    
    @task()
    def store_orders(parquet_file: str, cloud=True):
        time_of_execution = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        filename = str(time_of_execution) + "_orders.parquet"

        if cloud is True:
            bucket_name = "airflow-bucket-prun"
            filepath = f"/{filename}"

            gcs_hook = GCSHook(gcp_conn_id='gc_conn')
            gcs_hook.upload(bucket_name, filepath, "orders.parquet")
        else:
            pass

    orders = get_orders()
    store_orders(
        save_orders_parquet(orders, cloud=True),
        cloud=True
        )

dag_orders()