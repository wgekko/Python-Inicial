# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 00:15:55 2022

@author: Walter
"""

# graficos embebidos
%matplotlib inline 
# importando librerías
import numpy_financial as np
import matplotlib.pyplot as plt

# Calculando la tasa interna de retorno de la inversion en la compañía
IRR = np.irr([-1000, 300, 300, 300, 300])
IRR * 100

# Graficando el NPV en función de la tasa de descuento
def npv_irr(tasas):
    result = []
    for tasa in tasas:
        result.append(np.npv(tasa/100,[-1000, 300, 300, 300, 300] ))
    return result

tasas = list(range(14))

plt.title("NPV y la tasa de descuento")
plt.plot(tasas, npv_irr(tasas), marker='o', label='NPV')
plt.axhline(0, color='red')
axes = plt.gca()
axes.set_ylim([-200,250])
plt.xticks(tasas)
plt.legend(loc='upper right')
plt.show()

