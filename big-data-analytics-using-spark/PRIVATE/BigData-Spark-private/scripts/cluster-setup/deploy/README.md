This script is to launch a Spark cluster on Amazon Web Services.

By default, the latest release of Spark will be deployed.

We use spot instances as the default scenarios. However, you can 
use on-demand instances by setting $SPOT_PRICE to empty.

The Ganglia monitoring for the cluster is set up by default. It
can be disabled by appending --no-ganglia option.

# Options:
* launch:
	* Launch a new cluster.
* resume:
	* In case slave nodes launches fails, restart setup process on
      existing cluster.
* stop:
	* Pause the cluster. Note that spot instances cannot be paused.
* restart:
	* Restart the stopped cluster.
* destroy:
	* Shutdown the cluster and deleting everything.
* login:
	* Login to the master node of the cluster.

Please refer to http://spark.apache.org/docs/latest/ec2-scripts.html
for more information on running Spark on EC2.
