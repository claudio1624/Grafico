#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
from pylab import *
import matplotlib.pyplot as plt
# import matplotlib import *
import numpy as np
lista1 = [22,25,22,25,30,30,30,25]
lista2 = [15,15,15,15,2,10,2,15,15,15,15]
lista3 = [0,5,10,15,20,25,20,15,10,5,0]
plt.xlabel("ciisa")
plt.ylabel("ordenada")
plt.plot(lista1, marker="x", linestyle=":", color="B", label = "Enero")
plt.plot(lista2, color='g', linestyle=":", label = "Febrero")
plt.plot(lista3, marker='o',  linestyle="--", color='r', label = "Marzo")
title ("Graficos")
plt.legend()
plt.show()