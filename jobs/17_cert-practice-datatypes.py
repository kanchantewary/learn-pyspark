#spark certification practice - work on retail data, structured streaming, Definitive Guide chapter-2

from pyspark.sql import SparkSession
from pyspark.sql.functions import desc,col,window,column,date_format
import time

spark = SparkSession.Builder().appName("test13").master("local[3]").getOrCreate()

df=spark.read.format("csv")\
        .option("header","true")\
        .option("inferSchema","true")\
        .load("/home/user/workarea/projects/Spark-The-Definitive-Guide/data/retail-data/by-day/2010-12-01.csv")

df.printSchema()
df.createOrReplaceTempView("dfTable")


#converting to spark datatypes

from pyspark.sql.functions import lit

df.select(lit(5),lit("five"),lit(5.0))

#use of boolean expressions

df.where(col("InvoiceNo") == "536365")\
        .select("InvoiceNo","Description")\
        .show(5,False)

#another way

df.where("InvoiceNo = 536367")\
        .show(5,False)

#using multiple filters

from pyspark.sql.functions import instr

priceFilter=col("UnitPrice") > 600
descripFilter=instr(df.Description,"POSTAGE") >= 1
df.where(df.StockCode.isin("DOT")).where(priceFilter|descripFilter).show()

#specify a boolean column

DOTCodeFilter=col("StockCode") == "DOT"
priceFilter=col("UnitPrice") > 600
descripFilter=instr(df.Description,"POSTAGE") >= 1
df.withColumn("isExpensive", DOTCodeFilter & (priceFilter|descripFilter))\
        .where("isExpensive")\
        .select("UnitPrice","isExpensive")\
        .show(5,False)




#using expressions

from pyspark.sql.functions import expr

df.withColumn("isExpensive",expr(NOT UnitPrice <= 250))\
        .where("isExpensive")\
        .select("Description","UnitPrice")\
        .show(5)

#handling null data in boolean expressions


#working with numbers


#working with strings


#regular expressions


#working with dates, timestamps


#working with nulls in data


#working with complex types


#working with JSON


#user defined functions






























