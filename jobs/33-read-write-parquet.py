#read and write parquet files

from pyspark.sql import SparkSession
from pyspark.sql.types import *
import time

print(f'start time is {time.time()}')

spark = SparkSession.Builder().appName("parquet").master("local[2]").getOrCreate()


sc = spark.sparkContext

data = spark.read.format("csv").\
        option("inferSchema","true").\
        option("mode","FAILFAST").\
        option("header","true").\
        option("samplingRatio",0.05).\
        load("/home/user/workarea/projects/learn-pyspark/data/departuredelays.csv")

data.write.format("parquet").mode("overwrite").save("/home/user/workarea/projects/learn-pyspark/data/departure-delay.parquet")
data.write.format("parquet").option("compression","gzip").mode("overwrite").save("/home/user/workarea/projects/learn-pyspark/data/departure-delay-gzip.parquet")

print(f'end time is {time.time()}')
