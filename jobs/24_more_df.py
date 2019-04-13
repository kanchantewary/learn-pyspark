#practice on dataframes0

#create dataframe from rdd

#from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import *  #required to use StructType, to define schema

#create spark session, refer to config parameters for more elaboration
#following works fine, mysql access is working, but mongo access is not
#spark-submit --packages mysql:mysql-connector-java:8.0.13 pycook2.py
#multiple packages should be separated by comma, without whitespace
#below command had incorrect version of mongo connector, methodnot foud error was thrown
#spark-submit --packages mysql:mysql-connector-java:8.0.13,org.mongodb.spark:mongo-spark-connector_2.11:2.0.0 pycook2.py
#BELOW IS THE FINAL COMMAND WHICH IS WORKING AND SHOULD BE USED
#spark-submit --packages mysql:mysql-connector-java:8.0.13,org.mongodb.spark:mongo-spark-connector_2.11:2.3.0 pycook2.py
spark = SparkSession.builder.appName("Pyspark Dataframes basics").getOrCreate()

#create spart context from spark session

sc = spark.sparkContext

#set log level

sc.setLogLevel("ERROR")
#sc.setLogLevel("INFO")

#create rdd manually

rdd1 = sc.parallelize([(1,'kanchan', 2.29),(2,'sima',5.46),(3,'ribhu', 4.67)])

print(rdd1.collect())

#create dataframe from rdd. named columns are being added to the rdd

df1 = spark.createDataFrame(rdd1,['id','name','score'])

#show top 20 rows

df1.show()

df1.select('name').show()

df1.filter(df1['score']>3).show()

df1.withColumn('newscore', df1.score*10).show()

df1.show()

#print schema

df1.printSchema()

#create dataframe from file

df2 = spark.read.csv('/home/user/workarea/csv/cities.csv', header=True)
df2.show()

df2.dtypes

#df2 = spark.read.json('/home/user/workarea/projects/json/sample1.json')

#df2.show(5)


#------------------------------------------------------------------------------------------------------------------------------------------------------
#read using a schema


schema1 = StructType([StructField("Country",StringType(),True),StructField("City",StringType(),True),StructField("Population",IntegerType(),True)])

countries = ['India','USA','Brazil','Spain']
cities = ['kolkata','new york', 'sao paolo', 'madrid']
population = [1000,500,800,600]

df3 = spark.createDataFrame(list(zip(countries,cities,population)),schema=schema1)
df3.show()

#-------------------------------------------------------------------------------------------------------------------------------------------------------

#define schema to read biostats file

biostats_schema = StructType([
    StructField("Name",StringType(),True),
    StructField("Sex",StringType(),True),
    StructField("Age",IntegerType(),True), 
    StructField("Height",IntegerType(),True),
    StructField("Weight",IntegerType(),True)])

#df4 = spark.read.csv('/home/user/workarea/csv/biostats_wo_header.txt', schema=biostats_schema) #having issues here, all values are coming null
df4 = spark.read.csv('/home/user/workarea/csv/biostats_wo_header.txt')
df4.show()

#-------------------------------------------------------------------------------------------------------------------------------------------------------

#read from mysql

#mysql_url = "jdbc:mysql://localhost:3306"

#configuration details
hostname="localhost"
jdbcport=3306
dbname="TEST"
username="kanchan@localhost"
password="password"
mysql_url = "jdbc:mysql://{0}:{1}/{2}?user={3}&password={4}".format(hostname,jdbcport,dbname,username,password)
mysql_driver = "com.mysql.jdbc.Driver"
query = "(select * from cats) t1_alias"
df4 = spark.read.format("jdbc").options(driver=mysql_driver,url=mysql_url, dbtable=query).load()
df4.show()

#-------------------------------------------------------------------------------------------------------------------------------------------------------

#read from mongodb

#mongo_url = ""
#from pyspark.sql import SparkSession

#my_spark = SparkSession \
#    .builder \
#    .appName("myApp") \
#    .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/test.coll") \
#    .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/test.coll") \
#    .getOrCreate()

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

