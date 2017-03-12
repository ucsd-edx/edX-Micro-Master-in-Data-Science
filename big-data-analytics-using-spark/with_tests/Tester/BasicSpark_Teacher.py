
import pickle

from Tester import TestRDD





def GenPickle(func_teacher, inputs, filename, ex ):
    
    try:
        f = open(filename,'r')
        toPickle = pickle.load(f)
        f.close()
    except:
        toPickle = {}
    
    exData = []
    for input in inputs:
        exData.append([ func_teacher(input).collect()  , 
                      type(func_teacher(input)) ]) 
    toPickle[ex] = exData
    
    f = open(filename,'w')
    pickle.dump(toPickle,f)
    f.close()

    

def corFunc_ex1(A):
    import numpy as np
    return A.map(np.cos)



def exercise1(testPath, func_student, sc):
    RDDs=[ sc.parallelize(range(4)), 
          sc.parallelize(range(4,12)) ]

    for input in RDDs:
        TestRDD( data=input, func_student=func_student, corAns=corFunc_ex1(input).collect(), corType=type(corFunc_ex1(input))  )
        print ""

    
    

















