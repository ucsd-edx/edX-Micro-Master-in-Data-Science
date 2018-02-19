# check for master node
if grep isMaster /mnt/var/lib/info/instance.json | grep true;
then
   cd /mnt/workspace/

   echo '====================Starting======================'  >> /mnt/workspace/PrivateBootstrap.log
   
   date +%H.%M:%S:%N  >> /mnt/workspace/PrivateBootstrap.log
   echo “Start of bootsrap, set up git” >> /mnt/workspace/PrivateBootstrap.log
   git config --global user.email "yoav.freund@gmail.com"
   git config --global user.name “Yoav Freund”
   git config --global credential.helper cache
   echo "git clone https://github.com/ucsd-edx/edX-Micro-Master-in-Data-Science.git" > clone.sh

   date +%H.%M:%S:%N  >> /mnt/workspace/PrivateBootstrap.log
   echo “copy files from S3 to Local”  >> /mnt/workspace/PrivateBootstrap.log
   mkdir Data
   cd Data
   aws s3 cp --recursive s3://dse-weather/weather.parquet  ./weather.parquet
   aws s3 cp --recursive s3://dse-weather/info/stations.parquet/ ./stations.parquet
   date +%H.%M:%S:%N  >> /mnt/workspace/PrivateBootstrap.log
   echo “copy files from Local to HDFS”  >> /mnt/workspace/PrivateBootstrap.log
   hdfs dfs -mkdir /weather
   hdfs dfs -copyFromLocal weather.parquet /weather/weather.parquet
   hdfs dfs -copyFromLocal stations.parquet /weather/stations.parquet

   hdfs dfs -ls /weather/  >> /mnt/workspace/PrivateBootstrap.log

   date +%H.%M:%S:%N  >> /mnt/workspace/PrivateBootstrap.log
   echo “Bootstrap done”  >> /mnt/workspace/PrivateBootstrap.log
fi
