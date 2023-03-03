# %% LIBRERIAS
import numpy as np
import matplotlib.pyplot as plt

# %% VARIABLES GLOBALES

# %% BORDES


def bordes(t):
    for i in range(0, len(t)):
        t[(0, i)] = - 1
        t[(len(t)-1, i)] = - 1
        i = i + 1
    for i in range(0, len(t)):
        t[(i, 0)] = - 1
        t[(i, len(t)-1)] = - 1
        i = i + 1
    return t

# %% TABLERO


def crear_tablero(n, debug=False):
    tablero = np.repeat(0, n*n).reshape(n, n)
    if debug:
        print(tablero)
    return tablero

# %% TABLERO BASE . 3. Implemente una función crear_tablero(n) que reciba como entrada la cantidad n de las y columnas del valle, y devuelva un tablero vacío, con 0 en todas posiciones utilizables y -1 en los bordes.


def tablero_base(n, debug=False):
    tablero = crear_tablero(n)
    tablero = bordes(tablero)
    if debug:
        print(tablero)
    return tablero


# %% 4. Crear un tablero que contenga un valle de 7 × 7 posiciones utilizables y guardarlo en una variable llamada t1 (usar la función denida en el punto anterior).
t1 = tablero_base(9)

# %% 5. Implementar la función es_borde(tablero, coord) que reciba un tablero y una posición, y devuelva True si dicha posición es un borde y False si no


def es_borde(tablero, coord, debug=False):
    borde = False
    if tablero[coord] == -1:
        borde = True
    if debug:
        print(borde)
    return borde
# es_borde(t1, (5,6), True)

# %% 7

def tirar_copo(tablero, coord, debug=False):
    tablero[coord] = tablero[coord] + 1
    if debug:
        print(tablero)
    return tablero

#tirar_copo(t1, (4, 4), True)
#%% 8
def vecinos_de (tablero, coord, debug = False):
    vecinos = []
    
