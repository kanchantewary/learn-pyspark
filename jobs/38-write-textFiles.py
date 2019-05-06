#read and write ORC files

from pyspark.sql import SparkSession
from pyspark.sql import *
import time

start_time=time.time()

spark = SparkSession.Builder().appName("orc").master("local[2]").getOrCreate()


sc = spark.sparkContext

data = spark.read.format("csv").\
        option("inferSchema","true").\
        option("mode","FAILFAST").\
        option("header","true").\
        option("samplingRatio",0.05).\
        load("/home/user/workarea/projects/learn-pyspark/data/departuredelays.csv")

data.show(5)

#Codec [gzip] is not available. Available codecs are uncompressed, lzo, snappy, zlib, none, default is snappy (if nothing is mentioned
data.write.format('orc').option("compression","zlib").mode("overwrite").save("/home/user/workarea/projects/learn-pyspark/data/departure-delay.orc")

end_time = time.time()

print(f'execution time = {end_time-start_time} seconds')

#execution time (seconds), file size

#using snappy = 46, 6.2 MB
#using zlib = 48, 4.9 MB
#using uncompressed = 29.3,9.8 MB
#using lzo = 45.7, 6.3 MB 
