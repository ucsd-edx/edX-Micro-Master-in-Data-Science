import numpy as np
from Tester import *

def func_ex3_1(A):
    return A.map(max).reduce(lambda x,y:x+y)

def exercise3_1(pickleFile, func_student, sc):
    inputs=[ [[3,4],[2,1],[7,9]], [range(3,40,4),range(7,30,2),range(1,100,50)],
         [[3,42,12,4],[6,0,-1],[32,31,2,52,3]], [[5,2,1,28,21,54],range(1,1000,4),np.random.randint(3,1000,size=37)] ]
    checkExerciseCorrectAns(inputs, func_ex3_1, func_student, TestNumber, 'ex3_1', sc,isRDD=False)
    
def gen_exercise3_1(pickleFile, sc):
    inputs= [ [[3,4],[2,1],[7,9]], [[3,42,12,4],[6,0,-1],[32,31,2,52,3]] ]
    GenPickle(sc, func_ex3_1, inputs, pickleFile, "ex3_1",isRDD=False )

def func_ex3_2(A):
    return A.filter(lambda x: np.cos(x) > 0)

def exercise3_2(pickleFile, func_student, sc):
    inputs=[ [np.pi,0,100000,np.pi*10,np.log(44),-49.4902], 
           range(39,45), np.random.randint(-1000,1000,size=50), np.random.randint(-1000,1000,size=100)]
    checkExerciseCorrectAns(inputs, func_ex3_2, func_student, TestRDD, 'ex3_2', sc)

def gen_exercise3_2(pickleFile, sc):
    inputs = [ range(3), range(4,12), range(-4,0), [0,2,1] ]
    GenPickle(sc, func_ex3_2, inputs, pickleFile, "ex3_2")
    
def func_ex3_3(A):
    return A.filter(lambda w: len(w) >= 4)

def exercise3_3(pickleFile, func_student, sc):
        inputs = [['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit.', 'Morbi', 'posuere', 'suscipit', 'nisl,', 'nec', 'elementum', 'ex', 'ultricies', 'eu.', 'Vestibulum', 'tincidunt', 'metus', 'vel', 'luctus', 'gravida.', 'Suspendisse', 'potenti.', 'Sed', 'imperdiet,', 'ligula', 'ac', 'viverra', 'eleifend,', 'libero', 'velit', 'condimentum', 'enim,', 'sed', 'porta', 'elit', 'magna', 'sit', 'amet', 'tellus.', 'Aliquam', 'et', 'volutpat', 'diam.', 'Quisque', 'cursus', 'luctus', 'dolor', 'eget', 'pretium.', 'Vivamus', 'sollicitudin', 'elementum', 'quam,', 'eu', 'interdum', 'nisl', 'varius', 'ac.', 'Class', 'aptent', 'taciti', 'sociosqu'], ['Promotion', 'an', 'ourselves', 'up', 'otherwise', 'my.', 'High', 'what', 'each', 'snug', 'rich', 'far', 'yet', 'easy.', 'In', 'companions', 'inhabiting', 'mr', 'principles'], ['at', 'insensible', 'do.', 'Heard', 'their', 'sex', 'hoped', 'enjoy', 'vexed', 'child', 'for.', 'Prosperous', 'so', 'occasional', 'assistance', 'it', 'discovered', 'especially', 'no.', 'Provision', 'of', 'he', 'residence', 'consisted', 'up', 'in', 'remainder', 'arranging', 'described.', 'Conveying', 'has', 'concealed', 'necessary', 'furnished', 'bed', 'zealously', 'immediate', 'get', 'but'],['Praesent', 'id', 'orci', 'id', 'nunc', 'euismod', 'sollicitudin', 'quis', 'in', 'lectus.', 'Ut', 'pharetra', 'fringilla', 'lectus', 'a', 'gravida.', 'Vestibulum', 'sodales', 'mauris', 'tellus,', 'at', 'placerat', 'odio', 'euismod', 'feugiat.', 'Pellentesque', 'egestas', 'fringilla', 'congue.', 'Sed', 'vel', 'lectus', 'condimentum,', 'maximus', 'nisi', 'vel,', 'porttitor', 'mi.', 'Nulla', 'tempor', 'arcu', 'ultrices', 'nisl', 'sagittis,', 'non', 'consectetur', 'justo', 'egestas.', 'Duis', 'lacinia,', 'est', 'sit', 'amet', 'efficitur', 'commodo,', 'ligula', 'enim', 'eleifend', 'eros,', 'et', 'venenatis', 'urna', 'magna', 'vitae', 'mauris']]
        checkExerciseCorrectAns(inputs, func_ex3_3, func_student, TestRDDStr, 'ex3_3', sc)

