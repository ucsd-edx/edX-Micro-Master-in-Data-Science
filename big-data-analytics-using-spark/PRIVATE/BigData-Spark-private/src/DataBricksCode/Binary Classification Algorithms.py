# Databricks notebook source exported at Sun, 14 Feb 2016 04:39:56 UTC
# MAGIC %md 
# MAGIC # Binary Classification Algorithms with Pipelines API
# MAGIC 
# MAGIC In this notebook, we will test out the Binary Classification algorithms available in the ML Pipelines API using the Adult dataset. The Pipelines API provides higher-level API built on top of DataFrames for constructing ML pipelines. You can read more about the ML Pipelines API in the [programming guide](http://spark.apache.org/docs/latest/mllib-guide.html#sparkml-high-level-apis-for-ml-pipelines).
# MAGIC 
# MAGIC ####Table of Contents
# MAGIC - Dataset Review
# MAGIC - Load Data
# MAGIC - Data Preprocessing
# MAGIC - Creation and Evaluation of Models
# MAGIC   - Logistic Regression
# MAGIC   - Decision Trees
# MAGIC   - Random Forest
# MAGIC - Deployment

# COMMAND ----------

# MAGIC %md
# MAGIC ####Dataset Review
# MAGIC 
# MAGIC The Adult dataset is publicly available at the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Adult). This data was obtained from the Census, and consists of information about 48842 individuals and their annual income. We will use this information to predict if an individual earns >50k a year or <=50K a year. The dataset is rather clean, and consists of both numeric and categorical variables.
# MAGIC 
# MAGIC Attribute Information:
# MAGIC - age: continuous
# MAGIC - workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked
# MAGIC - fnlwgt: continuous
# MAGIC - education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc...
# MAGIC - education-num: continuous
# MAGIC - marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent...
# MAGIC - occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners...
# MAGIC - relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried
# MAGIC - race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black
# MAGIC - sex: Female, Male. 
# MAGIC - capital-gain: continuous
# MAGIC - capital-loss: continuous
# MAGIC - hours-per-week: continuous
# MAGIC - native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany...
# MAGIC 
# MAGIC 
# MAGIC Target/Label:
# MAGIC - <=50K, >50K

# COMMAND ----------

# MAGIC %md
# MAGIC ####Load Data
# MAGIC In this example, we will read in the adult dataset that is mounted on the DBFS using the spark-csv package. We will use SQL to read in the data and rename the columns appropriately.

# COMMAND ----------

# Filepath for adult dataset in DBFS
display(dbutils.fs.ls("databricks-datasets/adult/adult.data"))

# COMMAND ----------

# MAGIC %md ### Reading a file into an SQL database ###
# MAGIC First, we read the text file, parse it, and load it into a database (Hive). Note the directive `USING com.databricks.spark.csv` which identifies the code for parsing csv files.

# COMMAND ----------

# MAGIC %sql DROP TABLE IF EXISTS adult

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE adult (age double, workclass string, fnlwgt double, education string, education_num double, marital_status string, occupation string, relationship string, race string, sex string, capital_gain double, capital_loss double, hours_per_week double, native_country string, income string)
# MAGIC USING com.databricks.spark.csv
# MAGIC OPTIONS (path "/databricks-datasets/adult/adult.data", header "true")

# COMMAND ----------

# MAGIC %md 
# MAGIC ### Loading data into several computers ###
# MAGIC Next, we load the table into a `pyspark dataframe`. A dataframe is a specialized type of an `RDD`. 
# MAGIC 
# MAGIC **`RDD`s**, (which stands for `Resiliant Distributed Datasets`) is the central data structure that is at the core of Spark. It allows the programmer to manipulate, in parallel, data that is distributed among the memories of several computers.

# COMMAND ----------

dataset = sqlContext.table("adult")
cols = dataset.columns
type(dataset)

# COMMAND ----------

display(dataset)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Data Preprocessing
# MAGIC Since we are going to try algorithms like Logistic Regression, we will have to convert the categorical variables in the dataset into numeric variables. There are 2 ways we can do this.
# MAGIC 
# MAGIC 
# MAGIC - Category Indexing. This is basically assigning a numeric value to each category from {0, 1, 2, ...numCategories-1}. This introduces an implicit heirachy among your categories, and is more suitable for ordinal variables (eg: Poor: 0, Average: 1, Good: 2)
# MAGIC - [One-Hot Encoding](https://en.wikipedia.org/wiki/One-hot). This converts categories into binary vectors with at most one positive value (eg: (Blue: 1, 0, 0), (Green: 0, 1, 0), (Red: 0, 0, 1))

