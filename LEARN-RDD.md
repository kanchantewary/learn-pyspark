# learn RDD - Resilient Distributed Datasets

## about

RDDs are immutable, distributed (partitioned) collection of data. The partitions may be computed on different nodes of the cluster. It can be created in 3 ways, namely a) load from an external dataset b) parallelize a collection (list) c) transforming another RDD

## resources


[programming guides 1](https://spark.apache.org/docs/2.1.1/api/java/org/apache/spark/rdd/RDD.html)

[programming guides 2](https://spark.apache.org/docs/1.1.1/api/python/pyspark.rdd.RDD-class.html)

[programming guides 3](http://spark.apache.org/docs/2.2.0/api/python/_modules/pyspark.html)

[paper by Matei](https://cs.stanford.edu/~matei/papers/2012/nsdi_spark.pdf)

[Advanced Apache Spark- Sameer Farooqui (Databricks)](https://www.youtube.com/watch?v=7ooZ4S7Ay6Y)

[A Deeper Understanding of Spark Internals - Aaron Davidson (Databricks)](https://www.youtube.com/watch?v=dmL0N3qfSc8)

[Introduction to AmpLab Spark Internals](https://www.youtube.com/watch?v=49Hr5xZyTEA)

### types of RDD

Following are helpful to understand logical plan of rdd (rdd.toDebugString()). A logical plan is always generated, irrespective of whether an action is called or not.

a. HadoopRDD - returned by sc.textFile
b. mapPartitionRDD - returned by operations like map, flatmap, filter, mapPartitions.
c. shuffledRDD - result of repartition or coalesce transformations (? in case of Key-value rdds)
d. parallelCollectionRDD - returned by sc.parallelize (when used to create a rdd)
e. coalescedRDD - returned by a coalesce or repartition function

[also see](https://spark.apache.org/docs/0.6.2/api/core/spark/rdd/package.html)

### create

#### create from a text file


sc.textFile('filepath',minPartitions=n,use_unicode=True)

notes:
minPartitions and use_unicode are optional parameters
filepath can be path to a single file, or multiple files provided with wildcards, or compressed files (gz)
filepath should be accessible from driver and all worker nodes [either copied to all worker nodes, or placed in network-mounted file system]
increasing the value of minParitions would increase parallelism and improve execution time.

sc.wholeTextFiles('filepath')

notes:
read multiple files. each row would contain file name and content of each file as pairs.

further read: rdd programming guide

reading from hdfs:
sc.textFile('hdfs://folder/filename.csv')

reading from s3:
sc.textFile('s3://bucket/folder/filename.csv')

### create from a list

sc.parallelize(list)

## transformations

### narrow vs wide transformations

wide transformations are those, which require a shuffle, while narrow ones does not. In wide transformations, multiple child partitions depend on each parent partition.
In case of narrow transformations, each partition in parent rdd is used by at most one partition in child rdd.
example of narrow transformations are map,filter. SortByKey, join, GroupByKey are wide transformations e.g. Narrow transformations are faster to execute.

### map

using lambda function:

using custom function:

### flatmap

### filter

### distinct

### sample

### union

### intersection

### subtract

### join

### cartesian

### 
## actions

### reduce

### treeReduce

### fold

### aggregate

### collect

### take

### first

### top

### count

### countApprox

### countByValue

### countByValueApprox

### takeOrdered

### takeSample

### treeAggregate

### countApproxDistinct

### foreach
difference with map: map accumulates all of the results into a collection, whereas foreach returns nothing. map is usually used when you want to transform a collection of elements with a function, whereas foreach simply executes an action for each element.

### foreachPartition

### zip

### zipPartitions

### cache

### persist

### checkpoint


### comparison

https://github.com/JerryLead/SparkInternals/blob/master/markdown/english/6-CacheAndCheckpoint.md

https://stackoverflow.com/questions/35127720/what-is-the-difference-between-spark-checkpoint-and-persist-to-a-disk

### getCheckpointFile

### getNumPartitions

### glom

### groupBy

### groupByKey

### id

### isCheckpointed

### isEmpty

### iterator

### keyBy

### mapPartitions

### mapPartitionsWithIndex

### max

### min

### name

### partitioner

### partitions

### pipe

### randomSplit

### repartition

### saveAsObjectFile

### saveAsTextFile

### sortBy

use to sort a RDD

### setName

### toString

### toDebugString

### zipWithIndex

### zipWithUniqueId

### unpersist

