##DSE230/CSE255 plan:

### introduction:
* map-reduce
* counting words example, loading, processing, collecting.
* The work environment: Notebooks, markdown, code cells, display cells, S3, passwords and Vault, github, cloning, communicating through comments.
Local install vs. install on cloud. Cost monitoring
* the memory hierarchy, S3 File, SQL tables, data frames / RDD, Parquet files.

### minimizing squared error
* Built-in Regression and PCA
 * https://github.com/apache/spark/blob/master/examples/src/main/python/ml/pca_example.py
 * https://github.com/apache/spark/blob/master/examples/src/main/python/ml/linear_regression_with_elastic_net.py
* PCA with missing values
 * To be written
* Logistic regression
 * https://github.com/apache/spark/blob/master/examples/src/main/python/ml/logistic_regression_with_elastic_net.py
* Tree-based regression
 * https://github.com/apache/spark/blob/master/examples/src/main/python/mllib/decision_tree_regression_example.py

### Ensamble methods for classification
* Random forests
 * https://github.com/apache/spark/blob/master/examples/src/main/python/mllib/random_forest_classification_example.py
* gradient boosted trees
 * https://github.com/apache/spark/blob/master/examples/src/main/python/mllib/gradient_boosting_classification_example.py

### Performance tuning: measuring and tuning spark applications

### Other models of computation: Spark Streaming and GraphX


-----
Other (probably not cover)
Unsupervised learning
K-means (kmeans++)
https://github.com/apache/spark/blob/master/examples/src/main/python/mllib/kmeans.py
word2Vec
https://github.com/apache/spark/blob/master/examples/src/main/python/mllib/word2vec.py
Spectral clustering:would be nice but currently seems to be only supported under scala https://www.ocf.berkeley.edu/~sanjayk/pubs/AMPLabPoster_3.pdf https://github.com/apache/spark/blob/master/examples/src/main/scala/org/apache/spark/examples/mllib/PowerIterationClusteringExample.scala
