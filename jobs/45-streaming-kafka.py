#read activity data, example from spark definitive guide. files are in json format.
#spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.0 45-streaming-kafka.py [WORKING]
#spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:2.4.0 45-streaming-kafka.py [THIS CAUSED ERROR - 'KafkaSourceProvider could not be instantiated']

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
        .Builder().appName("streaming-kafka")\
        .master("local[3]")\
        .getOrCreate()

sc=spark.sparkContext

spark.conf.set("spark.sql.shuffle.partitions",5)

df=spark.readStream.format("kafka")\
        .option("kafka.bootstrap.servers","localhost:9092")\
        .option("subscribe","spark")\
        .option("startingOffsets","earliest")\
        .load()

#streaming.show() [THIS DOES NOT WORK FOR STREAMING]

df1=df.selectExpr("CAST(value) as string")

df1.writeStream.format("console").option("truncate","false").start().awaitTermination()

