import pickle

from Tester2 import *

def checkExerciseFromPickle(pickleFile, func_student, TestFunction, exerciseNumber, sc, twoInputs=False):
    data = getPickledData(pickleFile)
    inputs = data[exerciseNumber]['inputs']
    outputs = data[exerciseNumber]['outputs']
    checkExercise(inputs, outputs, func_student, TestFunction, exerciseNumber, sc,twoInputs=twoInputs)
    
def exercise3_1(pickleFile, func_student, sc):
    checkExerciseFromPickle(pickleFile, func_student,TestNumber,'ex3_1',sc)
def exercise3_2(pickleFile, func_student, sc):
    checkExerciseFromPickle(pickleFile, func_student,TestRDD,'ex3_2',sc)
def exercise3_3(pickleFile, func_student, sc):
    checkExerciseFromPickle(pickleFile, func_student,TestRDDStr,'ex3_3',sc)
def exercise3_4(pickleFile, func_student, sc):
    checkExerciseFromPickle(pickleFile, func_student,TestRDD,'ex3_4',sc)
def exercise3_5(pickleFile, func_student, sc):
    checkExerciseFromPickle(pickleFile, func_student,TestRDDStr2,'ex3_5',sc, twoInputs=True)
def exercise3_6(pickleFile, func_student, sc):
    checkExerciseFromPickle(pickleFile, func_student,TestRDDStr2,'ex3_6',sc, twoInputs=True)
def exercise3_7(pickleFile, func_student, sc):
    checkExerciseFromPickle(pickleFile, func_student,TestRDDStr2,'ex3_7',sc, twoInputs=True)
def exercise3_8(pickleFile, func_student, sc):
    checkExerciseFromPickle(pickleFile, func_student,TestRDDStr2,'ex3_8',sc, twoInputs=True)