# This script is to launch a Spark cluster on Amazon Web Services.
#
# By default, the latest release of Spark will be deployed.
#
# We use spot instances as the default scenarios. However, you can 
# use on-demand instances by setting $SPOT_PRICE to empty.
#
# The Ganglia monitoring for the cluster is set up by default. It
# can be disabled by appending --no-ganglia option.
#
# Options:
#   launch:
#       Launch a new cluster.
#   resume:
#       In case slave nodes launches fails, restart setup process on
#       existing cluster.
#   stop:
#       Pause the cluster. Note that spot instances cannot be paused.
#   restart:
#       Restart the stopped cluster.
#   destroy:
#       Shutdown the cluster and deleting everything.
#   login:
#       Login to the master node of the cluster.

if ! [[ $(python --version 2>&1) == *2\.7* ]]; then
      echo "Error: Only support python 2.7.";
      exit 1
fi

if [ -z "$SPARK_PATH" ] ; then
    echo 'Please set $SPARK_PATH variable to the Spark installed path.'
    exit 1
fi

if [[ $# -eq 0 ]] ; then
    echo 'Please choose an action among: launch, resume, stop, restart and destroy.'
    exit 1
fi

# Your access key can be obtained from the AWS homepage by clicking
# Account > Security Credentials > Access Credentials, or from
# whoever added you to their AWS account.
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""

# Your key pairs can be created at the AWS EC2 homepage by clicking
# Key Pairs -> Create Key Pair
# Note: the access permission of the identity file (key_name.pem) 
# must be 600, otherwise the launch will fail.
export KEY_PAIR=""
export KEY_IDENT_FILE=""

# Default instance type: r3.xlarge
# The spot instances pricing history can be viewed at the AWS EC2
# homepage by clicking Spot Requests -> Pricing History
export REGION=us-east-1
export ZONE=us-east-1c
export INSTANCE_TYPE="r3.xlarge"
export SPOT_PRICE=0.2

# Cluster details
export SLAVES=4
export CLUSTER_NAME="cse255-cluster"
export AUTHORIZED_ADDR="52.20.136.234/32"
# export AUTHORIZED_ADDR=0.0.0.0/0



if [ $1 = "launch" ]; then
    if [ -z "$SPOT_PRICE" ]; then
        $SPARK_PATH/ec2/spark-ec2 --key-pair=$KEY_PAIR --identity-file=$KEY_IDENT_FILE --region=$REGION --zone=$ZONE --slaves=$SLAVES --instance-type=$INSTANCE_TYPE --authorized-address=$AUTHORIZED_ADDR --use-existing-master launch $CLUSTER_NAME
    else
        $SPARK_PATH/ec2/spark-ec2 --key-pair=$KEY_PAIR --identity-file=$KEY_IDENT_FILE --region=$REGION --zone=$ZONE --slaves=$SLAVES --instance-type=$INSTANCE_TYPE --spot-price=$SPOT_PRICE --authorized-address=$AUTHORIZED_ADDR --use-existing-master launch $CLUSTER_NAME
    fi
elif [ $1 = "resume" ]; then
     $SPARK_PATH/ec2/spark-ec2 --key-pair=$KEY_PAIR --identity-file=$KEY_IDENT_FILE --region=$REGION --zone=$ZONE --slaves=$SLAVES --instance-type=$INSTANCE_TYPE --spot-price=$SPOT_PRICE --authorized-address=$AUTHORIZED_ADDR --use-existing-master launch --resume $CLUSTER_NAME
elif [ $1 = "stop" ]; then
    $SPARK_PATH/ec2/spark-ec2 --region=$REGION stop $CLUSTER_NAME
elif [ $1 = "restart" ]; then
    $SPARK_PATH/ec2/spark-ec2 -i $KEY_IDENT_FILE --region=$REGION start $CLUSTER_NAME
elif [ $1 = "destroy" ]; then
    $SPARK_PATH/ec2/spark-ec2 --region=$REGION destroy $CLUSTER_NAME
elif [ $1 = "login" ]; then
    $SPARK_PATH/ec2/spark-ec2 -k $KEY_PAIR -i $KEY_IDENT_FILE --region=$REGION login $CLUSTER_NAME
else
    echo "Cannot recognize the parameter."
fi

