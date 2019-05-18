# end to end: twitter-kafka-spark-kafka-elasticsearch-kibana dashboard
steps:
1. twitter-kafka integration:write a python program to read from twitter and write into a kafka topic
Refer this [blog](http://adilmoujahid.com/posts/2014/07/twitter-analytics/) or [this](http://people.ischool.berkeley.edu/~qianyu/my_ds_projects/twitter_sentiment_proj) or [this](https://dorianbg.wordpress.com/2017/11/11/ingesting-realtime-tweets-using-apache-kafka-tweepy-and-python/)  
2. kafka-spark-kafka:read the kafka topic in pyspark, perform some analysis and write back to another kafka topic  
3. kafka-elasticsearch: write a python program to read a kafka topic and write into elasticsearch(bonsai hosted cluster)  
4. elasticsearch-kibana: build some basic dashboard using the data  
5. run them end to end to create real-time dashboard  
