#!/usr/bin/env python3

#(2 puntos) 10 peces ocupan un arreglo 3-D de 5x5x5 de agua. Cada pez decide moverse a la
#posición (i, j, k) dado por el arreglo 2-D que esta más adelante. Si múltiples peces terminan
#ocupando la misma celda, el pez de mayor tamaño se come al más pequeño. Determina que peces sobreviven.

import numpy as np
locs = np . array ([
[0 ,0 ,0] ,
[1 ,1 ,2] ,
[0 ,0 ,0] ,
[2 ,1 ,3] ,
[5 ,5 ,4] ,
[5 ,0 ,0] ,
[5 ,0 ,0] ,
[0 ,0 ,0] ,
[2 ,1 ,3] ,
[1 ,3 ,1]
])
generator = np . random . default_rng (1010)
weights = generator . normal ( size =10)
#print ( weights )
# [ -1.699 0.538 -0.226 -1.09 0.554 -1.501
# 0.445 1.345 -1.124 0.212]

def creacion_pecera():
    "funcion que crea una pecera que consiste en el arreglo 5x5x5"
    estanque = np.zeros((5, 5, 5))
    return estanque

pecera = creacion_pecera()

#print(pecera)

def peces_sobreviven(): 
    "Esta funcion determina que peces fueron devorados o fallecieron por estar fuera del agua"
    sobrevivientes = [] #hacemos una lista donde metemos a los peces sobrevviiventes en este punto sacamos los muesrtos fuera de la pecera

    for n_pez in range(len(locs)):
        
        i, j, k = locs[n_pez] #extraemos la posicion en la que cada pez se movera, ejemplo pez 0 es (0, 0, 0,).

        if i == 5 or j == 5  or k == 5: #peces que cumplan esta condicion estan muertos
            continue #los ignoramos
        
        comido = False #peces no han sido comidos

        for otro_pez in sobrevivientes: #ahora comprobamos si algun pez choca con otro en las coordenadas comprobandolo desde el punto de vuista como si fuera un nuevo pez
            l, m, n = locs[otro_pez] #es como si otro pez llegara y ponemos como si fueran coordenadas nuevas para ver si tienen conflictos con las i, j, k que pusimos en la lista
    
            if (l, m, n) == (i, j, k): #si ambos peces coinciden en posicion hay conflicto
                if weights[n_pez] > weights[otro_pez]: #entocnes como coincidieron se comparan los pesos
                    sobrevivientes.remove(otro_pez)
            
                else:
                    comido = True #declaramos la variable devorado como cierta
                break


        if not comido:
            sobrevivientes.append(n_pez)
    
    return sobrevivientes

peces_que_vivieron = peces_sobreviven()

print (f"Peces que vivieron al final: {peces_que_vivieron}")

                

