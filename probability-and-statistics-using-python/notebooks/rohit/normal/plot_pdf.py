# Plots pdf of a normal distribution

import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets

from scipy.stats import norm

e = np.e
pi = np.pi

def plot_pdf(μ, var, x_range, y_max, CDF):
'''
Takes mean, variance, range of x and y axes, and whether CDF desired.
Plots PDF, and optionally CDF.
'''
    x_min = x_range[0]
    x_max = x_range[1]
    x = np.linspace(-100, 100, 10001)
    σ = var**0.5
    P_norm = norm.pdf(x, μ, σ)
    fig = plt.gcf()
    fig.set_size_inches(16,8)
    plt.plot(x, P_norm, 'b', linewidth=3.0, label = "PDF")
    if CDF == True:
        CDF_norm = norm.cdf(x, μ, σ)
        plt.plot(x, CDF_norm, 'r', linewidth=3.0, label = "CDF")
    y0 = (1/(σ*np.sqrt(2*pi)))*np.exp(-0.5)
    ym = 1/(σ*np.sqrt(2*pi))
    plt.plot([μ-σ, μ-σ], [0, y0], 'm--', linewidth = 2.0, label = '$\mu\pm\sigma$')
    plt.plot([μ+σ, μ+σ], [0, y0], 'm--', linewidth = 2.0)
    plt.plot([μ,μ], [0,ym], 'g--', linewidth = 2.0, label = r'$\mu$')
    plt.legend(fontsize = 20)
    axes = plt.gca()
   # w = e**α
    axes.set_xlim([x_min, x_max])
    axes.set_ylim([0,y_max])
    plt.title('PDF of N(%0.2f, %0.2f), %0.2f < x < %0.2f' %(μ,var,x_min,x_max), fontsize = 20)
    #plt.xlabel('Number of Successes')
    #plt.ylabel('Probability of Successes')
    #print('                   [%0.0f, %0.0f]' %(x_min, x_max))
    plt.xticks(fontsize = 16)
    plt.yticks(fontsize = 16)
    plt.xlabel('x', fontsize = 20)
    plt.ylabel('y', fontsize = 20)
    plt.show()
a = np.linspace(0, 5, 1001)
rng = e**a
widgets.interact(plot_pdf, μ=widgets.FloatSlider(description = '$\mu$', min=-50, max=50, step=0.1, value=0, continuous_update = False), var=widgets.FloatSlider(description = '$\sigma^2$', min=0.5, max=30, step=0.1, value=1, continuous_update = False), x_range = widgets.IntRangeSlider(description = "$[x_{min},  x_{max}]$",
    value=[-25, 25],
    min=-100,
    max=100,
    step=1, continuous_update = False), y_max=widgets.FloatSlider(description = '$y_{max}$', min=0.1, max=1, step=0.1, value=0.5, continuous_update = False), CDF = widgets.ToggleButton(value = False))
         
         #α = widgets.FloatSlider(description = "Range", min=0,max=5,step=0.01,value = 1.5, readout=False, continuous_update = False))
