#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 19:48:23 2021

@author: walter

Proyecto Básico de Python (Mad Libs / Historias Locas).
Basado en el proyecto de: Kylie Ying (@kylieyying). 
"""

# Concatenar cadenas de caracteres.
# Supongamos que queremos crear una cadena que diga:
# "Aprende a programar con ________."

organizador = "Walter" # Cadena de caracteres asignada a una variable.

# Algunas alternativas
print("Aprende a programar proyectos con " + organizador) # Concatenar
print("Aprende a programar proyectos con {}".format(organizador)) # Método .format()
print(f"Aprende a programar proyectos con {organizador}") # f-string

# Mad Libs (Historias Locas)
# desarrollamos ingresando adjetivos, verbos y sustantivo para crear la frase
print("ingrese  adjetivo, vervos y sustantivo para crear la frase ")
print ("para dar sentido a la frase pre cargada se sugiere adj: asombroso")
print ("para dar sentido a la frase pre cargada se sugiere verb: resolver / programar")
print ("para dar sentido a la frase pre cargada se sugiere sust: metas/ programar")
adj = input("Adjetivo: ") # asombroso
verbo1 = input("Verbo: ") # resolver
verbo2 = input("Verbo: ") # programar
sustantivo_plural = input("Sustantivo (plural): ") # metas, objetivos

madlib = f"¡Programar es {adj}! Siempre me emociona porque me encanta {verbo1} problemas. \
¡Aprende a {verbo2} proyectos con {organizador} y alcanza tus {sustantivo_plural}!"

print(madlib)