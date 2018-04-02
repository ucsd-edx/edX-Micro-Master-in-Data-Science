# A script for downloading and executing the "real" bootstrap script.
# check for master node

export PUBLIC_KEY=""

if grep isMaster /mnt/var/lib/info/instance.json | grep true;
then
    echo "$PUBLIC_KEY" >> ~/.ssh/authorized_keys
    cd /mnt/workspace/
    aws s3 cp s3://mas-dse-open/Twitter/RunFromTerminal.sh ./RunFromTerminal.sh
fi

