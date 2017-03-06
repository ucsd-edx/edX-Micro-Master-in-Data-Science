
# Install pip
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
rm get-pip.py
pip install uwsgi

# Run software
cd /root
git clone https://github.com/arapat/simple-spark-jobserver.git 
mkdir store
mkdir store/archive store/output store/result store/runtime store/upload
cd simple-spark-jobserver
pip install -r requirements.txt
cd server
wsgi -s /tmp/uwsgi.sock --module server --callable app & disown
chmod 666 /tmp/uwsgi.sock

adduser cse255
chown -R cse255 /root/store
touch executor-out executor-err
chown cse255 executor.py executor-out executor-err
cd /home/cse255
mkdir .ssh
cp ~/.ssh/authorized_keys .ssh/
chown -R cse255 .ssh

# Install nginx
yum install nginx

# now configure nginx, then `/etc/init.d/nginx restart`
# Then login as cse255, run
#     python executor.py > executor-out 2> executor-err & disown

