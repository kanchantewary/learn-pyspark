# read and write json files

from pyspark.sql import SparkSession
from pyspark.sql.types import *
import json,time

start=time.time()

spark = SparkSession.Builder().appName("hdfs").master("local[2]").getOrCreate()

sc = spark.sparkContext

r1 = sc.parallelize(["spark","hadoop","mongo","hive","nifi"])

######
# Get fs handler from java gateway
######
#URI = sc._gateway.jvm.java.net.URI
#Path = sc._gateway.jvm.org.apache.hadoop.fs.Path
#FileSystem = sc._gateway.jvm.org.apache.hadoop.fs.FileSystem

#fs = FileSystem.get(URI("hdfs://localhost:9000/"), sc._jsc.hadoopConfiguration())

# We can now use the Hadoop FileSystem API (https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html)
#fs.listStatus(Path('/user/hive/warehouse'))
# or
#fs.delete(Path('/test/sparkrdd.txt'))
#fs.delete(Path('/test/errors.txt'))


#import subprocess

#cmd='hdfs dfs -rm -r /test/sparkrdd.txt'

#def hdfs_delete(cmd):
#    try:
#        subprocess.call(cmd)
#    except FileNotFoundError:
#        pass

#hdfs_delete('hdfs dfs -rm -r /test/sparkrdd.txt')
#hdfs_delete('hdfs dfs -rm -r /test/errors.txt')


from pyarrow import hdfs
fs=hdfs.connect()
fs.delete('/test/errors.txt')

#r1.saveAsTextFile("hdfs://localhost:9000/test/sparkrdd.txt")

# create an rdd from hdfs file, write after applying filter

r2 = sc.textFile("hdfs://localhost:9000/test/*.log").filter(lambda x:"ERR" in x)

r2.saveAsTextFile("hdfs://localhost:9000/test/errors.txt")

