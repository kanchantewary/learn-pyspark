#create spark session

from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
import pyarrow

warehouseLocation = '/tmp'

spark = SparkSession\
        .Builder().appName("spark-arrow")\
        .master("local[3]")\
        .config("spark.warehouse.work.dir",warehouseLocation)\
        .enableHiveSupport()\
        .getOrCreate()

sc=spark.sparkContext

df=spark.range(10000).toDF('id').withColumn("x",rand())

df.printSchema()

spark.conf.set("spark.sql.execution.arrow.enabled","true")

#following warning is thrown, reason unknown:
#/home/user/.local/lib/python3.6/site-packages/pyarrow/__init__.py:152: UserWarning: pyarrow.open_stream is deprecated, please use pyarrow.ipc.open_stream
#  warnings.warn("pyarrow.open_stream is deprecated, please use "

pdf=df.toPandas()

print(pdf.describe())

#create dataframe from pandas df

spark.createDataFrame(pdf)
df.describe().show()