# COMMAND ----------

# MAGIC %md
# MAGIC Below is a quick example of what one-hot encoded variables will look like. The first column represents the categorical variable, and the second column represents the index assigned to each category value. The rest of the columns represent the resulting one-hot encoded binary vectors.

# COMMAND ----------

# MAGIC %md ### Creating RDDs from scratch ###
# MAGIC Here is a a way to create a dataframe from hard-coded data.

# COMMAND ----------

colors = [('Blue', 0, 1, 0, 0), ('Green', 1, 0, 1, 0), ('Red', 2, 0 , 0 , 1)] #create an array of tuples
rdd = sc.parallelize(colors)  # make the array into an RDD
df = sqlContext.createDataFrame(rdd, ['Colors', 'Index', 'OHE_attr1', 'OHE_attr2', 'OHE_attr3']) # transform the RDD into a dataframe.
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC In this dataset, we have ordinal variables like education (Preschool - Doctorate), and also nominal variables like relationship (Wife, Husband, Own-child, etc). For simplicity's sake, we will use One-Hot Encoding to convert all categorical variables into binary vectors. It might be possible here to improve prediction accuracy by converting each categorical column with an appropriate method.
# MAGIC 
# MAGIC Here, we will use a combination of [StringIndexer](http://spark.apache.org/docs/latest/ml-features.html#stringindexer) and [OneHotEncoder](http://spark.apache.org/docs/latest/ml-features.html#onehotencoder) to convert the categorical variables. The OneHotEncoder will return a [SparseVector](https://spark.apache.org/docs/latest/api/python/pyspark.mllib.html#pyspark.mllib.linalg.SparseVector).

# COMMAND ----------

###One-Hot Encoding
from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorAssembler
  
categoricalColumns = ["workclass", "education", "marital_status", "occupation", "relationship", "race", "sex", "native_country"]
for categoricalCol in categoricalColumns:
  # Category Indexing with StringIndexer
  stringIndexer = StringIndexer(inputCol=categoricalCol, outputCol=categoricalCol+"Index")
  model = stringIndexer.fit(dataset)
  indexed = model.transform(dataset)
  # Use OneHotEncoder to convert categorical variables into binary SparseVectors
  encoder = OneHotEncoder(inputCol=categoricalCol+"Index", outputCol=categoricalCol+"classVec")
  encoded = encoder.transform(indexed)
  dataset = encoded

print dataset.take(1)

# COMMAND ----------

# MAGIC %md
# MAGIC The above code basically indexes each categorical column using the StringIndexer, and then converts the indexed categories into one-hot encoded variables. The resulting output has the binary vectors appended to the end of each row.

# COMMAND ----------

# MAGIC %md
# MAGIC We use the StringIndexer() again here to encode our labels to label indices

# COMMAND ----------

# Convert label into label indices using the StringIndexer
label_stringIdx = StringIndexer(inputCol = "income", outputCol = "label")
label_model = label_stringIdx.fit(dataset)
label_indexed = label_model.transform(dataset)
print label_indexed.take(1)

# COMMAND ----------

# MAGIC %md
# MAGIC Next, we will use the VectorAssembler() to combine all the feature columns into a single vector column. This will include both the numeric columns and the one-hot encoded binary vector columns in our dataset.

# COMMAND ----------

# Transform all features into a vector using VectorAssembler
assembler = VectorAssembler(
    inputCols=["age","workclassclassVec","fnlwgt","educationclassVec","education_num","marital_statusclassVec",
               "occupationclassVec","relationshipclassVec","raceclassVec", "sexclassVec", "capital_gain", "capital_loss", "hours_per_week",
               "native_countryclassVec"],
    outputCol="features")
output = assembler.transform(label_indexed)

# Keep relevant columns
selectedcols = ["label", "features"] + cols
dataset = output.select(selectedcols)
display(dataset)

# COMMAND ----------

