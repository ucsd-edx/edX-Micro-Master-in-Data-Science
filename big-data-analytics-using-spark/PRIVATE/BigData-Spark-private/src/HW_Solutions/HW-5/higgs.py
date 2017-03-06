from pyspark import SparkContext, SparkConf

sc = SparkContext()


from pyspark.mllib.linalg import Vectors
from pyspark.mllib.regression import LabeledPoint

from string import split,strip

from pyspark.mllib.tree import GradientBoostedTrees, GradientBoostedTreesModel
from pyspark.mllib.tree import RandomForest, RandomForestModel

from pyspark.mllib.util import MLUtils

path='/HIGGS/HIGGS.csv'
inputRDD=sc.textFile(path)

Data=inputRDD.map(lambda line: [float(strip(x)) for x in line.split(',')])             .map(lambda x: LabeledPoint(x[0], x[1:]))

Data1=Data.sample(False,0.1, seed=255).cache()

(trainingData,testData) = Data1.randomSplit([0.7,0.3],seed=255)


from time import time
errors={}
for depth in [10]:
    start=time()
    model=GradientBoostedTrees.trainClassifier(trainingData, learningRate=0.2, numIterations=30,maxDepth=depth, categoricalFeaturesInfo={})

    errors[depth]={}
    dataSets={'train':trainingData,'test':testData}
    for name in dataSets.keys():
        data=dataSets[name]
        Predicted=model.predict(data.map(lambda x: x.features))
        LabelsAndPredictions=data.map(lambda x: x.label).zip(Predicted)
        Err = LabelsAndPredictions.filter(lambda (v,p):v != p).count()/float(data.count())
        errors[depth][name]=Err

print errors
