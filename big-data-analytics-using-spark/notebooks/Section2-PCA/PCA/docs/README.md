# Notebooks

1. **FunctionsAsVectors.ipynb** : Demonstration of the fourier orthonormal basis for functions.
2. **PCA_computation per state.ipynb** : Computing the PCA and other statistics for data from a single state.
3. **Weather Analysis - Initial Visualisation.ipynb** : Visualizing the statistics.
4. **Weather Analysis - reconstruction SNWD.ipynb** : Reconstruction using top eigenvector: generates reconstruction file
5. **Maps using iPyLeaflet.ipynb** : Plotting information about stations on an interactive map.
6. **Is SNWD variation spatial or temporal?.ipynb** : Using the "variance explained" criteria to decide whether space or time has a bigger effect on a coefficient.
7. **Smoothing.ipynb** : Code for smoothing the measurements across days.


# Files / Tables

## Readme file describing the original data
[download from s3](https://mas-dse-open.s3.amazonaws.com/Weather/Info/ghcnd-readme.txt)

## Data

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

A file with the name `data_dir/STAT_<state>.pickle.gz` is gzipped pickle file containing the statistics computed for the state of NY.  
The pickle file contains a pair: `(STAT,STAT_Descriptions)`. 
* `STAT` contains the calculated statistics as a dictionary. 
* `STAT_Descriptions` contains a human-readable description of each element of the dictionary `STAT`

### Reconstruction file

Stored in files named `recon_<state>_<measurement>.parquet`
#### Fields:
1. **Station** :  Station ID
21. **State** :  The state in which the station resides
22. **Name** :  The name of the station
17. **Dist_coast** :  Distance from Coast (units unclear)
18. **Latitude** :  of station
19. **Longitude** :  of station
20. **Elevation** :  Elevation of station in Meters
2. **Measurement** :  Type of measurement (TMAX, PRCP,...)
3. **Values** :  A byte array with all of the value (365X2 bytes)
4. **Year** :  The Year
5. **coeff_1** :  The coefficient of the 1st eigenvector
6. **coeff_2** :  The coefficient of the 2nd eigenvector
7. **coeff_3** :  The coefficient of the 3rd eigenvector
8. **coeff_4** :  The coefficient of the 4th eigenvector
9. **coeff_5** :  The coefficient of the 5th eigenvector
16. **total_var** : The total variance (square distance from the mean. 
15. **res_mean** :  The residual variance after subtracting the mean.
10. **res_1** :  The residual variance after subtracting the mean and eig1 
11. **res_2** :  The residual variance after subtracting the mean and eig1-2
12. **res_3** :  The residual variance after subtracting the mean and eig1-3 
13. **res_4** :  The residual variance after subtracting the mean and eig1-4 
14. **res_5** :  The residual variance after subtracting the mean and eig1-5 
