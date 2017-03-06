# Databricks notebook source exported at Wed, 2 Mar 2016 00:10:20 UTC
# MAGIC %md # Word-count in spark
# MAGIC 
# MAGIC This is a simple first example of using spark and databricks.
# MAGIC In this example we read a largish text file (Moby Dick) and count the occurances of each word
# MAGIC 
# MAGIC ### What is covered
# MAGIC * Setting permission for AWS in a safe way using a "Vault" file.
# MAGIC * Mounting an S3 bucket on the spark cluster.
# MAGIC * using spark style map reduce to count the words.
# MAGIC * Collecting the results to the head node and browsing the results.

# COMMAND ----------

# MAGIC %md ### Setting AWS Credentials
# MAGIC In order to use S3 we need to set the AWS credentials. Credentials are private to each user.
# MAGIC It is unsafe to put the credentials in a notebook that is backed up on a public repository such as github. Therefor the
# MAGIC recommended method is to create a separate file, just for storing the credentials, which is not backed on a public repository.
# MAGIC 
# MAGIC The file should have the following format
# MAGIC 
# MAGIC `import urllib`  
# MAGIC `# Access Key of ......`  
# MAGIC `ACCESS_KEY = "........" # ACCESS_KEY`   
# MAGIC `SECRET_KEY = "..........." # SECRET_KEY`   
# MAGIC `ENCODED_SECRET_KEY = urllib.quote(SECRET_KEY, "")`   
# MAGIC 
# MAGIC I created this script in the root directory of my databricks workspace. I can therefor run it with the following command

# COMMAND ----------

# MAGIC %run /Users/yfreund@ucsd.edu/Vault

# COMMAND ----------

AWS_BUCKET_NAME = "mas-dse-public" 
MOUNT_NAME = "NCDC-weather"
dbutils.fs.unmount("/mnt/%s" % MOUNT_NAME)
output_code=dbutils.fs.mount("s3n://%s:%s@%s" % (ACCESS_KEY, ENCODED_SECRET_KEY, AWS_BUCKET_NAME), "/mnt/%s" % MOUNT_NAME)
print 'Mount output status=',output_code
file_list=dbutils.fs.ls('/mnt/%s/Spark-Data/mllib/'%MOUNT_NAME)
file_list

# COMMAND ----------

text_file = sc.textFile(u'dbfs:/mnt/NCDC-weather/moby10b.txt')
counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)

# COMMAND ----------

C=counts.collect()

# COMMAND ----------

type(C)

# COMMAND ----------

C.sort(key=lambda x:x[1])
C[-5:]

# COMMAND ----------

