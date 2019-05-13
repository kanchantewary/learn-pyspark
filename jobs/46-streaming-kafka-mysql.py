#read from a spark topic and write out in console
#spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.0, mysql:mysql-connector-java:8.0.13 46-streaming-kafka-mysql.py

#Before triggering spark submit, follow below steps to start writing into kafka topic
#(1) go to /usr/local/zookeeper/bin/ and start zookeeper server
#zkServer.sh start
#(2) go to /usr/local/kafka/bin/ and start kafka server
#kafka-server-start.sh -daemon /usr/local/kafka/config/server.properties
#(3) create the kafka topic to be written
#kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic spark
#(4) describe the kafka topic (optional)
#kafka-topics.sh --zookeeper localhost:2181 --describe --topic spark
#(5) start writing into kafka topic from console:
#kafka-console-producer.sh --broker-list localhost:9092 --topic spark

#create spark session

from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

spark = SparkSession\
        .Builder().appName("streaming-kafka-console")\
        .master("local[3]")\
        .getOrCreate()

sc=spark.sparkContext

spark.conf.set("spark.sql.shuffle.partitions",5)

df=spark.readStream.format("kafka")\
        .option("kafka.bootstrap.servers","localhost:9092")\
        .option("subscribe","spark")\
        .option("startingOffsets","earliest")\
        .load()

df1=df.selectExpr("CAST(key as string)", "CAST(value as string)")

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
query = "KAFKA_TOPIC"

#write modes: append, Overwrite
#df2.write.format("jdbc").options(driver=mysql_driver,url=mysql_url, dbtable=query).mode('overwrite').save()

#-------------------------------------------------------------------------------------------------------------------------------------------------------


streaming_query = df1.writeStream.format("jdbc").outputMode("append").options(driver=mysql_driver,url=mysql_url, dbtable=query).start()
streaming_query.awaitTermination()

