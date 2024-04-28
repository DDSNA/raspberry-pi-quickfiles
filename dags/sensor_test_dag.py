from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.decorators import dag, task
from airflow.models import Variable, Connection
from airflow.datasets import Dataset

from airflow.providers.microsoft.azure.hooks.wasb import WasbHook

from datetime import datetime
import zipfile
# 	stock_market_source_api_key
# "Free accounts have access to the following countries: Mexico, New Zealand, Sweden, Thailand. For more, contact us at support@tradingeconomics.com."
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
    def get_new_updates():
        import requests
        api_key = Variable.get('stock_market_source_api_key')
        api_link= Variable.get('stock_market_source_api_link')
        api_countries: dict[str, list[str]] = Variable.get('stock_market_countries')
        api_country = api_countries[0[0]]
        try:
            data = requests.get(
                url=f'https://api.tradingeconomics.com/country/{api_country}?',
                headers={
                    'Authorization': f'{api_key}'
                }
            )
            return data
        except Exception:
            raise requests.exceptions.HTTPError
    @task
    def update_dataset():
        outlets=[Dataset("",
                         extra={"last_checked":f"{datetime.timestamp}"}
                         )]
    @task
    def upload_json_to_blob(json_string:str):
        import json
        json = json.loads(json_string)
        api_countries: dict[str, list[str]] = Variable.get('stock_market_countries')
        api_country = api_countries[0[0]]
        with open("../materials/data.json", "w") as outfile:
            json.dump(json, outfile, indent=4)  # Add indent for readability
        WasbHook(
            #TODO CONID
            wasb_conn_id=''
        ).load_file(
            file_path="../materials/data.json",
            container_name="sparkdata",
            blob_name=f"market_data_{api_country}_{datetime.today()}.json"
        )
    extract = get_new_updates()
    update_dataset()
    upload_json_to_blob(extract)

dataset_producer_dag()

        
    

# to be used if an archived dataset is found again
# def dataset_producer_dag():
#     @task
    # def get_new_archive():
    #     import requests
    #     api_link = Variable.get('RO_stock_market_api_link')
    #     r = requests.get(
    #         url=api_link,
    #         timeout=120
    #     )

        # with open(f'{local_file_destination}/stock_romanian_{datetime.today()}_archive.zip', 'wb') as file:
        #     file.write(r.content)

        # with zipfile.ZipFile(file=f'../materials/stock_romanian_{datetime.today()}_archive.zip',
        #                      mode='r') as zip_ref:
        #     zip_info = zip_ref.infolist()
        #     print(zip_info)
        #     zip_ref.extractall("../materials")

