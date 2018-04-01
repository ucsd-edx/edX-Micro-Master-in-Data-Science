# A script for downloading and executing the "real" bootstrap script.
# check for master node
if grep isMaster /mnt/var/lib/info/instance.json | grep true;
then
    cd /mnt/workspace/
    aws s3 cp s3://mas-dse-open/Twitter/RunFromTerminal.sh ./RunFromTerminal.sh
fi

