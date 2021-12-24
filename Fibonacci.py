#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 10:49:44 2021

@author: walter
"""

import functools

nro =  0
@functools.lru_cache()

def fibonacci(n):
    global nro 
    nro +=1
    if n<=3:
        return 1
    return (fibonacci(n-1)+ fibonacci(n-2))

try:
    r= int(input("ingrese la cantidad de veces que desea llamar la funcion de fibonacci : "))
    assert r>0
except AssertionError:
    print("ERROR, debe ingresar un valor positivo ...")
    dato=input("desea continuar con el cálculo de fibonacci SI = s / NO = n : ")
  
    if dato.lower == 'n':
        print("salió correctamente del programa ...")
    else:
        r= int(input("ingrese la cantidad de veces que desea llamar la funcion de calculo de fibonacci : "))
    
print("el numero es :", fibonacci(r), " la función de cálculo de Fibonacci fue llamada :", r)
#print(f"fibonacci() ha sido llamada  {nro:,} veces" )

#-------------- fibonacci ---------
# ------ mostrar la secuencia -------
#--desarrollo con recursion -----------

def recur_fibonacci(n):
   if n <= 1:
       return n
   else:
       return(recur_fibonacci(n-1) + recur_fibonacci(n-2))

secuencia = r

print("la secuencia de Fibonacci de números calculados es: ")
for i in range(secuencia):
       print(recur_fibonacci(i))

# validar si el numero es valido 
#if secuencia <= 0:
#   print("Por favor, verificar debe ingresar un numero positivo ...")
#else:
#   print("la secuencia de Fibonacci es: ")
#   for i in range(secuencia):
#       print(recur_fibonacci(i))