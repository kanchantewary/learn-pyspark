# learn RDD - Resilient Distributed Datasets

## create

### create from a text file


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

