from pyspark.sql import SparkSession

spark = SparkSession.builder.remote("sc://192.168.0.36:15002").getOrCreate()