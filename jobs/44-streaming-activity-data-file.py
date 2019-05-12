#read activity data, example from spark definitive guide. files are in json format.

#create spark session

from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

spark = SparkSession\
        .Builder().appName("streaming-activity-data")\
        .master("local[3]")\
        .getOrCreate()

sc=spark.sparkContext

spark.conf.set("spark.sql.shuffle.partitions",5)
static = spark.read.json("/home/user/workarea/projects/Spark-The-Definitive-Guide/data/activity-data/")

static.show(5)
static.printSchema()

streaming=spark.readStream.schema(static.schema).option("maxFilesPerTrigger",1).json("/home/user/workarea/projects/Spark-The-Definitive-Guide/data/activity-data/")

activityCounts=streaming.groupBy("gt").count()

activityQuery=activityCounts.writeStream.queryName("activity_counts").format("memory").outputMode("complete").start()

#activityQuery.awaitTermination()

from time import sleep

for i in range(100):
    spark.sql("select * from activity_counts").show()
    sleep(1)

activityQuery.awaitTermination()
