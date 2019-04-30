from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    conf = SparkConf().setAppName("rdd from text file").setMaster("local[3]")
    sc = SparkContext(conf = conf)
    sc.setLogLevel("ERROR")
    
    lines = sc.textFile("/home/user/workarea/data/cities.csv")
    print(lines)
