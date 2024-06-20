from pyspark.sql import SparkSession

def drop_columns_from_dataset(input_path, output_path):
    """
    Reads from input (CSV!) drops, to columns and saves to output
    """

    spark = SparkSession.builder.appName("DropColumnsApp").getOrCreate()

    df = spark.read.csv(input_path, header=True, inferSchema=True)

    columns_to_drop = ["column1", "column2"]
    df_transformed = df.drop(*columns_to_drop)

    df_transformed.write.csv(output_path, header=True)

    spark.stop()

if __name__ == '__main__':
    input_path = '../materials/columnsnotdropped.csv'
    output_path = '../materials/columnsshouldnowbedropped.csv'

    drop_columns_from_dataset(input_path, output_path)