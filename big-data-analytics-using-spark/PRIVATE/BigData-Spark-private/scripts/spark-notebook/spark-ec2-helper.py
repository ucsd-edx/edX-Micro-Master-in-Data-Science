#!/usr/bin/env python
'''
A script for launching a Spark cluster and an IPython notebook server on AWS

IMPORTANT: There can be only 1 running notebook. If you keep 2 notebooks
running, the second notebook will be pending forever until the first notebook
is shutdown.
'''

import argparse
import boto.ec2
import json
import os
import re
import select
import shutil
import subprocess
import sys
import time
import webbrowser
from os.path import expanduser
from urllib2 import urlopen
from IPython.lib import passwd

from local.Constants import *


def get_ipynb_config(password):
    if len(password) < 6:
        sys.exit('Password must be at least 6 characters long')
    return IPYNB_CONFIG % passwd(password)


def send_file(scp, src, tgt):
    os.system(' '.join(scp[:-1]) + ' ' + src + ' ' + scp[-1] + ':' + tgt)


def write_file(ssh, filepath, content):
    with open(".content.tmp", "w") as f:
        f.write(content)
    os.system("cat .content.tmp | " + ' '.join(ssh) + ' "cat > %s"' % filepath)
    os.remove(".content.tmp")


def send_command(command,
                 stdout_call_back=(lambda l: False),
                 stderr_call_back=(lambda l: False)):
    def data_waiting(source):
        return select.select([source], [], [], 0) == ([source], [], [])

    print 'Sending command:', ' '.join(command)
    command_output = subprocess.Popen(ssh + command,
                                      shell=False,
                                      stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)

    eof = False
    no_call_back = False
    while not eof:
        if data_waiting(command_output.stderr):
            command_stderr = command_output.stderr.readline()
            if not no_call_back:
                no_call_back = stderr_call_back(command_stderr)
        if data_waiting(command_output.stdout):
            command_stdout = command_output.stdout.readline()
            if not no_call_back:
                no_call_back = stdout_call_back(command_stdout)
            eof |= not command_stdout
        time.sleep(0.1)


def launch_notebook():
    # Parse the output of the launch_notebook.py command and exit
    # once the iPython Notebook server is launched
    def detect_launch_port(line):
        launch_match = re.search(
            "The Jupyter Notebook is running at:.*:(\d+)/", line)

        # Check if a new instance of iPython Notebook was launched
        # and open the URL in the default system browser
        if launch_match:
            port_no = launch_match.group(1)
            print("New iPython Notebook Launched, "
                  "opening http://%s:%s/" % (MASTER_URL, port_no))
            webbrowser.open("http://%s:%s/" % (MASTER_URL, port_no))
            sys.exit("Done.")
        return False

    send_command(["kill", "-9", "`pidof python2.7`"])
    time.sleep(3)
    send_command(["mkdir", "-p", "/root/ipython"])
    send_file(scp, './server/FilesIO.ipynb', '/root/ipython')
    send_command(["/root/spark/sbin/stop-all.sh"])
    send_command(["/root/spark/sbin/start-all.sh"])
    os.system(' '.join(ssh) + ' "nohup jupyter notebook '
                              '> jupyter.out 2> jupyter.err < /dev/null &"')
    time.sleep(10)
    send_command(["cat", "jupyter.err"],
                 stdout_call_back=detect_launch_port,
                 stderr_call_back=detect_launch_port)


def get_cluster_names(conn):
    names = []
    for instance in conn.get_only_instances():
        if instance.groups and instance.groups[0].name.endswith("-master"):
            names.append(instance.groups[0].name[:-7])
    if not names:
        sys.exit("No launched cluster exists.")
    return names


def get_master_url(conn, cluster_name):
    instances = conn.get_only_instances(
        filters={"instance.group-name": "%s-master" % cluster_name})
    if not instances:
        sys.exit("No master node exists in %s." % cluster_name)
    return instances[0].public_dns_name


