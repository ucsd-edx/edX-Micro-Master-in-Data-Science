
# coding: utf-8

# In[ ]:

# Name: Ankit Singh
# Email: ans049@eng.ucsd.edu
# PID: A53097552


# ## Homework 3
# 
# You will have to submit the following two completed ipython notebooks for this homework.
# 
# 1. PCA_analysis
# 2. Reconstruction

# In[1]:

get_ipython().magic(u'pylab inline')
data_dir = "./Data/Weather/"


# ### Downloading Pickled data from S3
# If `STAT.pickle` is not in the directory, get it using the following command

# In[ ]:

get_ipython().system(u'curl -o $data_dir/STAT.pickle http://mas-dse-open.s3.amazonaws.com/Weather/STAT.pickle')


# ### Get the statistics from the Pickle File

# In[2]:

import pickle
STAT,STAT_description=pickle.load(open(data_dir+'/STAT.pickle','r'))


# In[3]:

STAT.keys()


# In[4]:

STAT_description


# In[5]:

Scalars=['mean','std','low1000','low100','high100','high1000']
for meas in STAT.keys():
    get_ipython().system(u"grep $meas './Data/Weather/ghcnd-readme.txt'")
    S=STAT[meas]
    for scalar in Scalars:
        print '%s:%f'%(scalar,S[scalar]),
    print


# ### Script for plotting yearly plots 

# In[16]:

def YearlyPlots(T,ttl='',yl='',xl='',y=None,x=None,size=(10,7), c=None):
    yearday=[i for i in range(1,366)]
    fig=figure(1,figsize=size,dpi=300)
    if shape(T)[0] != 365:
        raise ValueError("First dimension of T should be 365. Shape(T)="+str(shape(T)))
    if c is not None:
        plot_date(yearday,T, '-',color=c);
    else:
        plot_date(yearday,T, '-', );
    # rotate and align the tick labels so they look better
    #fig.autofmt_xdate()
    ylabel(yl)
    xlabel(xl)
    if y is not None:
        ylim(y)
    if x is not None:
        xlim(x)
    grid()
    title(ttl)


# ### Plot the following 3 plots for each measurement:
# 
# 1. A histogram from the sample values (from SortedVals) restricted between low1000 and high1000
# 2. Plot of mean and mean $\pm$ std
# 3. Number of measurements recorded each day

# In[18]:

figure(figsize=(15,30))
offset=1
for meas in STAT.keys():
    subplot(6,3,offset)
    offset+=1
    ## Your code for Histogram
    lowlevel = STAT[meas]['low100']
    highlevel = STAT[meas]['high100']
    dataarray = STAT[meas]['SortedVals']
    #tmp = sc.parallelize(STAT[meas]['SortedVals']).filter(lambda x : x >= lowlevel and x <= highlevel).collect()
    tmp = [x for x in dataarray if x>=lowlevel and x<= highlevel]
    hist(tmp,bins=100)
    title(meas+' restricted Hist')
    display()
    ##Histogram ends
    subplot(6,3,offset)
    offset+=1
    ## Your code for mean and mean +- std
    mean = STAT[meas]['Mean']
    std =  sqrt(STAT[meas]['Var'])
    YearlyPlots(mean,ttl=meas+' mean +- std',c='red')
    YearlyPlots(mean+std,ttl=meas+' mean +- std',c='blue')
    YearlyPlots(mean-std,ttl=meas+' mean +- std',c='blue')
    #YearlyPlots(val.collect(),ttl=meas+' mean +- std')
    ##mean 
    subplot(6,3,offset)
    offset+=1
    ## Your code for number of measurements
    YearlyPlots(STAT[meas]['NE'],ttl = meas+' Counts',c='black')


# ### Plot the Number of measurements recorded each day for TMAX

# In[19]:

YearlyPlots(STAT['TMAX']['NE'],ttl ='TMAX Counts',c ='black')


# ### Extra Credit
# * Can you figure out what is the reason for these lower counts (especially at the beginning and end of the year and also the sudden dip at the end of each month)? Is it restricted to a subset of the stations? Suggest a way to remove this effect.
# 
# * Can you Explain the counts per day for "SNWD" ?
# 
# Provide your explanation in new markdown cells appended after this cell. Support your explanation
# using code cells and graphs. If you need more data that is available only in the full dataset in the cloud but not in the data you have downloaded, contact your TA.
# 

# ### Plot the following 3 plots for each measurement:
# 
# 1. The percentage of variance explained by top-k eigen vectors for k between 1 to 9
# 2. Plot of mean and mean $\pm$ std
# 3. Plot of top 3 eigenvectors

# In[20]:

figure(figsize=(15,30))
offset=1
for meas in STAT.keys():
    subplot(6,3,offset)
    offset+=1
    ## Your code for percentage of variance explained
    eigval = STAT[meas]['eigval']
    eigv   = STAT[meas]['eigvec']
    #eigvs = eigv[eigval.argsort()[::-1]]
    idx = eigval.argsort()[::-1]   
    D = eigval[idx]
    eigv = eigv[:,idx]
    D= ([0,]+list(cumsum(D[:9])))/sum(D)
    plot(D)
    subplot(6,3,offset)
    offset+=1
    ## Your code for mean and mean +- std
    mean = STAT[meas]['Mean']
    std =  sqrt(STAT[meas]['Var'])
    YearlyPlots(mean,ttl=meas+' mean +- std',c='red')
    YearlyPlots(mean+std,ttl=meas+' mean +- std',c='blue')
    YearlyPlots(mean-std,ttl=meas+' mean +- std',c='blue')
    subplot(6,3,offset)
    offset+=1
    ## Your code for top-3 eigenvectors
    YearlyPlots((eigv[:,:3]),ttl=meas+' Top 3 EigenVecs')


# In[ ]:



