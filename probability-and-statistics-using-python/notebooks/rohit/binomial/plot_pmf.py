from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets


def f(n, p):
    k = np.arange(0, n + 1)
    P_binom = binom.pmf(k, n, p)
    plt.plot(k, P_binom, '-o')
    axes = plt.gca()
    axes.set_xlim([0, n])
    axes.set_ylim([0, 1.1 * max(P_binom)])
    plt.title('PMF of Bin(%i, %.2f)' % (n, p))
    plt.xlabel('Number of Successes')
    plt.ylabel('Probability of Successes')
    plt.show()


interact(
    f,
    n=widgets.IntSlider(min=0, max=30, step=1, value=15),
    p=widgets.FloatSlider(min=0, max=1, step=0.01, value=0.5))
