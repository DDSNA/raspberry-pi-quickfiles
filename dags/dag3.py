from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

from datetime import datetime

with DAG(
    dag_id="Dan_postgres_operator_dag",
    start_date=datetime(2022, 1, 1),
    schedule_interval="@once",
    catchup=False,
    tags=["postgres", "operator", "dan"],
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

    insert_user = PostgresOperator(
        task_id="insert_user",
        postgres_conn_id="postgres_default",
        sql="INSERT INTO users (username, email, created_at) VALUES ('test', 'test', '2022-01-01')",
    )
    