def install_packages():
    # Install python dev
    send_command(["yum", "install", "-y", "python27-devel"])
    # Install pip
    send_command(["wget", "https://bootstrap.pypa.io/get-pip.py"])
    send_command(["python2.7", "get-pip.py"])
    # Install boto
    send_command(["pip", "install", "--upgrade", "boto"])
    # Install Jupyter
    send_command(["pip", "install", "--upgrade", "numpy"])
    send_command(["pip", "install", "--upgrade", "jupyter"])
    # Install matplotlib and networkx
    send_command(["yum", "install", "-y", "freetype-devel"])
    send_command(["yum", "install", "-y", "libpng-devel"])
    send_command(["yum", "install", "-y", "graphviz-devel"])
    send_command(["pip", "install", "--upgrade", "matplotlib"])
    send_command(["pip", "install", "--upgrade", "networkx"])
    send_command(["pip", "install", "--upgrade", "pygraphviz"])
    # Install requests
    send_command(["pip", "install", "--upgrade", "requests"])
    # Jupyter helper functions
    send_file(scp, "./server/init_sc.py", "~")
    send_file(scp, "./server/s3helper.py", "~")
    # Sync Python2.7 libraries
    send_command(["/root/spark-ec2/copy-dir",
                  "/usr/local/lib64/python2.7/site-packages/"])


def check_security_groups(cluster_name):
    '''
    Add current IP address to the security group.
    '''
    security_group_name = cluster_name + "-master"

    # Open http://httpbin.org/ip to get the public ip address
    ip_address = '0.0.0.0/0' # json.load(urlopen('http://httpbin.org/ip'))['origin']

    # Check for the security group and create it if missing
    for sg in conn.get_all_security_groups():
        if sg.name == security_group_name:
            tcp_rule = False

            # Verify the security group has the current ip address in it
            for rule in sg.rules:
                if (str(rule.ip_protocol) == "tcp" and
                        str(rule.from_port) == "0" and
                        str(rule.to_port) == "65535" and
                        str(ip_address) in str(rule.grants)):
                        # str(ip_address) + "/32" in str(rule.grants)):
                    print(str(ip_address) + " (TCP) is already added to " +
                          security_group_name + " security group")
                    tcp_rule = True

            # If the current ip address is missing from
            # the security group then add it
            if not tcp_rule:
                print("Adding " + str(ip_address) + " (TCP) to " +
                      security_group_name + " security group")
                # Allow all TCP
                sg.authorize('tcp', 0, 65535, str(ip_address))
                # sg.authorize('tcp', 0, 65535, str(ip_address) + "/32")


def get_ssh_command(MASTER_URL):
    return (["ssh", "-i", KEY_IDENT_FILE,
             "%s@%s" % (LOGIN_ID, MASTER_URL),
             "-o", "StrictHostKeyChecking=no"],
            ["scp", "-i", KEY_IDENT_FILE,
             "-o", "StrictHostKeyChecking=no",
             "%s@%s" % (LOGIN_ID, MASTER_URL)])


