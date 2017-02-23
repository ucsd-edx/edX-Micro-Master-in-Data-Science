#!/usr/bin/env python
import sys,os
#import subprocess
#name=sys.argv[1]
name='2.\ Execution\ plans\,\ Lazy\ Evaluation\,\ and\ caching.ipynb'
if name[-6:] != '.ipynb':
    sys.exit('error in filename:'+name)
command='jupyter nbconvert --to slides %s --reveal-prefix https://cdn.jsdelivr.net/reveal.js/2.6.2 --template=Reveal/slides_reveal_MM.tpl --post serve'%name
os.system(command)
#server=subprocess.Popen(['python','-m','SimpleHTTPServer','8080'])
#os.system(command)
#command='open %s.slides.html?print-pdf'%name[:-6]
#print command
#os.system(command)

