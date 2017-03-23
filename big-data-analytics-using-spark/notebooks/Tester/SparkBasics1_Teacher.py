import numpy as np

from Tester import TestRDD, TestNumber, TestList


###   Exercise 1   ###
def mapcos(A):
    return A.map(np.cos)
def exercise1(testPath, func, sc):    
    RDDs=[ sc.parallelize([np.pi,0,100000,np.pi*10,np.log(44),-49.4902]), 
           sc.parallelize(range(39,45)) ]
    
    for input in RDDs:
        TestRDD( data=input, func_student=func, corAns=mapcos(input).collect(), corType=type(mapcos(input))  )
        print ""

    
    
###   Exercise 2   ###
def mapwords(stringRDD):
    return stringRDD.map(lambda x: x.split() )
def exercise2(testPath, func, sc):    
    inputs = [ sc.parallelize(["ah", "ah ah ah", "ha ai ifo aoisdmf"]),
               sc.parallelize(["asdio", "i", "asdfasd","aasdf"]),
               sc.parallelize(["do asdnj aksdo adsof aos asod oasdf  mkmasdkf maso asdf okm"]) ]
    for input in inputs:
        TestRDD( data=input, func_student=func, corAns=mapwords(input).collect(), corType=type(mapwords(input)), isNum=False )
        print ""

        
        
###   Exercise 3   ###
def getMax(C):
    return C.reduce(max)
def exercise3(testPath, func, sc):
    inputs = [ sc.parallelize([0,3.49,2.4922,5.24,-24]),
               sc.parallelize([-3.01,-3.20,-3.001,-3.4]),
               sc.parallelize([7]) ]
    for input in inputs:
        TestNumber( data=input, func_student=func, corAns=getMax(input), corType=type(getMax(input)) )
        print ""

        
        
###   Exercise 4   ###
def reducewords(mapwords):
    return mapwords.reduce(lambda x,y: x+" "+y)
def exercise4(testPath, func, sc): 
    inputs = [ sc.parallelize(["ah", "ah ah ah", "ha ai ifo aoisdmf"]),
              sc.parallelize(["asdio", "i", "asdfasd","aasdf"]),
              sc.parallelize(["do asdnj aksdo adsof aos asod oasdf  mkmasdkf maso asdf okm"]) ]
    for input in inputs:
        TestList( data=input, func_student=func, corAns=reducewords(input), 
                   corType=type(reducewords(input)), isNum=False )
        print ""



###   Exercise 5   ###
def exercise5(testPath, func, sc):  
    inputs = [ sc.parallelize([[3,4],[2,1],[7,9]]),
               sc.parallelize([[-222],[-10,-33],[0,-5]]),
               sc.parallelize([[3.2,3.3,3.1,3.9],[-3.95],[3.4,3.7]]) ]
    
    def maxFunc(x,y):
        return [max(x+y)]
    def func_teacher(A):
        return A.reduce(lambda x,y: [max(x+y)])
    def func_student(A):
        return A.reduce(func)
    
    for input in inputs:
        corAns  = func_teacher(input)
        corType = type(func_teacher(input))
        
        TestList( data=input, func_student=func_student, corAns=corAns, corType=corType, isNum=True ) 
        print ""












