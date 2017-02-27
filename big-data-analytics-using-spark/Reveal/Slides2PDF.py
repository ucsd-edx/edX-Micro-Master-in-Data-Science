#!/usr/bin/env python
import sys,os,webbrowser
import subprocess,time

name=sys.argv[1]
if name[-6:] != '.ipynb':
    sys.exit('error in filename:'+name)
# command='jupyter nbconvert --to slides "%s" --reveal-prefix https://cdn.jsdelivr.net/reveal.js/2.6.2 --template=Reveal/slides_reveal_MM.tpl --post serve'%name
command='jupyter nbconvert --to slides "%s" --template=Reveal/slides_reveal_MM.tpl --post serve'%name
print command
subprocess.Popen(['jupyter', 'nbconvert', '--to', 'slides', "{}".format(name), '--template=Reveal/slides_reveal_MM.tpl', '--post', 'serve'],
                 stderr=subprocess.STDOUT)

time.sleep(3)  # wait nbconvert to do the conversion
html_name = name.replace('ipynb', 'slides.html')
webbrowser.open('http://127.0.0.1:8000/{}?print-pdf'.format(html_name), new=2)
