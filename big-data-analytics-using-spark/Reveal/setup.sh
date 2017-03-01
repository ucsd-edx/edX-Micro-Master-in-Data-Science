#!/bin/bash
mkdir -p bin
cp Slides2PDF.py Slides2PDF
cp toSlide.py toSlides
chmod +x Slides2PDF
chmod +x toSlides
mv Slides2PDF toSlides bin/

REVEAL_HOME=$PWD
export REVEAL_HOME
export PATH=$REVEAL_HOME/bin:$PATH
