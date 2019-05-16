sh kafka-topics.sh --zookeeper localhost:2181 --topic topic1 --create --partitions 3 --replication-factor 1
sh kafka-topics.sh --zookeeper localhost:2181 --list
sh kafka-topics.sh --zookeeper localhost:2181 --topic topic1 --describe
sh kafka-topics.sh --zookeeper localhost:2181 --topic topic2 --create --partitions 3 --replication-factor 1
sh kafka-topics.sh --zookeeper localhost:2181 --topic topic2 --delete

total 32
-rw-r--r-- 1 user user   54 May 16 14:44 meta.properties
drwxr-xr-x 2 user user 4096 May 16 14:52 topic1-0
drwxr-xr-x 2 user user 4096 May 16 14:52 topic1-1
drwxr-xr-x 2 user user 4096 May 16 14:52 topic1-2
-rw-r--r-- 1 user user    4 May 16 15:11 cleaner-offset-checkpoint
-rw-r--r-- 1 user user   37 May 16 15:15 recovery-point-offset-checkpoint
-rw-r--r-- 1 user user    4 May 16 15:15 log-start-offset-checkpoint
-rw-r--r-- 1 user user   37 May 16 15:15 replication-offset-checkpoint

total 44
-rw-r--r-- 1 user user   54 May 16 14:44 meta.properties
drwxr-xr-x 2 user user 4096 May 16 14:52 topic1-0
drwxr-xr-x 2 user user 4096 May 16 14:52 topic1-1
drwxr-xr-x 2 user user 4096 May 16 14:52 topic1-2
drwxr-xr-x 2 user user 4096 May 16 15:10 topic2-1.ccb8bd10930b4bea8d5aef617d78eda0-delete
drwxr-xr-x 2 user user 4096 May 16 15:10 topic2-2.b1f3029d6f5542d8851ccdf8f9543206-delete
drwxr-xr-x 2 user user 4096 May 16 15:10 topic2-0.190779af2f9f4213b4e2c2209043475a-delete
-rw-r--r-- 1 user user    4 May 16 15:11 cleaner-offset-checkpoint
-rw-r--r-- 1 user user   37 May 16 15:11 recovery-point-offset-checkpoint
-rw-r--r-- 1 user user    4 May 16 15:11 log-start-offset-checkpoint
-rw-r--r-- 1 user user   37 May 16 15:11 replication-offset-checkpoint

sh kafka-console-producer.sh --broker-list localhost:9092 --topic topic1 --producer-property acks=all
sh kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic topic1 --from-beginning
