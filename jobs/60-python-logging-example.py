# import logging module

import logging

#logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='/home/user/workarea/projects/learn-pyspark/logs/60-logging-example.log',filemode='w',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.debug("This is a debug message")
logging.info("This is an informational message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

