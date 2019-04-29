# Loading and saving data

My learning: Better to focus on dataframe APIs for this part, they are more robust and provide more flexibility.  
general format to read:  
`spark.read.format(...).option("key", "value").schema(...).load()`

Refer [this](https://szczeles.github.io/Reading-JSON-CSV-and-XML-files-efficiently-in-Apache-Spark/) for a good summary.

## Serialization/Deserialization

To serialize an object means to convert its state to a byte stream so that the byte stream can be reverted back into a copy of the object. A Java object is serializable if its class or any of its superclasses implements either the java.io.Serializable interface or its subinterface, java.io.Externalizable.

A class is never serialized only object of a class is serialized. Object serialization is needed if object needs to be persisted or transmitted over the network . 

Deserialization is the reverse process: turning a stream of bytes into an object in memory.

## text files

`rdd = sc.textFile("file:///home/work/input.txt")`
`rdd.saveAsTextFile()`

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

## ORC files

ORC is a self-describing, type-aware columnar file format designed for Hadoop workloads. It is optimized for large streaming reads, but with integrated support for finding required rows quickly.  
difference between ORC and Parquet? For the most part, they’re quite similar; the fundamental difference is that Parquet is further optimized for use with Spark, whereas ORC is further optimized for Hive.
## File Compression

## hdfs
Installed using [this](https://linuxconfig.org/how-to-install-hadoop-on-ubuntu-18-04-bionic-beaver-linux)
## Amazon S3

## Avro
