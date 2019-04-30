# read and write json files

from pyspark.sql import SparkSession
from pyspark.sql.types import *
import json,time

start=time.time()

spark = SparkSession.Builder().appName("hdfs").master("local[2]").getOrCreate()

sc = spark.sparkContext

r1 = sc.parallelize(["spark","hadoop","mongo","hive","nifi"])
r1.saveAsTextFile("hdfs://localhost:9000/test/sparkrdd.txt")

# create an rdd from hdfs file, write after applying filter

r2 = sc.textFile("hdfs://localhost:9000/test/*.log").filter(lambda x:"ERR" in x)

r2.saveAsTextFile("hdfs://localhost:9000/test/errors.txt")

