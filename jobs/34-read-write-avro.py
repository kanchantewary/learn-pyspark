#read and write parquet files
#spark-submit --packages org.apache.spark:spark-avro_2.12:2.4.2
#spark-submit --packages com.databricks:spark-avro_2.11:4.0.0 34-read-write-avro.py

from pyspark.sql import SparkSession
from pyspark.sql import *
import time
#import com.databricks.spark.avro
#from org.apache.spark.sql.avro import *

print(f'start time is {time.time()}')

spark = SparkSession.Builder().appName("avro").master("local[2]").getOrCreate()


sc = spark.sparkContext

data = spark.read.format("csv").\
        option("inferSchema","true").\
        option("mode","FAILFAST").\
        option("header","true").\
        option("samplingRatio",0.05).\
        load("/home/user/workarea/projects/learn-pyspark/data/departuredelays.csv")

data.show(5)

data.write.format('com.databricks.spark.avro').save("/home/user/workarea/projects/learn-pyspark/data/departure-delay.avro")

#following error occurs from above code snippet:
#py4j.protocol.Py4JJavaError: An error occurred while calling o43.save.
#: java.lang.ClassNotFoundException: Failed to find data source: org.apache.spark.sql.avro.AvroFileFormat. Please find packages at http://spark.apache.org/third-party-projects.html

#data.write.format("avro").save("/home/user/workarea/projects/learn-pyspark/data/departure-delay.avro")

print(f'end time is {time.time()}')
