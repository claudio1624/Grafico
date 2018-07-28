#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
from pylab import *
import matplotlib.pyplot as plt
import numpy as np

n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2 * X)

plt.axes([0.025, 0.025, 0.95, 0.95])
plt.plot(X, Y + 1, color='yellow', alpha=1.00)
plt.fill_between(X, 1, Y + 1, color='black', alpha=.40)
plt.plot(X, Y - 1, color='green', alpha=1.00)
plt.fill_between(X, -1, Y - 1, (Y - 1) > -1, color='blue', alpha=.50)
plt.fill_between(X, -1, Y - 1, (Y - 1) < -1, color='red',  alpha=.25)
plt.xlim(-np.pi, np.pi)
plt.xticks(())
plt.ylim(-2.5, 2.5)
plt.yticks(())
plt.show()