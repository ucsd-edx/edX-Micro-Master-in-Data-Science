import numpy as np
from YearPlotter import YearPlotter
import matplotlib.pyplot as plt
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

class recon_plot:
    """A class for creating an interactive demonstration of approximating 
    a function with an orthonormal set of function"""
    def __init__(self,x,f,mean,v,year_axis=False,labels=None):
        """ Initialize the widget

        :param x: defines the x locations
        :param f: the function to be approximated
        :param mean: The initial approximation (the mean)
        :param v: a list of numpy.arrays that are the eigenvectors
        :param: year_axis: set to true if X axis should correspond to the months of the year.
        :returns: None
        """
        error_header='recon_plot error:\n'
        err=error_header
        # Todo: test parameters for type and orthonormality.
        #if type(v) != list:
        #    err+='recon_plot: type of parameter v is'+)
        self.v=v
        self.x=x
        self.mean=mean
        self.U=np.vstack(v)
        self.f=f
        self.startup_flag=True
        self.C=np.dot(self.U,np.nan_to_num(f)-mean)
        #print 'nan=',sum(isnan(f))
        self.n,self.m=np.shape(self.U)
        self.coeff={'c'+str(i):self.C[i] for i in range(len(self.C))} 
        #print self.coeff
            
        self.year_axis=year_axis
        self.yearPlotter=None
        if year_axis:
            self.yearPlotter=YearPlotter()
        self.plot_combination(**self.coeff)
        return None
        
    def get_widgets(self):
        """return the slider widget that are to be used

        :returns: widget_list: the list of widgets in order
                  widget_dict: a dictionary of the widget to be used in `interact

        :todo: make the sliders smaller: http://ipywidgets.readthedocs.io/en/latest/examples/Widget%20Styling.html
        """
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
    
    def plot(self,y,label=''):
        if self.year_axis:
            self.yearPlotter.plot(y,self.fig,self.ax,label=label)
        else:
            self.ax.plot(self.x,y,label=label);

    def plot_combination(self,**coeff):
        """the plotting function that is called by `interactive`
           generates the plot according the the parameters set by the sliders

        :returns: None
        """
        if self.startup_flag:
            self.startup_flag=False
            
        self.A=self.mean
        self.fig=plt.figure(figsize=(8,6))
        self.ax=self.fig.add_axes([0,0,1,1])
        self.plot(self.A,label='mean')

        for i in range(self.n):
            g=self.v[i]*coeff['c'+str(i)]
            self.A=self.A+g
            self.plot(self.A,label='c'+str(i))
        self.plot(self.f,label='target')
        self.ax.grid(figure=self.fig)        
        self.ax.legend()
        return None
    