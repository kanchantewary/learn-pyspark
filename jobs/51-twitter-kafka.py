# This job would read from twitter and write into a kafka topic in real-time
#pip3 install tweepy
# sh kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic tweets --from-beginning
# to run: python3 51-twitter-kafka.py /home/user/workarea/projects/learn-pyspark/config/twitter.conf dev

from tweepy import OAuthHandler,Stream,StreamListener

# define variables to store user credentials to access twitter API, read the credentials from config file

import configparser as cp
import time
import sys

from kafka import KafkaProducer, KafkaConsumer, TopicPartition
from time import sleep
from json import dumps


conf = cp.ConfigParser()
conf.read(sys.argv[1])
env = sys.argv[2]

consumer_key=conf.get(env,'consumer_key')
consumer_secret=conf.get(env,'consumer_secret')
access_token=conf.get(env,'access_token')
access_token_secret=conf.get(env,'access_token_secret')

# create a basic listener which would write received tweets to stdout
class StdOutListener(StreamListener):
    def on_data(self,data):
        print(data)
        return True

    def on_error(self,status):
        print(status)

class KafkaListener(StreamListener):
    def on_data(self,data):
        producer=KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x:dumps(x).encode('utf-8'))
        producer.send("tweets",value=data)

if __name__ == '__main__':

    # This handles twitter authentication and connection to twitter streaming API
    l = KafkaListener()
    auth=OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    stream=Stream(auth,l)
    stream.filter(track=['kafka','apache spark'])
