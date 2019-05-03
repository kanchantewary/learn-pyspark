# Loading and saving data

Refer ITVersity training [here](https://youtu.be/ICKs1ACqK8U)

My learning: Better to focus on dataframe APIs for this part, they are more robust and provide more flexibility.  
general format to read:  
`spark.read.format(...).option("key", "value").schema(...).load()`

Refer [this](https://szczeles.github.io/Reading-JSON-CSV-and-XML-files-efficiently-in-Apache-Spark/) for a good summary.

## Serialization/Deserialization

To serialize an object means to convert its state to a byte stream so that the byte stream can be reverted back into a copy of the object. A Java object is serializable if its class or any of its superclasses implements either the java.io.Serializable interface or its subinterface, java.io.Externalizable.

A class is never serialized only object of a class is serialized. Object serialization is needed if object needs to be persisted or transmitted over the network . 

Deserialization is the reverse process: turning a stream of bytes into an object in memory.

### Compression schemes

## text files

`rdd = sc.textFile("file:///home/work/input.txt")`
`rdd.saveAsTextFile()`

See [this](https://databricks.com/session/why-you-should-care-about-data-layout-in-the-filesystem/) for a session on handling semi-structured data, bucketing, partitioning.

## JSON

JavaScript Object Notation (JSON) is a text format for the serialization of structured data. It is derived from the object literals of JavaScript 
JSON can represent four primitive types (strings, numbers, booleans, and null) and two structured types (objects and arrays).
python json module seem to be good to convert python objects to json structure.
dataframe APIs seem to be better. more on this later.

## XML

## Sequence files

## Protocol buffers

## Databases

Cassendra, Hbase, Elasticsearch, JDBC/ODBC, MongoDB etc.

## object files

## Hadoop Input and Output format

## Parquet files

Parquet is an open source column-oriented data store that provides a variety of storage optimizations, especially for analytics workloads. It provides columnar compression, which saves storage space and allows for reading individual columns instead of entire files. Reading from a Parquet file will always be more efficient than JSON or CSV. Another advantage of Parquet is that it supports complex types.  
Refer [this](https://spark.apache.org/docs/latest/sql-data-sources-parquet.html) later when working with spark SQL
Refer [this](https://github.com/apache/parquet-format) and [this](https://www.slideshare.net/dataera/parquet-format) to understand parquet format in depth

## ORC files

ORC is a self-describing, type-aware columnar file format designed for Hadoop workloads. It is optimized for large streaming reads, but with integrated support for finding required rows quickly.  
difference between ORC and Parquet? For the most part, they’re quite similar; the fundamental difference is that Parquet is further optimized for use with Spark, whereas ORC is further optimized for Hive.
## File Compression

## hdfs

Installed and configured hadoop,hdfs,yarn using [this](https://linuxconfig.org/how-to-install-hadoop-on-ubuntu-18-04-bionic-beaver-linux). Also, refer [this](http://www.michael-noll.com/tutorials/running-hadoop-on-ubuntu-linux-single-node-cluster/) for a better understanding of the architecture (but written for older hadoop version).
Tip - Install using hadoop user. If run from a different user, ownership of hadoop folders should be modified using chown.

`rdd.saveAsTextFile("hdfs://localhost:9000/test/sparkrdd.txt")`

If this path is already existing, the application would raise exception and fail. To overcome this, follow this [blog](https://diogoalexandrefranco.github.io/interacting-with-hdfs-from-pyspark/)

## Amazon S3

## Avro
