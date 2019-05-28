# schema evolution - schema merging support in parquet

from pyspark.sql import Row

from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

spark = SparkSession\
        .Builder().appName("parquet-schema-merging")\
        .master("local[3]")\
        .getOrCreate()

sc=spark.sparkContext

squaresDF = spark.createDataFrame(sc.parallelize(range(1,6)).map(lambda i: Row(single=i,Double=i**2)))
squaresDF.write.parquet("/home/user/workarea/projects/learn-pyspark/data/out/test-table/key=1")

cubesDF = spark.createDataFrame(sc.parallelize(range(6,11)).map(lambda i: Row(single=i,Triple=i**3)))
cubesDF.write.parquet("/home/user/workarea/projects/learn-pyspark/data/out/test-table/key=2")

mergedDF=spark.read.option("mergeschema","true").parquet("/home/user/workarea/projects/learn-pyspark/data/out/test-table")
mergedDF.printSchema()

