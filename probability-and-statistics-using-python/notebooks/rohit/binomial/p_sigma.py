import numpy as np
import matplotlib.pyplot as plt

p = np.linspace(0,1,1001)
sigma = np.sqrt(p*(1-p))

plt.plot(p, sigma, linewidth=4.0)

plt.xticks([0, 1/4, 1/2, 3/4, 1], fontsize = 30)
plt.yticks([1/4, 1/2], fontsize = 30)
plt.xlabel('$p$', fontsize = 30)
plt.ylabel('$\sigma$', fontsize = 30)
plt.title("$\sigma$ vs. $p$", fontsize = 40)
plt.grid()

plt.gca().set_xlim([0, 1])
plt.gca().set_ylim([0, 0.6])
plt.gcf().set_size_inches(20,12)

plt.savefig("p_sigma.pdf")
plt.show()
