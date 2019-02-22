#spark certification practice - work on retail data, structured streaming, Definitive Guide chapter-2

from pyspark.sql import SparkSession
from pyspark.sql.functions import desc,col,window,column

spark = SparkSession.Builder().appName("test13").master("local[3]").getOrCreate()

spark.conf.set("spark.sql.shuffle.partitions","5")

retaildata = spark.read.option("inferSchema","true").option("header","true").csv("/home/user/workarea/projects/Spark-The-Definitive-Guide/data/retail-data/by-day/*.csv")

retaildata.createOrReplaceTempView("retail_data")
staticSchema=retaildata.schema


retaildata\
        .selectExpr("CustomerId","(UnitPrice*Quantity) as total_cost","InvoiceDate")\
        .groupBy(col("CustomerId"),window(col("InvoiceDate"),"1 day"))\
        .sum("total_cost")\
        .show(5)


