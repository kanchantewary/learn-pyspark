#practice on dataframes0

#create dataframe from rdd

#from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import *  #required to use StructType, to define schema

#create spark session, refer to config parameters for more elaboration
#following works fine, mysql access is working, but mongo access is not
#spark-submit --packages mysql:mysql-connector-java:8.0.13 pycook3.py
#multiple packages should be separated by comma, without whitespace
#spark-submit --packages mysql:mysql-connector-java:8.0.13,org.mongodb.spark:mongo-spark-connector_2.11:2.3.0 pycook2.py
spark = SparkSession.builder.appName("Pyspark work with JSON and XML").getOrCreate()

#create spart context from spark session

sc = spark.sparkContext

#set log level

sc.setLogLevel("ERROR")
#sc.setLogLevel("INFO")

#create rdd manually

#create dataframe from file

df2 = spark.read.json('/home/user/workarea/projects/json/sample2.json',multiLine=True)
df2.show()

print(df2.storageLevel)
df2.persist(StorageLevel.DISK_ONLY_2)
print(df2.storageLevel)
df2.cache()
df2.dtypes

#df2 = spark.read.json('/home/user/workarea/projects/json/sample1.json')

#df2.show(5)


#------------------------------------------------------------------------------------------------------------------------------------------------------

#write into mysql

#configuration details
#hostname="localhost"
#jdbcport=3306
#dbname="TEST"
#username="kanchan@localhost"
#password="password"
#mysql_url = "jdbc:mysql://{0}:{1}/{2}?user={3}&password={4}".format(hostname,jdbcport,dbname,username,password)
#mysql_driver = "com.mysql.jdbc.Driver"
#query = "CITIES"

#write modes: append, Overwrite
#df2.write.format("jdbc").options(driver=mysql_driver,url=mysql_url, dbtable=query).mode('overwrite').save()

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

#df5 = spark.read.format("com.mongodb.spark.sql.DefaultSource").option("spark.mongodb.input.uri","mongodb://localhost:27017/MyDB1.inventory").load()

#df5.printSchema()
#df5.show()

#perform filter on the dataframe, it would run in mongo

#print("filter applied on mongo inventory collection:")

#df5.filter(df5['qty']>50).show()

#perform select query against the dataframe, create a temporary table first

#df5.createOrReplaceTempView("temp_inventory")

#df6 = spark.sql("SELECT ITEM, QTY, SIZE FROM TEMP_INVENTORY WHERE QTY>75")

#df6.show()

#add example of aggregation pipeline usage

