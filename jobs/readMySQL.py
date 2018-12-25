#practice on dataframes0

from pyspark.sql import SparkSession
from pyspark.sql.types import *  #required to use StructType, to define schema

#spark-submit --packages mysql:mysql-connector-java:8.0.13 --properties-file jdbc.properties
spark = SparkSession.builder.appName("Pyspark Dataframes basics").getOrCreate()

#create spart context from spark session

sc = spark.sparkContext


#read from mysql

#mysql_url = "jdbc:mysql://localhost:3306"

#configuration details
hostname=sc.getConf().get("spark.mysql.host")
jdbcport=sc.getConf().get("spark.mysql.port")
dbname="TEST"
username=sc.getConf().get("spark.mysql.user")
password=sc.getConf().get("spark.mysql.password")
mysql_url = "jdbc:mysql://{0}:{1}/{2}?user={3}&password={4}".format(hostname,jdbcport,dbname,username,password)
mysql_driver = "com.mysql.jdbc.Driver"
query = "(select * from cats) t1_alias"
df4 = spark.read.format("jdbc").options(driver=mysql_driver,url=mysql_url, dbtable=query).load()
df4.show()

#-------------------------------------------------------------------------------------------------------------------------------------------------------


