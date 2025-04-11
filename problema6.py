#!/usr/bin/env python3

#(2 puntos) Dado un arreglo de 10x10x10 de ceros, establece (i, j, k) = 1 sí, i es impar, j es par y
#k es primo. En otras palabras, establece esos elementos a 1: (1, 0, 2), (1, 0, 3), (1, 0, 5), (1, 0, 7),
#(1, 2, 2)...

import numpy as np

def arreglo_3D():
    "Esta funcion hace una matriz 3D que tiene 10x10x10 y sera en un inicio una rreglo de ceros"
    arreglo = np.zeros((10, 10, 10))
    return arreglo

arreglo = arreglo_3D()

#print(arreglo)

def coordenadas_arreglo():
    "Función que genera todas las combinaciones de coordenadas del arreglo"
    arreglo_coordenadas = []
    for i in range (10):
        for j in range (10):
            for k in range (10):
                arreglo_coordenadas.append((i, j, k))
    return arreglo_coordenadas

coordenadas = coordenadas_arreglo()
#print (coordenadas)


def es_impar(i):
    "funcion que detecta impar"
    return i % 2 == 1

def es_par(j):
    "funcion que detecta par"
    return j % 2 == 0

def es_primo(k):
    "funcion que detecta al primo"
    primos = [2, 3, 5, 7]
    return k in primos

coordenadas_validas = []

for i, j, k in coordenadas: #recorrer las coodenadas y encontrar en las que se cumple la consigna
    if es_impar(i) and es_par(j) and es_primo(k):
        coordenadas_validas.append((i, j, k))

for i, j, k in coordenadas_validas: #colocamos uno en el arreglo donde esta la coordenada valida
    arreglo[i][j][k] = 1

print(arreglo)

#print(coordenadas_validas) #esto es por si se quiere comprobar las coordenadas validas