from pyspark.sql import SparkSession
import logging
# Set up logging configuration
logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def source_to_target():
    try:
        spark = SparkSession.builder.appName("batch job 1").getOrCreate()

    except Exception as e:
        print("Cluster creation failed  due to ", e)

