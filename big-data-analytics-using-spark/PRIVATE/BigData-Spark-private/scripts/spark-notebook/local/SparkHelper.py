import boto.ec2
import imp
import json
import os
import re
import requests
import select
import shutil
import subprocess
import sys
import time
import webbrowser
from multiprocessing import Pool, Process
from os.path import expanduser
from urllib2 import urlopen
from IPython.lib import passwd

from Constants import *


def call_spark_ec2(argv):
    spark_ec2 = imp.load_source('spark_ec2',
                                SPARK_PATH + '/ec2/spark_ec2.py')
    sys.argv = argv
    try:
        spark_ec2.main()
    except:
        return False
    return True


class SparkHelper:
    def __init__(self):
        self.ready = None
        self.dead = False

    def init_account(self, _id):
        (self.AWS_NAME,
            (self.AWS_ACCESS_KEY_ID, self.AWS_SECRET_ACCESS_KEY),
            (self.KEY_PAIR, self.KEY_IDENT_FILE)) = AWS_ACCESS[int(_id)]
        self.conn = boto.ec2.connect_to_region(
            REGION,
            aws_access_key_id=self.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=self.AWS_SECRET_ACCESS_KEY)
        os.environ["AWS_ACCESS_KEY_ID"] = self.AWS_ACCESS_KEY_ID
        os.environ["AWS_SECRET_ACCESS_KEY"] = self.AWS_SECRET_ACCESS_KEY

    def init_cluster(self, name):
        def get_master_url():
            instances = self.conn.get_only_instances(
                filters={"instance.group-name": "%s-master" % name})
            if not instances:
                print "No master node exists in %s." % name
                return ''
            return instances[0].public_dns_name

        self.name = name
        self.master_url = get_master_url()
        options = ["-i", self.KEY_IDENT_FILE, "-o", "StrictHostKeyChecking=no",
                   "%s@%s" % (LOGIN_ID, self.master_url)]
        self.ssh = ["ssh"] + options
        self.scp = ["scp", "-r"] + options
        self.check_security_groups()

    def send_command(self, command,
                     stdout_call_back=(lambda l: False),
                     stderr_call_back=(lambda l: False)):

        def data_waiting(source):
            return select.select([source], [], [], 0) == ([source], [], [])

        print 'Sending command:', ' '.join(command)
        p = subprocess.Popen(self.ssh + command, shell=False,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        out, err = '', ''
        while True:
            if data_waiting(p.stderr):
                _stderr = p.stderr.readline()
                err = err + _stderr
                stderr_call_back(_stderr)
            if data_waiting(p.stdout):
                _stdout = p.stdout.readline()
                out = out + _stdout
                stdout_call_back(_stdout)
                if not _stdout:
                    break
            time.sleep(0.1)
        return out, err

    def get_cluster_names(self):
        names = []
        for instance in self.conn.get_only_instances():
            if instance.groups and instance.groups[0].name.endswith("-master"):
                names.append(instance.groups[0].name[:-7])
        return names

    def write_file(self, filepath, content):
        with open(".content.tmp", "w") as f:
            f.write(content)
        os.system("cat .content.tmp | " +
                  ' '.join(self.ssh) + ' "cat > %s"' % filepath)
        os.remove(".content.tmp")

    def send_file(self, src, tgt):
        command = (' '.join(self.scp[:-1]) + ' ' +
                   src + ' ' + self.scp[-1] + ':' + tgt)
        print command
        p = subprocess.Popen(command.split(), shell=False,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if p.poll() == 0:
            return None
        return err

    def get_file(self, src, tgt):
        command = (' '.join(self.scp[:-1]) + ' ' +
                   self.scp[-1] + ':' + src + ' ' + tgt)
        print command
        p = subprocess.Popen(command.split(), shell=False,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if p.poll() == 0:
            return None
        return err

    def list_files(self, path):
        out, err = self.send_command(["ls", "-lrt", path])
        return '\n'.join([out, err])

    def download(self, remote, local):
        os.system("mkdir -p local")
        self.send_command(["mv", "/root/ipython/metastore_db", "/root"])
        r = self.get_file(remote, local)
        self.send_command(["mv", "/root/metastore_db", "/root/ipython"])
        return r

    def upload(self, local, remote):
        if os.path.exists(local):
            r = self.send_file(local, remote)
        else:
            r = "%s doesn't exist." % local
        return r

    def destroy(self):
        command = ("%s/ec2/spark-ec2 --region=%s destroy %s" %
                   (SPARK_PATH, REGION, self.name))
        print command
        p = subprocess.Popen(command.split(), shell=False,
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        p.communicate(input="y\n")

    def check_security_groups(self):
        '''
        Add current IP address to the security group.
        '''
        security_group_name = self.name + "-master"

        # Open http://httpbin.org/ip to get the public ip address
        ip_address = json.load(urlopen('http://httpbin.org/ip'))['origin']

        # Check for the security group and create it if missing
        for sg in self.conn.get_all_security_groups():
            if sg.name == security_group_name:
                break

        # Verify the security group has the current ip address in it
        tcp_rule = False
        for rule in sg.rules:
            if (str(rule.ip_protocol) == "tcp" and
                    str(rule.from_port) == "0" and
                    str(rule.to_port) == "65535" and
                    str(ip_address) + "/32" in str(rule.grants)):
                print(str(ip_address) + " (TCP) is already added to " +
                      security_group_name + " security group")
                tcp_rule = True

        # If the current ip address is missing from
        # the security group then add it
        if not tcp_rule:
            print("Adding " + str(ip_address) + " (TCP) to " +
                  security_group_name + " security group")
            # Allow all TCP
            sg.authorize('tcp', 0, 65535, str(ip_address) + "/32")

    def launch_notebook(self):
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
                      "opening http://%s:%s/" % (self.master_url, port_no))
                webbrowser.open("http://%s:%s/" % (self.master_url, port_no))
                return True
            return False

        self.send_command(["kill", "-9", "`pidof python2.7`"])
        time.sleep(3)
        self.send_command(["mkdir", "-p", "/root/ipython"])
        if os.path.exists('./Credentials.ipynb'):
            self.send_file('./Credentials.ipynb', '/root/ipython')
        self.send_file('./server/FilesIO.ipynb', '/root/ipython')
        self.send_command(["/root/spark/sbin/stop-all.sh"])
        self.send_command(["/root/spark/sbin/start-all.sh"])
        command = ' '.join(self.ssh) + (' "nohup jupyter notebook '
                                        '> jupyter.out 2> jupyter.err '
                                        '< /dev/null &"')
        print command
        os.system(command)
        print "Jupyter notebook launched."

    def launch_spark(self, name,
                     num_of_workers=SLAVES, passwd=PASSWD, resume=False):
        self.name, self.workers, self.passwd = name, num_of_workers, passwd
        self.ready = self.dead = False
        # Launch a Spark cluster
        argv = [SPARK_PATH + "/ec2/spark-ec2",
                "--key-pair=" + self.KEY_PAIR,
                "--identity-file=" + self.KEY_IDENT_FILE,
                "--region=" + REGION, "--zone=" + ZONE,
                "--slaves=%d" % int(num_of_workers),
                "--instance-type=" + INSTANCE_TYPE,
                "--spot-price=" + str(SPOT_PRICE),
                "--hadoop-major-version=yarn", "--use-existing-master",
                "launch"]
        if resume:
            argv.append("--resume")
        argv.append(name)
        self.timer = time.time()
        pool = Pool(processes=1)
        pool.apply_async(call_spark_ec2, args=[argv],
                         callback=self.setup_spark)
        pool.close()

    def setup_spark(self, is_finished):
        def install_packages():
            # Install python dev
            self.send_command(["yum", "install", "-y", "python27-devel"])
            # Install pip
            self.send_command(["wget", "https://bootstrap.pypa.io/get-pip.py"])
            self.send_command(["python2.7", "get-pip.py"])
            # Install boto
            self.send_command(["pip", "install", "--upgrade", "boto"])
            # Install Jupyter
            self.send_command(["pip", "install", "--upgrade", "numpy"])
            self.send_command(["pip", "install", "--upgrade", "jupyter"])
            # Install matplotlib and networkx
            self.send_command(["yum", "install", "-y", "freetype-devel"])
            self.send_command(["yum", "install", "-y", "libpng-devel"])
            self.send_command(["yum", "install", "-y", "graphviz-devel"])
            self.send_command(["pip", "install", "--upgrade", "matplotlib"])
            self.send_command(["pip", "install", "--upgrade", "networkx"])
            self.send_command(["pip", "install", "--upgrade", "pygraphviz"])
            # Install requests
            self.send_command(["pip", "install", "--upgrade", "requests"])
            # Jupyter helper functions
            self.send_file("./server/init_sc.py", "~")
            self.send_file("./server/s3helper.py", "~")
            # Sync Python2.7 libraries
            self.send_command(["/root/spark-ec2/copy-dir",
                               "/usr/local/lib64/python2.7/site-packages/"])

        if not is_finished:
            self.dead = True
            print "Launching Spark failed."
            return

        print "setting up cluster..."
        self.init_cluster(self.name)

        # Write .bashrc
        self.write_file("~/.bashrc", BASHRC)

        # Set up IPython Notebook
        self.write_file(IPY_CONFIG_FILE_PATH, IPY_CONFIG)
        self.write_file(IPYNB_CONFIG_FILE_PATH,
                        IPYNB_CONFIG % passwd(self.passwd))
        install_packages()

        self.ready = True
        self.duration = int(time.time() - self.timer)
        print "The cluster is up! Total: %d seconds." % self.duration

    def check_notebook(self):
        try:
            requests.get("http://%s:8888" % self.master_url)
            print "Notebook ready."
            return None
        except:
            p = Process(target=self.launch_notebook)
            p.start()
            return p
