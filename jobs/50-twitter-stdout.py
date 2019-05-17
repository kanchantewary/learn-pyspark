# This job would read from twitter and write into a kafka topic in real-time
#pip3 install tweepy
# to run: python3 50-twitter-stdout.py /home/user/workarea/projects/learn-pyspark/config/twitter.conf dev

from tweepy import OAuthHandler,Stream,StreamListener

# define variables to store user credentials to access twitter API, read the credentials from config file

import configparser as cp
import time
import sys

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

if __name__ == '__main__':

    # This handles twitter authentication and connection to twitter streaming API
    l = StdOutListener()
    auth=OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    stream=Stream(auth,l)
    stream.filter(track=['kafka','apache spark'])

