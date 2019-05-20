# read parquet files created from kafka topic using structured streaming

from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
import time

print(f'start time is {time.time()}')

spark = SparkSession.Builder().appName("parquet").master("local[2]").getOrCreate()

tweets = spark.read.parquet("/home/user/workarea/projects/learn-pyspark/data/out/tweets-from-kafka/")

tweets.printSchema()

schema = tweets.select(schema_of_json(str(col("value"))))

print(schema)

tweets.withColumn('json',from_json(col('value'),schema)).show(5)

#tweets.show(5)

#tweets.select("value").write.json("/home/user/workarea/projects/learn-pyspark/data/out/tweets.json")

#tweet_json = spark.read.json("/home/user/workarea/projects/learn-pyspark/data/out/tweets.json/test.json")

#tweet_json.printSchema()

#tweet_json.show(5)


