from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
def f(s, height):
    a = s[0]
    b = s[1]
    x = np.linspace(a,b,11)
    if b != a:
        y = np.array([1/(b-a)]*11)
    xrange = np.linspace(0, 10, 1001)
    cdf = []
    cdf.extend([0 for z in xrange if z<=a])
    cdf.extend([(z-a)/(b-a) for z in xrange if z>a and z<=b])
    cdf.extend([1 for z in xrange if z>b])
    if b < a + 1/height:
        #f = plt.figure()
        #ax = f.add_subplot(111)
        #plt.gcf().set_size_inches(20,10)
        #plt.gca().set_xlim([0, 10])
        #plt.gca().set_ylim([0, 2])
        #ax.text(0.5, 0.8,'Please choose a and b such that |b - a| > %0.2f' %height, ha='center', va='center', transform=ax.transAxes, fontsize = 40, color = 'r')
        if b != a:
            plt.plot(x, y, linewidth = 3.0, label = 'PDF')
        plt.gcf().set_size_inches(20,10)
        plt.gca().set_xlim([0, 10])
        plt.gca().set_ylim([0, 1.01*height])
        plt.xticks(fontsize = 16)
        plt.yticks(fontsize = 16)
        if b != a:
            plt.plot([a, a], [0, 1/(b-a)], 'g--', linewidth = 2.0)
            plt.plot([b, b], [0, 1/(b-a)], 'g--', linewidth = 2.0)
        plt.plot([(a + b)/2, (a + b)/2], [0, height,], 'm--', linewidth = 4.0)
        plt.plot((a + b)/2, max(height,1), 'm^', markersize = 20)
        plt.title('PDF of U(%0.2f,%0.2f)' %(a,b), fontsize = 20)
        plt.xlabel('x', fontsize = 20)
        plt.ylabel('y', fontsize = 20)
        #plt.plot(xrange, cdf, 'r', linewidth = 3.0, label = 'CDF')
        plt.legend(fontsize = 20)
        plt.plot()
    else:
        plt.plot(x, y, linewidth = 3.0, label = 'PDF')
        plt.gcf().set_size_inches(20,10)
        plt.gca().set_xlim([0, 10])
        plt.gca().set_ylim([0, 1.01*height])
        plt.xticks(fontsize = 16)
        plt.yticks(fontsize = 16)
        plt.plot([a, a], [0, 1/(b-a)], 'g--', linewidth = 2.0)
        plt.plot([b, b], [0, 1/(b-a)], 'g--', linewidth = 2.0)
        plt.title('PDF of U(%0.2f,%0.2f)' %(a,b), fontsize = 20)
        plt.xlabel('x', fontsize = 20)
        plt.ylabel('y', fontsize = 20)
        #plt.plot(xrange, cdf, 'r', linewidth = 3.0, label = 'CDF')
        plt.legend(fontsize = 20)
    plt.show()
   # plt.plot(n, sum(abs(y0 - y))/n, 'o')
   # plt.show()
    
w = widgets.FloatRangeSlider(
    description = "[a, b]",
    value=[4, 6],
    min=0,
    max=10,
    step=0.01,
    continuous_update = False)
interact(f, s = w, height = widgets.FloatSlider(description = "Maximum height", min = 1, max = 100, value = 0.5, step = 1, continuous_update = False))