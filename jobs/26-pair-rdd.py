#work on pair rdd - containing key-value pairs

from pyspark.sql import SparkSession

spark = SparkSession.Builder().appName("pair-rdd").master("local[2]").getOrCreate()

sc = spark.sparkContext

#create
r1 = sc.parallelize([("a",1),("b",2),("c",3),("d",4),("a",5),("c",6),("c",2)])
print(r1.collect())
print(type(r1))

#keys and values
print(r1.keys().collect())
print(r1.values().collect())

#transform

#reducebykey
r2 = r1.reduceByKey(lambda x,y:x+y)

print(r2.collect())

print(r2.toDebugString().decode("utf-8"))

#groupbykey

r3 = r1.groupByKey()

print(r3.collect())

r4 = r3.map(lambda x:(x[0],list(x[1])))

print(r4.toDebugString().decode("utf-8"))
print(r4.collect())

#combinebykey
#mapvalues
#flatmapvalues
#sortbykey

#subtractbykey
#join
#rightouterjoin
#leftouterjoin
#cogroup

