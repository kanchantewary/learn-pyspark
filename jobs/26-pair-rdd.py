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

#mapvalues

r5 = r1.mapValues(lambda x:x**2)

print(r5.collect())

#flatmapvalues

#sortbykey


#combinebykey

createCombiner = 'lambda x:(x,1)'
mergeValue = 'lambda x,y:(x[0]+y,x[1]+1)'
mergeCombiner = 'lambda x,y:(x[0]+y[0],x[1],y[1])'

#r6 = r5.combineByKey(createCombiner,mergeValue,mergeCombiner)
r6 = r5.combineByKey((lambda x:(x,1)),(lambda x,y:(x[0]+y,x[1]+1)),(lambda x,y:(x[0]+y[0],x[1]+y[1])))

print(r6.collect())
#print(r6.map(lambda x,y:(x,y[0]/y[1])).collectAsMap())

#subtractbykey
#join
#rightouterjoin
#leftouterjoin
#cogroup

#foldbykey

r7 = sc.parallelize([('a',1),('b',1),('a',1)],3)
from operator import add
print(r7.foldByKey(1,add).collect())
print(r7.foldByKey(1,(lambda x,y:x+y)).collect())
print(r7.foldByKey(2,(lambda x,y:x*y)).collect())

print(f'id of r7 rdd is {r7.id()}')
print(f'r7 is empty - true/false - {r7.isEmpty()}')

#groupby

r8 = sc.parallelize(['apple','guava','cat','america','care','great'],3)

print(r8.groupBy(lambda x:x[0]).collect())



















