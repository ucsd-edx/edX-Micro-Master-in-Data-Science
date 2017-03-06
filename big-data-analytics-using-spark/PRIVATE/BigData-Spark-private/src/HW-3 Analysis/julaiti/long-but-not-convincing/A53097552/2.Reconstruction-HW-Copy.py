
# coding: utf-8

# In[ ]:

# Name: Ankit Singh
# Email: ans049@eng.ucsd.edu
# PID: A53097552


# In[1]:

get_ipython().magic(u'pwd')
get_ipython().magic(u'pylab inline')


# In[2]:

data_dir = "./Data/Weather/"
get_ipython().magic(u'matplotlib inline')
get_ipython().system(u'mkdir -p $data_dir')
get_ipython().system(u'ls $data_dir')


# ### Downloading Pickled data from S3
# If `SampleStations.pickle` is not in the directory, get it using the following command

# In[12]:

get_ipython().system(u'curl -o $data_dir/SampleStations.pickle http://mas-dse-open.s3.amazonaws.com/Weather/SampleStations.pickle')


# ### Plot Reconstructions
# 
# From each measurement, we take 2 sample stations with low residual error and 2 sample stations with high residual error and plot the following:
# 
# * Original Data Vector
# * Mean Vector
# * Reconstructed Data Vector using mean and top 1 eigen vectors
# * Reconstructed Data Vector using mean and top 2 eigen vectors
# * Reconstructed Data Vector using mean and top 3 eigen vectors

# ### Read and Preprocess data
# 
# Read data from the pickle files `SampleStations.pickle` and `STAT.pickle`
# 
# * `SampleStations.pickle` contains information about the 6 measurements taken from some sample stations. You have been provided the code to process this file. It converts the seemingly complicated structure into a list of lists where each sublist has the following information:
# 
# `['station','measurement','year','1', '2', '3', ...... , '365']`
# 
# *  station - The station ID
# *  measurement - One of the 6 types of measurements
# *  year - The year in which the measurements were recorded
# *  1-365 - The actual value of measurement for each day of the year
# 
# 
# 
# * `STAT.pickle` contains statistics about the weather data for each of the 6 measurements and its description.

# In[3]:

import pickle
Data=pickle.load(open('./Data/Weather/SampleStations.pickle','r'))
STAT,STAT_description=pickle.load(open('./Data/Weather/STAT.pickle','r'))


# In[4]:

FlatData=[]
for station in Data:
    stationname=station[0]
    for measurements in station[1]:
        measurement,year=measurements[0]
        yeardata=list(measurements[1])
        rowData=[stationname]+[measurement]+[year]+yeardata
        FlatData.append(rowData)


# In[5]:

import pandas as pd

frameheader=['station','measurement','year']+range(1,366)
df=pd.DataFrame(FlatData,columns=frameheader)

m_df={}
for m in ['TMIN', 'TOBS', 'TMAX', 'SNOW', 'SNWD', 'PRCP']:
    t_df=df[df['measurement']==m]
    m_df[m]=t_df    


# In[6]:

def reconstruction_k(vectors , mean , final):
    Reconstructed =[]
    #Reconstructed.append(null)
    newmat = np.matrix(vectors)
    #print shape(mean),shape(newmat)
    matrix2 = newmat - mean
    #matrix2[isnan(matrix2)]=0
    Reconstructed.append([])
    for i in range(1,4):
        Prod=matrix2*final[:,:i]
        Recon=array(final[:,:i]*Prod.transpose()+mean[:,np.newaxis])
        Reconstructed.append(Recon)
    return Reconstructed
    
    


# ### Define Reconstruction Function
# 
# You need to plot reconstructions for two stations with low reconstruction error and two stations with high reconstruction error. To do this, you will need to do the following:
# 
# 1. Calculate the reconstruction error for the data vector reconstructed using mean and top-3 eigenvectors.
# 2. Remove the ones for which reconstruction error is NaN.
# 3. Choose two with the lowest and two with the highest reconstruction error for plotting.

# In[7]:

def create_reconstructions(m):  
    
    ## Put your code for computating reconstructions here
    matrix = np.matrix(m_df[m].iloc[:,3:])
    Mean  = STAT[m]['Mean']
    matrix2 = matrix - Mean
    matrix2[isnan(matrix2)]=0
    meas = m
    eigval = STAT[meas]['eigval']
    eigv   = STAT[meas]['eigvec']
    #idx = eigval.argsort()[::-1]   
    #eigv = eigv[:,idx]
    final = eigv[:,:3] ##top 3 eigen vector 
    Prod=matrix2*final;
    Recon=array(final*Prod.transpose()+Mean[:,np.newaxis])
    #print shape(Recon)
    Recon = Recon.transpose()
    #print shape(Recon)
    matrix = np.array(matrix)
    dist = (Recon - matrix)**2
    dist = np.sum(dist, axis=1)
    dist = np.sqrt(dist)
    #err = np.asarray(dist).reshape(-1)
    err=dist
    #err= np.array(err)
    res = []
    for i in range(0,len(err)):
        if (isnan(err[i])== False):
            res.append(i)
    errnew = err[res]
    matrixnew = matrix[res] # matrix od data vector without nan
    Recon = Recon[res]
    err_idx_min = errnew.argsort()
    err_idx_max = errnew.argsort()[::-1]
    top2min = err_idx_min[:2]
    top2max = err_idx_max[:2]
    top2minmatrix = matrixnew[top2min]
    top2maxmatrix = matrixnew[top2max]
    Reconmin = Recon[top2min]
    Reconmax = Recon[top2min]
    
    original = np.asarray(top2minmatrix)
    Reconstructed = reconstruction_k(top2minmatrix,Mean,final)
    #print shape(Reconstructed)
    lower = [0,1]
    yeardays=[i for i in (1,366)]
    plt.figure(figsize=(20,30),dpi=300)
    j=1
    c=0
    for l in lower:
        subplot(4,2,j)
        j+=1
        c+=1
        plot(original[l])
        #plot(np.asarray(original[l]).reshape(-1))
        plot(STAT[m]['Mean'])
        #plot(Reconmin[l])
        plot(Reconstructed[1][:,l])
        plot(Reconstructed[2][:,l])
        plot(Reconstructed[3][:,l])
        title('#' + str(c) + ' Sample for ' + m + ' (low residual error)')
        xlim([0,365])
        legend(['original','Mean','1','2','3'],loc=2)
    
    c=0
    original = np.asarray(top2maxmatrix)
    Reconstructed = reconstruction_k(top2maxmatrix,Mean,final)
    upper =[1,0]
    for l in upper:
        subplot(4,2,j)
        j+=1
        c+=1
        plot(original[l])
        #plot(np.asarray(original[l]).reshape(-1))
        plot(STAT[m]['Mean'])
        #plot(Reconmax[l])
        plot(Reconstructed[1][:,l])
        plot(Reconstructed[2][:,l])
        plot(Reconstructed[3][:,l])
        title('#' + str(c) + ' Sample for ' + m + ' (high residual error)')
        xlim([0,365])
        legend(['original','Mean','1','2','3'],loc=2)
        


# In[8]:

for m in ['TMAX','SNWD']:
    print 'Reconstruction Plots for '+ m
    create_reconstructions(m)


# In[ ]:



