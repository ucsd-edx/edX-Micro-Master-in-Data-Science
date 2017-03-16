import pickle

from Tester import TestRDD,TestNumber

###   Exercise 4  ###
def exercise4(pickleFile, func_student, sc):
    f = open( pickleFile )
    data = pickle.load(f)
    f.close()
    
    inputs= [ sc.parallelize([[3,4],[2,1],[7,9]]),sc.parallelize([[3,42,12,4],[6,0,-1],[32,31,2,52,3]])   ]
    
    for input,case in zip( inputs, data['ex4'] ):
        TestNumber( data=input, func_student=func_student, corAns=case[0], corType=case[1]  )
        print ""

###   Exercise 5  ###
def exercise5(pickleFile, func_student, sc):
    f = open( pickleFile )
    data = pickle.load(f)
    f.close()
    
    inputs_1 = [ sc.parallelize(range(3)),
              sc.parallelize(range(4,12)), 
              sc.parallelize(range(-4,0)),
              sc.parallelize([0,2,1])
            ]
    inputs_2 = [sc.parallelize(['this','is','the','best','mac','ever']),
                sc.parallelize(['Hasta', 'la', 'vista', 'baby']),
                sc.parallelize(['A','long','time', 'ago', 'in', 'a', 'galaxy', 'far', 'far', 'away'])
               ]
    
    for input,case in zip( inputs, data['ex5'] ):
        TestRDD( data=input, func_student=func_student, corAns=case[0], corType=case[1]  )
        print ""
        
###   Exercise 4  ###
def exercise6(pickleFile, func_student, sc):
    f = open( pickleFile )
    data = pickle.load(f)
    f.close()
    
    inputs= [ sc.parallelize(range(3)),
              sc.parallelize([2,3,5])]
    
    for input,case in zip( inputs, data['ex6'] ):
        TestRDD( data=input, func_student=func_student, corAns=case[0], corType=case[1]  )
        print ""