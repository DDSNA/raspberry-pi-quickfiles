#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sqlalchemy
from pathlib import Path
import requests
import argparse
import os
from time import time
# parser setup

parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')
    
def main(params):
    # sqlalchemy_db = "postgresql"
    # sqlalchemy_db_jdbc = "psycopg2"
    # sqlalchemy_username = params.user
    # sqlalchemy_password = params.password
    # sqlalchemy_host_address = params.host
    # sqlalchemy_host_port = params.port
    # sqlalchemy_host_database = params.db
    # sqlalchemy_table_name = params.table_name
    sqlalchemy_db = "postgresql"
    sqlalchemy_db_jdbc = "psycopg2"
    sqlalchemy_username = "databricks_user"
    sqlalchemy_password = "Databricks"
    sqlalchemy_host_address = "viaduct.proxy.rlwy.net"
    sqlalchemy_host_port = "53745"
    sqlalchemy_host_database = "data_analytics"
    sqlalchemy_table_name = params.table_name
    csv_url = params.url

    if csv_url.endswith('.csv.gz'):
        csv_name = 'output.csv.gz'
    else:
        csv_name = 'output.csv'

    os.system(f"wget {csv_url} -O {csv_name}")

    engine = sqlalchemy.create_engine(f"{sqlalchemy_db}+{sqlalchemy_db_jdbc}://{sqlalchemy_username}:{sqlalchemy_password}@{sqlalchemy_host_address}:{sqlalchemy_host_port}/{sqlalchemy_host_database}")

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)
    df = next(df_iter)


    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.head(n=0).to_sql(name=sqlalchemy_table_name, con=engine, if_exists='replace', schema="powerbi_sets")
    df.to_sql(name=sqlalchemy_table_name, schema="powerbi_sets", chunksize=25000, con=engine, if_exists='append')

    while True:
        try:
            t_start = time()
            df = next(df_iter)
            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

            df.to_sql(name=sqlalchemy_table_name, con=engine, if_exists='append', schema="powerbi_sets")
            t_end = time()

            print('inserted another chunk, took %.3f second' % (t_end - t_start))
        except StopIteration:
            print("Finished ingesting data into the postgres database")
            break

if __name__ == "__main__":
    parser.add_argument('--user', help ='username for postgres')
    parser.add_argument('--password', help ='password for postgres')
    parser.add_argument('--host', help ='host address for postgres')
    parser.add_argument('--port', help ='host port for postgres')
    parser.add_argument('--db', help ='database name for postgres')
    parser.add_argument('--table-name', help ='name of table in postgres')
    parser.add_argument('--url', help ='url of the csv file')

    args = parser.parse_args()

    main(args)