### Randomly split data into training and test sets. set seed for reproducibility
(trainingData, testData) = dataset.randomSplit([0.7, 0.3], seed = 100)
print trainingData.count()
print testData.count()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Creation and Evaluation of Models
# MAGIC We are now ready to try out some of the Binary Classification Algorithms available in the new ML Pipelines API.
# MAGIC 
# MAGIC Out of these algorithms, the below are currently also capable of supporting multiclass classification with the Python API:
# MAGIC - Decision Trees
# MAGIC - Random Forest
# MAGIC 
# MAGIC These are the general steps we will take to build our models:
# MAGIC - Create initial model using the training set
# MAGIC - Tune parameters with a ParamGrid and 5-fold Cross Validation
# MAGIC - Evaluate the best model obtained from the Cross Validation using the test set
# MAGIC 
# MAGIC We will be using the BinaryClassificationEvaluator to evaluate our models. The default metric used here is [areaUnderROC](https://en.wikipedia.org/wiki/Receiver_operating_characteristic#Area_under_the_curve).

# COMMAND ----------

# MAGIC %md
# MAGIC ####Logistic Regression
# MAGIC 
# MAGIC You can read more about Logistic Regression from the Programming Guide [here](http://spark.apache.org/docs/latest/mllib-linear-methods.html#logistic-regression). In the new Pipelines API, we are now able to perform Elastic net regularization with Logistic Regression, as well as other linear methods.
# MAGIC 
# MAGIC 
# MAGIC Note: As of Spark 1.5.0, The Python API does not yet support multiclass classification for Logistic Regression, but will be available in future.

# COMMAND ----------

from pyspark.ml.classification import LogisticRegression
from pyspark.ml.param import Param, Params

# Create initial LogisticRegression model
lr = LogisticRegression(labelCol="label", featuresCol="features", maxIter=10)

# Train model with Training Data
lrModel = lr.fit(trainingData)

# COMMAND ----------

# Make predictions on test data using the Transformer.transform() method.
# LogisticRegression.transform() will only use the 'features' column.
predictions = lrModel.transform(testData)

# COMMAND ----------

predictions.printSchema()

# COMMAND ----------

# View model's predictions and probabilities of each prediction class
# You can select any columns in the above schema to view as well. For example's sake we will choose age & occupation
selected = predictions.select("label", "prediction", "probability", "age", "occupation")
display(selected)

# COMMAND ----------

# MAGIC %md
# MAGIC We can make use of the BinaryClassificationEvaluator method to evaluate our model. The Evaluator expects two input columns: (rawPrediction, label).

# COMMAND ----------

from pyspark.ml.evaluation import BinaryClassificationEvaluator

# Evaluate model
evaluator = BinaryClassificationEvaluator(rawPredictionCol="rawPrediction")
evaluator.evaluate(predictions)

# COMMAND ----------

# MAGIC %md Note that the default metric for the BinaryClassificationEvaluator is areaUnderROC

# COMMAND ----------

evaluator.getMetricName()

# COMMAND ----------

# MAGIC %md The evaluator currently accepts 2 kinds of metrics - areaUnderROC and areaUnderPR.
# MAGIC We can set it to areaUnderPR by using evaluator.setMetricName("areaUnderPR").

# COMMAND ----------

# MAGIC %md
# MAGIC Now we will try tuning the model with the ParamGridBuilder and the CrossValidator.
# MAGIC 
# MAGIC If you are unsure what params are available for tuning, you can use explainParams() to print a list of all params.

# COMMAND ----------

print lr.explainParams()

# COMMAND ----------

# MAGIC %md As we indicate 5 values for regParam, 4 values for maxIter, and 5 values for elasticNetParam, this grid will have 5 x 4 x 5 = 100 parameter settings for CrossValidator to choose from. We will create a 5-fold cross validator.

# COMMAND ----------

from pyspark.ml.tuning import ParamGridBuilder, CrossValidator

# Create ParamGrid for Cross Validation
paramGrid = (ParamGridBuilder()
             .addGrid(lr.regParam, [0.01, 0.1, 0.5, 1.0, 2.0])
             .addGrid(lr.elasticNetParam, [0.0, 0.1, 0.5, 0.8, 1.0])
             .addGrid(lr.maxIter, [1, 5, 10, 20])
             .build())

# COMMAND ----------

# Create 5-fold CrossValidator
cv = CrossValidator(estimator=lr, estimatorParamMaps=paramGrid, evaluator=evaluator, numFolds=5)

# Run cross validations
cvModel = cv.fit(trainingData)

# COMMAND ----------

