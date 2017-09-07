from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import warnings
warnings.filterwarnings("ignore")


def f(p, n_max, CDF):
    x = np.arange(1, n_max + 1)
    y = [((1 - p)**(z - 1)) * p for z in x]
    z = [(1 - (1 - p)**zz) for zz in x]
    plt.plot(x, y, 'o-', label='PDF')
    if CDF == True:
        plt.plot(x, z, 'ro-', label='CDF')
    #plt.title("Exponential(%.2f)" %λ, fontsize = 20)
    plt.gcf().set_size_inches(20, 10)
    axes = plt.gca().set_xlim([1, n_max])
    if n_max == 1:
        axes = plt.gca().set_xlim([0, 1])
        plt.plot([0, 1], [p, p], 'b')
        plt.xticks([1])
    plt.xlabel('n', fontsize=20)
    plt.ylabel('y', fontsize=20)
    plt.title('PMF of Geometric(%0.2f)' % p, fontsize=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.legend(fontsize=18)
    plt.show()


interact(
    f,
    p=widgets.FloatSlider(min=0, max=1, step=0.01, value=0.5),
    n_max=widgets.IntSlider(min=1, max=1000, step=1, value=10),
    CDF=widgets.ToggleButton(False))
