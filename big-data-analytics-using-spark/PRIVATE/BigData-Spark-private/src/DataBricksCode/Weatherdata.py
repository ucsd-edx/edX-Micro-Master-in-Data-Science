# Databricks notebook source exported at Wed, 9 Sep 2015 01:41:37 UTC
# MAGIC %run /Users/yfreund@ucsd.edu/Vault

# COMMAND ----------

# MAGIC %md ### Mount S3 bucket and navigate it

# COMMAND ----------

dbutils.fs.unmount("/mnt/%s" % MOUNT_NAME)
dbutils.fs.mount("s3n://%s:%s@%s" % (ACCESS_KEY, ENCODED_SECRET_KEY, AWS_BUCKET_NAME), "/mnt/%s" % MOUNT_NAME)

# COMMAND ----------

file_list=dbutils.fs.ls('/mnt/NCDC-weather/WeatherUncompressed/')
[file.path for file in file_list[:3]]

# COMMAND ----------

# MAGIC %md ### read the first csv file

# COMMAND ----------

data = sc.textFile("/mnt/%s/WeatherUncompressed/ALLaa" % MOUNT_NAME)
index = data.take(1)[0].split(',')
# The first three attributes in line 1 are in different order than those in rest of the lines,
# so we have to swap them into the correct order.
index[1], index[2] = index[2], index[1]
print index

# COMMAND ----------

data.take(3)

# COMMAND ----------

# MAGIC %md ### Sample a tiny part of the data
# MAGIC Note that this command takes very little time. The actual work is done when you want to read the sample and use it for something

# COMMAND ----------

data_sample=data.sample(False,0.0001).cache()
data_sample.collect()
type(data),type(data_sample)

# COMMAND ----------

data_sample.count()

# COMMAND ----------

# MAGIC %md ### Deleting a table
# MAGIC One can use the sql command "DROP TABLE", but the underlying hive file remains. To completely remove the tabl use `dbutils.fs.rm` as below.

# COMMAND ----------

dbutils.fs.ls('/user/hive/warehouse/')

# COMMAND ----------

dbutils.fs.rm('/user/hive/warehouse/weather/',recurse=True)

# COMMAND ----------

# MAGIC %md Using Loggly

# COMMAND ----------

# MAGIC %run /Users/yfreund@ucsd.edu/loggly

# COMMAND ----------

# An example routine that is inserted into the code to create the logs.
def extract(d):
  logger.info("message here")
  return d

# COMMAND ----------

# MAGIC %md ### Main data extraction code

# COMMAND ----------

def convert(x):
  x = x.strip()
  if x == '':
    # The value goes missing
    return np.nan
  return float(x)

# COMMAND ----------

from pyspark.sql import Row
import numpy as np
# 1. Split each line using comma,
# 2. remove first line (which is the names of each column)
# 3. sort the data based on the "year" attribute

dataRows=range(len(file_list))
dataFrames=range(len(file_list))

for i in range(len(file_list)):
    filename=file_list[i].path
    data = sc.textFile(filename)
    dataRows[i] = data.map(lambda s: s.split(',')) \
               .filter(lambda d: d[0] != 'station') \
               .map(lambda d: tuple(d[0:2]) + tuple([convert(x) for x in d[2:]])) \
               .sortBy(lambda d: d[2])
    dataFrames[i] = sqlContext.createDataFrame(dataRows[i], index)
    if i==0:
      combinedDataFrame=dataFrames[i]
    else:
      combinedDataFrame=combinedDataFrame.unionAll(dataFrames[i])
    print filename
    print combinedDataFrame.count()
#dataframe.saveAsTable("Weather")

# COMMAND ----------

# MAGIC %md ## Save dataframe as Table and as parquet files

# COMMAND ----------

combinedDataFrame.count()

# COMMAND ----------

combinedDataFrame.saveAsTable("Weather")

# COMMAND ----------

dbutils.fs.ls("/mnt/%s/Weather/parquet" % MOUNT_NAME)
#combinedDataFrame.count()

# COMMAND ----------

combinedDataFrame.write.parquet("/mnt/%s/Weather/parquet/Weather.parquet" % MOUNT_NAME)

