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
    'start_date': datetime(2024, 3, 29),
    'retries': 3,
    'schedule_interval': '@hourly',
    'tags': ['test-tag'],
    'catchup':"False"
}

sqlalchemy_db = os.getenv("SQLALCHEMY_DB")
sqlalchemy_db_jdbc = os.getenv("SQLALCHEMY_DB_JDBC")
sqlalchemy_username = os.getenv("SQLALCHEMY_USERNAME")
sqlalchemy_password = os.getenv("SQLALCHEMY_PASSWORD")
sqlalchemy_host_address = os.getenv("SQLALCHEMY_HOST_ADDRESS")
sqlalchemy_host_port = os.getenv("SQLALCHEMY_HOST_PORT")
# this is railway not data analytics
sqlalchemy_host_database = os.getenv("SQLALCHEMY_HOST_DATABASE")
    
@dag("test_scheduled_dag_20minutes",
     description="This dag should be scheduled for every 20 minutes",
     default_args=default_args,
     schedule_interval='*/20 * * * *',
     catchup=False
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
            data_dict = json.loads(jsonified_data)
            for individual_data in data_dict.values():
                # Assuming each individual_data is a dictionary with a 'cost' key
                if 'cost' in individual_data:
                    order_cost += individual_data['cost']
                    print(f"Cost found: {individual_data['cost']}")
                else:
                    print(f"No 'cost' key found in {individual_data}")
        else:
            print("No data to transform")
        return {"total_order_value": order_cost}
    
    @task()
    def load(json_value: dict):
        print("Loading data")
        try:
            # Assuming json_value is a dictionary with a single key-value pair
            # where the key is the column name and the value is the data
            df = pd.DataFrame.from_dict(json_value, orient='index', columns=['total_order_value'])
            display(df)
        except Exception as e:
            print("Task failed due to: ", e)
            print(json_value)
        return df
    
    @task()
    def upload_to_db(df: pd.DataFrame):
        print("Uploading to postgresql in schema prun_data and table order_summary")
        try:
            df = df
            engine = create_engine(f"{sqlalchemy_db}+{sqlalchemy_db_jdbc}://{sqlalchemy_username}:{sqlalchemy_password}@{sqlalchemy_host_address}:{sqlalchemy_host_port}/{sqlalchemy_host_database}")
            df.to_sql('order_summary', con=engine, if_exists='replace', schema='prun_data')
        except Exception as e:
            print("Task failed due to: ", e)
            print(df)

    user_total_order_value = extract()
    order_summary = transform(user_total_order_value)
    df = load(order_summary)
    upload_to_db(df)

basic_dag()
