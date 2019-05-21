# work on sentiment analysis using spark nlp module
# pip3 install spark-nlp==2.0.1
#imports

import time
import sys
import os

from pyspark.ml import Pipeline,PipelineModel
from pyspark.sql import SparkSession
from pyspark.sql.functions import array_contains, when
from pyspark.sql.functions import col

import sparknlp
from sparknlp.annotator import *
from sparknlp.base import DocumentAssembler, Finisher

spark=SparkSession.builder\
        .appName("sentiment-analysis")\
        .master("local[3]")\
        .config("spark.driver.memory","1G")\
        .config("spark.driver.maxResultSize","500m")\
        .config("spark.jars.packages","JohnSnowLabs:spark-nlp:2.0.1")\
        .config("spark.kryoserializer.buffer.max","500m")\
        .getOrCreate()


