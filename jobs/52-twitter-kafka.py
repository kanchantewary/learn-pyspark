# This job would read from twitter and write into a kafka topic in real-time
#pip3 install tweepy
# sh kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic tweets --from-beginning
# to run: python3 52-twitter-kafka.py /home/user/workarea/projects/learn-pyspark/config/twitter.conf dev

from tweepy import OAuthHandler,Stream,StreamListener

# define variables to store user credentials to access twitter API, read the credentials from config file

import configparser as cp
import time
import sys

from kafka import KafkaProducer, KafkaConsumer, TopicPartition

conf = cp.ConfigParser()
conf.read(sys.argv[1])
env = sys.argv[2]

consumer_key=conf.get(env,'consumer_key')
consumer_secret=conf.get(env,'consumer_secret')
access_token=conf.get(env,'access_token')
access_token_secret=conf.get(env,'access_token_secret')

producer=KafkaProducer(bootstrap_servers='localhost:9092',compression_type='snappy',acks='all',batch_size=(64*1024),linger_ms=1000,max_in_flight_requests_per_connection=5)
topic_name='tweets'

auth=OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

class MyStreamListener(StreamListener):

    def on_data(self,data):
        producer.send(topic_name,data.encode('utf-8'))
        #print(data)
        return True
    def on_error(self,status):
        print(status)
        if status==420:
            return False

l=MyStreamListener()
myStream = Stream(auth, l)
myStream.filter(track=['india election'],languages=['en'])

