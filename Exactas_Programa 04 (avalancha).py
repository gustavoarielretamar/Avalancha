# %% LIBRERIAS:


import numpy as np
import matplotlib.pyplot as plt
import random

# %% VARIABLES GLOBALES:


# %% TABLERO EN 0:


def crear_tablero(n, debug=False):
    t = np.repeat(0, (n+2)*(n+2)).reshape((n+2), (n+2))
    if debug:
        print(t)
    return t


# %% BORDES EN -1:


def bordes(t, debug = False):
    for i in range(0, len(t)):
        t[(0, i)] = - 1
        t[(len(t)-1, i)] = - 1
        i = i + 1
    for i in range(0, len(t)):
        t[(i, 0)] = - 1
        t[(i, len(t)-1)] = - 1
        i = i + 1
    if debug:
        print(t)
    return t


# %% 4. TABLERO BASE CON 0 en el medio y bordes -1


def tablero_base(n, debug=False):
    t = crear_tablero(n)
    t = bordes(t)
    if debug:
        print(t)
    return t


# %% IDENTIFICA LOS BORDES


def es_borde(t, coord, debug=False):
    borde = False
    if t[coord] == -1:
        borde = True
    if debug:
        print(borde)
    return borde


# %% 7 CAIDA DE LOS COPOS


def tirar_copo(t, coord, debug=False):
    t[coord] = t[coord] + 1
    if debug:
        print(t)
    return t


# %% 8, 9 y 10 COORDENADA DE VECINOS


def vecinos_de(t, coord, debug=False):
    vecinos = []
    a = coord[0]
    b = coord[1]
    v1 = ((a+1),b)
    c1 = t[((a+1),b)] != -1
    v2 = ((a-1),b)
    c2 = t[((a-1),b)] != -1
    v3 = (a, (b + 1))
    c3 = t[(a,(b+1))] != -1
    v4 = (a,(b-1))
    c4 = t[(a,(b-1))] != -1
    if c1:
        vecinos.append(v1)
    if c2:
        vecinos.append(v2)
    if c3:
        vecinos.append(v3)
    if c4:
        vecinos.append(v4)
    if debug:
        print(vecinos)
    return vecinos


# %% 11. DESBORDAR


def desbrodar_pocision(t, coord, debug=False):
    vecinos = vecinos_de(t, coord)
    i = 0
    while t[coord] >= 4:
        t[coord] = t[coord] - 4
        while i < len(vecinos):
            tirar_copo(t, vecinos[i])
            i = i + 1
        if debug:
            print(t)
    return t

# %% DESBORDAR EL TABLERO:


def desbordar_valle(t, debug = False):
    cantidad_filas = t1.shape[0]
    cantidad_columnas = t1.shape[1]
    for i in range(1, cantidad_filas - 1):
        for j in range(1, cantidad_columnas - 1):
            if t[(i,j)] >= 4:
                t = desbrodar_pocision(t, (i,j), True)
    if debug:
       print(t)
    return t


# %% 13. LUGARES A DESBORDAR devuelve True si hay alguna posición en el tablero que hay que desbordar, y False si no.


def hay_que_desbordar(t, debug = False):
    cantidad_filas = t1.shape[0]
    cantidad_columnas = t1.shape[1]
    falta = False
    for i in range(1, cantidad_filas - 1):
        for j in range(1, cantidad_columnas - 1):
            if t[i,j] >= 4:
                falta = True
    if debug:
        print(falta)
    return falta


# %% ESTABILIZAR mientras haya alguna posición que tenga al menos cuatro copos, llame a desbordar_valle.
def estabilizar(t, debug = False):
    while (hay_que_desbordar(t)):
        desbordar_valle(t)
    if debug:
        print(t)
    return t

# %% LLAMADAS:


# t1 = crear_tablero(7, True)
# bordes(t1, True)
t1 = tablero_base(7)
# es_borde(t1, (0,0), True)
# tirar_copo(t1, (2,5), True)
# vecinos_de(t1, (7,7), True)
# tirar_copo(t1, (4,4))
# tirar_copo(t1, (4,4))
# tirar_copo(t1, (4,4))
# tirar_copo(t1, (4,4))
# desbrodar_pocision(t1, (4,4), True)
# hay_que_desbordar(t1, True)
# tirar_copo(t1, (4,4))
# tirar_copo(t1, (4,4))
# tirar_copo(t1, (4,4))
# tirar_copo(t1, (4,4))
# tirar_copo(t1, (3,4))
# tirar_copo(t1, (3,4))
# tirar_copo(t1, (3,4))
# desbordar_valle(t1, True)
# estabilizar(t1, True)
