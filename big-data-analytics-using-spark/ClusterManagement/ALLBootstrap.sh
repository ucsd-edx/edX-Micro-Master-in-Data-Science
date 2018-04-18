#This script is to be executed on all nodes, both master and workers

echo '====================General Bootstrap Starting======================'  
echo $PATH
env
#/mnt/anaconda/bin/conda install astropy

sudo easy_install-3.4 pip
sudo pip-3.4 install --upgrade pip
# export PATH="/usr/local/bin:$PATH"
sudo pip-3.4 install astropy

#add some useful commands to the end of .bashrc
echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.bashrc
echo "export PROMPT_COMMAND='echo -n \"\$PWD \$ \" ' " >> ~/.bashrc
echo "cd /mnt/workspace/">> ~/.bashrc

echo '====================General Bootstrap Ending======================'  
