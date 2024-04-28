from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.decorators import dag, task
from airflow.models import Variable, Connection

from datetime import datetime
import zipfile

some_args = {
    'owner':'airflow',
    'start_date': datetime(2024, 3, 29),
    'end_date': datetime(2024,5,20),
    'retries': 3,
    'schedule_interval': '@daily',
    'tags': ['test-tag'],
    'catchup': "False"
}

local_file_destination = "../materials"
@dag(
    dag_id='Sensor DAG for Market Stocks Daily Update',
    description='Checks daily if the condition is true or false',
    default_args=some_args,
    )

def dataset_producer_dag():
    @task
    def get_new_archive():
        import requests
        api_link = Variable.get('RO_stock_market_api_link')
        r = requests.get(
            url=api_link,
            timeout=120
        )

        with open(f'{local_file_destination}/stock_romanian_{datetime.today()}_archive.zip', 'wb') as file:
            file.write(r.content)

        with zipfile.ZipFile(file=f'../materials/stock_romanian_{datetime.today()}_archive.zip',
                             mode='r') as zip_ref:
            zip_info = zip_ref.infolist()
            print(zip_info)
            zip_ref.extractall("../materials")

