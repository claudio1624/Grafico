#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
from pylab import *
import matplotlib.pyplot as plt
import numpy as np

x = linspace(0, 5, 10)
y = x ** 222
figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('GRAFICO-EJEMPLO')
show()