#spark certification practice - Spark Definitive Guide chapter-6

from pyspark.sql import SparkSession
from pyspark.sql.functions import desc,col,window,column,date_format,pow,round,bround,corr,coalesce
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

df.withColumn("isExpensive",expr("NOT UnitPrice <= 250"))\
        .where("isExpensive")\
        .select("Description","UnitPrice")\
        .show(5)

#handling null data in boolean expressions

df.where(col("Description").eqNullSafe("hello")).show()

#working with numbers

fabricatedQuantity = pow(col("Quantity") * col("UnitPrice"),2) + 5
df.select(expr("CustomerId"),fabricatedQuantity.alias("realQuantity")).show()

##rounding

df.select(round(col("UnitPrice"),1).alias("rounded")).show(5)
df.select(round(lit("2.5")).alias("rounded"),bround(lit("2.5")).alias("brounded")).show(2)

##basic statistics

df.describe().show()

##using the stat package

###find correlation

df.stat.corr("UnitPrice","Quantity")
df.select(corr("Quantity","UnitPrice")).show()

from pyspark.sql.functions import count,mean,max,min,stddev_pop

quantileProbs=[0.5]
relError=0.05
df.stat.approxQuantile("UnitPrice",quantileProbs,relError)
df.stat.crosstab("StockCode","Quantity").show()
df.stat.freqItems(["StockCode","Quantity"]).show()

##creating a unique sequence id

from pyspark.sql.functions import monotonically_increasing_id

df.select(monotonically_increasing_id()).show(10)

#working with strings

#perform case converstions

from pyspark.sql.functions import initcap,lower,upper,ltrim,rtrim,trim,lpad,rpad
df.select(initcap(col("Description"))).show(5)
df.select(col("Description"),initcap(col("Description")),lower(col("Description")),upper(col("Description"))).show(5)

string_with_space="     hello     "

df.select(ltrim(lit(string_with_space)),rtrim(lit(string_with_space)),trim(lit(string_with_space))).show()

#regular expressions


#working with dates, timestamps
from pyspark.sql.functions import current_date,current_timestamp,date_add,date_sub,datediff,months_between,to_date,to_timestamp

dateDF=spark.range(10).withColumn("today",current_date()).withColumn("now",current_timestamp())
dateDF.show()

dateDF.select(date_add(col("today"),5).alias("today+5"),date_sub(col("today"),5).alias("today-5")).show()

#convert string to date, default format is 'YYYY-MM-DD'
spark.range(1).select(to_date(lit("2019-02-01")).alias("start_date"),to_date(lit("2019-03-06")).alias("end_date")).select(datediff(col("start_date"),col("end_date"))).show()

cleanDateDF=spark.range(1).withColumn("date1",current_date())
date_format='YYYY-MM-DD'
cleanDateDF.select(to_timestamp(col("date1"),date_format)).show()

#working with nulls in data

#coalesce, returns first not null value from a set of columns

df.select(coalesce(col("Description"),col("customerId"))).show()

#ifnull,nullif,nvl,nvl2

#drop - removes rows that contain null

#use the na subpackage

df.na.drop("all") #drop if all of the columns have null
df.na.drop("any") #drop if any of the columns have null
df.na.drop("all",subset=["InvoiceNo","StockCode"]) #drop if there is null in a subset of columns

df.na.fill("Not Available") #replace all null values to 'Not Available'

fill_col_vals={"StockCode":5,"InvoiceNo":"No value"}
df.na.fill(fill_col_vals) #fill null selectively

df.na.replace([" "],"UNKNOWN","Description") #replace space to UNKNOWN


#working with complex types


#working with JSON


#user defined functions






























