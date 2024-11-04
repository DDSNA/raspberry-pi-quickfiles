from pyspark.sql import SparkSession
import requests

spark: SparkSession = SparkSession.builder \
    .appName("PostgreSQL Connection") \
    .config("spark.jars", "postgresql-42.7.4.jar") \
    .getOrCreate()

response = requests.get("https://www.kaggle.com/api/v1/datasets/download/jjinho/wikipedia-20230701")
with open("wikipedia-20230701.zip", "wb") as file:
    file.write(response.content)

df = spark.read.option("header", "true").csv("wikipedia-20230701.zip")

