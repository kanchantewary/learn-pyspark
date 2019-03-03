#spark certification practice - work on retail data, structured streaming, Definitive Guide chapter-2

from pyspark.sql import SparkSession
from pyspark.sql.functions import desc,col,window,column,date_format
import time

spark = SparkSession.Builder().appName("test13").master("local[3]").getOrCreate()

spark.conf.set("spark.sql.shuffle.partitions","5")

spark.conf.set("spark.executor.memory", '256m')
spark.conf.set("spark.executor.cores",'3')
spark.conf.set("spark.cores.max",'3')
spark.conf.set("spark.driver.memory",'256m')
spark.conf.set("spark.logConf",'True')
spark.conf.set("spark.driver.supervise",'True')

staticdf = spark.read.option("inferSchema","true").option("header","true").csv("/home/user/workarea/projects/Spark-The-Definitive-Guide/data/retail-data/by-day/*.csv")

staticdf.createOrReplaceTempView("retail_data")
staticSchema=staticdf.schema

preppeddf=staticdf.na.fill(0).withColumn("day_of_the_week",date_format(col("InvoiceDate"),"EEEE")).coalesce(5)

traindf=preppeddf.where("InvoiceDate < '2011-07-01'")
testdf=preppeddf.where("InvoiceDate >= '2011-07-01'")

traindf.count()
testdf.count()

#will come back to complete the remaining steps later. KT
