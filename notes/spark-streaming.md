# Notes on Spark Streaming
### Design patterns
a. continuous  
b. micro-batch

### APIs
a. Dstreams  
b. Structured Streaming  
Uses existing structured APIs in Spark (DataFrames, Datasets, and SQL), ensures end-to-end, exactly-once processing. Supports kafka, hdfs and s3 as a source. kafka, memory and console as sinks are supported, in addition to other file formats.  
supported output modes:  
    a. Append (only add new records to the output sink)  
    b. Update (update changed records in place)  
    c. Complete (rewrite the full output)  
The main idea behind Structured Streaming is to treat a stream of data as a table to which data is continuously appended. The job then periodically checks for new input data, process it, updates some internal state located in a state store if needed, and updates its result. 
Other concepts:  
Event time  
Watermark  
Triggers for output
Stateful processing
concept of Window - tumbling window and sliding window

# kafka integration
Refer the [programming guide](https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html)
