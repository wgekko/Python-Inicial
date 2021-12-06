#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 20:22:21 2021

@author: walter

Proyecto Básico de Python (Piedra, Papel o Tijera).
Basado en el proyecto de: Kylie Ying (@kylieyying). 

""" 
import random

def jugar():
    usuario = input("Escoge una opción: \n 'p'=para piedra,\n 'a'=para papel, \n 't'= para tijera.\n").lower()
    computadora = random.choice(['p', 'a', 't'])

    if usuario == computadora:
        return '¡ OOOppppsss Empate...!!!'

    if ganó_el_jugador(usuario, computadora):
        return '¡ Felicitaciones Ganaste...!!!'

    return '¡ Lo siento Perdiste...!!!'


def ganó_el_jugador(jugador, oponente):
    # Retornar True (verdadero) si gana el jugador.
    # Piedra gana a Tijera (pi > ti).
    # Tijera gana a Papel (ti > pa).
    # Papel gana a Piedra (pa > pi).
    if ((jugador == 'p' and oponente == 't')
        or (jugador == 't' and oponente == 'a')
        or (jugador == 'a' and oponente == 'p')):
        return True
    else:
        return False


print(jugar())

