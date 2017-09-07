# %load C:\Users\Rohit\Dropbox\Hanwen\code\normalbinomial.py
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import warnings
warnings.filterwarnings("ignore")
e = np.e


def f(n, p, x_range):
    x_min = x_range[0]
    x_max = x_range[1]
    k = np.arange(0, n + 1)
    x = np.linspace(0, n + 1, 1001)
    P_binom = binom.pmf(k, n, p)
    stddev = (n * p * (1 - p))**0.5
    P_norm = norm.pdf(x, n * p, stddev)
    fig = plt.gcf()
    fig.set_size_inches(20, 10)
    plt.plot(
        x,
        P_norm,
        'r',
        linewidth=2.0,
        label="N(%0.2f, %0.2f)" % (n * p, stddev**2))
    plt.plot(k, P_binom, '-', linewidth=2.0, label="Bin(%i, %0.2f)" % (n, p))
    plt.legend(fontsize=20)
    axes = plt.gca()
    axes.set_xlim([x_min, x_max])
    axes.set_ylim([0, 1.02 * max(max(P_binom), max(P_norm))])
    plt.title(
        'Normal Approximation of Binomial, %0.2f < x < %0.2f' % (x_min, x_max),
        fontsize=20)
    plt.xlabel('x', fontsize=20)
    plt.ylabel('y', fontsize=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    print('                   [%0.0f, %0.0f]' % (x_min, x_max))
    plt.show()
    x = np.linspace(0, n + 1, n + 1)
    P_norm = norm.pdf(x, n * p, stddev)
    print("")
    print('|| P_Normal - P_Binomial ||\u2081 = ', sum(abs(P_norm - P_binom)))
    print("")
    print("")


a = np.linspace(0, 5, 1001)
rng = e**a
interact(
    f,
    n=widgets.IntSlider(
        min=1, max=2000, step=1, value=30, continuous_update=False),
    p=widgets.FloatSlider(
        min=0, max=1, step=0.01, value=0.5, continuous_update=False),
    x_range=widgets.FloatRangeSlider(
        description="[a, b]",
        value=[0, 30],
        min=0,
        max=2000,
        step=1,
        readout=False))
