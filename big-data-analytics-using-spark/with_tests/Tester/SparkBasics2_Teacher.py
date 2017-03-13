import numpy as np
from Tester import TestRDD,TestNumber

###   Exercise 4  ###
def func_ex4(A):
    return A.map(max).reduce(lambda x,y:x+y)

def exercise4(testPath, func, sc):
    RDDs=[ sc.parallelize([[3,4],[2,1],[7,9]]), sc.parallelize([range(3,40,4),range(7,30,2),range(1,100,50)]),
         sc.parallelize([[3,42,12,4],[6,0,-1],[32,31,2,52,3]])]
    for input in RDDs:
        tmpAns = func_ex4(input)
        TestNumber( data=input, func_student=func, corAns=tmpAns, corType=type(tmpAns)  )
        print ""

###   Exercise 5  ###
def func_ex5_1(A):
    return A.filter(lambda x: np.cos(x) > 0)

def func_ex5_2(A):
    return A.filter(lambda w: len(w) >= 4)

def exercise5(testPath, func, sc):
    RDDs_1=[ sc.parallelize([np.pi,0,100000,np.pi*10,np.log(44),-49.4902]), 
           sc.parallelize(range(39,45)), sc.parallelize([0,2,1]),sc.parallelize(range(3)),
              sc.parallelize(range(4,12)),sc.parallelize(range(-4,0)) ]
    RDDs_2 = [
        sc.parallelize(['this','is','the','best','mac','ever']), 
        sc.parallelize(['this','is','a','very','good','cup'])
         ]
    for input in RDDs:
        tmpAns = func_ex5_1(input)
        TestRDD( data=input, func_student=func, corAns=tmpAns.collect(), corType=type(tmpAns)  )
        print ""
        
def func_ex6(A):
    return A.flatMap(lambda x:range(1,x+1))

def exercise6(testPath, func, sc):
    RDDs=[ sc.parallelize([2,3,5]),sc.parallelize([5,3,1]),sc.parallelize(range(1,6)) ]
    for input in RDDs:
        TestRDD( data=input, func_student=func, corAns=func_ex6(input).collect(), corType=type(func_ex6(input))  )
        print ""
        
def func_ex7_1(RDD1,RDD2):
    return RDD1.union(RDD2)
def func_ex7_2(RDD1,RDD2):
    return RDD1.intersection(RDD2)
def func_ex7_3(RDD1,RDD2):
    return RDD1.subtract(RDD2)
def func_ex7_4(RDD1,RDD2):
    return RDD1.cartesian(RDD2)

def exercise7(testPath, func, sc):
    RDDs=[ sc.parallelize([np.pi,0,100000,np.pi*10,np.log(44),-49.4902]), 
           sc.parallelize(range(39,45)), sc.parallelize([[3,4],[2,1],[7,9]]) ]
    for input in RDDs:
        TestRDD( data=input, func_student=func, corAns=func_ex7_1(input).collect(), corType=type(func_ex7_1(input))  )
        print ""