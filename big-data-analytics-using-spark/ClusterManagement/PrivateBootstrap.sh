# check for master node
if grep isMaster /mnt/var/lib/info/instance.json | grep true;
then

   echo '====================Bootstrap Starting======================'  
   
   date +%H.%M:%S:%N  
   echo “copy files from S3 to Local”  
   aws s3 cp s3://dse-weather/RunFromTerminal.sh ./RunFromTerminal.sh
   cd /mnt/workspace/

   mkdir Data
   cd Data
   aws s3 cp --recursive s3://dse-weather/weather.parquet  ./weather.parquet
   aws s3 cp s3://mas-dse-open/Weather/Info/US_stations.tsv.gz ./US_stations.tsv.gz
   gunzip US_stations.tsv.gz

   date +%H.%M:%S:%N  
   echo “Bootstrap done”  
fi
