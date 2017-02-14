#!/usr/bin/env python
import sys,os

name=sys.argv[1]
name='2.\ Execution\ plans\,\ Lazy\ Evaluation\,\ and\ caching.ipynb'
if name[-6:] != '.ipynb':
    sys.exit('error in filename:'+name)
command='jupyter nbconvert --to slides %s --template=Reveal/slides_reveal_MM.tpl'%name
os.system(command)
command='open %s.slides.html'%name[:-6]
print command
os.system(command)


