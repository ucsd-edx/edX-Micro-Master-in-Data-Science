import numpy as np
from YearPlotter import YearPlotter
from Eigen_decomp import Eigen_decomp
import matplotlib.pyplot as plt
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

class recon_plot:
    """A class for creating an interactive demonstration of approximating 
    a function with an orthonormal set of function"""
    def __init__(self,eigen_decomp,year_axis=False,fig=None,ax=None,interactive=False,Title=None):
        """ 

        :param eigen_decomp: An Eigen_decomp object that encapsulate the numerical calculations for the decomposition.
        :param year_axis: If True: assumes vectors of length 365 and plots month names on X axis
        :param fig: The fig environment for plotting
        :param ax: The axis environment for plotting (used for generating multi-plots)
        :param interactive: Set to True if you want to use the plot in an interactive reconstruction Widget.
        :param Title: A string to be used as the title of this plot.
        """
        self.eigen_decomp=eigen_decomp
        self.interactive=interactive
        self.fig=fig
        self.ax=ax
        self.Title=Title
        
        self.year_axis=year_axis
        self.yearPlotter=None
        if year_axis:
            self.yearPlotter=YearPlotter()
        self.plot_combination(**self.eigen_decomp.coeff)
        return None

    def get_widgets(self):
        """return the slider widget that are to be used

        :returns: widget_list: the list of widgets in order
                  widget_dict: a dictionary of the widget to be used in `interact

        :todo: make the sliders smaller: http://ipywidgets.readthedocs.io/en/latest/examples/Widget%20Styling.html
        """
        coeff=self.eigen_decomp.C
        widge_dict={}
        widge_list=[]
        for i in range(self.eigen_decomp.n):
            if coeff[i]>0:
                r=[0,coeff[i]*2]
            else:
                r=[coeff[i]*2,0]

            widge_list.append(widgets.FloatSlider(min=r[0],max=r[1],step=coeff[i]/10.,\
                                                  value=coeff[i],orientation='vertical',decription='v'+str(i)))
            widge_dict['c'+str(i)]=widge_list[-1]

        return widge_list,widge_dict

    def plot(self,y,label=''):
        if self.year_axis:
            self.yearPlotter.plot(y,self.fig,self.ax,label=label)
        else:
            self.ax.plot(self.eigen_decomp.x,y,label=label);

    def plot_combination(self,**coeff):
        """
        the plotting function that performs the actual rendering. It is called either directly (non-interactive) or by 
        `interactive` when used in a widget.

        :coeff: a dictionary that contains the name and value of each coefficient
        :returns: None

        """
        print 'in plot_combination', coeff,'\n'
        return None
#        if self.interactive or (self.fig is None):
        if self.fig is None:
            self.fig=plt.figure(figsize=(8,6))
            self.ax=self.fig.add_axes([0,0,1,1])
        else:
            self.fig.clear()

        A=self.eigen_decomp.mean
        self.plot(A,label='mean')

        for i in range(self.eigen_decomp.n):
            g=self.eigen_decomp.v[i]*coeff['c'+str(i)]
            A=A+g
            self.plot(A,label='cumul '+str(i))
        self.plot(self.eigen_decomp.f,label='target')
        self.ax.grid(figure=self.fig)        
        self.ax.legend()
        self.ax.set_title(self.Title)
        return None
    
