from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
def f(n, λ):
    k = np.arange(0, n+1)
    P_poisson = poisson.pmf(k, λ)
    plt.plot(k, P_poisson, '-o')
    plt.title('PMF of Poisson(%i)' %λ)
    plt.xlabel('Number of Events')
    plt.ylabel('Probability of Number of Events')
    plt.show()
interact(f, n=widgets.IntSlider(min=0, max=50, step=1, value=25), λ=widgets.FloatSlider(min=0, max=30, step=0.1, value=5))