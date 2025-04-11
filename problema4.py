#!/usr/bin/env python3

#(2 puntos) Eres un profesor vengativo y una de tus manías es que los estudiantes se apresuren
#en sus exámenes. Para darles una lección, decides dar ceros a los tres primeros estudiantes que
#saquen menos de 60 puntos, en el orden que entregaron sus exámenes.
#Dada un arreglo 1-D de números enteros, identifica los tres primeros valores menores a 60 y
#reemplázalos por cero.

import numpy as np
def calificaciones_random():
    "funcion para realizar un arreglo 1D de forma random de calificaciones de 30 alumnos"
    calificacion = np.random.randint (0, 101, 30) #np.random.randint(bajo, alto, tamaño) creeamos las califiaciones aleatorias de las 1o personas
    return(calificacion) 

orden_entrega = calificaciones_random()
print (f"califiaciones originales en orden de entrega de mis 30 estudiantes:{orden_entrega}")

def venganza(orden_entrega, venganzas = 0, i = 0):
    "Esta funcion sirve para realizar la venganza de aquellos tres primeros estudiantes que hayan sacado menor "
    "a 60 puntos en el examen, se les asigna un 0"
   
    if venganzas == 3: #si el marcador llega a tres venganzas se termina entonces, el resto de los alumnos ya no tendran cero
                return orden_entrega #auque hayan sacado menos de 60

    if i >= len(orden_entrega): #tambien se impone que si se revisa la lista del orden de calificaciones termine la recursion
        return orden_entrega #en el probable caso de que no hubiera mas alumnos, por ejemplo que solo dos alumnos sacaran menos de 60

    if orden_entrega[i] <= 59: #si la calificación es igual o menor a 59 se cambia por cero
        orden_entrega[i] = 0
        venganzas += 1 #finalmente se aumenta el contador de la venganza a 1 si se cumple

    i += 1 #se aumenta el indice para pasar a revisar la siguiente calificacion
    
    return venganza(orden_entrega, venganzas, i)

resultado = venganza(orden_entrega)

print (f"Calificaciones después de la venganza: {resultado}")
      


