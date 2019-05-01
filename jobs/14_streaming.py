#spark certification practice - work on retail data, structured streaming, Definitive Guide chapter-2

from pyspark.sql import SparkSession
from pyspark.sql.functions import desc,col,window,column
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


staticdf\
        .selectExpr("CustomerId","(UnitPrice*Quantity) as total_cost","InvoiceDate")\
        .groupBy(col("CustomerId"),window(col("InvoiceDate"),"1 day"))\
        .sum("total_cost")\
        .show(5)

streamingdf=spark.readStream.schema(staticSchema)\
        .option("maxFilesPerTrigger",1)\
        .format("csv")\
        .option("header","true")\
        .load("/home/user/workarea/projects/Spark-The-Definitive-Guide/data/retail-data/by-day/*.csv")

streamingdf.isStreaming


purchaseByCustomerPerHour =streamingdf\
        .selectExpr("CustomerId","(UnitPrice*Quantity) as total_cost","InvoiceDate")\
        .groupBy(col("CustomerId"),window(col("InvoiceDate"),"1 day"))\
        .sum("total_cost")

purchaseByCustomerPerHour.writeStream.format("memory").queryName("customer_purchases").outputMode("complete").start()

time.sleep(10)

spark.sql("select * from customer_purchases order by `sum(total_cost)` desc").show(5)


