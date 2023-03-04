# %% LIBRERIAS
import numpy as np
import matplotlib.pyplot as plt

# %% VARIABLES GLOBALES

# %% TABLERO EN 0
def crear_tablero(n, debug=False):
    tablero = np.repeat(0, n*n).reshape(n, n)
    if debug:
        print(tablero)
    return tablero

# %% BORDES EN -1
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

# %% TABLERO BASE CON 0 en el medio y bordes -1 
def tablero_base(n, debug=False):
    tablero = crear_tablero(n)
    tablero = bordes(tablero)
    if debug:
        print(tablero)
    return tablero


# %% 4. Crear un tablero que contenga un valle de 7 × 7 posiciones utilizables y guardarlo en una variable llamada t1 (usar la función de nida en el punto anterior).
t1 = tablero_base(9, True)

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

# tirar_copo(t1, (3, 3))
# tirar_copo(t1, (5, 3), True)
#%% 8 
# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=' ')
#     print()

def vecinos_de (tablero, coord, debug = False):
    vecinos = []
    a = coord[0]
    b = coord[1]
    down = [(a + 1, b)]
    d = tablero [(a + 1, b)] != -1
    up = [(a - 1, b)]
    u = tablero [(a - 1, b)] != -1
    right = [(a, b + 1)]
    r = tablero [(a, b + 1)] != -1
    left = [(a, b - 1)]
    l = tablero [(a, b - 1)] != -1
    if d:
        vecinos.append(down)
    if u:
        vecinos.append(up)
    if r:
        vecinos.append(right)
    if l:
        vecinos.append(left)
    if debug:
        print(vecinos)
    return vecinos
vecinos_de(t1, (1, 4), True)
