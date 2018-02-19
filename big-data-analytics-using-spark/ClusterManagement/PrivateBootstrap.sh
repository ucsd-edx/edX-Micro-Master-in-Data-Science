


# check for master node
if grep isMaster /mnt/var/lib/info/instance.json | grep true;
then
   cd /mnt/workspace/

   date +%H.%M:%S:%N  #>> /mnt/workspace/PrivateBootstrap.log
   echo “Start of bootsrap, set up git” #>> /mnt/workspace/PrivateBootstrap.log
   git config --global user.email "yoav.freund@gmail.com"
   git config --global user.name “Yoav Freund”
   git config --global credential.helper cache
   git clone https://github.com/ucsd-edx/edX-Micro-Master-in-Data-Science.git

   date +%H.%M:%S:%N  #>> /mnt/workspace/PrivateBootstrap.log
   echo “copy files from S3 to Local”  #>> /mnt/workspace/PrivateBootstrap.log
   mkdir Data
   cd Data
   aws s3 cp --recursive s3://dse-weather/weather.parquet  ./weather.parquet

   date +%H.%M:%S:%N  #>> /mnt/workspace/PrivateBootstrap.log
   echo “copy files from Local to HDFS”  #>> /mnt/workspace/PrivateBootstrap.log
   hadoop fs -mkdir /weather
   hadoop fs -copyFromLocal weather.parquet /weather/weather.parquet

   date +%H.%M:%S:%N  #>> /mnt/workspace/PrivateBootstrap.log
   echo “Bootstrap done”  #>> /mnt/workspace/PrivateBootstrap.log
fi
