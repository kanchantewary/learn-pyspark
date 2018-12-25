
#from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import *  #required to use StructType, to define schema

#create spark session, refer to config parameters for more elaboration
#before running spark-submit, ensure mongodb service is running. run 'sudo service mongod start' to start the service
#spark-submit --packages org.mongodb.spark:mongo-spark-connector_2.11:2.3.0 read-mongodb.py
spark = SparkSession.builder.appName("Pyspark work with JSON and XML").getOrCreate()

#create spart context from spark session

sc = spark.sparkContext

#set log level

sc.setLogLevel("ERROR")
#sc.setLogLevel("INFO")

#-------------------------------------------------------------------------------------------------------------------------------------------------------

#read from mongodb

df5 = spark.read.format("com.mongodb.spark.sql.DefaultSource").option("spark.mongodb.input.uri","mongodb://localhost:27017/MyDB1.inventory").load()

df5.printSchema()
df5.show()

#perform filter on the dataframe, it would run in mongo

print("filter applied on mongo inventory collection:")

df5.filter(df5['qty']>50).show()

#perform select query against the dataframe, create a temporary table first

df5.createOrReplaceTempView("temp_inventory")

df6 = spark.sql("SELECT ITEM, QTY, SIZE FROM TEMP_INVENTORY WHERE QTY>75")

df6.show()

#add example of aggregation pipeline usage

