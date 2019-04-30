#spark certification practice - work on retail data, structured streaming, Definitive Guide chapter-4

from pyspark.sql import SparkSession
from pyspark.sql.functions import desc,col,window,column,date_format,lit
import time

spark = SparkSession.Builder().appName("test13").master("local[3]").getOrCreate()

df=spark.range(500).toDF("number")

df.show()

df1=df.select(df["number"]+10)

df1.explain()

df1.show()

#data types in python:

#a=ByteType()
#b=ShortType()
#c=IntegerType()
#d=LongType()
#e=FloatType()
#f=DoubleType()
#g=DecimalType()
#h=StringType()
#i=BinaryType()
#j=BooleanType()
#k=DateType()
#l=TimestampType()
#m=ArrayType()
#n=MapType()
#o=StructType()
#p=StructField()

#create a dataframe first

df=spark.read.format("json").load("/home/user/workarea/projects/Spark-The-Definitive-Guide/data/flight-data/json/2015-summary.json")

print(df.schema)

df.printSchema()

#define schema manually

from pyspark.sql.types import StructField, StructType, StringType, LongType

myManualSchema = StructType([
    StructField("DEST_COUNTRY_NAME",StringType(),True),
    StructField("ORIGIN_COUNTRY_NAME",StringType(),True),
    StructField("count",LongType(),True)])

df1 = spark.read.format("json").schema(myManualSchema).load("/home/user/workarea/projects/Spark-The-Definitive-Guide/data/flight-data/json/2015-summary.json")

#list all columns in a dataframe

print(df1.columns)

#creating a row

from pyspark.sql import Row

myRow = Row("Hello", None, 1, False)

#print(myRow)
print(myRow[0])


#selecting columns of a dataframe

df1.select("DEST_COUNTRY_NAME","ORIGIN_COUNTRY_NAME").show(5)

#different ways

from pyspark.sql.functions import col,column,expr

df1.select(expr("DEST_COUNTRY_NAME"),col("DEST_COUNTRY_NAME"),column("DEST_COUNTRY_NAME"),expr("DEST_COUNTRY_NAME AS DESTINATION")).show(5)

df1.selectExpr("DEST_COUNTRY_NAME AS DEST","DEST_COUNTRY_NAME").show(5)

df1.selectExpr("*","(DEST_COUNTRY_NAME=ORIGIN_COUNTRY_NAME) as WithinCountry").show(5)


#aggregation functions

df1.selectExpr("avg(count)", "count(distinct(DEST_COUNTRY_NAME))").show(5)

#passing a value using literals

df1.select(expr("*"), lit(1).alias("One")).show(5)

#adding columns

df1.withColumn("column_one",lit(1)).show(5)
df1.withColumn("withinCountry",expr("DEST_COUNTRY_NAME==ORIGIN_COUNTRY_NAME")).show(5)

#renaming columns

print(df1.withColumn("dest",expr("DEST_COUNTRY_NAME")).columns)
print(df1.withColumnRenamed("DEST_COUNTRY_NAME", "dest").columns)

#removing columns

print(df1.drop("DEST_COUNTRY_NAME").columns)

#typecasting

print(df1.withColumn("count2",col("count").cast("long")).schema)

#filtering rows

df1.filter(col("count") < 2).show(2)
df1.where("count < 2").show(2)

#getting unique rows

print(df1.select("ORIGIN_COUNTRY_NAME").distinct().count())

#random samples

seed=5
withReplacement=False
fraction=0.5
print(df1.sample(withReplacement,fraction,seed).count())

#random splits
#useful in case of ML, to divide the source dataset into training and validation sets

proportion=[0.25,0.75] #should add up to 1
dataframes=df1.randomSplit(proportion,seed)

print(dataframes[0].count())
print(dataframes[1].count())

#concatenating and union


#sorting
#default sort direction is ascending

df1.sort("count").show(5)
df1.orderBy("count").show(5)
df1.orderBy("count","ORIGIN_COUNTRY_NAME").show(5)
df1.orderBy(col("count"),col("ORIGIN_COUNTRY_NAME")).show(5)

#specify sort direction explicitly

from pyspark.sql.functions import asc, desc

df1.orderBy(expr("count desc")).show(5)
df1.orderBy(col("count").desc(),col("DEST_COUNTRY_NAME").asc()).show(5)

#use null first/last

df2=spark.createDataFrame([('Tom',80),('Ram',None),(None,60)],["name","height"])

df2.orderBy(col("name").desc_nulls_last()).show(5)

df2.orderBy(col("name").asc_nulls_first()).show(5)

#repartition and colesce

#get number of partitions

print(df1.rdd.getNumPartitions())

#collecting rows to the driver

collectdf1 = df1.limit(20)

collectdf1.take(5)

collectdf1.show(5)



