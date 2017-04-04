# Script to test hint class
# Run this script with the folder that contains all the hint class files,
# it will check if a hint class is valid for the attempts
#
# NOTICE: Name of the hint class has to be the same as the hint class file
#
# Name: Zeng Fan / Zhen Zhai
# Date: Oct 5, 2016
from hint_class_helpers.make_params import make_params
from hint_class_helpers.find_matches import find_matches
from hint_class_helpers.get_numerical_answer import get_numerical_answer
import pickle
import sys
from pydoc import locate
import os
import traceback
from os import listdir
from os.path import isfile, join, expanduser, splitext
import json

def check_final_answer(params,tol = 1+1e-3):
    att_tree = params['att_tree']
    ans_tree = params['ans_tree']
    att_result = get_numerical_answer(att_tree)
    ans_result = get_numerical_answer(ans_tree)
    if ans_result != 0:
        ratio = att_result/ans_result
    else:
        if att_result == 0:
            ratio = 1
        else:
            ratio = 0

    if ratio < tol and ratio > (1/tol):
        return True
    else:
        return False


def get_all_classes(path):
    'Read first universal hint functions'''
    uni_folder_name = 'hint_class/first_Universal'
    first_universal_hint_files = []
    for f in listdir(expanduser(uni_folder_name)):
        if isfile(join(expanduser(uni_folder_name), f)) and \
                f.endswith('.py') and f != '__init__.py':
            first_universal_hint_files.append(splitext(f)[0])

    'Read hint class'''
    folder_name = path
    hint_classes = []
    for f in listdir(expanduser(folder_name)):
        if isfile(join(expanduser(folder_name), f)) and \
                f.endswith('.py') and f != '__init__.py' and f != 'template.py':
            hint_classes.append(splitext(f)[0])

    'Read last universal hint functions'''
    l_uni_folder_name = 'hint_class/last_Universal'
    last_universal_hint_files = []
    for f in listdir(expanduser(l_uni_folder_name)):
        if isfile(join(expanduser(l_uni_folder_name), f)) and \
                f.endswith('.py') and f != '__init__.py':
            last_universal_hint_files.append(splitext(f)[0])


    return first_universal_hint_files, hint_classes, last_universal_hint_files