# Use test set here so we can measure the accuracy of our model on new data
predictions = cvModel.transform(testData)

# COMMAND ----------

# cvModel uses the best model found from the Cross Validation
# Evaluate best model
evaluator.evaluate(predictions)

# COMMAND ----------

# MAGIC %md
# MAGIC We can also access the model's feature weights and intercepts easily

# COMMAND ----------

print 'Model Intercept: ', cvModel.bestModel.intercept

# COMMAND ----------

from pyspark.sql import Row

weights = cvModel.bestModel.weights
rdd = sc.parallelize(weights)
rdd = rdd.map(lambda x: Row(float(x)))
weightsDF = sqlContext.createDataFrame(rdd, ["Feature Weights"])
display(weightsDF)

# COMMAND ----------

# View Best model's predictions and probabilities of each prediction class
selected = predictions.select("label", "prediction", "probability", "age", "occupation")
display(selected)

# COMMAND ----------

# MAGIC %md
# MAGIC ####Decision Trees
# MAGIC You can read more about Decision Trees from the Programming Guide [here](http://spark.apache.org/docs/latest/mllib-decision-tree.html).
# MAGIC 
# MAGIC Decision Trees is a popular algorithm as it can handle categorical data and work with multiclass data.

# COMMAND ----------

from pyspark.ml.classification import DecisionTreeClassifier

# Create initial Decision Tree Model
dt = DecisionTreeClassifier(labelCol="label", featuresCol="features", maxDepth=3)

# Train model with Training Data
dtModel = dt.fit(trainingData)

# COMMAND ----------

# MAGIC %md We can extract the number of nodes in our decision tree as well as the tree depth of our model.

# COMMAND ----------

print "numNodes = ", dtModel.numNodes
print "depth = ", dtModel.depth

# COMMAND ----------

# Make predictions on test data using the Transformer.transform() method.
predictions = dtModel.transform(testData)

# COMMAND ----------

predictions.printSchema()

# COMMAND ----------

# View model's predictions and probabilities of each prediction class
selected = predictions.select("label", "prediction", "probability", "age", "occupation")
display(selected)

# COMMAND ----------

# MAGIC %md
# MAGIC We will evaluate our Decision Tree model with BinaryClassificationEvaluator.

# COMMAND ----------

from pyspark.ml.evaluation import BinaryClassificationEvaluator

# Evaluate model
evaluator = BinaryClassificationEvaluator()
evaluator.evaluate(predictions)


# COMMAND ----------

# MAGIC %md 
# MAGIC Entropy and the Gini coefficient are the supported measures of impurity for Decision Trees. This is set to Gini by default.
# MAGIC 
# MAGIC This can be changed by using model.setImpurity("Entropy").

# COMMAND ----------

dt.getImpurity()

# COMMAND ----------

# MAGIC %md
# MAGIC Now we will try tuning the model with the ParamGridBuilder and the CrossValidator.
# MAGIC 
# MAGIC As we indicate 6 values for maxDepth and 5 values for maxBin, this grid will have 6 * 5 = 30 parameter settings for CrossValidator to choose from. We will create a 5-fold CrossValidator.

# COMMAND ----------

# Create ParamGrid for Cross Validation
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator

paramGrid = (ParamGridBuilder()
             .addGrid(dt.maxDepth, [1,2,4,6,8,10])
             .addGrid(dt.maxBins, [20,40,60,80,100])
             .build())

# COMMAND ----------

# Create 5-fold CrossValidator
cv = CrossValidator(estimator=dt, estimatorParamMaps=paramGrid, evaluator=evaluator, numFolds=5)

# Run cross validations
cvModel = cv.fit(trainingData)

# COMMAND ----------

print "numNodes = ", cvModel.bestModel.numNodes
print "depth = ", cvModel.bestModel.depth

# COMMAND ----------

# Use test set here so we can measure the accuracy of our model on new data
predictions = cvModel.transform(testData)

# COMMAND ----------

# cvModel uses the best model found from the Cross Validation
# Evaluate best model
evaluator.evaluate(predictions)

# COMMAND ----------

# View Best model's predictions and probabilities of each prediction class
selected = predictions.select("label", "prediction", "probability", "age", "occupation")
display(selected)

# COMMAND ----------