# COMMAND ----------

dbutils.fs.ls("/mnt/%s/Weather.parquet" % MOUNT_NAME)

# COMMAND ----------

#Expose sql table as dataframe
import pandas as pd
dataframe = sqlContext.table("Weather")

# COMMAND ----------

# MAGIC %md ### Playing around with SQL

# COMMAND ----------

# MAGIC %sql select * from Weather limit 10

# COMMAND ----------

# MAGIC %sql  select W.measurement,COUNT(*) from Weather W group by W.measurement

# COMMAND ----------

dbutils.fs.ls('dbfs:/mnt/NCDC-weather/')

# COMMAND ----------

# MAGIC %md ### Loading and Parsing Stations data

# COMMAND ----------

stations_txt = sc.textFile('dbfs:/mnt/NCDC-weather/Weather/Info/ghcnd-stations_buffered.txt')

# COMMAND ----------

line=stations_txt.take(3)[2]
line

# COMMAND ----------

# MAGIC %text
# MAGIC IV. FORMAT OF "ghcnd-stations.txt"
# MAGIC 
# MAGIC ------------------------------
# MAGIC Variable   Columns   Type
# MAGIC ------------------------------
# MAGIC ID            1-11   Character
# MAGIC LATITUDE     13-20   Real
# MAGIC LONGITUDE    22-30   Real
# MAGIC ELEVATION    32-37   Real
# MAGIC STATE        39-40   Character
# MAGIC NAME         42-71   Character
# MAGIC GSNFLAG      73-75   Character
# MAGIC HCNFLAG      77-79   Character
# MAGIC WMOID        81-85   Character
# MAGIC ------------------------------

# COMMAND ----------

#0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
#          1         2         3         4         5         6         7         8         9
#AJ000037575  41.5500   46.6670  490.0    ZAKATALA                               37575
#US1CAAL0002  37.7075 -122.0687   87.5 CA CASTRO VALLEY 0.5 WSW
colspecs = [(0, 11), (11, 20), (20, 30), (30, 37),(37,41),(41,54),(72,76),(76,80),(80,86)]
colnames=['ID','latitude','longitude','elevation','state','name','GSNFLAG','HCNFLAG','WMOID']
coltypes=[type(x) for x in ['str',1.1,1.1,1.1,'str','str','str','str','str']]
print len(colspecs),len(colnames),len(coltypes)
coltypes

# COMMAND ----------

coltypes

# COMMAND ----------

from string import strip
def parse_station(line):
  line=line.encode('utf-8')
  out=range(len(colspecs))
  for i in range(len(colspecs)):
    fr,to = colspecs[i]
    value = coltypes[i](line[fr:to])
    if type(value)==str:
      value=strip(value)
    #print colnames[i],'\t"%s"'%str(value)
    out[i]=value
  return tuple(out)

# COMMAND ----------

stations_text=sc.textFile("/mnt/%s/Weather/Info/ghcnd-stations_buffered.txt" % MOUNT_NAME)

# COMMAND ----------

stations_text.take(3)

# COMMAND ----------

stations_rows=stations_text.map(parse_station)

# COMMAND ----------

stations_rows.take(3)

# COMMAND ----------

station_info=sqlContext.createDataFrame(stations_rows, colnames)

# COMMAND ----------

station_info.show()

# COMMAND ----------

station_info.drop_duplicates(['state']).show()

# COMMAND ----------

state_col=station_info.select('state')
states_table=state_col.distinct()
type(states_table)
states=[a.state for a in states_table.collect()]
','.join(states)

# COMMAND ----------

# MAGIC %sql DROP TABLE Stations

# COMMAND ----------

dbutils.fs.rm('/user/hive/warehouse/stations/',recurse=True)
station_info.saveAsTable('Stations')

# COMMAND ----------

station_info.write.parquet("/mnt/%s/Weather/parquet/stations.parquet" % MOUNT_NAME)

# COMMAND ----------

dbutils.fs.ls("/mnt/%s/Weather/" % MOUNT_NAME)

# COMMAND ----------



# COMMAND ----------

