# Big Data Analytics Using Spark

## Installing:
 0. Install / Upgrade Jupter >= 4.0.0 and Openssl >= 1.0.2k in order to use this tool properly.
 1. `source setup.sh` (This can be run from anywhere)

## Convert Ipython notebooks to Slides using Reveal:
 `toSlides notebook.ipynb`

  This will convert the `notebook.ipynb` to `notebook.slides.html` under the same directory where `notebook.ipynb` is located, and open a new tab in the web browser that displays the Reveal slides.

## Convert Ipython notebooks to Slides and then pdf:
 `Slides2PDF notebook.ipynb`

  This convert the notebook to a Reveal slides file and then convert it to a PDF file. Both of the outputs have the same name as the original notebook, but with different extensions. (.slides.html and .pdf)


## Issues:
 1. If you see an error message containing `jinja2.exceptions.TemplateNotFound`, upgrading Jupyter to > 4.0.0 will solve the problem. To upgrade, use `conda update jupyter` or `pip install -U jupyter`

 2. If the error message contains `dyld: Library not loaded: /usr/local/opt/openssl/lib/libssl.1.0.0.dylib`, you probably need to install / upgrade Openssl. To do that, run `pip install openssl [-U]`. If that does not solve the problem, please check where the openssl is installed by `which openssl`, and create a symbolic link of the .dylib file by `ln -s path/to/openssl/libssl.1.0.0.dylib /usr/local/opt/openssl/lib/`

 3. If you see some `.css.` file loading problem when using Slides2PDF, the output may have illed format with Math Expressions. We are working on that now.
