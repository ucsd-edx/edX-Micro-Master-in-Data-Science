# Script to update the pickle file
# Run this script with the folder that contains all the hint class files,
# it will check for any new hint classes, and add them to the dictionary in the pickle file
# 
# NOTICE: Name of the hint class has to be the same as the hint class file
#
# Name: Xueyang Li
# Date: Sep 21, 2016

import pickle
from pydoc import locate
import os
from os import listdir
from os.path import isfile, join
import sys

# Folder path on developer's macbook pro
# ~/Desktop/cse/edex/Developers_repo/hint_database/testHintClassFolder

pickle_filename = 'dict.pkl'
hint_class_dir = 'hint_class'

if __name__ == "__main__":
    
    folder_path = raw_input("Type in relative path of class folder(starting with 'hint_class/':\n")
    
    # changed
    #hint_class_files = [f for f in listdir(os.path.expanduser(folder_path)) 
    #if isfile(join(os.path.expanduser(folder_path), f)) and f.endswith('.py')]
    #
    #hint_class_files.remove("__init__.py")

    hint_class_files = []
    for f in listdir(os.path.expanduser(folder_path)):
        if isfile(join(os.path.expanduser(folder_path), f)) and \
                f.endswith('.py') and f != '__init__.py' and f != 'template.py':
            hint_class_files.append(f)

    hint_classes = []
    for n in hint_class_files:
        hint_classes.append(os.path.splitext(n)[0]) 

    #package_name = "".join(folder_path.split('/')[-1]) changed
    class_path = folder_path[folder_path.find(hint_class_dir):]


    ''' Load the content from pickle file as a dictionary '''
    try:
        with open(pickle_filename, 'rb') as handle:
            pc_dictionary = pickle.load(handle)
    # Check for empty pickle file
    except EOFError:
            pc_dictionary = {}


    for class_name in hint_classes:
        class_address = class_path.replace('/','.') + "." + class_name + "." + class_name
        #print class_address
        ClassName = locate(class_address)

        try:
            hint_instance = ClassName()
        except TypeError:
            sys.exit("ERROR: name of the HINT CLASS has to be the same as the name of the FILE !!")
        
        problem_list = hint_instance.get_problems()
        #class_name = hint_instance.__class__.__name__

        ''' Add new prblem-hint pair to the dictionary '''
        for problem_name in problem_list:
            if(problem_name not in pc_dictionary):
                pc_dictionary[problem_name] = []

            if(class_address not in pc_dictionary[problem_name]):
                pc_dictionary[problem_name].append(class_address)                            


    ''' Dump the updated dictionary back to the pickle file '''
    with open(pickle_filename, 'wb') as handle:
      pickle.dump(pc_dictionary, handle)



    # Testing
    # with open(pickle_filename, 'rb') as handle:
    #   pc_dictionary = pickle.load(handle)

    # print pc_dictionary    
  
