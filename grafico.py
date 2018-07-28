#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
from pylab import *
import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S, B = np.cos(X), np.sin(X), np.sinh(X)

plt.plot(X, C)
plt.plot(X, S)
plt.plot(X, B)

plt.show()