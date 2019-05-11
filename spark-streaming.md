# Notes on Spark Streaming
### Design patterns
a. continuous  
b. micro-batch

### APIs
a. Dstreams  
b. Structured Streaming
    uses existing structured APIs in Spark (DataFrames, Datasets, and SQL), ensures end-to-end, exactly-once processing.
    supports kafka, hdfs and s3 as a source. kafka, memory and console as sinks are supported, in addition to other file formats.
    supported output modes:
    a. Append (only add new records to the output sink) 
    b. Update (update changed records in place)
    c. Complete (rewrite the full output)
