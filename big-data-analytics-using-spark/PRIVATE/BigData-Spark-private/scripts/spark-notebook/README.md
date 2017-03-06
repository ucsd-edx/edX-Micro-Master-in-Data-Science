### Files

* spark-ec2-helper.py:      
	The main script, use `python spark-ec2-helper.py --help` for more help.
* Constants.py     
    The credentials that define the AWS account to use.
* README.md	   
  This file	
* s3helper.py   
   A script for interacting with S3 through the notebook.
* FilesIO.ipynb   
   An example of a notebook using `s3helper.py`

### The Launch UI

1. Install required packages: `pip install -r requirements.txt`
2. Run `python deploy-server.py`
3. In the Jupyter notebook, the variable `master_url` is predefined with the master node URL. A SparkContext instance can be created as follows:
```
from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster(master_url)
sc = SparkContext(conf=conf)
```
