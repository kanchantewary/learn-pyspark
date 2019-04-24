#work on pair rdd - containing key-value pairs

from pyspark.sql import SparkSession

spark = SparkSession.Builder().appName("pair-rdd").master("local[2]").getOrCreate()

sc = spark.sparkContext

#create
r1 = sc.parallelize([("a",1),("b",2),("c",3),("d",4)])
print(r1.collect())
print(type(r1))

#keys and values
print(r1.keys().collect())
print(r1.values().collect())

#transform

#reducebykey
#groupbykey
#combinebykey
#mapvalues
#flatmapvalues
#sortbykey

#subtractbykey
#join
#rightouterjoin
#leftouterjoin
#cogroup

