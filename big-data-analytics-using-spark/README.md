# Big Data Analytics Using Spark

## Before using Reveal:
 1. copy the `Reveal` directory to the location where you will be running the reveal commands
 2. cd to where the `Reveal` directory is located
 3. clone the reveal.js repo or just make a symbolic link by `ln -s Reveal/reveal.js`

## Convert Ipython notebooks to Slides using Reveal:
 run `Reveal/toSlides.py [NOTEBOOK_FILE_NAME]`

## Convert Ipython notebooks to Slides and then pdf:
 run `Reveal/Slides2PDF.py [NOTEBOOK_FILE_NAME]` 
 This will open two tabs in your web browser: one is the slides, the other is the converted pdf. Just print the page with the 'save as pdf' option.
 example output: `notebooks/BasicSpark/1. Spark Basics.pdf`
