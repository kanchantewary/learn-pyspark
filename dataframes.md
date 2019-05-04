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

to add custom rule to optimization, refer [this](http://blog.madhukaraphatak.com/introduction-to-spark-two-part-6/)  
Spark [Catalog API](https://jaceklaskowski.gitbooks.io/mastering-spark-sql/spark-sql-CatalogImpl.html)

