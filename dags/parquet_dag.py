import pandas as pd
import psycopg2
import os

from datetime import datetime

from airflow import DAG
from airflow.providers.google.cloud.hooks.gcs import GCSHook
from airflow.decorators import dag, task


default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 3, 29, 7, 30),
    "retries": 5,
    "schedule_interval": "@weekly",
    "tags": ["dan", "parquet"]
}

sqlalchemy_db = os.getenv("SQLALCHEMY_DB")
sqlalchemy_db_jdbc = os.getenv("SQLALCHEMY_DB_JDBC")
sqlalchemy_username = os.getenv("SQLALCHEMY_USERNAME")
sqlalchemy_password = os.getenv("SQLALCHEMY_PASSWORD")
sqlalchemy_host_address = os.getenv("SQLALCHEMY_HOST_ADDRESS")
sqlalchemy_host_port = os.getenv("SQLALCHEMY_HOST_PORT")
# this is railway not data analytics
sqlalchemy_host_database = os.getenv("SQLALCHEMY_HOST_DATABASE")

@dag("Orders_Backup",
    description="DAG for backing up orders data",
    default_args=default_args
    )


def dag_orders():
    engine =  engine = create_engine(f"{sqlalchemy_db}+{sqlalchemy_db_jdbc}://{sqlalchemy_username}:{sqlalchemy_password}@{sqlalchemy_host_address}:{sqlalchemy_host_port}/{sqlalchemy_host_database}")
    
    @task()
    def get_orders():
        with engine.connect() as connection:
            result = connection.execute("SELECT * FROM prun_data.temporary_df_hold_orders")
            orders = result.fetchall()
            return orders
        
    @task()
    def save_orders_parquet(orders: list):
        df = pd.DataFrame(orders)
        parquet_file = df.to_parquet("orders.parquet")
        return parquet_file
    
    @task()
    def store_orders(parquet_file: str):
        time_of_execution = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        filename = str(time_of_execution) + "_orders.parquet"
        bucket_name = "airflow-bucket-prun"
        filepath = f"/{filename}"

        gcs_hook = GCSHook(gcp_conn_id='gc_conn')
        gcs_hook.upload(bucket_name, filepath, "orders.parquet")

    orders = get_orders()
    save_orders_parquet(orders)
    store_orders(save_orders_parquet(orders))

dag_orders()