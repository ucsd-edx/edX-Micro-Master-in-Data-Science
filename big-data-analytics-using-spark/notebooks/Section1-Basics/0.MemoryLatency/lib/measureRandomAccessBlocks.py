# %load lib/measureRandomAccess.py
import numpy as np
from numpy.random import rand
import time

def measureRandomAccessMemBlocks(sz,k=1000,batch=100):
    """Measure the distribution of random accesses in computer memory.

    :param sz: size of memory block.
    :param k: number of times that the experiment is repeated.
    :param batch: The number of locations poked in a single experiment (multiple pokes performed using numpy, rather than python loop)
    :returns: (_mean,std,T):
              _mean = the mean of T
              _std = the std of T
              T = a list the contains the times of all k experiments
    :rtype: tuple

    """
    # Prepare buffer.
    A=np.zeros(sz,dtype=np.int8)
            
    # Read and write k*batch times from/to buffer.
    sum=0; sum2=0
    T=np.zeros(k)
    for i in range(k):
        if (i%100==0): print('\r',i, end=' ')
        loc=np.int32(rand(batch)*sz)
        t=time.time()
        x=A[loc]
        A[loc]=loc
        d=(time.time()-t)/batch
        T[i]=d
        sum += d
        sum2 += d*d
    _mean=sum/k; var=(sum2/k)-_mean**2; _std=np.sqrt(var)
    return (_mean,_std,T)
