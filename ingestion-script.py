#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sqlalchemy
from pathlib import Path
import requests
import argparse
import os
# parser setup

parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

# user
#password
#host
#port
#database name
#table name
#url of the csv
    
def main(params):
    sqlalchemy_db = "postgresql"
    sqlalchemy_db_jdbc = "psycopg2"
    sqlalchemy_username = params.user
    sqlalchemy_password = params.password
    sqlalchemy_host_address = params.host
    sqlalchemy_host_port = params.port
    sqlalchemy_host_database = params.db
    sqlalchemy_table_name = params.table_name
    csv_url = params.url

    csv_name = 'output.csv'

    os.system(f"wget {csv_url} -O {csv_name}")

    engine = sqlalchemy.create_engine(f"{sqlalchemy_db}+{sqlalchemy_db_jdbc}://{sqlalchemy_username}:{sqlalchemy_password}@{sqlalchemy_host_address}:{sqlalchemy_host_port}/{sqlalchemy_host_database}")
    df = pd.read_csv(csv_name)


    query_all_pgdatabase_tables = """
    SELECT *
    FROM pg_catalog.pg_tables

    WHERE schemaname != 'pg_catalog' AND
        schemaname != 'information_schema';
    """

    pd.read_sql(sql=query_all_pgdatabase_tables, con=engine)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)


    df.to_sql(name=sqlalchemy_table_name, con=engine, schema="powerbi_sets", chunksize=25000)


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