# %load pdf_shade
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import warnings
warnings.filterwarnings("ignore")
e = np.e
pi = np.pi
def f(x_range, y_max, shade):
    x_min = x_range[0]
    x_max = x_range[1]
    a = shade[0]
    b = shade[1]
    x = np.linspace(-100, 100, 10001)
    σ = 1**0.5
    μ = 0
    P_norm = norm.pdf(x, μ, σ)
    fig = plt.gcf()
    fig.set_size_inches(16,8)
    plt.plot(x, P_norm, 'b', linewidth=3.0, label = "PDF")
    #if CDF == True:
      #  CDF_norm = norm.cdf(x, μ, σ)
       # plt.plot(x, CDF_norm, 'r', linewidth=3.0, label = "CDF")
    y0 = (1/(σ*np.sqrt(2*pi)))*np.exp(-((a-μ)**2)/(2*σ**2))
    y1 = (1/(σ*np.sqrt(2*pi)))*np.exp(-((b-μ)**2)/(2*σ**2))
    plt.plot([a, a], [0, y0], 'm--', linewidth = 2.0, label = '$\mu\pm\sigma$')
    plt.plot([b, b], [0, y1], 'm--', linewidth = 2.0)
    plt.gca().fill_between(x, P_norm, where = ((x>a) & (x<b)), facecolor='cyan')
    axes = plt.gca()
   # w = e**α
    axes.set_xlim([x_min, x_max])
    axes.set_ylim([0,y_max])
    #plt.xlabel('Number of Successes')
    #plt.ylabel('Probability of Successes')
    #print('                   [%0.0f, %0.0f]' %(x_min, x_max))
   # plt.xticks([])
   # plt.yticks([])
    plt.axis('off') # turns off axis
#    plt.savefig('name.pdf')
    plt.savefig('name.png', transparent=True)
    plt.show()

interact(f, μ=widgets.FloatSlider(description = '$\mu$', min=-50, max=50, step=0.1, value=0, continuous_update = False), var=widgets.FloatSlider(description = '$\sigma^2$', min=0.5, max=30, step=0.1, value=1, continuous_update = False), x_range = widgets.IntRangeSlider(description = "$[x_{min},  x_{max}]$",
    value=[-5, 5],
    min=-10,
    max=10,
    step=1, continuous_update = False), y_max=widgets.FloatSlider(description = '$y_{max}$', min=0.1, max=1, step=0.1, value=0.5, continuous_update = False), CDF = widgets.ToggleButton(value = False), shade = widgets.FloatRangeSlider(description = "Shaded region", value = [-1,1] , min = -5, max = 5, step = 0.2, readout = False))
         
         #α = widgets.FloatSlider(description = "Range", min=0,max=5,step=0.01,value = 1.5, readout=False, continuous_update = False))
