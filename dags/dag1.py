from datetime import datetime

from airflow import DAG

from airflow.decorators import dag, task

from sqlalchemy import create_engine, select
import pandas as pd


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 14),
    'retries': 1,
    'schedule_interval': '@daily'
}


@dag(".dan_dag_1",
     description="Simple dag",
     default_args=default_args
     )
def basic_dag():
    @task()
    def extract():
        print("Extracting data")
        # this should be a secret, consider making all that a .env
        engine = create_engine('postgresql://databricks_user:Databricks@viaduct.proxy.rlwy.net/railway')
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
    def transform(jsonified_data: dict):
        print("Transforming data")
        order_cost = 0
        if jsonified_data is not None:
            for individual_cost in jsonified_data.values():
                order_cost += individual_cost
        else:
            print("No data to transform")
        return {"total_order_value": order_cost}

    @task()
    def load(total_order_value : float):
        print("Loading data")
        print(f"Total order cost is: {total_order_value:.2f}")

    user_total_order_value = extract()
    order_summary = transform(user_total_order_value)
    load(order_summary["total_order_value"])

basic_dag()