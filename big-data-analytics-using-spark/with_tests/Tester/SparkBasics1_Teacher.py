import numpy as np

from Tester import TestRDD




###   Exercise 1  ###
def func_ex1(A):
    return A.map(np.cos)

def exercise1(testPath, func, sc):
    RDDs=[ sc.parallelize([np.pi,0,100000,np.pi*10,np.log(44),-49.4902]), 
           sc.parallelize(range(39,45)) ]
    for input in RDDs:
        TestRDD( data=input, func_student=func, corAns=func_ex1(input).collect(), corType=type(func_ex1(input))  )
        print ""

    
    
###   Exercise 2  ###
def func_ex2(A):
    return A.map(np.cos)

def exercise2(testPath, func, sc):
    RDDs=[ sc.parallelize([np.pi,0,100000,np.pi*10,np.log(44),-49.4902]), 
           sc.parallelize(range(39,45)) ]
    for input in RDDs:
        TestRDD( data=input, func_student=func, corAns=func_ex1(input).collect(), corType=type(func_ex1(input))  )
        print ""

    
