def gen_exercise3_3(pickleFile, sc):
    inputs = [ ['this','is','the','best','mac','ever'],['Hasta', 'la', 'vista', 'baby'], ['A','long','time', 'ago', 'in', 'a', 'galaxy', 'far', 'far', 'away'] ]
    GenPickle(sc, func_ex3_3, inputs, pickleFile, "ex3_3")

def func_ex3_4(A):
    return A.flatMap(lambda x:range(1,x+1))

def exercise3_4(pickleFile, func_student, sc):
    inputs = [np.random.randint(1,10,size=10),np.random.randint(1,5,size=20), 
              np.random.randint(1,20,size=50), np.random.randint(5,10,size=30)]
    checkExerciseCorrectAns(inputs, func_ex3_4, func_student, TestRDD, 'ex3_4', sc)
def gen_exercise3_4(pickleFile, sc):
    inputs=[ [2,3,5],[5,3,1],range(1,6) ]
    GenPickle(sc, func_ex3_4, inputs, pickleFile, "ex3_4")
        
def func_ex3_5(RDD1,RDD2):
    return RDD1.flatMap(lambda x:x.split()).union(RDD2.flatMap(lambda x:x.split()))
def func_ex3_6(RDD1,RDD2):
    return RDD1.flatMap(lambda x:x.split()).intersection(RDD2.flatMap(lambda x:x.split()))
def func_ex3_7(RDD1,RDD2):
    return RDD1.flatMap(lambda x:x.split()).subtract(RDD2.flatMap(lambda x:x.split()))
def func_ex3_8(RDD1,RDD2):
    return RDD1.flatMap(lambda x:x.split()).cartesian(RDD2.flatMap(lambda x:x.split()))

def exercise3_5(pickleFile, func_student, sc):
    inputs = [ [ ["machine learning","neural networks","big data"],["computer networks","big systems","scalable"] ] ]
    checkExerciseCorrectAns(inputs, func_ex3_5, func_student, TestRDDStr2, 'ex3_5', sc, twoInputs=True)
def exercise3_6(pickleFile, func_student, sc):
    inputs = [ [ ["machine learning","neural networks","big data"],["computer networks","big systems","scalable"] ] ]
    checkExerciseCorrectAns(inputs, func_ex3_6, func_student, TestRDDStr2, 'ex3_6', sc, twoInputs=True)
def exercise3_7(pickleFile, func_student, sc):
    inputs = [ [ ["machine learning","neural networks","big data"],["computer networks","big systems","scalable"] ] ]
    checkExerciseCorrectAns(inputs, func_ex3_7, func_student, TestRDDStr2, 'ex3_7', sc, twoInputs=True)
def exercise3_8(pickleFile, func_student, sc):
    inputs = [ [ ["machine learning","neural networks","big data"],["computer networks","big systems","scalable"] ] ]
    checkExerciseCorrectAns(inputs, func_ex3_8, func_student, TestRDDStr2, 'ex3_8', sc, twoInputs=True)
    
def gen_exercise3_5(pickleFile, sc):
    inputs = [ [["spark basics", "big data analysis", "spring"],["spark using pyspark", "big data"]] ]
    GenPickle(sc, func_ex3_5, inputs, pickleFile, "ex3_5", twoInputs=True)
def gen_exercise3_6(pickleFile, sc):
    inputs = [ [["spark basics", "big data analysis", "spring"],["spark using pyspark", "big data"]] ]
    GenPickle(sc, func_ex3_6, inputs, pickleFile, "ex3_6", twoInputs=True)
def gen_exercise3_7(pickleFile, sc):
    inputs = [ [["spark basics", "big data analysis", "spring"],["spark using pyspark", "big data"]] ]
    GenPickle(sc, func_ex3_7, inputs, pickleFile, "ex3_7", twoInputs=True)
def gen_exercise3_8(pickleFile, sc):
    inputs = [ [["spark basics", "big data analysis", "spring"],["spark using pyspark", "big data"]] ]
    GenPickle(sc, func_ex3_8, inputs, pickleFile, "ex3_8", twoInputs=True)