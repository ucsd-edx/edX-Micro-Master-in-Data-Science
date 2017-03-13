
import pickle

from Tester import TestRDD


###   Exercise 1  ###
def exercise1(pickleFile, func_student, sc):
    f = open( pickleFile )
    data = pickle.load(f)
    f.close()
    
    inputs= [ sc.parallelize(range(3)),
              sc.parallelize(range(4,12)), 
              sc.parallelize(range(-4,0))   ]
    
    for input,case in zip( inputs, data['ex1'] ):
        TestRDD( data=input, func_student=func_student, corAns=case[0], corType=case[1]  )
        print ""

        
###   Exercise 2  ###
def exercise2(pickleFile, func_student, sc):
    f = open( pickleFile )
    data = pickle.load(f)
    f.close()
    
    inputs= [ sc.parallelize(range(3)),
              sc.parallelize(range(4,12)), 
              sc.parallelize(range(-4,0))   ]
    
    for input,case in zip( inputs, data['ex1'] ):
        TestRDD( data=input, func_student=func_student, corAns=case[0], corType=case[1]  )
        print ""

    
    








