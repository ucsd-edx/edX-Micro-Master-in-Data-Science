from __future__ import print_function
from IPython.display import display
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import warnings
warnings.filterwarnings("ignore")
e = np.e
def f(n, p, α):
    k = np.arange(0, n+1)
    x = np.linspace(0, n+1, 1000)
    λ = n*p
    stddev = λ**0.5
    P_poisson = poisson.pmf(k, λ)
    P_binom = binom.pmf(k, n, p)
    plt.plot(k, P_poisson, 'r', label = "Poisson(%0.2f)" %λ)
    #plt.title('PMF of Poisson(%i)' %λ)
    #plt.xlabel('Number of Events')
    #plt.ylabel('Probability of Number of Events')
    P_binom_shifted = P_binom 
    fig = plt.gcf()
    fig.set_size_inches(20,10)
    plt.plot(k, P_binom, 'b-', label = "Bin(%i, %0.2f)" %(n,p))
    axes = plt.gca()
    axes.set_xlim([max(0,(1-e**α)*λ),min((1+e**α)*λ,n)])
    if n<10:
        axes.set_xlim([0,n])
    axes.set_ylim([0,1.02*max(max(P_binom_shifted),max(P_poisson))])
    w = e**α
    plt.title('Poisson Approximation of Binomial, |x - μ| < %0.1fσ' %(w), fontsize = 20)
    plt.xlabel('n', fontsize = 20)
    plt.ylabel('y', fontsize = 20)
    plt.legend(fontsize = 20)
    plt.xticks(fontsize = 16)
    plt.yticks(fontsize = 16)
    print('       %0.3f' %e**α)
    plt.show()
    print("")
    print('|| P_Poisson - P_Binomial ||\u2081 = ',sum(abs(P_poisson-P_binom)))
    print("")
    print("")
    #return e**α
interact(f, n=widgets.IntSlider(min=2, max=2000, step=1, value=15), p=widgets.FloatSlider(min=0.01, max=0.3, step=0.01, value=0.1), α = widgets.FloatSlider(description = 'Range', min=0,max=5,step=0.01, value = 3, readout = False))