def single_hint_test(path, new_class_name, testdata):
    first_u_hints, hint_classes, last_u_hints = get_all_classes(path)
   
    try:
        hint_classes.remove(new_class_name)
    except:
        sys.exit('ERROR: Cannot find the input class name')
    
    i = 1

    # Try new hint
    folder_name = path
    package_name = folder_name.replace('/', '.')
    class_address = package_name + "." + new_class_name + "." + new_class_name
    try:
        cond_ClassName = locate(class_address)
    except:
        traceback.print_exc()
        sys.exit("ERROR: syntax error in hint class {0}.".format(class_address))

    try:
        cond_hint_instance = cond_ClassName()
    except TypeError:
        sys.exit("ERROR: name of the HINT CLASS has to be the same as the name of the FILE {0}.".format(cond_ClassName))

    try:
        pro_list = cond_hint_instance.get_problems()
    except:
        sys.exit("ERROR: no function get_problems in hint class {0}.".format(class_address))

    all_pros = json.loads(open("../problem_database/problems_mapping.json").read())
    for p in pro_list:
        if not '/part' in p:
            sys.exit("ERROR: please include part id in the get_problems.")
        par_index = p.index('/part')
        if not any(p[:par_index] == pros[1] for pros in all_pros.items()):
            sys.exit("ERROR: wrong problem name in get_problems.")



    for test in testdata:
        attempt = test['attempt']
        answer = test['answer']
        if not attempt:
            print "Attempt is empty"
            continue

        params = make_params(answer,attempt)

        if params == {}:
            continue

        match = find_matches(params)
        ans_tree = params['ans_tree'][0]
        if match==ans_tree or check_final_answer(params):
            #print "Correct answer!"
            continue

        hint = ""
        # try first universal hints
        package_name = 'hint_class.first_Universal'
        if len(params['att_tree']) > 1:
            for f_name in first_u_hints:
                f_address = package_name + "." + f_name
                try:
                    uni_f = locate(f_address)
                except:
                    #traceback.print_exc()
                    sys.exit("ERROR: syntax error in universal hint function {0}.".format(f_address))

                try:
                    hint = uni_f.check_attempt(params)
                except:
                    #traceback.print_exc()
                    sys.exit("ERROR: syntax error in universal hint function {0}.".format(f_address))

                if hint:
                    break
            if hint:
                continue

        # try conditional hints
        folder_name = path
        package_name = folder_name.replace('/', '.')
        for class_name in hint_classes:
            class_address = package_name + "." + class_name + "." + class_name
            try:
                ClassName = locate(class_address)
            except:
                traceback.print_exc()
                sys.exit("ERROR: syntax error in HINT CLASS {0}.".format(ClassName))

            try:
                hint_instance = ClassName()
            except TypeError:
                sys.exit("ERROR: name of the HINT CLASS has to be the same as the name of the FILE {0}.".format(class_address))

            try:
                hint, hint_ans = hint_instance.check_attempt(params)
            except:
                traceback.print_exc()
                sys.exit("ERROR: syntax error in HINT CLASS {0}.".format(class_address))

            if hint and not hint_ans:
                sys.exit("ERROR: you can't leave the second returned string empty. Please ask a question in your hint.")
            
            if len(hint) > 210:
                sys.exit("ERROR: your hint can't be longer than 210 characters.")

            if hint:
                break

        if hint:
            continue


        print "\nUserID:",i
        i+=1
        print "attempt:",attempt
        print "answer:",answer

        # Try new hint
        class_address = package_name + "." + new_class_name + "." + new_class_name
        try:
            hint, hint_ans = cond_hint_instance.check_attempt(params)
        except:
            traceback.print_exc()
            sys.exit("ERROR: syntax error in HINT CLASS {0}.".format(class_address))
        if hint and not hint_ans:
                sys.exit("ERROR: you can't leave the second returned string empty. Please ask a question in your hint.")

        if hint:
            print "hint:", hint
            print "solution:", hint_ans
            continue


        # Try last universal hint
        package_name = 'hint_class.last_Universal'
        last_universal_hint = ""
        for f_name in last_u_hints:
            f_address = package_name + "." + f_name
            try:
                uni_f = locate(f_address)
            except:
                traceback.print_exc()
                sys.exit("ERROR: syntax error in universal hint function {0}.".format(f_address))

            try:
                hint = uni_f.check_attempt(params)
            except:
                traceback.print_exc()
                sys.exit("ERROR: syntax error in universal hint function {0}.".format(f_address))

            if hint:
                print "hint:", hint
                break

        if not hint:
            print "Hint does not hit!"




