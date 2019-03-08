#spark definitive guide chapter 7 - aggregations

#create the spark session object
from pyspark.sql import SparkSession
spark = SparkSession.Builder().appName("chapter7").master("local[3]").getOrCreate()

#create the retail data fram to work with

df=spark.read.format("csv")\
        .option("header","true")\
        .option("inferSchema","true")\
        .load("/home/user/workarea/projects/Spark-The-Definitive-Guide/data/retail-data/all/*.csv")\
        .coalesce(5)
df.cache()

#taking count

print(df.count())

#count distinct


#first and last


#min and max


#sum


#average


#variance


#standard deviation


#skewness and kurtosis


#covariance and correlation


#aggregating to complex types


#grouping



#grouping with expressions



#grouping with maps



#window functions



#grouping sets


#rollups


#cube



#grouping metadata



#pivot



#user-defined aggegate functions [UDAF]


