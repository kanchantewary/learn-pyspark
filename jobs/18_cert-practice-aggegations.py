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

from pyspark.sql.functions import count, countDistinct, approx_count_distinct, min, max, sum, sumDistinct,avg,expr
df.select(countDistinct("stockCode")).show()
df.select(approx_count_distinct("stockCode",0.1)).show()

#count distinct


#first and last


#min and max


#sum
df.select(sum("Quantity"),min("Quantity"),max("Quantity"),sumDistinct("Quantity")).show()

#average


#variance - how far the data is spread out, can be calculated over a sample or a population
from pyspark.sql.functions import var_pop,var_samp, stddev_pop,stddev_samp


#standard deviation - like variance, but gives more concrete picture of the spread of the data


#skewness - a measure of the symmetry in the data (or the lack of it)  and kurtosis
from pyspark.sql.functions import skewness, kurtosis

df.select(skewness("Quantity"),kurtosis("Quantity")).show()

#covariance and correlation
#covariance is a measure of how two random variables in a dataset will change together, a positive covariance means that the two variables go in the same direction, while a negetive value means that they are inversely related and move in opposite direction
#correlation also provides the information that covariance provides, but in addition, it can tell us the degree to which the variables tend to move together
#correlation can have value between -1 to +1. If the value is -1, is perfect negetive, meaning that if one variable increases, the other would decrease proportionately
#if the value is +1, it is perfectly positive, mean that dependent variable would increase proportionately.
#if the value is 0, it means there is no relationship between the two variables.
#covariance can be calculated over a sample or a population, use resp formula

from pyspark.sql.functions import covar_samp,covar_pop, corr

df.select(corr("InvoiceNo", "Quantity"),covar_samp("InvoiceNo","Quantity")).show()

#aggregating to complex types


#grouping
df.groupBy("InvoiceNo","customerId").count().show()


#grouping with expressions
df.groupBy("InvoiceNo").agg(count("Quantity").alias("quan"),expr("count(Quantity)")).show()


#grouping with maps



#window functions



#grouping sets


#rollups


#cube



#grouping metadata



#pivot



#user-defined aggegate functions [UDAF]


