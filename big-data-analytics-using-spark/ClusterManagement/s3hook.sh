# A script for downloading and executing the "real" bootstrap script.
# Run on all nodes

aws s3 cp s3://dse-weather/ALLBootstrap.sh ./ALLBootstrap.sh
/bin/bash ./ALLBootstrap.sh &>> ./Bootstrap.log

# check for master node
if grep isMaster /mnt/var/lib/info/instance.json | grep true;
then
    aws s3 cp s3://dse-weather/MasterBootstrap.sh ./MasterBootstrap.sh
    /bin/bash ./MasterBootstrap.sh &>> ./Bootstrap.log
fi

