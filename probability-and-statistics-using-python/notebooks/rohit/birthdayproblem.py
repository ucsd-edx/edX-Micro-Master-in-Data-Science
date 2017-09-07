import matplotlib.pyplot as plt
import numpy as np
import random
import itertools
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

def cartesian(A, B):
    C = []
    for i in itertools.product(A, B):
        C.append(i)

    return C
n = list(range(1,25))
n = np.asarray(n)
y = []
r = 1
for i in n:
    r *= (366-i)/365
    y.append(r)

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
days = np.arange(1,32)
dates = cartesian(months, days)
dates.remove(('February',29))
dates.remove(('February',30))
dates.remove(('February',31))
dates.remove(('April',31))
dates.remove(('June',31))
dates.remove(('September',31))
dates.remove(('November',31))
random.seed(1)
def iterate(Iterations):
    P_emp = []
    for n in range(1, 25):
        count = 0
        for ite in range(1, Iterations+1):
            randate = []
            for i in range(1, n+1):
                randate.append(random.choice(dates))
            if len(set(randate)) == n:
                count += 1
        P_emp.append(count/Iterations)
    n = list(range(1,25))
    n = np.asarray(n)
    y = []
    r = 1
    for i in n:
        r *= (366-i)/365
        y.append(r)
    plt.plot(n, y, 'o-')
    plt.plot(n, [0.5]*24)
    plt.plot(n, P_emp, 'ro-')
    plt.xlabel('n')
    plt.ylabel('Probability')
    plt.xticks(range(1,25))
    plt.show()
interact(iterate, Iterations=widgets.IntSlider(min = 50, max = 5000), continuous_update=False, layout='bottom')