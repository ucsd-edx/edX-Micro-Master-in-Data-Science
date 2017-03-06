#!/usr/bin/env python
import sys,os,webbrowser
import subprocess,time

name=sys.argv[1]
if name[-6:] != '.ipynb':
    sys.exit('error in filename:'+name)
# command='jupyter nbconvert --to slides "%s" --reveal-prefix http://cdn.js/reveal.js --template=Reveal/slides_reveal_MM.tpl --post serve'%name
command = ['jupyter', 'nbconvert', '--to', 'slides', "{}".format(name), '--template={}/slides_reveal_MM.tpl'.format(os.environ['REVEAL_HOME']), '--post', 'serve']
print ' '.join(command)
subprocess.Popen(command, stderr=subprocess.STDOUT)

time.sleep(3)  # wait nbconvert to do the conversion
html_name = os.path.split(name.replace('ipynb', 'slides.html'))[-1]
webbrowser.open('http://127.0.0.1:8000/{}?print-pdf'.format(html_name), new=2)
