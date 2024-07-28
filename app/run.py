from pyspark.sql import SparkSession
import time

def main():
    # Initialize SparkSession
    spark = SparkSession.builder \
        .appName("PythonApp") \
        .master("spark://spark:7077") \
        .getOrCreate()

    # Example data processing
    # You can replace this with your actual data processing logic

    # Creating a sample DataFrame
    data = [("Alice", 34), ("Bob", 45), ("Catherine", 29)]
    columns = ["Name", "Age"]
    df = spark.createDataFrame(data, columns)

    # Perform a transformation (e.g., filter data)
    df_filtered = df.filter(df.Age > 30)

    # Show the results
    df_filtered.show()

    # Stop the Spark session
    #spark.stop()
    # Keep the container running indefinitely
    #while True:
    #    time.sleep(1)


if __name__ == "__main__":
    main()