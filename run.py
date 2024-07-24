import os
from pyspark.sql import SparkSession

# Get Spark master URL from environment variable
spark_master_url = os.getenv("SPARK_MASTER_URL", "spark://spark-master:7077")

# Create a SparkSession
spark = SparkSession.builder \
    .appName("MyApp") \
    .master(spark_master_url) \
    .getOrCreate()

# Example Spark code
df = spark.createDataFrame([(1, 'foo'), (2, 'bar')], ['id', 'value'])
df.show()

# Stop the SparkSession
spark.stop()