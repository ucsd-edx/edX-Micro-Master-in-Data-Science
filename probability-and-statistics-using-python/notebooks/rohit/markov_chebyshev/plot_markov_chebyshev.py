# Plots the Markov and Chebyshev bounds as a function of a

import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets

def plot_markov(μ, σ):

    a_min = μ
    a_max = min(μ*20,σ*10)

    a = np.linspace(a_min, a_max, 10001)
    plt.plot(a, μ/a, 'b', linewidth=3.0, label='$\mu/a$')

    b_min = μ+σ
    b = np.linspace(b_min, a_max, 10001)
    plt.plot(b, (σ/(b-μ))**2, 'r', linewidth=3.0, label='$(a-\mu)/\sigma^2$')
    plt.plot([μ,μ],[0,1.1])
    plt.plot([μ+σ,μ+σ],[0,1.1],'r')
    plt.legend(fontsize = 30)

    plt.title('Markov and Chebyshev bounds on $P(X\geq a)$ for $\mu=$%0.1f and $\sigma=$%0.1f' %(μ,σ), fontsize = 20)
    plt.grid()
  
    xticks_array = np.concatenate((np.linspace(μ, np.ceil(a_max/μ)*μ, int(np.ceil(a_max/μ))), np.array([0, μ+σ])))
    #xticks_array=[0,μ+σ]+xticks_array
    plt.xticks(xticks_array, fontsize = 16)
    plt.yticks(np.linspace(0.2, 1, 5), fontsize = 16)
    plt.xlabel('a', fontsize = 20)
    plt.ylabel('Probability bounds', fontsize = 20)
    plt.gcf().set_size_inches(16,8)
    plt.gca().set_xlim([0, a_max])
    plt.gca().set_ylim([0,1.1])
    plt.show()

widgets.interact(plot_markov, μ=widgets.FloatSlider(description = '$\mu$', min=0.5, max=20, step=0.1, value=8, continuous_update = False), 
σ=widgets.FloatSlider(description = '$\sigma$', min=0.5, max=20, step=0.1, value=5, continuous_update = False))
