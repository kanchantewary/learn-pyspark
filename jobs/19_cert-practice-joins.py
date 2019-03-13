#spark certification practice - chapter 08: Joins

from pyspark.sql import SparkSession
spark = SparkSession.Builder().appName("chapter7").master("local[3]").getOrCreate()



#create datasets

person = spark.createDataFrame([ 
(0, "Bill Chambers", 0, [100]), 
(1, "Matei Zaharia", 1, [500, 250, 100]), 
(2, "Michael Armbrust", 1, [250, 100])])\
        .toDF("id", "name", "graduate_program", "spark_status")


graduateProgram = spark.createDataFrame([ 
(0, "Masters", "School of Information", "UC Berkeley"), 
(2, "Masters", "EECS", "UC Berkeley"), 
(1, "Ph.D.", "EECS", "UC Berkeley")])\
        .toDF("id", "degree", "department", "school")

sparkStatus = spark.createDataFrame([ 
(500, "Vice President"), 
(250, "PMC Member"), 
(100, "Contributor")])\
        .toDF("id", "status")

person.show()
graduateProgram.show()
sparkStatus.show()

#inner joins

joinExpression= person["graduate_program"]==graduateProgram["id"]
joinType = "inner"

person.join(graduateProgram,joinExpression).show() #inner join is performed by default
person.join(graduateProgram,joinExpression,joinType).show()

#outer joins
joinType="outer"

person.join(graduateProgram,joinExpression,joinType).show()

#Left outer joins
joinType="left_outer"

person.join(graduateProgram,joinExpression,joinType).show()


#Right outer joins
joinType="right_outer"

person.join(graduateProgram,joinExpression,joinType).show()

#Left semi joins
joinType="left_semi" #semi joins are not like regular joins. It only checks if the value exists in right df, if yes, rows from left df is kept (works as a filter)

person.join(graduateProgram,joinExpression,joinType).show()

#Left anti joins - works like semi joins, but instead of keeping the rows those exist in right df, it keeps the rows that does not exist
joinType="left_anti"

person.join(graduateProgram,joinExpression,joinType).show()

#natural joins

#not recommended, use with caution

#cross joins
joinType="cross"

person.join(graduateProgram,joinExpression,joinType).show()

#joins on complex types


#handling duplicate column names


#optimizing joins

#use broadcast join

from pyspark.sql.functions import broadcast
joinType="left_outer"
person.join(broadcast(graduateProgram),joinExpression,joinType).show()

