import csv
import re
import os
import sys

def format(input, keyword):
    
    input = re.sub('print', '', input)
    
    idx = input.find('=')
    idx2 = input.find(keyword)
    if idx > 0 and idx < idx2:
        program = "output" + input[idx:]
    else:
        program = "output=" + input
    return program

def runAndCheck(program, answer):
    
    if os.path.exists('.temp'):
        os.remove('.temp')
    if os.path.exists('run.py'):
        os.remove('run.py')
    
    CODE = ''
    CODE = CODE + 'x = nums = input = L = [1,2,3,4,5]\n'
    CODE = CODE + 'a = 3\n'
    CODE = CODE + program + '\n'
    CODE = CODE + answer + '\n'
    CODE = CODE + 'res = (output == output2)\n'
    CODE = CODE + 'print res\n'

    file_object = open('run.py', 'w')
    file_object.write(CODE)
    file_object.close( )

    command = 'python run.py > .temp';
    try:
        os.system(command)
    except:
        return False

    if not os.path.exists('.temp'):
        return False
    checkfile = open('.temp', 'r')
    tf = checkfile.read()[:-1]
    checkfile.close( )
    if tf == 'True':
        return True
    return False


def checkq1(student, ans):
    return student == ans

def checkq2(student, ans):
    return student == ans

def checkq3(student, ans):
    return student == ans

def checkmr1(mr1):
    if 'reduce' not in mr1:
        return False
    program = format(mr1, 'reduce')
    #print program
    answer = 'output2 = reduce( lambda x , y: x if x>y  else y, L )'
    return runAndCheck(program, answer)

def checkmr2(mr2):
    if 'reduce' not in mr2:
        return False
    program = format(mr2, 'reduce')
    answer = 'output2 = reduce(lambda x, y : x + y, map (lambda x: x * x, L))'
    return runAndCheck(program, answer)

def checkmr3(mr3):

    if 'reduce' in mr3:
        program = format(mr3, 'reduce')
    elif 'filter' in mr3:
        program = format(mr3, 'filter')
    elif 'map' in mr3:
        program = format(mr3, 'map')
    else:
        return False

    answer = 'output2 = filter(lambda x: x <=a, L)'
    return runAndCheck(program, answer)



'''
q1, q2, q3, mr1, mr2, mr3 are 6 quizs.
name, pid and email are important infomation.
'''

if len(sys.argv) < 2:
    print "usage : python grade.py input.csv"
    exit(-1)

reader = csv.reader(open(sys.argv[1]))

resultfile = open('results.csv', 'w')
fieldnames = ['name', 'pid', 'email', 'q1', 'q2', 'q3', 'mr1', 'mr2', 'mr3']
writer = csv.DictWriter(resultfile, fieldnames=fieldnames)
writer.writeheader()
for Timestamp, Course, q1, q2, q3, experience, mr1, hadoop, academic_year, name, pid, email, mr2, mr3 in reader:
    if '2016' in Timestamp:
        res1 = checkq1(q1, '4n')
        res2 = checkq2(q2, '9')
        res3 = checkq3(q3, 'Dependent and uncorrelated')
        res4 = checkmr1(mr1)
        res5 = checkmr2(mr2)
        res6 = checkmr3(mr3)
        if (not (res4 and res5 and res6)):
            print 'Exception: '
            print ','.join([Timestamp, Course, q1, q2, q3, experience, mr1, hadoop, academic_year, name, pid, email, mr2, mr3])
            

        writer.writerow({'name': name, 'pid': pid, 'email':email, 'q1':res1, 'q2':res2, 'q3':res3, 'mr1':res4, 'mr2':res5, 'mr3':res6})

        if os.path.exists('.temp'):
            os.remove('.temp')
        if os.path.exists('run.py'):
            os.remove('run.py')
