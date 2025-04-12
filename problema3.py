#!/usr/bin/env python3

#(2 puntos) Tu eres un científico de las relaciones1, y has desarrollado un cuestionario que 
# determina el puntaje de amor, es decir, un valor real entre cero y cien. Tu teoría es que dos personas
#con puntajes de amor similares deberían de hacer un buen match.
#Dado los puntajes del amor para 10 personas distintas, crea un arreglo 2-D donde cada entrada
#(i, j) da la diferencia absoluta entre los puntajes del amor de la persona i y la persona j.
#Hint: Recuerda revisar np.random.

import numpy as np

def numeros_random():
    "Esta funcion genera puntajes aleatorios de 10 personas entre 0 y 100"
    puntajes_amors = np.random.randint (0, 101, 10) #np.random.randint(bajo, alto, tamaño) creeamos las califiaciones aleatorias de las 1o personas
    return(puntajes_amors)                              #randint genera numeros enteros dentro del conjunto

a= numeros_random()

def resta_de_matriz(a):
    "esta funcion crea una matriz comparativa entree los participantes en los que se muestra la diferencia absoulta entre puntajes"
    matriz = np.zeros((10,10)) #matriz vacia de 10x10, osea la llenamois con ceros usando np.zeros
    for i in range(10): #for para recorrer cada fila
        for j in range(10): #for apra recorrer cada columna
            if i != j: #si i y j no son la misma persona entonces vamos restar
                matriz [i][j]= abs(a[i] - a[j]) #se obtiene la diferencia abosulta entre putnajes por que tener numeros en negativo no nos importa
    return matriz

print(resta_de_matriz(a))
        