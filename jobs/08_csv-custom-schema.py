#practice on csv files, read using custome schema

#from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import *  #required to use StructType, to define schema

#create spark session, refer to config parameters for more elaboration
#spark-submit --packages mysql:mysql-connector-java:8.0.13,org.mongodb.spark:mongo-spark-connector_2.11:2.3.0 pycook2.py
spark = SparkSession.builder.appName("read csv using custom schema").getOrCreate()

#create spart context from spark session

sc = spark.sparkContext

#set log level

sc.setLogLevel("ERROR")
#sc.setLogLevel("INFO")

#create dataframe from file

city_schema = StructType([StructField('latd',StringType(), True),
StructField('latm',StringType(), True),
StructField('lats',StringType(), True),
StructField('ns',StringType(), True),
StructField('longd',IntegerType(), True),
StructField('longm',IntegerType(), True),
StructField('longs',IntegerType(), True),
StructField('ew',StringType(), True),
StructField('city',StringType(), True),
StructField('state',StringType(), True)])

#df2 = spark.read.csv('/home/user/workarea/projects/pyspark-kt-01/tests/data/cities.csv', header=True, inferSchema=True, sep=',',mode='DROPMALFORMED',ignoreLeadingWhiteSpace=True,ignoreTrailingWhiteSpace=True)

df2 = spark.read.csv('/home/user/workarea/projects/pyspark-kt-01/tests/data/cities.csv', header=True, schema=city_schema, sep=',',mode='DROPMALFORMED',ignoreLeadingWhiteSpace=True,ignoreTrailingWhiteSpace=True)

df2.show()

df2.printSchema()

df2.dtypes

#-------------------------------------------------------------------------------------------------------------------------------------------------------

