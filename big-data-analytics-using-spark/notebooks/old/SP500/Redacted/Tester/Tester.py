import pickle


def GenPickle(func_teacher, inputs, filename, ex, isRDD=False,multiInputs=False ):
    try:
        f = open(filename,'r')
        toPickle = pickle.load(f)
        f.close()
    except:
        toPickle = {}
    
    exData = []
    for input in inputs:
        if multiInputs:
            tmpAns = func_teacher(input[0],input[1])
        else:
            tmpAns = func_teacher(input)
        if isRDD:
            exData.append([ tmpAns.collect()  , 
                      type(tmpAns) ]) 
        else:
            exData.append([ tmpAns, 
                      type(tmpAns) ]) 
    toPickle[ex] = {'inputs': inputs, 'outputs':exData}
    
    f = open(filename,'w')
    pickle.dump(toPickle,f)
    f.close()


def TestNumber(input, func_student, corAns, corType, multiInputs=True):
    
    if multiInputs == True:
        studentAns = func_student(input[0], input[1])
    else:
        studentAns = func_student(input[0])
    
    print "Input: " + str(input[1])
    print "Correct Output: " + str(corAns)
    
    try:
        assert(abs(studentAns - corAns) < 0.3)
    except AssertionError as e:
        print "\nError: Function returned incorrect output"
        print "Your Output: ", studentAns
        return False
    print "Great Job!"
    return True


def getPickledData(pickleFileName):
    f = open( pickleFileName )
    data = pickle.load(f)
    f.close()
    return data

def checkExercise(inputs, outputs, func_student, TestFunction, exerciseNumber, multiInputs=False):
    for input,case in zip( inputs, outputs ):
        if multiInputs:
            input = [input[0], input[1]]
        else:
            input = input
        noError= TestFunction( input, func_student=func_student, corAns=case[0], corType=case[1],multiInputs=True)
        if noError == False: raise AssertionError('Your Answer is Incorrect') 
        print 

def checkExerciseFromPickle(pickleFile, func_student, TestFunction, exerciseNumber, multiInputs=True):
    data = getPickledData(pickleFile)
    inputs = data[exerciseNumber]['inputs']
    outputs = data[exerciseNumber]['outputs']
    checkExercise(inputs, outputs, func_student, TestFunction, exerciseNumber, multiInputs=multiInputs)
    
        
def checkExerciseCorrectAns(inputs, func_teacher, func_student, TestFunction, exerciseNumber, 
                            multiInputs=True,isRDD=False):
    outputs = []
    for input in inputs:
        if multiInputs:
            tmpAns = func_teacher(input[0], input[1])
        else:
            tmpAns = func_teacher(input)
        if isRDD:
            ty = type(tmpAns)
            tmpAns = tmpAns.collect()
            outputs.append([tmpAns,ty])
        else:
            outputs.append([tmpAns, type(tmpAns)])
    checkExercise(inputs, outputs, func_student, TestFunction, exerciseNumber, multiInputs=multiInputs)