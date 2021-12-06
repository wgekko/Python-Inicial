#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 20:01:14 2021

@author: walter

Proyecto Básico de Python (Adivina el Número).
Basado en el proyecto de: Kylie Ying (@kylieyying). 
"""

import random
# este ejercicio se basa en adivinar un numero random que genera el programa
# El usuario adivina el número aleatorio generado por la computadora.
def adivina_el_número(x):

    print("================================")
    print("  ¡Comenzamos a Jugar .....!!!  ")
    print("================================")
    print("El objetivo es adivinar el número generado por la computadora...")

    número_aleatorio = random.randint(1, x) # número aleatorio entre 1 y x.

    # se decidio que la predicción es 0 inicialmente para que no coincida con el número aleatorio. 
    predicción = 0

    # Continuar prediciendo el número hasta que la predicción sea correcta.
    while predicción != número_aleatorio:
        # El usuario ingresa un número.
        predicción = int(input(f'Adivina un número entre 1 y {x}: '))
        # Si el número es menor que el número aleatorio, se 
        # muestra un mensaje.
        if predicción < número_aleatorio:
            print('Intenta otra vez... Este número está por debajo del número elegido.')
        # Si el número es mayor que el número aleatorio, se
        # muestra un mensaje.
        elif predicción > número_aleatorio:
            print('Intenta otra vez... Este número está por sobre del numero elegido.')

    # El ciclo o bucle se detiene cuando el usuario adivina el número
    # correctamente y se muestra un mensaje final.
    print(f'¡Felicitaciones.....!!! Adivinaste el número {número_aleatorio} correctamente.....')

#  desde aqui se llama a la función
adivina_el_número(10)
