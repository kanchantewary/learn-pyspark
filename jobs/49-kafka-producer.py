# kafka lessons, using kafka-python module
# pip3 install kafka-python

from kafka import KafkaProducer, KafkaConsumer, TopicPartition
from time import sleep
from json import dumps

producer=KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x:dumps(x).encode('utf-8'))
for e in range(1000):
    data={'number' : e }
    producer.send('numtest',value=data)
    sleep(5)
