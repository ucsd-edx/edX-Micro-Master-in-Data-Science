#This script is to be executed on all nodes, both master and workers

echo '====================General Bootstrap Starting======================'  

conda install astropy

#add some useful commands to the end of .bashrc
echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.bashrc
echo "export PROMPT_COMMAND='echo -n \"\$PWD \$ \" ' " >> ~/.bashrc
echo "cd /mnt/workspace/">> ~/.bashrc

echo '====================General Bootstrap Ending======================'  
