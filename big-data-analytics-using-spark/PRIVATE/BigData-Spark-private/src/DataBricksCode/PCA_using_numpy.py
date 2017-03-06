# Databricks notebook source exported at Mon, 29 Feb 2016 02:16:59 UTC
# MAGIC %md ### Performing PCA on vectors with NaNs
# MAGIC This notebook demonstrates the use of numpy arrays as the content of RDDs

# COMMAND ----------

import numpy as np

def outerProduct(X):
  """Computer outer product and indicate which locations in matrix are undefined"""
  O=np.outer(X,X)
  N=1-np.isnan(O)
  return (O,N)
def sumWithNan(M1,M2):
  """Add two pairs of matrix,count"""
  (X1,N1)=M1
  (X2,N2)=M2
  N=N1+N2
  X=np.nansum(np.dstack((X1,X2)),axis=2)
  return (X,N)
  

# COMMAND ----------

# computeCov recieves as input an RDD of np arrays, all of the same length, and computes the covariance matrix for that set of vectors
def computeCov(RDDin):
  RDD=RDDin.map(lambda v:np.insert(v,0,1)) # insert a 1 at the beginning of each vector so that the same 
                                           #calculation also yields the mean vector
  OuterRDD=RDD.map(outerProduct)   # separating the map and the reduce does not matter because of Spark uses lazy execution.
  (S,N)=OuterRDD.reduce(sumWithNan)
  # Unpack result and compute the covariance matrix
  #print 'RDD=',RDD.collect()
  print S.shape, N.shape
  #print 'S=',S
  #print 'N=',N
  E=S[0,1:]
  NE=N[0,1:]
  Mean=E/NE
  O=S[1:,1:]
  NO=N[1:,1:]
  Cov=O/NO - np.outer(Mean,Mean)
  return Cov,Mean

# COMMAND ----------

# MAGIC %md #### Demonstration on a small example

# COMMAND ----------

A=np.array([1,2,3,4,np.nan,5,6])
B=np.array([2,np.nan,1,1,1,1,1])
np.nansum(np.dstack((A,B)),axis=2)

# COMMAND ----------

RDD=sc.parallelize([A,B])

# COMMAND ----------

computeCov(RDD)

# COMMAND ----------

# MAGIC %md #### Demonstration on real data
# MAGIC The following cells demonstrate the use of the code we wrote on the maximal-dayly temperature records for the state of california.

# COMMAND ----------

Ca = sqlContext.sql("select * from weather2 where (state='CA' and measurement = 'TMAX')")

# COMMAND ----------

Ca.first()

# COMMAND ----------

# remove the entries that do not correspond to temperature and devide by 10 so that the result is in centigrates.
RDD_ca=Ca.map(lambda v:np.array(v[3:-1])/10)
RDD_ca.count()

# COMMAND ----------

# Remove entries that have 10 or more nan's
RDD_ca=RDD_ca.filter(lambda row:sum(np.isnan(row))<10)
RDD_ca.count()

# COMMAND ----------

RDD_ca.first()

# COMMAND ----------

UnDef=RDD_ca.map(lambda row:sum(np.isnan(row))).collect()
x = range(365)
fig, ax = plt.subplots()
ax.hist(UnDef,bins=36)
display(fig)

# COMMAND ----------

OUT=computeCov(RDD_ca)
OUT

# COMMAND ----------

[(i,OUT[i].shape) for i in range(len(OUT))]

# COMMAND ----------

(Cov,Mean)=OUT

# COMMAND ----------

Cov[:10,:10]

# COMMAND ----------

from numpy import linalg as LA
w,v=LA.eig(Cov)

# COMMAND ----------

from datetime import date
from numpy import shape
import matplotlib.pyplot as plt
import pylab as py
from pylab import ylabel,grid,title

dates=[date.fromordinal(i) for i in range(1,366)]
def YearlyPlots(T,ttl='',size=(10,7)):
    fig=plt.figure(1,figsize=size,dpi=300)
    fig, ax = plt.subplots(1)
    if shape(T)[0] != 365:
        raise ValueError("First dimension of T should be 365. Shape(T)="+str(shape(T)))
    ax.plot(dates,T);
    # rotate and align the tick labels so they look better
    fig.autofmt_xdate()
    ylabel('temperature')
    grid()
    title(ttl)
    return fig
fig=YearlyPlots(v[:,0:3],'Eigen-Vectors')
display(fig)

# COMMAND ----------

fig=YearlyPlots(Mean,'Mean')
display(fig)

# COMMAND ----------

Var=np.cumsum(w)
Var=Var/Var[-1]
fig, ax = plt.subplots()
#ax.plot(x, Mean, 'r')
ax.plot(x,Var)
ax.grid()
display(fig)

# COMMAND ----------

