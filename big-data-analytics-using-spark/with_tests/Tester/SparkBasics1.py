
import pickle

from Tester import TestRDD, TestNumber, TestList



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

        

def exercise2(pickleFile, func_student, sc):
    f = open( pickleFile )
    data = pickle.load(f)
    f.close()
    
    inputs = [ sc.parallelize(["Spring quarter", "Learning spark basics", "Big data analytics with Spark"]),
               sc.parallelize(["Do not go gentle", "into that good night", "old age should burn and rave"]),
               sc.parallelize(["do","I dare disturb","the universe","there will be time there will be","time"]) ]
    
    for input,case in zip( inputs, data['ex2'] ):
        TestRDD( data=input, func_student=func_student, corAns=case[0], corType=case[1], isNum=False  )
        print ""

    
    
    
def exercise3(pickleFile, func_student, sc):
    f = open( pickleFile )
    data = pickle.load(f)
    f.close()
    
    inputs = [ sc.parallelize([0,4,2,3,1]),
               sc.parallelize([-3.2,-3.233,-3.1,-3.9]),
               sc.parallelize([2,2,2,2,2,2]) ]

    for input,case in zip( inputs, data['ex3'] ):
        TestNumber( data=input, func_student=func_student, corAns=case[0], corType=case[1] )
        print ""


        
def exercise4(pickleFile, func_student, sc):
    f = open( pickleFile )
    data = pickle.load(f)
    f.close()
    
    inputs = [ sc.parallelize(["Spring quarter", "Learning spark basics", "Big data analytics with Spark"]),
               sc.parallelize(["Do not go gentle", "into that good night", "old age should burn and rave"]),
               sc.parallelize(["do","I dare disturb","the universe","there will be time there will be","time"]) ]

    for input,case in zip( inputs, data['ex4'] ):
        TestList( data=input, func_student=func_student, corAns=case[0], corType=case[1], isNum=False )
        print ""


def exercise5(pickleFile, func_student, sc):
    f = open( pickleFile )
    data = pickle.load(f)
    f.close()
    
    inputs = [ sc.parallelize(["Spring quarter", "Learning spark basics", "Big data analytics with Spark"]),
               sc.parallelize(["Do not go gentle", "into that good night", "old age should burn and rave"]),
               sc.parallelize(["do","I dare disturb","the universe","there will be time there will be","time"]) ]

    for input,case in zip( inputs, data['ex5'] ):
        TestList( data=input, func_student=func_student, corAns=case[0], corType=case[1], isNum=False )
        print ""

        
        
        
        
        
        
        
        
        
        
        
        



