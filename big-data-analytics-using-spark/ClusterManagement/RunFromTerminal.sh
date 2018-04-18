date +%H.%M:%S:%N  
echo “copy files from Local to HDFS”
cd /mnt/workspace/Data
/usr/bin/hdfs dfs -mkdir /weather
/usr/bin/hdfs dfs -copyFromLocal US_weather.parquet /weather/US_weather.parquet
/usr/bin/hdfs dfs -copyFromLocal US_stations.parquet /weather/US_stations.parquet
/usr/bin/hdfs dfs -ls /weather/  
cd ..

date +%H.%M:%S:%N  
echo “set up git” 
git config --global user.email "yoav.freund@gmail.com"
git config --global user.name “Yoav Freund”
git config --global credential.helper cache
git clone https://github.com/ucsd-edx/edX-Micro-Master-in-Data-Science.git


echo "RunFromTerminal done"
