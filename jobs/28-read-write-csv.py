# read and write json files

from pyspark.sql import SparkSession
from pyspark.sql.types import *
import json,time

start=time.time()

spark = SparkSession.Builder().appName("csv").master("local[2]").getOrCreate()

sc = spark.sparkContext

data = spark.read.format("csv").\
        option("inferSchema","true").\
        option("mode","FAILFAST").\
        option("header","true").\
        option("samplingRatio",0.05).\
        load("/home/user/workarea/projects/learn-pyspark/data/departuredelays.csv")

schema = StructType([
    StructField("date",StringType()),
    StructField("delay",StringType()),
    StructField("distance",StringType()),
    StructField("origin",StringType()),
    StructField("destination",StringType())
    ])

data1 = spark.read.format("csv").\
        option("inferSchema","false").\
        option("mode","FAILFAST").\
        option("header","true").\
        option("compression","gzip").\
        option("samplingRatio",0.1).\
        load("/home/user/workarea/projects/learn-pyspark/data/departuredelays1.csv.gz",schema=schema)


#data.show(5)
#data1.show(5)

end=time.time()

data.printSchema()
data1.printSchema()

#
#options for mode
#PERMISSIVE - missing values would be set to null and corrupt records would be populated
#FAILFAST - process would fail if corrupt record is found 
#DROPMALFORMED - corrupt records would be dropped
#

#names = spark.read.format("csv").\
#        option("inferSchema","true").\
#        option("mode","PERMISSIVE").\
#        option("header","true").\
#        load("/home/user/workarea/projects/learn-pyspark/data/names.txt")

#names.show()

#names.write.format("csv").mode("overwrite").option("compression","gzip").option("sep","\t").save("/home/user/workarea/projects/learn-pyspark/data/names-tsv.out")

print(end-start)

#print(names.schema.json())

#run the following code to generate schema file in json format
#f=open("/home/user/workarea/projects/learn-pyspark/config/names.schema","w+")
#f.write(names.schema.json())
#f.close()

#pass custome schema from the file generated earlier, convert to struct type

name_schema_json = spark.read.text("/home/user/workarea/projects/learn-pyspark/config/names.schema").first()[0]
name_schema = StructType.fromJson(json.loads(name_schema_json))
names = spark.read.format("csv").\
        option("inferSchema","false").\
        option("mode","PERMISSIVE").\
        option("header","true").\
        load("/home/user/workarea/projects/learn-pyspark/data/names.txt",schema=name_schema)
names.show()
