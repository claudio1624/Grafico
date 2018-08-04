#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
from pylab import *
import matplotlib.pyplot as plt
# import matplotlib import *
import numpy as np
#definimos el periodo de la grafica
periodo = 2
#definimos el array dimensional
x = np.linspace(0, 10, 1000)
#defimos la funcion
y = np.sin(2*np.pi*x/periodo)
#creamos la figura
plt.figure()
#primer grafico
plt.subplot(2,2,1)
plt.plot(x, y, 'r', linestyle=":")
#segundo grafico
plt.subplot(2,2,2)
plt.plot(x, y, 'g', linestyle="--")
#tercer grafico
plt.subplot(2,2,3)
plt.plot(x, y, 'B', linestyle=":")
#cuarto grafica
plt.subplot(2,2,4)
plt.plot(x, y, 'k',  linestyle="--")
#mostramos en pantalla
plt.show()
