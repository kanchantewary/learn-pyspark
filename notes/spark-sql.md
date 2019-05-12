### spark-sql

run options:
a) run through spark-sql shell  
b) run inside spark application. use spark-sql("select 1+1"). Can be used together with dataframe code seamlessly.  
c) connect from an external application (e.g. Tableau) through jdbc connection, using thrift JDBC/ODBC server.

### hive metastore

https://jaceklaskowski.gitbooks.io/mastering-spark-sql/spark-sql-hive-metastore.html  
https://www.cloudera.com/documentation/enterprise/5-6-x/topics/cdh_ig_hive_metastore_configure.html

### Managed and External tables

https://www.learningjournal.guru/courses/spark/spark-foundation-training/spark-sql-database-and-table/

[Language manual from databricks](https://docs.databricks.com/spark/latest/spark-sql/index.html)

https://www.waitingforcode.com/apache-spark-sql/apache-spark-2.4.0-features-array-higher-order-functions/read

[Hive SerDe](https://cwiki.apache.org/confluence/display/Hive/DeveloperGuide#DeveloperGuide-HiveSerDe) and 
Note: table properties are generic key value pairs, technically anything can be stored ('key'='value'). 

### Command reference

Refer [more](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL)

    Alter Database
    Alter Table or View
    Alter Table Partitions
    Analyze Table
    Cache
    Cache Table
    Clear Cache
    Convert To Delta (Delta Lake)
    Create Database
    Create Function
    Create Table
    Create View
    Delete From (Delta Lake)
    Describe Database
    Describe Function
    Describe Table
    Drop Database
    Drop Function
    Drop Table
    Explain
    Fsck Repair Table (Delta Lake)
    Functions
    Insert
    Load Data
    Merge Into (Delta Lake)
    Optimize (Delta Lake)
    Refresh Table
    Reset
    Select
    Set
    Show Columns
    Show Create Table
    Show Databases
    Show Functions
    Show Partitions
    Show Table Properties
    Show Tables
    Truncate Table
    Uncache Table
    Update (Delta Lake)
    Use Database
    Vacuum
