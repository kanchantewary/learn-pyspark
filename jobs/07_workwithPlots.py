#basics of spark dataframes

#from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import *  #required to use StructType, to define schema

#import python modules

import pandas as pd
from pandas import Series, DataFrame

import matplotlib
#define the backend, tkinter error occurs if this is not added, other option=agg
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#spark-submit sparkDataframes.py

spark = SparkSession.builder.appName("spark SQL basics").getOrCreate()

#create spart context from spark session

sc = spark.sparkContext

#set log level

sc.setLogLevel("ERROR")

df1 = spark.read.csv('/home/user/workarea/csv/cities.csv', header=True)
df1.show()

df1.dtypes

#create a temp table

df1.createOrReplaceTempView("city")

sqlDf1 = spark.sql("select * from city")

sqlDf1.show()
sqlDf1.printSchema()

spark.sql("describe city").show()
#spark.sql("describe detail city").show() --giving error

#spark.sql("analyze table city compute statistics").show() --giving error

sqlDf2 = spark.sql("select latd, count(1) from city group by latd")

sqlDf2.show()

pdf2 = sqlDf2.toPandas()

x = pdf2.latd

plt.bar(x,1,0.2)

plt.show()

