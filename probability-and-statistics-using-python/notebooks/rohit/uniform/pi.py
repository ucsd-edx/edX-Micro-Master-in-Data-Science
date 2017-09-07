# %load C:\Users\Rohit\Dropbox\Hanwen\code\pi2.py
import matplotlib.pyplot as plt
import numpy as np
import random
import math
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import itertools
pi = np.pi
x = np.linspace(-1, 1, 1001)
x_scatter = []
y_scatter = []
redx = []
redy = []
for i in range(1, 10001):
    x_rand = random.choice(x)
    y_rand = random.choice(x)
    x_scatter.append(x_rand)
    y_scatter.append(y_rand)
    if (x_rand)**2 + (y_rand)**2 <= 1:
        redx.append(x_rand)
        redy.append(y_rand)
    else:
        redx.append(-10)
        redy.append(-10)
Pi_emp = []
for i in range(1, 10001):
    x_plot = x_scatter[0:i]
    y_plot = y_scatter[0:i]
    circle = [j for j in range(0, i) if (x_plot[j])**2 + (y_plot[j])**2 <= 1]
    Pi_emp.append(4 * len(circle) / i)


def f(n):
    x_plot = x_scatter[0:n]
    y_plot = y_scatter[0:n]
    redx_plot = redx[0:n]
    redy_plot = redy[0:n]
    plt.subplot(1, 2, 1)
    plt.plot(x_plot, y_plot, 'g.')
    plt.plot(redx_plot, redy_plot, 'r.')
    plt.plot([-1, 1], [1, 1], 'k', linewidth=5.0)
    plt.plot([-1, 1], [-1, -1], 'k', linewidth=5.0)
    plt.plot([-1, -1], [-1, 1], 'k', linewidth=5.0)
    plt.plot([1, 1], [-1, 1], 'k', linewidth=5.0)
    x = np.linspace(-1, 1, 101)
    y = (1 - x * x)**0.5
    plt.plot(x, y, 'b', linewidth=5.0)
    y = -y
    plt.plot(x, y, 'b', linewidth=5.0)
    fig = plt.gcf()
    fig.set_size_inches(16, 8)
    axes = plt.gca()
    axes.set_ylim([-1.1, 1.1])
    axes.set_xlim([-1.1, 1.1])
    plt.subplot(1, 2, 2)
    axes = plt.gca()
    axes.set_ylim([min(Pi_emp), max(Pi_emp)])
    plt.plot(np.arange(1, 10001), [pi] * 10000, 'b', linewidth=3.0)
    plt.plot(np.arange(1, 10001), Pi_emp, 'g')
    plt.plot(n, Pi_emp[n - 1], 'ro', markersize=7)
    plt.show()
    print(Pi_emp[n - 1])


#interact(f, n = widgets.IntSlider(min = 10, max = 10000))
play = widgets.Play(
    interval=20,
    value=10000,
    #min=10,
    max=10000,
    step=10,
    description="Press play",
    disabled=False,
    show_repeat=False)
slider = widgets.IntSlider(min=10, max=10000, step=10)
widgets.jslink((play, 'value'), (slider, 'value'))
interact(
    f,
    n=slider, )
widgets.HBox([play, slider])
