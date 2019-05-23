# develop a consumer to write twitter data from kafka topic to mongodb
# to start mongo service: sudo service mongod start
# to start mongo shell: mongo
# python3 58-kafka-consumer-mongo.py

from pprint import pprint
import json

# use pymongo library

from pymongo import MongoClient

# use kafka-python library

from kafka import KafkaConsumer

# setup mongo connection

client=MongoClient("mongodb://localhost:27017")

db=client.test
tweets=db.tweets_from_kafka

#pprint(db.command("serverStatus"))

kafka_topic='tweets'

consumer1=KafkaConsumer(kafka_topic, group_id='mongo-group-1',bootstrap_servers='localhost:9092')

for msg in consumer1:
    msg_json=json.loads(msg.value)
    print(tweets.insert_one(msg_json).inserted_id)

