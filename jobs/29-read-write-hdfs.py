# read and write json files

from pyspark.sql import SparkSession
from pyspark.sql.types import *
import json,time

start=time.time()

spark = SparkSession.Builder().appName("hdfs").master("local[2]").getOrCreate()

sc = spark.sparkContext

r3 = sc.parallelize(["spark","hadoop","mongo","hive","nifi"])
r3.saveAsTextFile("hdfs://localhost:9000/test/sparkrdd.txt")


