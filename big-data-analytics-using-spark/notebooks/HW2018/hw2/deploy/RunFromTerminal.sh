date +%H.%M:%S:%N  
echo “copy files from S3 to HDFS”
/usr/bin/hdfs dfs -mkdir -p /twitter
/usr/bin/hdfs dfs -cp s3://mas-dse-open/Twitter/users-partition.pickle /twitter
/usr/bin/hdfs dfs -cp s3://mas-dse-open/Twitter/hw2-files-10mb.txt /twitter
/usr/bin/hdfs dfs -cp s3://mas-dse-open/Twitter/hw2-files-1gb.txt /twitter
/usr/bin/hdfs dfs -cp s3://mas-dse-open/Twitter/hw2-files-10gb.txt /twitter
/usr/bin/hdfs dfs -cp s3://mas-dse-open/Twitter/hw2-files-20gb.txt /twitter

date +%H.%M:%S:%N  
echo "RunFromTerminal done"
