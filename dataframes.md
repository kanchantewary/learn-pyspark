# Dataframe API
## Resources
Chapter 4, definitive guide  
dataframes and datasets are two structured collections that spark have.  
dataframes = untyped, spark checks type at runtime. it is dataset of type Row.  
datasets = typed, spark checks type at compile time, only available in JVM based languages (scala, java)

Catalyst Optimizer
[See](https://youtu.be/5ajs8EIPWGI) and [this](https://youtu.be/GDeePbbCz2g)
Read the [blog](https://databricks.com/blog/2015/04/13/deep-dive-into-spark-sqls-catalyst-optimizer.html)

![](catalyst.jpeg)

Refer this [blog post](https://virtuslab.com/blog/spark-sql-hood-part-i/) to learn the internals  
to add custom rule to optimization, refer [this](http://blog.madhukaraphatak.com/introduction-to-spark-two-part-6/)  
Spark [Catalog API](https://jaceklaskowski.gitbooks.io/mastering-spark-sql/spark-sql-CatalogImpl.html)

[Rule based optimizer]
[Cost based optimizer](https://youtu.be/qS_aS99TjCM) and [this](https://youtu.be/WSIN6f-wHcQ)

Optimization techniques:
a) Review spark UI, look for tasks that take much longer to run than others
b) speculative tasks that are launching
c) shards that have lot more input or shuffle output

Refer this [blog](https://mapr.com/blog/tips-and-best-practices-to-take-advantage-of-spark-2-x/) from MapR
