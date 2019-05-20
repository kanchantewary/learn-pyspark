# read and write json files
#pip3 install langdetect

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from langdetect import detect

import json

spark = SparkSession.Builder().appName("json").master("local[2]").getOrCreate()

sc = spark.sparkContext

#data = json.load(open("/home/user/workarea/projects/learn-pyspark/data/colors.json","r"))

#rdd = sc.parallelize(data)

data = spark.read.format("json").\
        option("multiline","true").\
        option("mode","FAILFAST").\
        load("/home/user/workarea/projects/learn-pyspark/data/source/tweets.json")

#data.printSchema()
#print(data.schema)

tweets = spark.read.parquet("/home/user/workarea/projects/learn-pyspark/data/out/tweets-from-kafka/")


tweets1=tweets.withColumn('json',from_json(col('value'),data.schema))

tweets1.withColumn('text',substring_index(col('json.text'),':',-1)).withColumn("lang",detect(col('text'))).select('text','lang').show(5)


#.write.format("csv").mode("overwrite").save("/home/user/workarea/projects/learn-pyspark/data/out/tweets-text")

#tweets1.select(explode(col('value')).alias('flattened')).show(5)



