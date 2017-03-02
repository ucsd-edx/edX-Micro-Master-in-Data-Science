#!/usr/bin/env python
import sys,os

def runCommand(command):
    print 
name=sys.argv[1]
if name[-6:] != '.ipynb':
    sys.exit('error in filename:'+name)
command='jupyter nbconvert --to slides "{}" --template={}/slides_reveal_MM.tpl --post serve'.format(name, os.environ['REVEAL_HOME'])
print 'running command:',command
os.system(command)


