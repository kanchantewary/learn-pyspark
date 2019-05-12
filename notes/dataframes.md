# Dataframe API
## Resources
Chapter 4, definitive guide  
dataframes and datasets are two structured collections that spark have.  
dataframes = untyped, spark checks type at runtime. [It is dataset of type Row](https://databricks.com/blog/2016/06/22/apache-spark-key-terms-explained.html)  
datasets = typed, spark checks type at compile time, only available in JVM based languages (scala, java)
[IBM watson studio notebook](https://dataplatform.cloud.ibm.com/exchange/public/entry/view/5ad1c820f57809ddec9a040e37b2bd55)

Catalyst Optimizer
[See](https://youtu.be/5ajs8EIPWGI) and [this](https://youtu.be/GDeePbbCz2g)
Read the [blog](https://databricks.com/blog/2015/04/13/deep-dive-into-spark-sqls-catalyst-optimizer.html)

![](catalyst.jpeg)

Refer this [blog post](https://virtuslab.com/blog/spark-sql-hood-part-i/) to learn the internals  
to add custom rule to optimization, refer [this](http://blog.madhukaraphatak.com/introduction-to-spark-two-part-6/)  
Spark [Catalog API](https://jaceklaskowski.gitbooks.io/mastering-spark-sql/spark-sql-CatalogImpl.html)

[Rule based optimizer]
[Cost based optimizer](https://youtu.be/qS_aS99TjCM) and [this](https://youtu.be/WSIN6f-wHcQ)

Optimization techniques (refer this [session](https://youtu.be/fp53QhSfQcI))  
a) Review spark UI, look for tasks that take much longer to run than others  
b) speculative tasks that are launching  
c) shards that have lot more input or shuffle output  
d) use broadcast hash join over shuffle hash join, if one dataframe can fit into memory  
e) use explain to review the plan, add hint not chosen automatically (prefer parquet files as source if possible)  
f) resolve data skew problem - apply salting approach  
g) resolve cartesian join requirement with alternative design
h) define schemas manually in production environment, esp while using csv,json formats as source.

Refer this [blog](https://mapr.com/blog/tips-and-best-practices-to-take-advantage-of-spark-2-x/) from MapR


[Fuzzy matching](https://medium.com/@mrpowers/fuzzy-matching-in-spark-with-soundex-and-levenshtein-distance-6749f5af8f28)

[Details on metadata property in StructType](https://stackoverflow.com/questions/32628845/is-there-a-way-to-add-extra-metadata-for-spark-dataframes)

[MarR training](https://mapr.com/training/on-demand/dev-360-v21-introduction-to-apache-spark/)
