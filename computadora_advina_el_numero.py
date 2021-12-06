#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 20:11:28 2021

@author: walter
 
Proyecto Básico de Python (Adivina el Número (Computadora)).
Basado en el proyecto de: Kylie Ying (@kylieyying). 
"""
import random

# este ejercicio se basa en adivinar el programa un numero que ingresa el usuario que 
# La computadora debe adivinar el número seleccionado por el jugador.
def adivina_el_número_computadora(x):

    print("==================================")
    print("  ¡Comenzamos a Jugar .....!!!    ")
    print("==================================")
    print(f"Selecciona un número entre 1 y {x} para que la computadora intente adivinarlo.")

    # Intervalo de valores válidos
    límite_inferior = 1
    límite_superior = x
    respuesta = ""

    # Miestras el usuario no indique que la respuesta es correcta,
    # continuar el proceso.
    while respuesta != "c":
        # Generar predicción
        if límite_inferior != límite_superior:
            predicción = random.randint(límite_inferior, límite_superior)
        else:
            predicción = límite_inferior  # también podría ser límite_superior porque los límites son iguales.
        
        # Obtener respuesta del usuario
        respuesta = input(f"Mi predicción es {predicción}. Si está por sobre el número, ingresa (A). Si está por debajor del número, ingresa (B). Si es correcta ingresa (C) ").lower()
        
        if respuesta == "a":
            límite_superior = predicción - 1
        elif respuesta == "b":
            límite_inferior = predicción + 1

    print(f"¡Siii felicitaciones .....! La computadora adivinó tu número correctamente: {predicción}")


adivina_el_número_computadora(10)