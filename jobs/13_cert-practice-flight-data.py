#spark certification practice - work on flight data, Definitive Guide chapter-2

from pyspark.sql import SparkSession
from pyspark.sql.functions import max,desc

spark = SparkSession.Builder().appName("test13").master("local[3]").getOrCreate()

flightdata = spark.read.option("inferSchema","true").option("header","true").csv("/home/user/workarea/projects/learn-pyspark/data/2015-flight-data.txt")

flightdata.take(5)
flightdata.explain()
flightdata.sort("count").explain()

spark.conf.set("spark.sql.shuffle.partitions","5")

flightdata.sort("count").explain()

fd1=flightdata.groupBy("DEST_COUNTRY_NAME").count()
fd1.explain()

fd2=flightdata.select(max("count"))

fd2.explain()

fd3 = flightdata.groupBy("DEST_COUNTRY_NAME").sum("count").withColumnRenamed("sum(count)","destination_total").sort(desc("destination_total")).limit(5)

fd3.explain()

fd3.show()
