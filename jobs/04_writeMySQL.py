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
spark = SparkSession.builder.appName("Pyspark write into mysql").getOrCreate()

#create spart context from spark session

sc = spark.sparkContext

#set log level

sc.setLogLevel("ERROR")
#sc.setLogLevel("INFO")

#create rdd manually

#create dataframe from file

df2 = spark.read.csv('/home/user/workarea/csv/cities.csv', header=True)
df2.show()

df2.dtypes

#df2 = spark.read.json('/home/user/workarea/projects/json/sample1.json')

#df2.show(5)


#------------------------------------------------------------------------------------------------------------------------------------------------------

#write into mysql

#configuration details
hostname="localhost"
jdbcport=3306
dbname="TEST"
username="kanchan@localhost"
password="password"
mysql_url = "jdbc:mysql://{0}:{1}/{2}?user={3}&password={4}".format(hostname,jdbcport,dbname,username,password)
mysql_driver = "com.mysql.jdbc.Driver"
query = "CITIES"

#write modes: append, Overwrite
df2.write.format("jdbc").options(driver=mysql_driver,url=mysql_url, dbtable=query).mode('overwrite').save()

#-------------------------------------------------------------------------------------------------------------------------------------------------------

