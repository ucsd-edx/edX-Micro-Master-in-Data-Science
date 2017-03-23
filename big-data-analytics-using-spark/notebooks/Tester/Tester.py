import pickle

def GenPickle(func_teacher, inputs, filename, ex, isRDD=True ):
    try:
        f = open(filename,'r')
        toPickle = pickle.load(f)
        f.close()
    except:
        toPickle = {}
    
    exData = []
    for input in inputs:
        tmpAns = func_teacher(input)
        if isRDD:
            exData.append([ tmpAns.collect()  , 
                      type(tmpAns) ]) 
        else:
            exData.append([ tmpAns, 
                      type(tmpAns) ]) 
    toPickle[ex] = exData
    
    f = open(filename,'w')
    pickle.dump(toPickle,f)
    f.close()

    
def very_close(A,B,tol=0.000001):
    ''' Check that the two firs parameters are lists of equal length 
    and then check'''
    if (not type(A)==list and type(B) ==list) or len(A)!=len(B):
        return False
    for i in range(len(A)):
        a=A[i]; b=B[i]
        if abs(a-b)>tol:
            return False
    return True 









def TestList(data, func_student, corAns, corType, isNum=True):
    studentAns = func_student(data)
    
    print "Input: " + str( data.collect() )
    print "Correct Output: " + str(corAns)
    
    try: assert( type(studentAns) == corType )
    except AssertionError as e:
        print "\nError: Incorrect return type. The return type of your function should be: " + str(corType)
        return False
    
    try:
        if isNum:  assert( very_close(studentAns,corAns))
        else:      assert(studentAns == corAns)
    except AssertionError as e:
        print "\nError: Function returned incorrect output"
        print "Your Output: ", studentAns
        return False
    print "Great Job!"
    return False



def TestNumber(data, func_student, corAns, corType):
    studentAns = func_student(data)
    
    print "Input: " + str( data.collect() )
    print "Correct Output: " + str(corAns)
    
    try: assert( type(studentAns) == corType )
    except AssertionError as e:
        print "\nError: Incorrect return type. The return type of your function should be: " + str(corType)
        return False
    
    try: assert( very_close([studentAns],[corAns]) )
    except AssertionError as e:
        print "\nError: Function returned incorrect output"
        print "Your Output: ", studentAns
        return False
    print "Great Job!"
    return False



def TestRDD( data, func_student, corAns, corType, isNum=True ):
    initDebugStr = data.toDebugString()
    studentRDD = func_student(data)
    
    print "Input: " + str( data.collect() )
    print "Correct Output: " + str(corAns)
    
    try: assert( type(studentRDD) == corType )
    except AssertionError as e:
        print "\nError: Incorrect return type. The return type of your function should be: " + str(corType)
        return False
    
    newDebugStr  = studentRDD.toDebugString()
    initDebugStr = ' '.join(initDebugStr.split(' ')[1:])

    try: assert( initDebugStr in newDebugStr )
    except AssertionError as e:
        print "\nError: Did you use only Spark commands? Original RDD is not found in execution path."
        return False

    try:
        if isNum:  assert( very_close(studentRDD.collect(),corAns))
        else:      assert(studentRDD.collect() == corAns)
    except AssertionError as e:
        print "\nError: Function returned incorrect output"
        print "Your Output: ",studentRDD.collect()
        return False
    
    print "Great Job!"
    return True