# Plots the Markov bound as a function of a

import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets

def plot_markov(μ):

    a_min = μ
    a_max = μ*20

    a = np.linspace(a_min, a_max, 10001)

    plt.gcf().set_size_inches(16,8)

    plt.plot(a, μ/a, 'b', linewidth=3.0)
    plt.plot([μ,μ],[0,1.1])

    plt.gca().set_xlim([0, a_max])
    plt.gca().set_ylim([0,1.1])
    plt.title('Markov\'s bound $P(X\geq a)\leq\mu/a$ for $\mu=$%0.1f' %(μ), fontsize = 20)
    plt.grid()

    plt.xticks(fontsize = 16)
    plt.xticks(np.linspace(μ, 20*μ, 20), fontsize = 16)
    plt.yticks(fontsize = 16)
    plt.xlabel('a', fontsize = 20)
    plt.ylabel('$P(X\geq a)$', fontsize = 20)

    plt.show()

widgets.interact(plot_markov, μ=widgets.FloatSlider(description = '$\mu$', min=0.5, max=20, step=0.1, value=8, continuous_update = False))
