import matplotlib.pyplot as plt
import numpy as np
import random
import math
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
pi = np.pi
theta = np.linspace(0, pi, 1001)
h = np.linspace(0, 1, 1001)
count = 0
X1 = []
X2 = []
Y1 = []
Y2 = []
count = 0
for i in range(1, 1001):
    H = random.choice(h)
    Theta = random.choice(theta)
    X1.append(-0.5 * np.cos(Theta))
    X2.append(+0.5 * np.cos(Theta))
    Y1.append(H - 0.5 * np.sin(Theta))
    Y2.append(H + 0.5 * np.sin(Theta))
    if Y1[i - 1] < 0 or Y2[i - 1] > 1:
        count += 1
plt.xlabel('x', fontsize=24)
plt.ylabel('y', fontsize=24)


def f(n):
    axes = plt.gca()
    fig = plt.gcf()
    fig.set_size_inches(20, 10)
    plt.plot(range(0, 1000), [0] * 1000, 'k', linewidth=7.0)
    plt.plot(range(0, 1000), [1] * 1000, 'k', linewidth=7.0)
    for i in range(0, len(X1)):
        off = 4 * (i + 1) / n
        X1[i] += off
        X2[i] += off
        plt.plot([X1[i], X2[i]], [Y1[i], Y2[i]], linewidth=3.0)
        X1[i] -= off
        X2[i] -= off
    axes.set_xlim([0, 4])
    axes.set_ylim([-0.5, 1.5])
    qr = divmod(n, 10)
    q = qr[0]
    if qr[1] != 0:
        n = n + 10 - qr[1]
        qr = divmod(n, 10)
        q = qr[0]
    x_ax = np.arange(0, n + 1, q)
    plt.xticks(np.linspace(0, 4, 11), fontsize=20)
    axes.set_xticklabels(x_ax)
    plt.yticks(fontsize=20)
    plt.show()


interact(f, n=widgets.IntSlider(min=10, max=1000))
