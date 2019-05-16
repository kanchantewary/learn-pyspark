# Kafka
Resources:  
a. Kafka Definitive Guide
b. https://medium.com/@stephane.maarek/how-to-prepare-for-the-confluent-certified-developer-for-apache-kafka-ccdak-exam-ab081994da78
c. https://www.udemy.com/user/stephane-maarek/

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
acks=1: Producers would wait for acknowledgement from leader (limited data loss)
acks=all: Producers would wait for acknowledgement from both leader and replicas (no data loss)
#### Message Keys
Producers can choose to send a key with the message. It can be anything (string, number e.g.). Kafka would ensure that all messages with a key goes to same partition (uses hashing). If key is null, round-robin partitioning is used.

bootstrap.servers
key.serializer
value.serializer

### Kafka Consumers
consumer
consumer groups
offsets
Consumer offsets - __consumer_offsets
#### Delivery Simantics for consumers  
At most once
At least once
Exactly Once