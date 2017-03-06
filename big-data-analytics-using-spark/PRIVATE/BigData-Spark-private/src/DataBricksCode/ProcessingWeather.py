# Databricks notebook source exported at Fri, 11 Sep 2015 02:52:47 UTC
# MAGIC %run /Users/yfreund@ucsd.edu/Vault

# COMMAND ----------

# MAGIC %md ### This notebook demonstrates how to process the full NCDC weather dataset inside spark.

# COMMAND ----------

dbutils.fs.unmount("/mnt/%s" % MOUNT_NAME)
dbutils.fs.mount("s3n://%s:%s@%s" % (ACCESS_KEY, ENCODED_SECRET_KEY, AWS_BUCKET_NAME), "/mnt/%s" % MOUNT_NAME)

# COMMAND ----------

file_list=dbutils.fs.ls('/mnt/NCDC-weather/')
[file.path for file in file_list[:3]]

# COMMAND ----------

# MAGIC %md #### Find all distinct state values

# COMMAND ----------

# MAGIC %sql select distinct state from stations

# COMMAND ----------

# MAGIC %sql select * from stations limit 5

# COMMAND ----------

# MAGIC %md #### Count stations
# MAGIC The following sql command counts the number of stations in each state in the US.

# COMMAND ----------

# MAGIC %sql select state as state,count(*) as count from stations where substr(id,0,2)=="US"  group by state

# COMMAND ----------

states = sqlContext.sql('select state as state,count(*) as count from stations where substr(id,0,2)=="US"  group by state')
states.sort(['state']).show(100)

# COMMAND ----------

dataframe.count()

# COMMAND ----------

Continental_states = """Alabama		AL
Arizona		AZ
Arkansas	AR
California	CA
Colorado	CO
Connecticut	CT
Delaware	DE
Florida		FL
Georgia		GA
Idaho		ID
Illinois	IL
Indiana		IN
Iowa		IA
Kansas		KS
Kentucky	KY
Louisiana	LA
Maine		ME
Maryland	MD
Massachusetts	MA
Michigan	MI
Minnesota	MN
Mississippi	MS
Missouri	MO
Montana		MT
Nebraska	NE
Nevada		NV
New Hampshire	NH
New Jersey	NJ
New Mexico	NM
New York	NY
North Carolina	NC
North Dakota	ND
Ohio		OH
Oklahoma	OK
Oregon		OR
Pennsylvania	PA
Rhode Island	RI
South Carolina	SC
South Dakota	SD
Tennessee	TN
Texas		TX
Utah		UT
Vermont		VT
Virginia	VA
Washington	WA
West Virginia	WV
Wisconsin	WI
Wyoming		WY""";

non_continental_states= """Alaska		AK
Hawaii		HI
"""

# COMMAND ----------

us_states={line.split('\t')[-1]:line.split('\t')[0] for line in Continental_states.split('\n')}
us_states


# COMMAND ----------

stations= sqlContext.sql('select * from stations')

# COMMAND ----------

stations.show()

# COMMAND ----------

cont_acronyms=us_states.keys()
print len(cont_acronyms)
print ','.join(cont_acronyms)

# COMMAND ----------

in_continental = [row.state in cont_acronyms for row in stations.select('state').collect()]
print len(in_continental)
print sum(in_continental)

# COMMAND ----------

# MAGIC %sql select s.ID as station from stations as s where s.state='CA'

# COMMAND ----------

# MAGIC %sql create table selectedstations as select s.ID from stations as s where s.state='CA'

# COMMAND ----------

# MAGIC %sql select * from selectedstations limit 10

# COMMAND ----------

# MAGIC %sql create table weather2 as select w.*, s.state from weather w join stations s on w.station = s.ID

# COMMAND ----------

# MAGIC %sql select * from weather2 where (state='CA' and measurement='TMAX') limit 10

# COMMAND ----------

# MAGIC %md subqueries are not supported in spark-sql:
# MAGIC `%sql select * from weather as w where (w.measurement = 'TMAX' and 
# MAGIC                                   w.station in (select s.ID as station from stations as s where s.state='CA')
# MAGIC                                  ) limit 10`

# COMMAND ----------

Ca = sqlContext.sql("select * from weather2 where (state = 'CA' and measurement = 'TMAX')")

# COMMAND ----------

Ca.count()

# COMMAND ----------

from pyspark.mllib.stat import Statistics

# COMMAND ----------

TMAX=Ca.select([str(i) for i in range(1,365)])

# COMMAND ----------

from pyspark.mllib.stat import Statistics
from pyspark.mllib.linalg.distributed import RowMatrix

mat = RowMatrix(TMAX)

# Compute column summary statistics.
summary = Statistics.colStats(mat)
print(summary.mean())
print(summary.variance())
print(summary.numNonzeros())

# COMMAND ----------

pyspark.mllib.linalg.help() 

# COMMAND ----------



# COMMAND ----------

pyspark.mllib.ver

# COMMAND ----------

