
from pyspark.sql import SparkSession

spark = SparkSession.Builder().appName("rdd-transform").master("local[2]").getOrCreate()

sc = spark.sparkContext

#narrow transformations - doesnt require a shuffle

#wide transformations  - require a shuffle

list1 = [1,2,3,3]
list2 = [1,2,3]
list3 = [3,4,5]

r1 = sc.parallelize(list1)

type(r1)

r1.persist()

print(r1.collect())

r2 = r1.map(lambda x:x+1)

print(r2.collect())

#filter
#using lambda
r3 = r1.filter(lambda x:x!=1)

print(r3.collect())

#using custom function

#distinct
r4 = r1.distinct()

print(r4.collect())

#sample
r5 = r1.sample("false", 0.5)

print(r5.collect())

#work with multiple datasets

rx = sc.parallelize(list2)
ry = sc.parallelize(list3)

r6 = rx.union(ry)

print(r6.collect())

r7 = rx.intersection(ry)

print(r7.collect())

r8 = rx.subtract(ry)

print(r8.collect())

r9 = r8.cartesian(ry)

print(r9.collect())

r1sum = r1.reduce(lambda x,y:x+y)

print(r1sum)

type(r1sum)

r1count = r1.count()

print(r1count)

r1first = r1.first()

print(r1first)

r1take2 = r1.take(2)

print(r1take2)

flight_rdd = sc.textFile("/home/user/workarea/projects/learn-pyspark/data/2015-flight-data.txt",minPartitions=4, use_unicode=True)

print(flight_rdd.take(5))

flight_rdd2 = flight_rdd.map(lambda x:x.split('\t'))

print(flight_rdd2.take(5))

print(flight_rdd.getNumPartitions())
print(r1.getNumPartitions())

r1.repartition(4)

print(r1.getNumPartitions())

flight_rdd3 = flight_rdd.map(lambda x: (x[0],x[1]))

print(flight_rdd3.take(5))

# create two rdds and work on joins