def connect_aws():
    try:
        return boto.ec2.connect_to_region(
            REGION,
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    except Exception, e:
        sys.exit("There was an error connecting to AWS: %s" % e)


def get_launch_command(resume=False):
    BASE_COMMAND = (("%s/ec2/spark-ec2 --key-pair=%s --identity-file=%s " +
                     "--region=%s --zone=%s --slaves=%s --instance-type=%s " +
                     "--spot-price=%s --authorized-address=%s " +
                     "--hadoop-major-version=yarn --use-existing-master ") %
                    (SPARK_PATH, KEY_PAIR, KEY_IDENT_FILE, REGION, ZONE,
                     SLAVES, INSTANCE_TYPE, SPOT_PRICE, AUTHORIZED_ADDR))
    if resume:
        return BASE_COMMAND + " launch --resume " + CLUSTER_NAME
    return BASE_COMMAND + " launch " + CLUSTER_NAME


def list_files(remote):
    def _print(s):
        print s,
        return False
    send_command(["ls", "-lrt", remote],
                 stdout_call_back=_print,
                 stderr_call_back=_print)


def download(remote, local):
    os.system("mkdir -p local")
    send_command(["mv", "/root/ipython/metastore_db", "/root"])
    os.system("scp -i %s %s -r %s %s"
              % (KEY_IDENT_FILE, NO_HOST_CHECK, remote, local))
    send_command(["mv", "/root/metastore_db", "/root/ipython"])


def upload(local, remote):
    if os.path.isdir(local):
        send_command(["mkdir", "-p", remote])
        os.system("scp -i %s %s -r %s %s"
                  % (KEY_IDENT_FILE, NO_HOST_CHECK,
                     os.path.join(local, '*'), remote))
    elif os.path.isfile(local):
        os.system("scp -i %s %s %s %s"
                  % (KEY_IDENT_FILE, NO_HOST_CHECK,
                     local, remote))
    else:
        sys.exit("%s doesn't exist." % local)


def initialize():
    conn = connect_aws()
    MASTER_URL = get_master_url(conn, CLUSTER_NAME)
    ssh, scp = get_ssh_command(MASTER_URL)
    return conn, MASTER_URL, ssh, scp


if __name__ == "__main__":
    if sys.version_info.major != 2:
        sys.exit("Only support Python 2.")

    parser = argparse.ArgumentParser(
        description="Launch a Spark cluster on AWS and then start an "
                    "ipython notebook server")

    parser.add_argument('-l', '--launch', dest='launch', action='store_true',
                        default=False,
                        help='Launch a new Spark cluster and then install '
                             'IPython Notebook')
    parser.add_argument('-r', '--resume', dest='resume', action='store_true',
                        default=False, help='Restart the setup process on the '
                                            'existing Spark cluster')
    parser.add_argument('-d', '--destroy', dest='destroy', action='store_true',
                        default=False, help='Terminate the Spark cluser')
    parser.add_argument('-i', '--ipython', dest='ipython', action='store_true',
                        default=False,
                        help='Start IPython Notebook server on '
                             'the Spark cluster')
    parser.add_argument('--show', action='store_true', default=False,
                        help='Show the names of all launched clusters.')
    parser.add_argument('--list', const='/root/ipython', nargs='?',
                        help='List all files under a remote directory. If not '
                             'specified, list files under the working '
                             'directory')
    parser.add_argument('--download', nargs=2,
                        metavar=("REMOTE_PATH", "LOCAL_PATH"),
                        help='Download the remote directory to local')
    parser.add_argument('--upload', nargs=2,
                        metavar=("LOCAL_PATH", "REMOTE_PATH"),
                        help='Upload a local file/directory to a remote '
                             'directory')
    parser.add_argument('-p', '--password', default='csedse321', dest='passwd',
                        help='Specify password for notebook '
                             '(if missing will use the default password)')
    parser.add_argument('-n', '--workers', default='2', dest='workers',
                        help='Number of worker nodes to launch in '
                             'the Spark cluster (default: 2)')
    parser.add_argument('-a', '--name', default='demo-cluster', dest='name',
                        help='Name of the Spark cluster, used for '
                             'distinguishing between multiple clusters '
                             '(default: demo-cluster).')

    args = vars(parser.parse_args())

    PASSWD = args['passwd']
    SLAVES = args['workers']
    CLUSTER_NAME = args['name']

    os.environ["AWS_ACCESS_KEY_ID"] = AWS_ACCESS_KEY_ID
    os.environ["AWS_SECRET_ACCESS_KEY"] = AWS_SECRET_ACCESS_KEY

    if args['show']:
        conn = connect_aws()
        print "Launched clusters:", ', '.join(get_cluster_names(conn))
        sys.exit('Done.')
    elif args['list'] or args['download'] or args['upload']:
        conn, MASTER_URL, ssh, scp = initialize()
        remote_path = "root@%s:" % MASTER_URL
        NO_HOST_CHECK = "-o StrictHostKeyChecking=no"
        if args["list"]:
            list_files(args["list"])
        elif args["download"]:
            remote, local = args["download"]
            remote = remote_path + remote
            download(remote, local)
        else:
            local, remote = args["upload"]
            remote = remote_path + remote
            upload(local, remote)
        sys.exit("Done.")
    elif (args['launch'] + args['resume'] +
          args['destroy'] + args['ipython'] != 1):
        sys.exit("Please select one and only one action.")

    if args['destroy']:
        command = ("%s/ec2/spark-ec2 --region=%s destroy %s" %
                   (SPARK_PATH, REGION, CLUSTER_NAME))
        os.system(command)
        sys.exit("Done.")
    elif args['ipython']:
        conn, MASTER_URL, ssh, scp = initialize()
        check_security_groups(CLUSTER_NAME)
    else:
        # Launch a Spark cluster
        resume = args['resume']
        command = get_launch_command(resume)
        os.system(command)
        conn, MASTER_URL, ssh, scp = initialize()

        # Write .bashrc
        write_file(ssh, "~/.bashrc", BASHRC)

        # Set up IPython Notebook
        write_file(ssh, IPY_CONFIG_FILE_PATH, IPY_CONFIG)
        write_file(ssh, IPYNB_CONFIG_FILE_PATH, get_ipynb_config(PASSWD))
        install_packages()
        check_security_groups(CLUSTER_NAME)
    launch_notebook()

    print "Failed."