# MAGIC %md
# MAGIC ####Random Forest
# MAGIC 
# MAGIC Random Forests uses an ensemble of trees to improve model accuracy.
# MAGIC 
# MAGIC You can read more about Random Forest from the programming guide [here](http://spark.apache.org/docs/latest/mllib-ensembles.html#random-forests).

# COMMAND ----------

from pyspark.ml.classification import RandomForestClassifier

# Create an initial RandomForest model.
rf = RandomForestClassifier(labelCol="label", featuresCol="features")

# Train model with Training Data
rfModel = rf.fit(trainingData)

# COMMAND ----------

# Make predictions on test data using the Transformer.transform() method.
predictions = rfModel.transform(testData)

# COMMAND ----------

predictions.printSchema()

# COMMAND ----------

# View model's predictions and probabilities of each prediction class
selected = predictions.select("label", "prediction", "probability", "age", "occupation")
display(selected)

# COMMAND ----------

# MAGIC %md
# MAGIC We will evaluate our Random Forest model with BinaryClassificationEvaluator.

# COMMAND ----------

from pyspark.ml.evaluation import BinaryClassificationEvaluator

# Evaluate model
evaluator = BinaryClassificationEvaluator()
evaluator.evaluate(predictions)

# COMMAND ----------

# MAGIC %md
# MAGIC Now we will try tuning the model with the ParamGridBuilder and the CrossValidator.
# MAGIC 
# MAGIC As we indicate 6 values for maxDepth, 5 values for maxBin, and 4 values for numTrees, this grid will have 6 x 5 x 4 = 120 parameter settings for CrossValidator to choose from. We will create a 5-fold CrossValidator.

# COMMAND ----------

# Create ParamGrid for Cross Validation
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator

paramGrid = (ParamGridBuilder()
             .addGrid(rf.maxDepth, [1,2,4,6,8,10])
             .addGrid(rf.maxBins, [20,40,60,80,100])
             .addGrid(rf.numTrees, [5,10,20,30])
             .build())

# COMMAND ----------

# Create 5-fold CrossValidator
cv = CrossValidator(estimator=rf, estimatorParamMaps=paramGrid, evaluator=evaluator, numFolds=5)

# Run cross validations
cvModel = cv.fit(trainingData)

# COMMAND ----------

# Use test set here so we can measure the accuracy of our model on new data
predictions = cvModel.transform(testData)

# COMMAND ----------

# cvModel uses the best model found from the Cross Validation
# Evaluate best model
evaluator.evaluate(predictions)

# COMMAND ----------

# View Best model's predictions and probabilities of each prediction class
selected = predictions.select("label", "prediction", "probability", "age", "occupation")
display(selected)

# COMMAND ----------

# MAGIC %md #### Deployment
# MAGIC 
# MAGIC As Random Forest gives us the best areaUnderROC value, we will use the bestModel obtained from Random Forest for deployment, and use it to generate predictions on new data. In this example, we will simulate this by generating predictions on the entire dataset.

# COMMAND ----------

bestModel = cvModel.bestModel

# COMMAND ----------

# Generate predictions for entire dataset
finalPredictions = bestModel.transform(dataset)

# COMMAND ----------

# Evaluate best model
evaluator.evaluate(finalPredictions)

# COMMAND ----------

# MAGIC %md Since there are no userIds in this dataset, we will use the row indices as userIds as we know that each row corresponds to a unique individual. We will create a table of rowIndex and incomePredicition. In this example, we will also look into an individual's age and occupation.

# COMMAND ----------

finalPredictions.registerTempTable("finalPredictions")

# COMMAND ----------

# Create new deploymentTable containing rowIndex, incomePrediction, age, occupation
sql("SELECT ROW_NUMBER() OVER (ORDER BY prediction) AS rowIndexes, prediction AS incomePrediction, age, occupation FROM finalPredictions").registerTempTable("deploymentTable")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM deploymentTable

# COMMAND ----------

# MAGIC %md In an operational environment, analysts may use a similar machine learning pipeline to obtain predictions on new data, organize it into a table and use it for analysis or lead targeting.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT occupation, incomePrediction, count(*) AS count
# MAGIC FROM deploymentTable
# MAGIC GROUP BY occupation, incomePrediction
# MAGIC ORDER BY occupation

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT age, incomePrediction, count(*) AS count
# MAGIC FROM deploymentTable
# MAGIC GROUP BY age, incomePrediction
# MAGIC ORDER BY age

# COMMAND ----------

# MAGIC %md Now we can target our users better!