# %% LIBRERIAS
import numpy as np
import matplotlib.pyplot as plt
import random

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

#%% 4. TABLERO BASE CON 0 en el medio y bordes -1 
def desbordar_valle(tablero, debug=False):
    cantidad_filas = t1.shape[0]
    cantidad_columnas = t1.shape[1]
    for i in range(1, cantidad_filas - 1):
        for j in range(1, cantidad_columnas - 1):
            if tablero(i, j) >= 4:
                desbrodar_pocision(tablero, (i, j))
    if debug:
        print(tablero)
    return tablero


# %% 13. LUGARES A DESBORDAR devuelve True si hay alguna posición en el tablero que hay que desbordar, y False si no.


def hay_que_desbordar(tablero):
    cantidad_filas = t1.shape[0]
    cantidad_columnas = t1.shape[1]
    falta = False
    for i in range(1, cantidad_filas - 1):
        for j in range(1, cantidad_columnas - 1):
            if 
                falta = True
    print(falta)
    return falta


#    i = 0
#    desbordar = False
#    while (i < tablero.shape[0] and desbordar == False):
#        j = 0
#        while (i < tablero.shape[1] and not desbordar):
#            if tablero [(i, j)] >= 4:
#                desbordar = True
#            j = j + 1
#        i = i + 1
#    print(desbordar)
#    return desbordar

#     # %% ESTABILIZAR mientras haya alguna posición que tenga al menos cuatro copos, llame a desbordar_valle.
# def estabilizar(tablero):
#     while (hay_que_desbordar(tablero)):
#         desbordar_valle(tablero)

# %% LLAMADAS:


t1 = tablero_base(9)
tirar_copo(t1, (4, 4))
tirar_copo(t1, (4, 4))
tirar_copo(t1, (4, 4))
tirar_copo(t1, (4, 4))
tirar_copo(t1, (6, 6))
tirar_copo(t1, (6, 6))
tirar_copo(t1, (6, 6))
tirar_copo(t1, (6, 6))
hay_que_desbordar(t1)
desbordar_valle(t1)
