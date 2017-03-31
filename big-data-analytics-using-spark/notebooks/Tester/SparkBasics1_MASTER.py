import numpy as np

from Tester import *



###   Exercise 1   ###
def func_ex1_1(A):
    return A.map(np.cos)
def exercise1_1(pickleFile, func_student, sc):    
    inputs= [ [np.pi,0,100000,np.pi*10,np.log(44),-49.4902],  range(39,45) ]
    checkExerciseCorrectAns(inputs, func_ex1_1, func_student, TestRDD, 'ex1_1', sc)    
def gen_exercise1_1(pickleFile, sc):
    inputs= [range(3), range(4,12), range(-4,0) ]
    GenPickle(sc, func_ex1_1, inputs, pickleFile, "ex1_1" )
    
    
###   Exercise 2   ###
def func_ex1_2(stringRDD):
    return stringRDD.map(lambda x: x.split() )
def exercise1_2(testPath, func_student, sc):    
    inputs = [ ["ah", "ah ah ah", "ha ai ifo aoisdmf"],
               ["asdio", "i", "asdfasd","aasdf"],
               ["do asdnj aksdo adsof aos asod oasdf  mkmasdkf maso asdf okm"] ]
    checkExerciseCorrectAns(inputs, func_ex1_2, func_student, TestRDDStr, 'ex1_2', sc)
def gen_exercise1_2(pickleFile, sc):
    inputs = [ ["Spring quarter", "Learning spark basics", "Big data analytics with Spark"],
               ["Do not go gentle", "into that good night", "old age should burn and rave"],
               ["do","I dare disturb","the universe","there will be time there will be","time"] ]
    GenPickle(sc, func_ex1_2, inputs, pickleFile, "ex1_2" )

        
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













