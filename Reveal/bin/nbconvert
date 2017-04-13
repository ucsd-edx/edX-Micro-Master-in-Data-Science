#!/usr/bin/env python
"""
Run nbconvert to generate html, don't serve
"""
import sys,os

def runCommand(command):
    print 'running command:',command
    os.system(command)

name=sys.argv[1]
dir_path = os.path.split(__file__)[0]  # get relative path of Reveal directory

if not os.path.isfile(name):
    sys.exit('file not found')

if name[-6:] != '.ipynb':
    sys.exit('error in filename:'+name)

command='jupyter nbconvert --to slides "{}" --reveal-prefix http://cdn.bootcss.com/reveal.js/3.4.1/'
runCommand(command.format(name))
