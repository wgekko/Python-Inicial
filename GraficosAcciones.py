# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 00:17:03 2022

@author: Walter
"""

# Importando pandas y datetime
import pandas as pd
import pandas_datareader.data as web
import datetime as dt

# Extrayendo información financiera de Yahoo! Finance
inicio = dt.datetime(2017, 1, 13)
fin = dt.datetime(2021, 1, 13)

amd = web.DataReader("AMD", 'yahoo', inicio, fin)  # información de AMD
intc = web.DataReader("INTC", 'yahoo', inicio, fin)  # información de INtel

# insertando una nueva columna con el simbolo
amd.insert(0, 'Symbol', 'AMD')
intc.insert(0, 'Symbol', 'INTC')

amd.head()
# concatenando toda la información y reseteando el indice
combinado = pd.concat([amd, intc]).sort_index()
datos_todo = combinado.reset_index()

datos_todo.head()

# Armando una tabla pivot del precio de cierre
pivot = datos_todo.pivot(index='Date', columns='Symbol', 
                         values='Close')

pivot.head()

# Obteniendo datos de multiples empresas
def all_stocks(symbols, start, end):
       def data(symbols):
           return web.DataReader(symbols, 'yahoo', start, end)
       datas = map(data, symbols)
       return pd.concat(datas, keys=symbols, names=['symbols','Date'])

simbolos = ['AMD','INTC', 'MU']

all_data = all_stocks(simbolos, inicio, fin)
all_data.head()

# Graficando los datos.
solo_cierre = all_data[['Close']].reset_index()
pivot_cierre = solo_cierre.pivot('Date', 'symbols', 'Close')

pivot_cierre.head()
# Graficando todos
plot = pivot_cierre.plot(figsize=(12,8))
