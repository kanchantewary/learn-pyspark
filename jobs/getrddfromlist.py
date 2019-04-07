from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    conf = SparkConf().setAppName("create int rdd").setMaster("local[3]")
    sc = SparkContext(conf = conf)
    sc.setLogLevel("ERROR")

inputIntegers = list(range(0,10))
integerRdd = sc.parallelize(inputIntegers)
print(integerRdd)

