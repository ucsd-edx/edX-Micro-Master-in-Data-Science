if [[ $# -eq 0 ]] ; then
    echo 'Error: Please specify the work directory.'
    exit 0
fi

export SPARK_PATH=/Users/yoavfreund/spark-latest/
export PYSPARK_DRIVER_PYTHON="jupyter"
export PYSPARK_DRIVER_PYTHON_OPTS="notebook"
# Uncomment next line if the default python on your system is python3
# export PYSPARK_PYTHON=python3
cd "$1"
$SPARK_PATH/bin/pyspark --master local[2]
