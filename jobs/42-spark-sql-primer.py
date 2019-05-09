# work on spark-sql api

#create spark session

from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
import pyarrow

warehouseLocation = '/tmp'

spark = SparkSession\
        .Builder().appName("spark-sql-primer")\
        .master("local[3]")\
        .config("spark.warehouse.work.dir",warehouseLocation)\
        .enableHiveSupport()\
        .getOrCreate()

sc=spark.sparkContext

spark.sql("create table if not exists mysparkdb.customer(custid long,name string,email string) using csv options(header='false',path='/home/user/workarea/projects/learn-pyspark/data/source/customer.csv')").show()

df=spark.range(100).toDF("number")

df.createOrReplaceTempView("number_temp")
df.createGlobalTempView("number_global")

