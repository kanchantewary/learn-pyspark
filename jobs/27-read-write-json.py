# read and write json files

from pyspark.sql import SparkSession
import json

spark = SparkSession.Builder().appName("json").master("local[2]").getOrCreate()

sc = spark.sparkContext

#data = json.load(open("/home/user/workarea/projects/learn-pyspark/data/colors.json","r"))

#rdd = sc.parallelize(data)

data = spark.read.format("json").\
        option("multiline","true").\
        option("mode","FAILFAST").\
        load("/home/user/workarea/projects/learn-pyspark/data/colors.json")

data.show(3)


