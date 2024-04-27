from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from datetime import datetime

with DAG('spark_submit_job',
         start_date=datetime(2024,5,28),
         catchup=False,
         schedule_interval='@hourly',
         tags=['test', 'spark-submit']
         ) as dag:
    
    submit_job = SparkSubmitOperator(
        task_id='submit_job',
        application='include/pyspark_script.py',
        conn_id='spark_default',
        total_executor_cores='1',
        executor_cores='1',
        executor_memory='2g',
        num_executors='1',
        driver_memory='2g',
        verbose=True
    )
    
    load_to_snowflake = SnowflakeOperator(
         task_id='load_to_snowflake',
         snowflake_conn_id='snowflake_default',
         database="SNOWFLAKE_SPARK",
         schema="PUBLIC",
         sql=f"""
            COPY INTO your_table
            FROM '@your_stage/yourfile'
            FILE_FORMAT = (TYPE = 'CSV')
        """
     )
    
    