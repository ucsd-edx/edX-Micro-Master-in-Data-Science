from pyspark import SparkContext, SparkConf

sc = SparkContext()

from pyspark.mllib.linalg import Vectors
from pyspark.mllib.regression import LabeledPoint

from string import split,strip

from pyspark.mllib.tree import GradientBoostedTrees, GradientBoostedTreesModel
from pyspark.mllib.util import MLUtils


from string import split,strip


path='/covtype/covtype.data'
inputRDD=sc.textFile(path)

Label=2.0

Data = inputRDD.map(lambda line: [float(x) for x in line.split(',')]).map(lambda V:LabeledPoint((V[-1]==Label), V[:-1])).cache()

(trainingData,testData) = Data.randomSplit([0.7,0.3],seed=255)

from time import time
errors={}
catInfo = {}
for i in range(10,54):
    catInfo[i] = 2

for depth in [10]:
    start=time()
    model=GradientBoostedTrees.trainClassifier(trainingData,learningRate = 0.2, numIterations = 30, maxDepth = depth,
                                               categoricalFeaturesInfo=catInfo)
    errors[depth]={}
    dataSets={'train':trainingData,'test':testData}
    for name in dataSets.keys():  # Calculate errors on train and test sets
        data=dataSets[name]
        Predicted=model.predict(data.map(lambda x: x.features))
        LabelsAndPredictions=data.map(lambda x: x.label).zip(Predicted)
        Err = LabelsAndPredictions.filter(lambda (v,p):v != p).count()/float(data.count())
        errors[depth][name]=Err
print errors
