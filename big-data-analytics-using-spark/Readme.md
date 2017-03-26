## Installation directions for course staff.

* To install jupyter on your computer, follow the directions here: https://mas-dse.github.io/startup/
* To install Spark on your computer, for the directions here: https://mas-dse.github.io/DSE230/installation/
* To set up Reveal, do `source Reveal/setup.sh`

## Directory structure

For each of the 5 parts (spark basics, PCA, ...)
* Root: contains the output-cleared master notebooks (MASTER_...)
   * lib: contains python code for performing complex things.
   * SLides: the html files and the pdf/png files generated for the class. Also PPT files.
   * public: this subdirectory is released to the public github available to the students.
     Contains the redacted notebooks. 
      * lib: contains libraries and redacted libraries.
      * tests: includes .py and pickle files for the tests
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
 
