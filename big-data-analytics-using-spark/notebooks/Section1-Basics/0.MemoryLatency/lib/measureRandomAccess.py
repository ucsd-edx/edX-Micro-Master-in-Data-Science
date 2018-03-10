import numpy as np
from numpy.random import rand
import time

def measureRandomAccess(sz,filename='',k=1000,batch=100):
    """Measure the distribution of random accesses in computer memory.

    :param sz: size of memory block.
    :param filename: a file that is used as an external buffer. If filename=='' then everything is done    :param k: number of times that the experiment is repeated.
    :param batch: The number of locations poked in a single experiment (multiple pokes performed using numpy, rather than python loop)
    :returns: (_mean,std,T):
              _mean = the mean of T
              _std = the std of T
              T = a list the contains the times of all k experiments
    :rtype: tuple

    """

    if filename == '':  #Using main memory as storage
        # Prepare buffer.
        A=np.zeros(sz,dtype=np.int8)

        # Read and write k*batch times from/to buffer.
        sum=0; sum2=0
        T=np.zeros(k)
        for i in range(k):
            if (i%100==0): print('\r',i, end=' ')
            loc=np.int32(rand(batch)*sz)
            
            t=time.time()       # ------------------------------------
            x=A[loc]            # Measured piece, read and write
            A[loc]=loc
            d=(time.time()-t)/batch # ------------------------------------

            T[i]=d
            sum += d
            sum2 += d*d
        _mean=sum/k; _vard=(sum2/k)-_mean**2;
        _std=np.sqrt(_vard*batch)

    else:                   # Using external storage (disk /SSD)
        file=open(filename,'r+')
        
        # Read and write k times from/to buffer.
        sum=0; sum2=0
        T=np.zeros(k)
        for i in range(k):
            if (i%10000==0): print('\r',i, end=' ')
            loc=int(rand()*sz)

            t=time.time()       # ------------------------------------
            file.seek(loc)      #  Measured piece, seek read and write
            poke=file.read(1)
            file.write("X")
            d=time.time()-t     # ------------------------------------

            T[i]=d
            sum += d
            sum2 += d*d
        _mean=sum/k; _var=(sum2/k)-_mean**2; _std=np.sqrt(_var)
        
        file.close()
    return (_mean,_std,T)
