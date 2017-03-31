import pickle

def GenPickle(func_teacher, inputs, filename, ex, twoInputs=False ):
    try:
        f = open(filename,'r')
        toPickle = pickle.load(f)
        f.close()
    except:
        toPickle = {}
    
    exData = []
    for input in inputs:
        if twoInputs:
            tmpAns = func_teacher(input[0], input[1])
        else:
            tmpAns = func_teacher(input)

        exData.append([ tmpAns, 
                      type(tmpAns) ]) 
    toPickle[ex] = {'inputs': inputs, 'outputs':exData}
    
    f = open(filename,'w')
    pickle.dump(toPickle,f)
    f.close()

def TestList(data, func_student, corAns, corType, two_inputs=False):
    
    if two_inputs:
        studentAns = func_student(data[0], data[1])
    else:
        studentAns = func_student(data[0])
    
    print "Input: " + str(data)
    print "Correct Output: " + str(corAns)
    
    try: assert( type(studentAns) == corType )
    except AssertionError as e:
        print "\nError: Incorrect return type. The return type of your function should be: " + str(corType)
        return False
    
    try:
        assert(studentAns == corAns)
    except AssertionError as e:
        print "\nError: Function returned incorrect output"
        print "Your Output: ", studentAns
        return False
    print "Great Job!"
    return False

def getPickledData(pickleFileName):
    f = open( pickleFileName )
    data = pickle.load(f)
    f.close()
    return data

def checkExerciseFromPickle(pickleFile, func_student, TestFunction, exerciseNumber, twoInputs=False):
    data = getPickledData(pickleFile)
    inputs = data[exerciseNumber]['inputs']
    outputs = data[exerciseNumber]['outputs']
    checkExercise(inputs, outputs, func_student, TestFunction, exerciseNumber, twoInputs=twoInputs)

def checkExercise(inputs, outputs, func_student, TestFunction, exerciseNumber, twoInputs=False):
    for input,case in zip( inputs, outputs ):
        TestFunction( data=inputs, func_student=func_student, corAns=case[0], corType=case[1], twoInputs=True) 