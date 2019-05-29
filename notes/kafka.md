# Kafka
Resources:  
a. Kafka Definitive Guide  
b. [Certification](https://medium.com/@stephane.maarek/how-to-prepare-for-the-confluent-certified-developer-for-apache-kafka-ccdak-exam-ab081994da78)
c. [Udemy courses by Stephane](https://www.udemy.com/user/stephane-maarek/)

https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1
https://github.com/simplesteph/kafka-beginners-course

https://aseigneurin.github.io/

### Why Apache Kafka

decouples data streams and systems. A traditional approach would need peer to peer integration, which would increase the number of integration points as more number of source and target systems are added in the network, increasing complexity (protocol, file format, schema evolution). We can attain horizontal scalability by adding more number of brokers. Kafka would be the data transporter in the overall system architecture.

### Concepts

Topic - stream of data. topics are split into partitions.each partition is ordered. Each messege in a partition is assigned an offset (incremental id). messeges can be stored in a topic for a finite amount of time (default is one week)
messeges in a topic are immutable (can not be updated). Data is assigned a partition randomly i.e. round-robin partitioning (if a key is not specified) or based on hashing algorithm (on the key specified).

A kafka cluster consists of one or multiple brokers (servers). Brokers are identified by a numeric id

replication factor - each partition will have one leader and multiple ISRs(In-sync replica). The broker which is the leader will receive data and serve to other replicas. A replication factor of 3 is a good idea, considering one might be taken down for maintenance, another might be down unexpectedly.
If a leader goes down, the replica broker becomes the leader for that partition.


See [creating multiple brokers](https://www.michael-noll.com/blog/2013/03/13/running-a-multi-broker-apache-kafka-cluster-on-a-single-node/)


### Zookeeper configuration
Zookeeper manages kafka brokers. It helps in performing leader election. Kafka manages all metadata in zookeeper (but not consumer offsets any more in recent kafka versions).

All Kafka brokers can answer a metadata request that describes the current state of the cluster: what topics there are, which partitions those topics have, which broker is the leader for those partitions etc.

ZooKeeper is responsible for:

    Electing a controller broker - and making sure there is only one
    Cluster membership - allowing brokers to join a cluster
    Topic configuration - which topics exist, how many partitions each has, where are the replicas, who is the preferred leader, what configuration overrides are set for each topic
    Quotas - how much data is each client allowed to read and write
    ACLs - who is allowed to read and write to which topic

There is regular communication between Kafka and ZooKeeper such that ZooKeeper knows a Kafka broker is still alive (ZooKeeper heartbeat mechanism) and also in response to events such as a topic being created or a replica falling out of sync for a topic-partition.

Apache Kafka uses Zookeeper to store metadata about the Kafka cluster(broker and topic metadata), as well as consumer client details (consumer metadata, partition offsets)
config/zookeeper.properties

### Kakfa Broker Configuration
broker.id
port
zookeeper.connect
log.dirs
num.recovery.threads.per.data.dir
auto.create.topics.enable
num.partitions
log.retention.hours
log.retention.minutes
log.retention.ms
log.retention.bytes
message.max.bytes

### Kafka Producer
1. Producers write to data to topics (which is made up of multiple partitions). Producers automatically know to which broker and partition it should write to. In case of broker failures, producers will automatically recover.
2. Producers can choose to receive acknowledgement of data writes from brokers, There are 3 write modes:
acks=0: Producers wont wait for acknowledgement (possible data loss)
acks=1: Producers would wait for acknowledgement from leader (limited data loss). replication is not guaranteed. if ack is not received, producer may retry.
acks=all: Producers would wait for acknowledgement from both leader and replicas (no data loss). it must be used in conjunction with min.insync.replicas
exception of NOT_ENOUGH_REPLICAS would be thrown

3. If a topic does not exist, broker will create it first with default configuration (config/server.properties) i.e. number of partitions and replication factor. A warning will be thrown.

retries

max.in.flight.requests.per.connection

idempotent producer
set enable.idempotence to true

compression_type - snappy,lz4,gzip

linger.ms - number of ms a producer would be waiting before sending a batch out
batch_size - max no of bytes that will be included in a batch. default is 16 KB, try setting this to 32 or 64 KB.
buffer.memory
max.block.ms

#### Message Keys
Producers can choose to send a key with the message. It can be anything (string, number e.g.). Kafka would ensure that all messages with a key goes to same partition (uses hashing). If key is null, round-robin partitioning is used.

bootstrap.servers
key.serializer
value.serializer

exception handling,error logging
try tweeting a tweet on the subject being followed, and see if it appears in real-time
stopping application, closing producer

### Kafka Consumers
consumer will always read data in order per partition (as per offsets). However, across partitions, data may not be ordered. Each consumer within a consumer group reads from an exclusive partition. If there are more number of consumers than partitions, some consumers would be inactive.
ConsumerCoordinator, ConsumerGroupCoordinator
Consumers reads messeges in the order it is stored in each topic-partition
Remember that, as long as number of partitions remain constant for a topic, the same key will always go to the same partition.

#### Consumer Offsets
When a consumer reads data from a topic, it needs to commit the offsets. Offsets are stored in a special kafka topic named *__consumer_offsets*. Consumers can choose when to commit the offsets - *At most once*, *At least once*(preferred), *Exactly Once*


https://towardsdatascience.com/getting-started-with-apache-kafka-in-python-604b3250aa05
https://medium.com/@durgaswaroop/a-practical-introduction-to-kafka-storage-internals-d5b544f6925f
Refer details of kafka protocol [here](https://cwiki.apache.org/confluence/display/KAFKA/A+Guide+To+The+Kafka+Protocol)

configuration
max_poll_records 
enable_auto_commit 
auto_offset_reset 
max_in_flight_requests_per_connection 
#### batching - 
dealing with null pointer exception
reset consumer offset
offset.retention.minutes

### Kafka Connect

### Schema Registry


### ElasicSearch, kibana, bonsai

https://docs.bonsai.io/article/102-python


http://www.zekelabs.com/
https://github.com/zekelabs/kafka-cassandra-tutorial


log.segment.bytes
log.segment.ms
log cleanup policy
log.cleanup.backoff.ms
log.retention.hours
log.retention.bytes
