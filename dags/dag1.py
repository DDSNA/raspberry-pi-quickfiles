from datetime import datetime

from airflow import DAG

from airflow.decorators import dag, task

from sqlalchemy import create_engine, select

import pandas as pd
import psycopg2
import os
import json

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 14),
    'retries': 1,
    'schedule_interval': '@daily'
}

sqlalchemy_db = os.getenv("SQLALCHEMY_DB")
sqlalchemy_db_jdbc = os.getenv("SQLALCHEMY_DB_JDBC")
sqlalchemy_username = os.getenv("SQLALCHEMY_USERNAME")
sqlalchemy_password = os.getenv("SQLALCHEMY_PASSWORD")
sqlalchemy_host_address = os.getenv("SQLALCHEMY_HOST_ADDRESS")
sqlalchemy_host_port = os.getenv("SQLALCHEMY_HOST_PORT")
# this is railway not data analytics
sqlalchemy_host_database = os.getenv("SQLALCHEMY_HOST_DATABASE")
    
@dag(".dan_dag_1",
     description="Simple dag",
     default_args=default_args
     )
def basic_dag():
    @task()
    def extract():
        print("Extracting data")
        # this should be a secret, consider making all that a .env
        engine = create_engine(f"{sqlalchemy_db}+{sqlalchemy_db_jdbc}://{sqlalchemy_username}:{sqlalchemy_password}@{sqlalchemy_host_address}:{sqlalchemy_host_port}/{sqlalchemy_host_database}")
        try:
            stmt = """
            SELECT * 
            FROM prun_data."Dimitri Company Orders"
            """
            dataframe = pd.read_sql(
                sql=stmt,
                con=engine
            )
            jsoned_dataframe = dataframe.to_json()
            return jsoned_dataframe
        except Exception as e:
            print("Task failed due to: ", e)

    @task()
    def transform(jsonified_data: str):
        print("Transforming data")
        order_cost = 0
        if jsonified_data is not None:
            # Parse the JSON string back into a dictionary
            data_dict = json.loads(jsonified_data)
            for individual_cost in data_dict.values():
                order_cost += individual_cost
        else:
            print("No data to transform")
        return {"total_order_value": order_cost}

    @task()
    def load(dataframe: pd.DataFrame):
        json = dataframe
        df = pd.read_json(json)
        try:
            display(df)
        except Exception as e:
            print("Task failed due to: ", e)
            print(df)

    user_total_order_value = extract()
    order_summary = transform(user_total_order_value)
    load(order_summary["total_order_value"])

basic_dag()