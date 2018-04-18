# check for master node
echo '====================Master Bootstrap Starting======================'  
   
date +%H.%M:%S:%N  
cd /mnt/workspace/
echo “copy files from S3 to Local”  
aws s3 cp s3://dse-weather/RunFromTerminal.sh ./RunFromTerminal.sh

mkdir Data
cd Data

aws s3 cp --recursive --quiet s3://dse-weather/US_stations.parquet  ./US_stations.parquet
aws s3 cp --recursive --quiet s3://dse-weather/US_weather.parquet  ./US_weather.parquet

date +%H.%M:%S:%N  
echo '====================Bootstrap done======================'  

