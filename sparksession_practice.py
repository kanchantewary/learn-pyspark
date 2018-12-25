#create a spark session
#spark-submit --conf spark.executor.memory=0.25g 
import os

from pyspark.sql import SparkSession

spark = SparkSession.Builder().appName("test").master("local[3]").getOrCreate()

spark.conf.set("spark.executor.memory", '0.5g')
spark.conf.set("spark.executor.cores",'3')
spark.conf.set("spark.cores.max",'3')
spark.conf.set("spark.driver.memory",'0.5g')
spark.conf.set("spark.logConf",'True')
spark.conf.set("spark.driver.supervise",'True')
spark.conf.set("spark.local.dir",'/home/user/workarea/')
spark.conf.get("spark.sql.warehouse.dir")

x = spark.sparkContext._conf.getAll()

for item in x:
    print(item)

#print(x)

for item in sorted(os.environ.items()):
    print(item)

#logger.info(x.mkString("\n")

spark.sparkContext.stop()
