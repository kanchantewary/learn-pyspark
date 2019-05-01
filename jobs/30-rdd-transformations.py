
from pyspark.sql import SparkSession

spark = SparkSession.Builder().appName("rdd-transform").master("local[2]").getOrCreate()

spark.conf.set("logLineage",'true')

sc = spark.sparkContext

#sc.setLogLevel("INFO")

#set log lineage to true
#--conf spark.logLineage=true

#narrow transformations - doesnt require a shuffle

#wide transformations  - require a shuffle

list1 = [1,2,3,3,6,7,8,12,6,23,45,76,9,10]
list2 = [1,2,3]
list3 = [3,4,5]

r1 = sc.parallelize(list1,20)

print(type(r1))

#r1.persist()

#print(r1.collect())

r3 = r1.map(lambda x:x**2).filter(lambda x:x>5)
r3.count()

#print(r2.collect())

#filter
#using lambda
#r3 = r1.filter(lambda x:x!=1)

#print(r3.collect())
print(r3.toDebugString().decode("utf-8"))

print(r1.getNumPartitions())
r1g = r1.repartition(30).glom()

print(r1g.collect())
print(r1g.getNumPartitions())

def adder(iterator):
    if iterator.isEmpty:
        yield 'None'
    else:
        yield sum(iterator)

print(r1.mapPartitions(adder).collect())
