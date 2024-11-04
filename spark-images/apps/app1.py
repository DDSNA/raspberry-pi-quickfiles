from pyspark.sql import SparkSession

from urllib.request import Request, urlopen
import requests

spark: SparkSession = SparkSession.builder \
    .appName("PostgreSQL Connection") \
    .config("spark.jars", "postgresql-42.7.4.jar") \
    .getOrCreate()

response = requests.get("https://www.kaggle.com/api/v1/datasets/download/jjinho/wikipedia-20230701")
with open("wikipedia-20230701.zip", "wb") as file:
    file.write(response.content)

df = spark.read.option("header", "true").csv("wikipedia-20230701.zip")


database_host = "viaduct.proxy.rlwy.net"
database_port = "53745" # update if you use a non-default port
database_name = "railway"
table = "prun_data.temporary_df_hold_bids"
user = "databricks_user"
password = "Databricks"

url = f"jdbc:postgresql://{database_host}:{database_port}/{database_name}"


