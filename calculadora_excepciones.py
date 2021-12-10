#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 02:32:11 2021

@author: walter
"""


def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):		
   try:
        return num1/num2    
   except ZeroDivisionError:
        print("ERROR; no se puede dividor por cero")
        return "Operación invalida"
        
print("calculadora ")

while True:
    try:
        op1=(int(input("Introduce el primer número: ")))
        op2=(int(input("Introduce el segundo número: ")))	
        break
    except ValueError:
            print("ha ingrasodo una dato no numerico, digite nuevamente los numeros")

	
operacion=input("Introduce la operación a realizar \n suma \n resta \n multiplica \n divide \n ... : ")


print ("resultado----")

try:
    if operacion=="suma":   
        print(suma(op1,op2))

    elif operacion=="resta":
        print(resta(op1,op2))

    elif operacion=="multiplica":
        print(multiplica(op1,op2))

    elif operacion=="divide":
        print(divide(op1,op2))

    else:
        print ("Operación no contemplada")
except TypeError("debe ingresar el nombre de la operación correcta"):
    print("debe elegir entre suma, resta, multiplica o divide")

print("------------------------------------------------------------")
print("Operación ejecutada. Continuación de ejecúción del programa ")