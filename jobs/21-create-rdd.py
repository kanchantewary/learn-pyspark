#chapter 12 - rdd, spark definitive guide
#refer chapter 3, programming with rdds, learning spark

from pyspark.sql import SparkSession
spark = SparkSession.Builder().appName("rdd").master("local[3]").getOrCreate()

sc = spark.sparkContext

r1 = spark.range(10).rdd

#below statement would fail if file does not exist
r2 = sc.textFile("/home/user/workarea/projects/learn-pyspark/data/sampledata/sample01.txt")

#to handle the situation, use below code:

from py4j.protocol import Py4JJavaError

def try_read(path):
    rdd = sc.textFile(path)
    try:
        rdd.first()
        return rdd
    except Py4JJavaError as e:
        print("file does not exist, returning empty rdd")
        return sc.emptyRDD()

#now, passing a non-existent file path
rdd = try_read("/home/user/workarea/projects/learn-pyspark/data/sample01.txt")

if rdd.isEmpty():
    print ("rdd is empty")

#persist sample01 dataset

r2.persist()

print(r2.first())

count = r2.count()

print(count)

#print("end of program\n")

#pass a list to the parallelize method to create a rdd

r3 = sc.parallelize(["spark","hadoop","mongo","hive","nifi"])

print(r3.count())

r4 = sc.textFile("/home/user/workarea/projects/learn-pyspark/data/boot.log")

print(r4.count())

errR4 = r4.filter(lambda x: 'boot' in x)

print(errR4.first())

myCollection = "Spark The definitive guide : big data processing made simple".split(" ")

r5 = sc.parallelize(myCollection, 2) #second parameter is number of partitions

r5.setName("myWords")
r5.name()

#r6 = sc.wholeTextFiles()
#r7 = sc.pickleFile()

#read from URI

#read from s3


#read from HDFS

#saving and loading sequence files

#saving and loading other hadoop input/output formats

#read multiple files with pattern

r8 = sc.textFile('/home/user/workarea/projects/learn-pyspark/data/sampledata/*.txt')

print(r8.collect())

r9 = sc.wholeTextFiles('/home/user/workarea/projects/learn-pyspark/data/sampledata/')

print(r9.collect())

#but can I read multiple files stored in different places? put multiple paths in double quotes as below


r10 = sc.textFile("/home/user/workarea/projects/learn-pyspark/data/sampledata/*.txt,/home/user/workarea/projects/learn-pyspark/data/*.txt")

print(r10.take(10))
