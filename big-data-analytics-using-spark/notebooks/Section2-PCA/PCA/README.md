## Measurements tables

The data is stored in parquet files. `ALL.parquet` contains all of the data, `NY.parquet` includes the data for all stations in New-York State.

### Schema

* **Station:** Station ID
* **Measurement:** Type of measurement (TMAX,TMIN,TOBS,...)
* **Year**
* **Values:** a byte array of length 2*365 representing 365 floats (np.float16)
* **State**

|    Station|Measurement|Year|              Values|State|
|-----------|-----------|----|--------------------|-----|
|USC00303452|       PRCP|1903|[00 7E 00 7E 00 7...|   NY|
|USC00303452|       PRCP|1904|[00 00 28 5B 00 0...|   NY|
|USC00303452|       PRCP|1905|[00 00 60 56 60 5...|   NY|
|USC00303452|       PRCP|1906|[00 00 00 00 00 0...|   NY|
|USC00303452|       PRCP|1907|[00 00 00 00 60 5...|   NY|

### Reading measurement data into a dataframe

#### When using your own computer
The files are stored on AWS as compressed tar files. The bucket `mas-dse-open` can be accessed through an HTTP connection. 

1) Download all of the measurements for a particular state (here NY) or ALL for the file that contains all of the states


> curl https://mas-dse-open.s3.amazonaws.com/Weather/by_state/NY.tgz 
  \> `data_dir`/NY.tgz

> Where `data_dir` is the local data directory, here `big-data-analytics-using-spark/notebooks/Data/Weather`

2) Untar the tar file 

> tar -xzf `data_dir`/NY.tgz

> Creates the parquet directory `data_dir`/NY.parquet

3) Read the parquet file into a dataframe:

> df=sqlContext.read.parquet(`data_dir`/NY.parquet)

#### When using a Spark Cluster on AWS/EMR

To Be Completed

## Station information

To get information about each station in the united states:

> curl https://mas-dse-open.s3.amazonaws.com/Weather/Info/US_stations.tsv.gz > `data_dir`/US\_stations.tsv.gz    
> gunzip `data_dir`/US\_stations.tsv.gz 

To read the station data into a spark dataframe:

```python 
## Read tab-separated data into a Pandas dataframe.
import pandas as pd
stations_pdf=pd.read_csv(data_dir+'/US_stations.tsv',sep='\t')

## Define the schema for spark DataFrame
from pyspark.sql.types import Row, StructField, StructType, StringType, IntegerType, FloatType

schema = StructType([StructField("Station", StringType(), False),
                     StructField("Dist_coast", FloatType(), False),
                     StructField("Latitude", FloatType(), False),
                     StructField("Longitude", FloatType(), False),
                     StructField("Elevation", FloatType(), False),
                     StructField("State", StringType(), True),                  
                     StructField("Name", StringType(), False)])
                     
stations_df = sqlContext.createDataFrame(stations,schema)
stations_df.show(4)                
```
### Schema
* **Station:** Station ID.
* **Dist\_coast:** Distance from the coast (shoreline) (units? 1.4 of this  per mile?)
* **Latitude**
* **Longitude**
* **Elevation** in meters, missing = -999.9
* **Name:** the name of the station.

|    Station|Dist_coast|Latitude|Longitude|Elevation|State|            Name|
|-----------|----------|--------|---------|---------|-----|----------------|
|USC00044534|   107.655| 36.0042|  -119.96|     73.2|   CA|  KETTLEMAN CITY|
|USC00356784|   0.61097| 42.7519|-124.5011|     12.8|   OR|PORT ORFORD NO 2|
|USC00243581|   1316.54| 47.1064|-104.7183|    632.8|   MT|        GLENDIVE|
|USC00205601|   685.501|   41.75| -84.2167|    247.2|   MI|         MORENCI|
|USC00045853|   34.2294| 37.1364|-121.6025|    114.3|   CA|         MORGAN HILL|


### Statistics file

A file with the name `data_dir/STAT_NY.pickle.gz` is gzipped pickle file containing the statistics computed for the state of NY.  
The pickle file contains a pair: `(STAT,STAT_Descriptions)`. 
* `STAT` contains the calculated statistics as a dictionary. 
* `STAT_Descriptions` contains a human-readable description of each element of the dictionary `STAT`


# Notebooks

* 1. FunctionsAsVectors_CLASS.ipynb
* 2. PCA\_computation per state.ipynb: Generates STAT_state.pickle
* Prelim.Weather-Analysis-Smoothing.ipynb: running a gaussian smoother.
* 4.0 Weather Analysis - Initial Visualisation.ipynb: Visualizing overall statistics
* 4.4 Weather Analysis - Visualisation.ipynb: 
* 4.5 Weather Analysis - reconstruction SNWD.ipynb : Reconstruction games
* 5. maps using iPyLeaflet.ipynb  : Maps
* 5.5 DataOnMaps.ipynb : Maps
* 6. Is SNWD variation spatial or temporal?.ipynb

### Move to old
* 2. Small\_PCA_computation_CLASS.ipynb
* 7. Analyzing residuals-Cov.ipynb
* 7. Analyzing residuals.ipynb

