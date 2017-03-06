from pyspark import SparkContext
from numpy.random import random
sc = SparkContext()


NUM_SAMPLES = 100000
def sample(p):
    x, y = random(), random()
    return 1 if x*x + y*y < 1 else 0

count = sc.parallelize(xrange(0, NUM_SAMPLES)).map(sample) \
             .reduce(lambda a, b: a + b)
print "Homework: Pi is roughly %f" % (4.0 * count / NUM_SAMPLES)