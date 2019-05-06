#read and write ORC files

from pyspark.sql import SparkSession
from pyspark.sql import *
import time,os

start_time=time.time()

spark = SparkSession.Builder().appName("orc").master("local[2]").getOrCreate()


sc = spark.sparkContext
filepath = '/home/user/workarea/projects/learn-pyspark/data/departure-delay.orc'

if os.path.exists(filepath):
    data = spark.read.format("orc").load(filepath)
    data.show(5)
else:
    print('ERROR: file does not exist')


end_time = time.time()

print(f'execution time = {end_time-start_time} seconds')

