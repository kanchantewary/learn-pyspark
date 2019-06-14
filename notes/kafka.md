# Kafka

### Why Apache Kafka

- decouples data streams and systems. A traditional approach would need peer to peer integration, which would increase the number of integration points as more number of source and target systems are added in the network, increasing complexity (protocol, file format, schema evolution). We can attain horizontal scalability by adding more number of brokers. Kafka would be the data transporter in the overall system architecture.

### Concepts

- Topic - stream of data. topics are split into partitions.each partition is ordered. Each messege in a partition is assigned an offset (incremental id). messeges can be stored in a topic for a finite amount of time (default is one week)
messeges in a topic are immutable (can not be updated). Data is assigned a partition randomly i.e. round-robin partitioning (if a key is not specified) or based on hashing algorithm (on the key specified).

- A kafka cluster consists of one or multiple brokers (servers). Brokers are identified by a numeric id

- replication factor - each partition will have one leader and multiple ISRs(In-sync replica). The broker which is the leader will receive data and serve to other replicas. A replication factor of 3 is a good idea, considering one might be taken down for maintenance, another might be down unexpectedly.
If a leader goes down, the replica broker becomes the leader for that partition.


See [creating multiple brokers](https://www.michael-noll.com/blog/2013/03/13/running-a-multi-broker-apache-kafka-cluster-on-a-single-node/)


### Zookeeper configuration
- Zookeeper manages kafka brokers. It helps in performing leader election. Kafka manages all metadata in zookeeper (but not consumer offsets any more in recent kafka versions).

- All Kafka brokers can answer a metadata request that describes the current state of the cluster: what topics there are, which partitions those topics have, which broker is the leader for those partitions etc.

ZooKeeper is responsible for:

    Electing a controller broker - and making sure there is only one
    Cluster membership - allowing brokers to join a cluster
    Topic configuration - which topics exist, how many partitions each has, where are the replicas, who is the preferred leader, what configuration overrides are set for each topic
    Quotas - how much data is each client allowed to read and write
    ACLs - who is allowed to read and write to which topic

- There is regular communication between Kafka and ZooKeeper such that ZooKeeper knows a Kafka broker is still alive (ZooKeeper heartbeat mechanism) and also in response to events such as a topic being created or a replica falling out of sync for a topic-partition.

- Apache Kafka uses Zookeeper to store metadata about the Kafka cluster(broker and topic metadata), as well as consumer client details (consumer metadata, partition offsets)
config/zookeeper.properties

### Kakfa Broker Configuration
- broker.id
- port
- zookeeper.connect
- log.dirs
- num.recovery.threads.per.data.dir
- auto.create.topics.enable
- num.partitions
- log.retention.hours
- log.retention.minutes
- log.retention.ms
- log.retention.bytes
- message.max.bytes

### Kafka Producer
1. Producers write to data to topics (which is made up of multiple partitions). Producers automatically know to which broker and partition it should write to. In case of broker failures, producers will automatically recover.
2. Producers can choose to receive acknowledgement of data writes from brokers, There are 3 write modes:
acks=0: Producers wont wait for acknowledgement (possible data loss)
acks=1: Producers would wait for acknowledgement from leader (limited data loss). replication is not guaranteed. if ack is not received, producer may retry.
acks=all: Producers would wait for acknowledgement from both leader and replicas (no data loss). it must be used in conjunction with min.insync.replicas
exception of NOT_ENOUGH_REPLICAS would be thrown  
3. If a topic does not exist, broker will create it first with default configuration (config/server.properties) i.e. number of partitions and replication factor. A warning will be thrown.  
4. retries, max.in.flight.requests.per.connection - retries is set to 0 by default. It can be increased to a large value. However, this can lead to messeges sent out of order.  
5. idempotent producer - Producer might introduce duplicate messeges into kafka due to network error(ack never reaches the producer and it retries the messege again, introducing request). set enable.idempotence to true (beyond version 0.11)  
6. Producer compression - set compression_type to one of the following: snappy,lz4,gzip  
7. Producer Batching - control using batch_size or linger.ms. Linger.ms is the number of ms a producer would be waiting before sending a batch out. batch_size is max no of bytes per partition that will be included in a batch. default is 16 KB, try setting this to 32 or 64 KB. Setting these would introduce a small delay, helps compression and increase throughput.  
8. Kafka uses murmur2 algorithm to perform hasing
9. buffer.memory (size of the send buffer, default is 32 MB). If buffer memory is full, .send() method would start to block. and max.block.ms (the time .send() would be blocked before throwing an exception)  

#### Message Keys
Producers can choose to send a key with the message. It can be anything (string, number e.g.). Kafka would ensure that all messages with a key goes to same partition (uses hashing). If key is null, round-robin partitioning is used.

bootstrap.servers
key.serializer
value.serializer

exception handling,error logging
try tweeting a tweet on the subject being followed, and see if it appears in real-time
stopping application, closing producer

### Kafka Consumers
1. consumer will always read data in order per partition (as per offsets). However, across partitions, data may not be ordered. Each consumer within a consumer group reads from an exclusive partition. If there are more number of consumers than partitions, some consumers would be inactive.
2. Each consumer in a consumer group would poll the broker (poll thread), as well as send heartbeats to ConsumerCoordinator (heartbeat thread). Rebalancing would happen if a consumer is down. 
session_timeout_ms(default 10s) - if no hearbeat is received during this period, a consumer is considered dead
heartbeat_interval_ms(default 3s) - how often to send heartbeats, usually 1/3rd of session_timeout_ms.
max_poll_inerval_ms (default 5 minutes) - time between two poll events. if the application takes more time for processing, consider changing this. ConsumerGroupCoordinator
3. Consumers reads messeges in the order it is stored in each topic-partition. Remember that, as long as number of partitions remain constant for a topic, the same key will always go to the same partition.
4. Consumer Offsets - When a consumer reads data from a topic, it needs to commit the offsets. Offsets are stored in a special kafka topic named *__consumer_offsets*. Consumers can choose when to commit the offsets - *At most once*, *At least once*(preferred), *Exactly Once*
5. Consumer Groups - describe consumer group and check out current offset, log-end offset, lag
reset offsets: to earliest, shift by, 
https://towardsdatascience.com/getting-started-with-apache-kafka-in-python-604b3250aa05
https://medium.com/@durgaswaroop/a-practical-introduction-to-kafka-storage-internals-d5b544f6925f
Refer details of kafka protocol [here](https://cwiki.apache.org/confluence/display/KAFKA/A+Guide+To+The+Kafka+Protocol)
6. configuration - max_poll_records 
7. enable_auto_commit = true by default. offsets would be committed automatically at regular interval(auto.commit.interval.ms=5000 or 5 seconds). This is not preferred option. Rather make it false and commit manaully in the code.
8. auto_offset_reset (latest, earliest, none). offset.retention.minutes
9. max_in_flight_requests_per_connection 
10. Performance improvement using batching - 
11. Replay - reset consumer offset
12. topic+partition+offset can give us a generic unique id while reading using a consumer.
13. dealing with null pointer exception


### Kafka Connect
basically reusable code for producer and consumers, for speific source and sinks. Confluent connectors, certified connectors, community connectors

### Kafka Streams
java based data processing and transformation library, contender to apache spark, flink or nifi
supports per-record stream processing, stateful and stateless, windowing. deploy in bare metals, VMs, containers, cloud, on prem. fully integrated with kafka security. it runs inside the consumer application and not on kafka brokers.

### Schema Registry
Kafka does not perform any data verification

### Choosing partition count and replication factor
guidelines:
number of partitions should at least match number of brokers.
more partitions would increase parallelism, meaning more throughput
but, more brokers mean more elections to be performed by zookeeper, more open file handles, which would be a limiting factor
replication factor should be at least 2, usually 3, maximum 4. Never set to 1
across all topics, a broker should not hold more than 4000 partitions (common standard, specific reason not mentioned)\

topic naming conventions:
https://riccomini.name/how-paint-bike-shed-kafka-topic-naming-conventions

### Kafka cluster setup

### Kafka monitoring
under replicated partitions
utilization of threads

### Operations and maintenance tasks
rolling restart of brokers
updating configurations
rebalancing partitions
increasing replication factor
adding a broker
replacing a broker
removing a broker
upgrading a kafka cluster with zero downtime


### Kafka security

a. Authentication : SSL, SASL, Kerberos,SCRAM
b. Encryption
c. Authorization : Access control list or ACL

### Kafka Multi Cluster - replication
Kafka MirrorMaker - refer hortonworks best practices page
uReplicator
tools from confluent, comcast, netflix



### ElasicSearch, kibana, bonsai

https://docs.bonsai.io/article/102-python
http://www.zekelabs.com/
https://github.com/zekelabs/kafka-cassandra-tutorial

### Advanced Kafka

#### Configure a topic
add, delete or describe a topic configuration

#### Partition and segments
Topics are made of partitions, each partition is made of multiple segments. Only one segment is active at a given time (the one data is being written into). Following are two segment settings:
log.segment.bytes (default 1GB) - max size of a single segment in bytes
log.segment.ms (default 1 week) - the time kafka will wait before committing the segment, if not full
segments come with two other index(files) - position index (.index) and timestamp index (.timeindex)

#### Log Cleanup policies
following are the available policies: 

compact - delete based on keys of the messeges. will delete old duplicate keys after the active segment is committed. It is very useful if we are concerned about the latest information only (snapshot) and not history. issue - if log compaction is broken, restart kafka, this is a open bug
min.cleanable.dirty.ratio
segment.ms

delete - delete based on age or size (default settings)
log.retention.hours - default 168, i.e. one week
log.retention.bytes - 
log.cleanup.backoff.ms

#### Other notes

a. min.insync.replicas - can be set at topic level (configure topic) or at the broker level (modify server.properties)
b. unclean.leader.election - leave as default (false)
c. launch kafka from docker
https://github.com/simplesteph/kafka-stack-docker-compose
d. client-broker communication
advertised.listeners, public and private ip
e. launch kafka in cloud
f. kafka heap options
g. real-time integration with databases
use CDC connectors e.g. debezium

### Use Cases
a. movie streaming and recommendation
b. log aggregation and monitoring
c. big data ingestion
d. bank transaction alert mechanism
e. social media, trending topics

https://www.confluent.io/blog/avro-kafka-data/


Resources:  
a. Kafka Definitive Guide  
b. [Certification](https://medium.com/@stephane.maarek/how-to-prepare-for-the-confluent-certified-developer-for-apache-kafka-ccdak-exam-ab081994da78)
c. [Udemy courses by Stephane](https://www.udemy.com/user/stephane-maarek/)

https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1
https://github.com/simplesteph/kafka-beginners-course

https://aseigneurin.github.io/
