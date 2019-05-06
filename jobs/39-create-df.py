#work on approaches to create a spark dataframe

#create the spark session object
from pyspark.sql import SparkSession
from pyspark.sql.types import *

spark = SparkSession.Builder().appName("create-df").master("local[3]").getOrCreate()
sc=spark.sparkContext

print('created spark session object')

#create df from a parallel collection (list), using toDF() method

print('create df from a parallel collection (list)')

df=spark.range(500).toDF("number")
df.show()
df.printSchema()

df.first()

#rename the columns and create another dataframe
df_renamed=df.toDF("id")
df_renamed.printSchema()

#create row objects
r1=[('alice',1)]
r2=[{'name':'alice','age':1}]

schema = StructType([
    StructField("name",StringType(),True),
    StructField("age",IntegerType(),True)
    ])

#using createDataFrame() method
df1=spark.createDataFrame(r1)
df1.show()
df1.printSchema()

df2=spark.createDataFrame(r1,['name','age'])
df2.show()
df2.printSchema()

df3=spark.createDataFrame(r2)
df3.show()
df3.printSchema()

#create dataframe from an rdd
rdd1 = sc.parallelize(r1)
df4 = spark.createDataFrame(rdd1)
df4.show()
df4.printSchema()

df5 = spark.createDataFrame(rdd1,['name','age'])
df5.show()
df5.printSchema()

df6=spark.createDataFrame(rdd1,schema)
df6.show()
df6.printSchema()

# create a new dataframe - **usage unknown**

df7=df6.alias("df6_alias")

df7.show()

#create a row object
"""
from pyspark.sql import Row

person=Row('name','age')
person=rdd1.map(lambda x:person(*x))
df6=spark.createDataFrame(person)
df6.show()
df6.printSchema()
"""
#create df from pandas dataframe

import pandas as pd

d={'col1':[1,2],'col2':[3,4]}
pd_df1=pd.DataFrame(data=d)

df8=spark.createDataFrame(pd_df1)
df8.show()

#rename columns in a dataframe

df9=df8.withColumnRenamed('col1','id1').withColumnRenamed('col2','id2')
df9.show()
#rename all columns
df10=df8.toDF('column1','column2')
df10.show()

#create dataframe with metadata defined in schema

schema1 = StructType([
    StructField("name",StringType(),True,{'description':'person name'}),
    StructField("age",IntegerType(),True,{'description':'max=99'})
    ])

df11=spark.read.format('csv').\
        option("mode","FAILFAST").\
        option("path",'/home/user/workarea/projects/learn-pyspark/data/source/name-age.txt').\
        schema(schema1).\
        load()
#below steps would print the schema, but does not show the metadata added,*** need to figure out the way***

df11.printSchema()
print(df11.schema)
df11.show()

#work with spark datatypes

#create dataframe from external sources

#
