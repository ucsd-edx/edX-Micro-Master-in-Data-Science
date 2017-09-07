# %load C:\Users\Rohit\Dropbox\Hanwen\code\stirling.py
import matplotlib.pyplot as plt
import numpy as np
import random
import math
from ipywidgets import interact, interactive, fixed, interact_manual, ToggleButton, Layout
import ipywidgets as widgets
pi = np.pi
e = np.e
s = []
sb = []
c = []
x = 0
for i in range(1, 91):
    temp = 0.5*np.log(2*pi*i) + i*np.log(i/e)
    s.append(temp)
    sb.append(temp + 1/(12*i))
for i in range(1, 91):
    x += np.log(i)
    c.append(x)
S = np.array(s)
Sb = np.array(sb)
C = np.array(c)
def f(Higher_order_approximation, n):
    Sn = S[0:n]
    Sbn = Sb[0:n]
    Cn = C[0:n]
    fig = plt.gcf()
    fig.set_size_inches(12,6)
    axes = plt.gca()
    axes.set_ylim([0.92,1.005])
    axes.set_xlim([1,n])
    handles, labels = axes.get_legend_handles_labels()
    axes.legend(handles, labels)
    #matplotlib.legend_handler(fontsize = 11)
    if n <= 30:
        plt.xticks(np.linspace(1,n,n))
    else:
        qr = divmod(n, 10)
        xmarks = np.linspace(0,n,11)
        q = qr[0]
        if qr[1] != 0:
            n0 = n - qr[1]
            #qr = divmod(n0, 10)
            #q = qr[0]
            if n>70:
                xmarks = np.linspace(0,n0-10,11)
            else:
                xmarks = np.linspace(0,n0,11)
            xmarks = np.append(xmarks, n)
        plt.xticks(xmarks)
        axes.set_xlim([1,n])
    stir = plt.plot(range(1, n+1), e**(Sn-Cn),'b-', label = "s[n]/n!")
    if Higher_order_approximation:
        stirb = plt.plot(range(1, n+1), e**(Sbn-Cn),'g-', label = "s*[n]/n!")
    plt.plot(range(1, n+1), [1]*n, 'r')
    plt.legend( prop={'size': 16})
    plt.show()
    print("ln s(n) = ", S[n-1], "    ln n! = ", C[n-1], "     s(n)/n! = ", e**(S[n-1]-C[n-1]), "     Error = ", e**(S[n-1]-C[n-1])-1)
    if Higher_order_approximation:
        print("Higher Order Approximation Error = ", e**(Sb[n-1]-C[n-1])-1)
interact(f, Higher_order_approximation = ToggleButton(value=False, description = 'Higher order approximation s*[n]', layout=Layout(width='25%', height='40px')), n = widgets.IntSlider(min = 2, max = 90))

def g(Higher_order_approximation, n):
    Sn = S[0:n]
    Cn = C[0:n]
    Sbn = Sb[0:n]
    fig = plt.gcf()
    fig.set_size_inches(16,8)
    plt.plot(range(1, n+1), e**C[0:n], 'r', label = 'n!')
    plt.plot(range(1, n+1), e**S[0:n], 'b', label = "s[n]")
    axes = plt.gca()
    axes.set_xlim([1,n])
    plt.xticks(np.linspace(1,n,n))
    if Higher_order_approximation:
        plt.plot(range(1, n+1), e**Sb[0:n], 'g', label = "s*[n]")
    plt.legend( prop={'size': 16})
    plt.show()
interact(g, Higher_order_approximation = ToggleButton(value=False, description = 'Higher order approximation s*[n]', layout=Layout(width='25%', height='40px')), n = widgets.IntSlider(min = 2, max = 20))