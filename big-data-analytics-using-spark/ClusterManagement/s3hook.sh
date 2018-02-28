# A script for downloading and executing the "real" bootstrap script.
# check for master node
if grep isMaster /mnt/var/lib/info/instance.json | grep true;
then
    aws s3 cp s3://dse-weather/PrivateBootstrap.sh ./PrivateBootstrap.sh
    /bin/bash ./PrivateBootstrap.sh &> ./PrivateBootstrap.log
fi

