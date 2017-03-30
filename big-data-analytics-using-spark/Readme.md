## Installation directions for course staff.

* To install jupyter on your computer, follow the directions here: https://mas-dse.github.io/startup/
  * To pip install a bunch of nbextensions, together with a configurator for those extensions, check out: https://github.com/ipython-contrib/jupyter_contrib_nbextensions
* To install Spark on your computer, for the directions here: https://mas-dse.github.io/DSE230/installation/
* To set up Reveal, do `source Reveal/setup.sh`

## Directory structure

For each of the 5 parts (spark basics, PCA, ...)
* Root: Contains all of the .ipynb files. There are two flavors for each notebook:
   1. **<name>_MASTER.ipynb** contains the output-cleared master notebooks that contain the solutions to the excercises. 
   2. **<name>.ipynb** redacted notebooks fully executed and with all outputs (other than excercises) for the students.
* Subdirectories:
   * lib: contains python code for performing complex things.
   * Lib_redacted: contains redacted code that the students are asked to complete.
   * SLides: the html files and the pdf/png files generated for the class.
   * tests: includes .py and pickle files for the tests that are part of the HW.
   * grader: Contains the full tests for the grader
             contains just python files.

## Some resources for pyspark

 * [An up-to-date documentation of the spark API](http://takwatanabe.me/pyspark/generated/pyspark.html)
 * [Mastering Apache Spark](https://jaceklaskowski.gitbooks.io/mastering-apache-spark/) by Jacek Laskowski
 * [A spark Dataframe Cheat-sheet](https://gist.github.com/evenv/b4d5f3054d7260e6c3d3)
 * The new abstractions in Spark2.0 are dataframes and sparksession: [introduction](http://spark.apache.org/docs/latest/sql-programming-guide.html#datasets-and-dataframes)  
 Supposedly, RDD's are demoted to "low level API"
 * [Dataframes API](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html?highlight=dataframe#pyspark.sql.DataFrame)

 
 ## AWS CLI (Command line interface)
 * On mac, the best way to install is with `brew install awscli`
 * Reference: http://docs.aws.amazon.com/cli/latest/reference/index.html#cli-aws
 * Specific for S3: http://docs.aws.amazon.com/cli/latest/reference/s3/
 