def all_hints_test(path,testdata):
    first_u_hints, hint_classes, last_u_hints = get_all_classes(path)

    i = 1

    for test in testdata:
        print "\nUserID:",i
        i+=1
        attempt = test['attempt']
        answer = test['answer']
        print "attempt:",attempt
        print "answer:",answer

        if not attempt:
            print "Attempt is empty"
            continue

        params = make_params(answer,attempt)


        if params == {}:
            continue
            
        match = find_matches(params)
        ans_tree = params['ans_tree'][0]
        if match==ans_tree or check_final_answer(params):
            print "Correct answer!"
            continue

        # try first universal hints
        package_name = 'hint_class.first_Universal'
        universal_hint = ""
        if len(params['att_tree']) > 1:
            for f_name in first_u_hints:
                f_address = package_name + "." + f_name
                try:
                    uni_f = locate(f_address)
                except:
                    traceback.print_exc()
                    sys.exit("ERROR: syntax error in universal hint function!!")

                try:
                    universal_hint = uni_f.check_attempt(params)
                except:
                    traceback.print_exc()
                    sys.exit("ERROR: syntax error in universal hint function!!")

                if universal_hint:
                    print universal_hint
                    break
            if universal_hint:
                continue


        # try conditional hints
        folder_name = path
        package_name = folder_name.replace('/', '.')#"".join(package_name.split('/')[-1])

        hint = ""
        for class_name in hint_classes:
            class_address = package_name + "." + class_name + "." + class_name
            try:
                ClassName = locate(class_address)
            except:
                traceback.print_exc()
                sys.exit("ERROR: syntax error in HINT CLASS!!")

            try:
                hint_instance = ClassName()
            except TypeError:
                sys.exit("ERROR: name of the HINT CLASS has to be the same as the name of the FILE !!")

            try:
                hint, hint_ans = hint_instance.check_attempt(params)
            except:
                traceback.print_exc()
                sys.exit("ERROR: syntax error in HINT CLASS!!")

            if hint and not hint_ans:
                sys.exit("ERROR: you can't leave the second returned string empty. Please ask a question in your hint.")

            if len(hint) > 210:
                sys.exit("ERROR: your hint can't be longer than 210 characters.")

            if hint:
                print hint, hint_ans
                break
        if hint:
            continue


        # Try last universal hint
        package_name = 'hint_class.last_Universal'
        last_universal_hint = ""
        for f_name in last_u_hints:
            f_address = package_name + "." + f_name
            try:
                uni_f = locate(f_address)
            except:
                traceback.print_exc()
                sys.exit("ERROR: syntax error in universal hint function!!")

            try:
                last_universal_hint = uni_f.check_attempt(params)
            except:
                traceback.print_exc()
                sys.exit("ERROR: syntax error in universal hint function!!")

            if last_universal_hint:
                print "hint:", last_universal_hint
                break

        if not hint:
            print "Hint does not hit!"




if __name__ == "__main__":
    # week = raw_input("Week ID:")
    # problem = raw_input("Problem ID:")
    # part = raw_input("Part_ID:")
    # test_length = raw_input("How many samples you want to see:")
    # file_path = raw_input("Type in relative path of class file:\n")

    #print 'argv=',sys.argv
    if sys.argv[1] == "--help":
        print("Please type in parameters as follow:")
        print("<Week ID> <Problem ID> <Part ID> <Sample Numbers> <Hint Class Name(Optional)>")
        print("If you are using 2015 data to test, please type in the week id, problem id, and part id in 2015 data")
        print("If you don't want to suppress other hints, please type in the class name.")
        sys.exit()

    try:
        week,problem,part,test_length = sys.argv[1:5]
        int(week)
        int(problem)
        int(part)
        int(test_length)
        class_name = ""
        if len(sys.argv) > 5:
            class_name = sys.argv[5]
            print('Week_ID='+week+', Problem_ID='+problem+', Part_ID='+part+', Sample Numbers='+test_length+', Hint Class='+class_name+
                '. Suppress other hints.')
        else:
            print('Week_ID='+week+', Problem_ID='+problem+', Part_ID='+part+', Sample Numbers='+test_length+'. Don\'t suppress other hints.')
    except:
        sys.exit("Error, invalid input. Please see 'python test.py --help' for input requirement")

    '''Read data file from 2015 set'''
    week2015 = week
    problem2015 = problem
    #if week == '2' and int(problem) > 6:
    #    problem2015 = str(int(problem) + 1)
    #elif week == '6':
    #    week2015 = '6.2'
    #elif week == '7':
    #    week2015 = '7a'
    data_file = "2015data/pkl/Week"+week2015+"_data.pkl"
    print "Reading ",data_file
    weekdata = pickle.load(open(data_file,'rb'))

    key = (problem2015,part)
    problem_data = weekdata[key]
    testdata = problem_data[0:int(test_length)]
    testdata = tuple(testdata)

    path = 'hint_class/Week{0}'.format(week)
    if class_name:
        single_hint_test(path, class_name, testdata)
    else:
        all_hints_test(path,testdata)



