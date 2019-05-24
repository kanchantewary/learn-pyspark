# Kafka
Resources:  
a. Kafka Definitive Guide
b. https://medium.com/@stephane.maarek/how-to-prepare-for-the-confluent-certified-developer-for-apache-kafka-ccdak-exam-ab081994da78
c. https://www.udemy.com/user/stephane-maarek/

https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1

https://aseigneurin.github.io/

## Concepts
1. Apache Kafka uses Zookeeper to store metadata about the Kafka cluster(broker and topic metadata), as well as consumer client details (consumer metadata, partition offsets)
### Zookeeper configuration
2. replication factor - each partition will have one leader and multiple ISRs(In-sync replica)
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
consumer
consumer groups
offsets
Consumer offsets - __consumer_offsets
#### Delivery Simantics for consumers  
At most once
At least once
Exactly Once
https://towardsdatascience.com/getting-started-with-apache-kafka-in-python-604b3250aa05

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
