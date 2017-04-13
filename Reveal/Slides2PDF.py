#!/usr/bin/env python
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

command='jupyter nbconvert --to slides "{}" --reveal-prefix http://cdn.bootcss.com/reveal.js/3.4.1/ --template={}'
runCommand(command.format(name, os.path.join(dir_path, 'slides_reveal_MM.tpl')))

slides_file = name.replace('.ipynb', '.slides.html')
out = name.replace('.ipynb', '.pdf')
command = '{} {} automatic "{}" "{}"'.format(os.path.join(dir_path, 'decktape', 'phantomjs'),
                                         os.path.join(dir_path, 'decktape', 'decktape.js'), slides_file, out)
runCommand(command)
