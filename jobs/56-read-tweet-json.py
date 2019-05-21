# read and write json files
#pip3 install langdetect

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from langdetect import detect
from pyspark.sql.types import *

import json

spark = SparkSession.Builder().appName("json").master("local[2]").getOrCreate()

sc = spark.sparkContext

#data = json.load(open("/home/user/workarea/projects/learn-pyspark/data/colors.json","r"))

#rdd = sc.parallelize(data)

#register a udf for language detection

def detect_tweet_lang(s):
    return detect(s)

spark.udf.register("detect_tweet_lang",detect_tweet_lang)

"""
data = spark.read.format("json").\
        option("multiline","true").\
        option("mode","FAILFAST").\
        load("/home/user/workarea/projects/learn-pyspark/data/source/tweets.json")

#data.printSchema()
#print(data.schema)

#run the following code to generate schema file in json format
f=open("/home/user/workarea/projects/learn-pyspark/config/tweets.schema","w+")
f.write(data.schema.json())
f.close()

"""

#pass custome schema from the file generated earlier, convert to struct type


tweet_schema_json = spark.read.text("/home/user/workarea/projects/learn-pyspark/config/tweets.schema").first()[0]
tweet_schema = StructType.fromJson(json.loads(tweet_schema_json))

tweets = spark.read.parquet("/home/user/workarea/projects/learn-pyspark/data/out/tweets-from-kafka/")


tweets1=tweets.withColumn('json',from_json(col('value'),tweet_schema))

t2 = tweets1.withColumn('text',substring_index(col('json.text'),':',-1))
#t2.printSchema()

#t3 = t2.withColumn("lang",detect_tweet_lang(t2["text"].cast("string"))).select('text','lang')
t3 = t2.withColumn("lang",lit("en")).select('text','lang')
t3.printSchema()


#.write.format("csv").mode("overwrite").save("/home/user/workarea/projects/learn-pyspark/data/out/tweets-text")

#tweets1.select(explode(col('value')).alias('flattened')).show(5)



