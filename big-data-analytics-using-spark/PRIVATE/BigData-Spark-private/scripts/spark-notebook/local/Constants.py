import os
import sys

AWS_ACCESS = [
    ("Research account",
        ("AKIAIARSR4ULGIOZOORA", "P4bsCShOwko52wIL3Oiz44jNnIhDpJVhDCxQ25Vj"),
        ("jalafate-ucsd", "./server/jalafate-ucsd.pem")),
    ("CSE255 account",
        ("AKIAJZG24PJ7QPEZ323A", "ElzLC/JltZPL25+rYfhUIriBesZw4jA4m8UYG4Gp"),
        ("cse255", "./server/cse255.pem"))
]

LOGIN_ID = "root"

REGION = "us-east-1"
# ZONE = "us-east-1c"
ZONE = "us-east-1b"
INSTANCE_TYPE = "r3.2xlarge"
SPOT_PRICE = 0.5

SLAVES = 2
CLUSTER_NAME = "demo-cluster"
AUTHORIZED_ADDR = "0.0.0.0/0"

PASSWD = "csedse321"
IPY_CONFIG_FILE_PATH = (
    "/root/.ipython/profile_default/ipython_config.py")
IPY_CONFIG = '''c = get_config()
c.InteractiveShellApp.exec_files = ["/root/s3helper.py", "/root/init_sc.py"]
'''
IPYNB_CONFIG_FILE_PATH = (
    "/root/.ipython/profile_default/ipython_notebook_config.py")
IPYNB_CONFIG = '''c = get_config()
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.notebook_dir = '/root/ipython'
c.NotebookApp.password = u'%s'
'''

BASHRC = '''
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

export SPARK_HOME=/root/spark
export PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH
export PYTHONPATH=$SPARK_HOME/python/lib/py4j-0.9-src.zip:$PYTHONPATH
export PYSPARK_PYTHON=python2.7

# Source global definitions
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi
'''

SPARK_PATH = os.getenv("SPARK_HOME", '')

if not SPARK_PATH:
    sys.exit("SPARK_HOME is not set.")
