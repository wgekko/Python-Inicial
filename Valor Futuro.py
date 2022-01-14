# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 00:15:55 2022

@author: Walter
"""

#%matplotlib inline

# Ejemplo FV con python
# $1000 al 6% anual por 3 años.

# importando librerías
import numpy_financial as np
import matplotlib.pyplot as plt

x = -1000  # deposito
r = .06    # tasa de interes
n = 3      # cantidad de años

# usando la funcion fv de numpy
FV = np.fv(pv=x, rate=r, nper=n, pmt=0)
print (FV)


# Graficando las funciones con interes de 6 y 12 % a 20 años.
t = list(range(0, 21))

def fv6(num):
    return np.fv(pv=-1000, rate=r, pmt=0, nper=num)

def fv12(num):
    return np.fv(pv=-1000, rate=.12, pmt=0, nper=num)

plt.title("Graficando FV 6 y 12 %")
plt.plot(t, fv6(t), label="interes 6 %")
plt.plot(t, fv12(t), label="interes 12 %")
plt.legend(loc='upper left')
plt.show()