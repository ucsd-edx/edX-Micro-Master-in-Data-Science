from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import warnings
warnings.filterwarnings("ignore")

pr = 0.2
X = np.random.geometric(p=pr, size=1000)
r = 0.2
Power = r**X
EPower = []

for i in range(1, 1001):
    EPower.append(sum(Power[0:i]) / i)


def f(n_max):
    EPower_trunc = EPower[0:n_max]
    x = np.arange(1, n_max + 1)
    plt.plot(x, EPower_trunc, linewidth=3.0)
    plt.plot(x, [(pr**2) / (1 - pr + pr**2)] * len(x), 'r', linewidth=5.0)
    #plt.title("Exponential(%.2f)" %λ, fontsize = 20)
    plt.gcf().set_size_inches(20, 10)
    axes = plt.gca().set_xlim([1, n_max])
    axes = plt.gca().set_ylim([0, pr])
    plt.xlabel('n', fontsize=20)
    plt.ylabel('y', fontsize=20)
    # plt.title('PMF of Geometric(%0.2f)' % p, fontsize=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.legend(fontsize=18)
    plt.show()


interact(
    f,
    n_max=widgets.IntSlider(min=100, max=1000, step=1, value=10), )
