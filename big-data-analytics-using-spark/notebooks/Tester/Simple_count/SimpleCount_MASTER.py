from basic_tester import *
import re 

text = ["Coordinating conjunctions are useful for connecting sentences, but compound sentences often are overused.", "While     coordinating conjunctions can indicate some type of relationship between the two independent clauses in the sentence, they sometimes do not indicate much of a relationship"]

def checkExerciseCorrectAns(inputs, func_teacher, func_student, TestFunction, exerciseNumber,
                            multiInputs=False):
    outputs = []
    for input in inputs:
        if multiInputs == True:
            print len(input)
            tmpAns = eval(function_string(input, "func_teacher"))
        else:
            tmpAns = func_teacher(input)

        outputs.append([tmpAns, type(tmpAns)])
    checkExercise(inputs, outputs, func_student, TestFunction, exerciseNumber, multiInputs=multiInputs)

def preprocess(text):
    result = []
    for line in text:
        line = line.strip()
        if line != '':
            line = re.sub("[^0-9a-zA-Z ]", " ", line)
            line = line.lower()
            result.append(line)
    return result

def func_ex0_1(text, k):
    result=[]
    for sentence in text:
        word_list = sentence.split()
        for i in xrange(len(word_list)-k):
            result.append(word_list[i:i+k])
    return result

def exercise0_1(pickleFile, func_student):
    input_file = '../../Data/Moby-Dick.txt'
    f = open(input_file, "r")
    text = preprocess( f.readlines() )
    inputs = [ [text,3] ]
    checkExerciseCorrectAns(inputs, func_ex0_1, func_student, TestList, 'ex0_1', multiInputs=True)
    
def gen_exercise0_1(pickleFile):
    input_text = preprocess(text)
    inputs = [[input_text, 2]]
    GenPickle(func_ex0_1, inputs, pickleFile, "ex0_1", multiInputs=True)
    

def func_ex0_2(kmers):
    result= dict()
    print len(kmers)
    print kmers[0]
    for kmer in kmers:
        kmer_string = " ".join(kmer)
        if kmer_string not in result:
            result[kmer_string] = 0
        result[kmer_string] += 1
    return result

def exercise0_2(pickleFile, func_student):
    input_file = '../../Data/Moby-Dick.txt'
    f = open(input_file, "r")
    text = preprocess(f.readlines())
    kmers = func_ex0_1(text, 3)
    inputs = [kmers]
    checkExerciseCorrectAns(inputs, func_ex0_2, func_student, TestList, 'ex0_2')
    
def gen_exercise0_2(pickleFile):
    input_text = preprocess(text)
    inputs = [func_ex0_1(input_text, 2)]
    GenPickle(func_ex0_2, inputs, pickleFile, "ex0_2")

    
def func_ex0_3(count_kmers):
    return sorted(count_kmers.items(), key=lambda x: (-x[1], x[0]))

def exercise0_3(pickleFile, func_student):
    input_file = '../../Data/Moby-Dick.txt'
    f = open(input_file, "r")
    text = preprocess(f.readlines())
    kmers = func_ex0_1(text, 3)
    count_kmers = func_ex0_2(kmers)
    inputs = [count_kmers]
    checkExerciseCorrectAns(inputs, func_ex0_3, func_student, TestList, 'ex0_3')
    
def gen_exercise0_3(pickleFile):
    input_text = preprocess(text)
    kmers = func_ex0_1(input_text, 2)
    inputs = [func_ex0_2(kmers)]
    GenPickle(func_ex0_3, inputs, pickleFile, "ex0_3")
    
    
def func_ex0_4(text, n, k):
    kmers = func_ex0_1(text, k)
    count_kmers = func_ex0_2(kmers)
    sorted_counts = func_ex0_3(count_kmers)
    return sorted_counts[0:n]

def exercise0_4(pickleFile, func_student):
    input_file = '../../Data/Moby-Dick.txt'
    f = open(input_file, "r")
    text = preprocess(f.readlines())
    inputs = [[text, 5, 3]]
    checkExerciseCorrectAns(inputs, func_ex0_4, func_student, TestList, 'ex0_4', multiInputs=True)
    
def gen_exercise0_4(pickleFile):
    input_text = preprocess(text)
    inputs = [[input_text, 5, 2]]
    GenPickle(func_ex0_4, inputs, pickleFile, "ex0_4", multiInputs=True)