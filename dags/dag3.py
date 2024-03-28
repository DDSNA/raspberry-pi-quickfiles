from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

from datetime import datetime

with DAG(
    dag_id="postgres_operator_dag",
    start_date=datetime(2022, 1, 1),
    schedule_interval="@once",
    catchup=False,
    tags=["postgres", "operator"],
) as dag:

    create_table = PostgresOperator(
        task_id="create_table",
        postgres_conn_id="postgres_default",
        sql="""
        CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR NOT NULL,
            email VARCHAR NOT NULL,
            created_at TIMESTAMP NOT NULL
        )
        """,
    )
