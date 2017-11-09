import numpy as np
from math import sqrt

def ComputeStatistics(P,x,y):
    P/=np.sum(P) # normalize the disttribution
    Px=np.sum(P,axis=0) # compute marginals
    Py=np.sum(P,axis=1)
    Ex=np.dot(Px,x)
    Ey=np.dot(Py,y)
    Ex2=np.dot(Px,x**2)
    Ey2=np.dot(Py,y**2)
    stdx=sqrt(Ex2-Ex**2)
    stdy=sqrt(Ey2-Ey**2)
    
    nx=x-Ex
    ny=y-Ey
    
    cov=np.dot(P.flatten(), np.outer(ny,nx).flatten())
    corr=cov/(stdx*stdy)
    return {
        'P':P,
        'x':x,
        'y':y,
        'Px':Px,
        'Py':Py,
        'Ex':Ex,
        'Ey':Ey,
        'stdx':stdx,
        'stdy':stdy,
        'cov':cov,
        'corr':corr
    }
