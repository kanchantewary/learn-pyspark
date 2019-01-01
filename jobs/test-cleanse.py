#spark-submit test-cleanse.py /home/user/workarea/projects/pyspark-kt-01/config/param.conf dev

import sys
sys.path.append('/home/user/workarea/projects/pyspark-kt-01/jobs/python/dq/dq')
import cleanse as cl
import configparser as cp
import time


config = cp.ConfigParser()
config.read(sys.argv[1])
env = sys.argv[2]
#config.read('/home/user/workarea/projects/pyspark-kt-01/config/param.conf')
srcdir = config.get(env,'srcdir')
outdir = config.get(env,'outdir')
srcfilename = config.get(env,'srcfilename')

#from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import *  #required to use StructType, to define schema
from pyspark.sql.functions import udf

spark = SparkSession.builder.appName("run cleansing").getOrCreate()

#create spart context from spark session

sc = spark.sparkContext

#set log level

sc.setLogLevel("ERROR")
#sc.setLogLevel("INFO")

#create rdd manually

#create dataframe from file

df2 = spark.read.csv(srcdir+srcfilename, header=True)
df2.show()

pass_udf = udf(lambda x:cl.passport(x),StringType())

#facing error here --no module named cleanse

df2_modified = df2.withColumn("cleansed", pass_udf(df2.passport))
df2_modified.show()

df2.dtypes

print(srcdir)
print(outdir)
print(srcfilename)

x=cl.passport('            m123          ')
print(x)

