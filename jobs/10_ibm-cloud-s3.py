#https://github.com/IBM/ibm-cos-sdk-python
#spark-submit 

import ibm_boto3
from ibm_botocore.client import Config
import configparser as cp
import time
import sys

conf = cp.ConfigParser()
conf.read(sys.argv[1])
env = sys.argv[2]
#config.read('/home/user/workarea/projects/pyspark-kt-01/config/param.conf')

# Constants for IBM COS values
COS_ENDPOINT = conf.get(env,'endpoints') # Current list avaiable at https://cos-service.bluemix.net/endpoints
COS_API_KEY_ID = conf.get(env,'apikey')
COS_AUTH_ENDPOINT = "https://iam.ng.bluemix.net/oidc/token"
COS_RESOURCE_CRN = conf.get(env,'resource_instance_id')
COS_BUCKET_LOCATION = 'jp-tok'

# Create resource
cos = ibm_boto3.resource("s3",
    ibm_api_key_id=COS_API_KEY_ID,
    ibm_service_instance_id=COS_RESOURCE_CRN,
    ibm_auth_endpoint=COS_AUTH_ENDPOINT,
    config=Config(signature_version="oauth"),
    endpoint_url=COS_ENDPOINT
)
