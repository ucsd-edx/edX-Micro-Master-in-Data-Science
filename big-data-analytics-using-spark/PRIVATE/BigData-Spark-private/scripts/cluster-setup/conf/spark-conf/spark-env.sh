#!/usr/bin/env bash

export SPARK_LOCAL_DIRS="/mnt/spark"

# Standalone cluster options
export SPARK_MASTER_OPTS=""
if [ -n "1" ]; then
  export SPARK_WORKER_INSTANCES=1
fi
export SPARK_WORKER_CORES=4

export HADOOP_HOME="/root/ephemeral-hdfs"
export SPARK_MASTER_IP=ec2-52-4-159-110.compute-1.amazonaws.com
export MASTER=`cat /root/spark-ec2/cluster-url`

export SPARK_SUBMIT_LIBRARY_PATH="$SPARK_SUBMIT_LIBRARY_PATH:/root/ephemeral-hdfs/lib/native/"
export SPARK_SUBMIT_CLASSPATH="$SPARK_CLASSPATH:$SPARK_SUBMIT_CLASSPATH:/root/ephemeral-hdfs/conf"

# Bind Spark's web UIs to this machine's public EC2 hostname otherwise fallback to private IP:
export SPARK_PUBLIC_DNS=`
wget -q -O - http://169.254.169.254/latest/meta-data/public-hostname ||\
wget -q -O - http://169.254.169.254/latest/meta-data/local-ipv4`

# Used for YARN model
export YARN_CONF_DIR="/root/ephemeral-hdfs/conf"

# Set a high ulimit for large shuffles, only root can do this
if [ $(id -u) == "0" ]
then
    ulimit -n 1000000
fi
