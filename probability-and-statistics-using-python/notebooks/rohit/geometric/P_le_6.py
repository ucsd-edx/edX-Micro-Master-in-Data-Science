from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import warnings
warnings.filterwarnings("ignore")

X = np.random.geometric(p=0.2, size=5000)
P6 = []

for i in range(1, 5001):
    X_trunc = X[0:i]
    X6 = X_trunc[X_trunc <= 6]
    P6.append(len(X6) / len(X_trunc))


def f(n_max):
    P6n = P6[0:n_max]
    plt.gcf().set_size_inches(20, 10)
    plt.plot(np.arange(1, n_max + 1), P6n)
    plt.plot(np.arange(1, n_max + 1), [1 - 0.8**6] * n_max, 'r', linewidth=3.0)
    plt.show()


interact(f, n_max=widgets.IntSlider(min=1, max=5000, step=1, value=100))

