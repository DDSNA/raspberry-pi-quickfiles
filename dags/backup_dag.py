from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.datasets import Dataset
from airflow.sensors.http_sensor import HttpSensor

from airflow.providers.google.cloud.hooks.gcs import GCSHook
from airflow.providers.http.operators.http import SimpleHttpOperator

import datetime




 # utility function to time tasks
def airflow_backup_main():
    import subprocess
    import os
    import logging
    from utils import timeit
    """
    A script for dumping airflow database to s3
    """
    logging.basicConfig(level='INFO', format='%(asctime)s %(levelname)s %(message)s',filename='airflow_backup.log')
    gcs_hook: GCSHook = GCSHook(gcp_conn_id="gcp-dan")

    @timeit
    def do_airflow_backup():
        @timeit
        def move_old_backups():
            for k in reversed(range(7)):
                source = '{}{}{}'.format(gcp_folder, output_file.name, k if k > 0 else '')
                target = '{}{}{}'.format(gcp_folder, output_file.name, k + 1)
                logging.info("moving %s to %s" % (source, target))
                try:
                    copy_source = {'Bucket': gcp_bucket, 'Key': source}
                    gcs_hook.copy(source, gcp_bucket, target)
                except Exception as ex:
                    logging.info(ex)

        @timeit
        def generate_fresh_backup():
            # first airflow is AIRFLOW_USER, second is AIRFLOW_PASS
            dump_airflow_db = subprocess.Popen(["mysqldump", "-u", "airflow", "-p" + "airflow", 'airflow'],
                                            stdout=output_file)
            dump_airflow_db.wait()
            if dump_airflow_db.returncode != 0:
                raise Exception("Failed to dump airflow db")

        @timeit
        def upload_new_backup():
            gcs_hook.upload(
            bucket_name="simple-bucket-ddsna",
            object_name=f"testing/airflow/backups/{output_file.name}",
            filename=f"{output_file.name}")
            logging.info("Removing local file: {}".format(output_file.name))
            os.remove(output_file.name)

        output_file = open("airflow_backup.sql", "w")
        gcp_folder = "testing/airflow/backups/"
        gcp_bucket = "simple-bucket-ddsna"

        generate_fresh_backup()
        move_old_backups()
        upload_new_backup()

        logging.info("Backup complete!!!")

with DAG(
    dag_id="Dan_airflow_backup",
    start_date=datetime.datetime(2024,6,6),
    schedule="@daily",
    tags=["gcp", "dan", "backup"],
    catchup=False
) as dag:

    airflow_backup = PythonOperator(
        task_id="airflow_backup",
        python_callable=airflow_backup_main
    )

airflow_backup