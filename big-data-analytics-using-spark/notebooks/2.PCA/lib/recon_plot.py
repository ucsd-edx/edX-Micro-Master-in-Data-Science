import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

class recon_plot:
    """A class for creating an interactive demonstration of approximating 
    a function with an orthonormal set of function"""
    def __init__(self,x,f,mean,v):
        """ initialize the Widget

        :param x: defines the x locations
        :param f: the function to be approximated
        :param mean: The initial approximation (the mean)
        :param v: a list of numpy.arrays the are the eigenvectors
        :returns: None
        """
        self.v=v
        self.x=x
        self.mean=mean
        self.U=np.vstack(v)
        self.f=f
        self.C=np.dot(self.U,f-mean)
        self.n,self.m=np.shape(self.U)
        self.coeff={'c'+str(i):self.C[i] for i in range(len(self.C))} 
        self.plot_combination(**self.coeff)
        return None
        
    def get_widgets(self):
        coeff=self.C
        widge_dict={}
        widge_list=[]
        for i in range(self.n):
            if coeff[i]>0:
                r=[0,coeff[i]*2]
            else:
                r=[coeff[i]*2,0]

            widge_list.append(widgets.FloatSlider(min=r[0],max=r[1],step=coeff[i]/10.,\
                                                  value=coeff[i],orientation='vertical',decription='v'+str(i)))
            widge_dict['c'+str(i)]=widge_list[-1]

        return widge_list,widge_dict

    def get_C(self):
        return self.C
    
    def plot_combination(self,**coeff):
        self.A=self.mean
        self.fig=plt.figure(figsize=(8,6))
        self.ax=self.fig.add_axes([0,0,1,1])
        #print coeff.keys()
        for i in range(self.n):
            g=self.v[i]*coeff['c'+str(i)]
            self.A=self.A+g
            self.ax.plot(self.x,self.A,label='sum '+str(i+1));
        self.ax.plot(self.x,self.f,label='target')
        plt.legend()
        plt.grid()
        return None
    
