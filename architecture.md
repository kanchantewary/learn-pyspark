# Spark Internals - Architecture and Configuration

Spark is an in-memory distributed computing engine.

Hadoop is a framework for distributed storage (HDFS) and distributed processing (YARN).

Spark can run with or without Hadoop components (HDFS/YARN)
Distributed Storage:

Since Spark does not have its own distributed storage system, it has to depend on one of these storage systems for distributed computing.

S3 – Non-urgent batch jobs. S3 fits very specific use cases when data locality isn’t critical.

Cassandra – Perfect for streaming data analysis and an overkill for batch jobs.

HDFS – Great fit for batch jobs without compromising on data locality.

Further, refer [this](https://stackoverflow.com/questions/28664834/which-cluster-type-should-i-choose-for-spark/34657719#34657719)

## Talk about different deployments - Local, Standalone, YARN, Mesos

## Learn little bit of YARN

## Learn little bit of Mesos

https://open.mesosphere.com/advanced-course/

## Learn little bit of HDFS
[See](https://hadoop.apache.org/docs/r1.2.1/hdfs_design.html)
