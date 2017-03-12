
import pickle

from Tester import TestRDD



def exercise1(testPath, func_student, sc):
    
    f = open(testPath +"/SparkBasic1.pkl" )
    data = pickle.load(f)
    f.close()
    
    RDDs=[sc.parallelize(range(3)),
         sc.parallelize(range(4,12))   
        ]
    
    for input,case in zip( RDDs, data['ex1'] ):
        TestRDD( data=input, func_student=func_student, corAns=case[0], corType=case[1]  )
        print ""

    
    








