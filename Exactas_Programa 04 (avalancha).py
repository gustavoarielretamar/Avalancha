# %% LIBRERIAS:
import numpy as np
import matplotlib.pyplot as plt
import random
import imageio
import os


# %% TABLERO EN 0:
def crear_tablero(n, debug=False):
    t = np.repeat(0, (n + 2) * (n + 2)).reshape((n + 2), (n + 2))
    if debug:
        print(t)
    return t
# %% BORDES EN -1:
def bordes(t, debug=False):
    for i in range(0, len(t)):
        t[(0, i)] = -1
        t[(len(t) - 1, i)] = -1
        i = i + 1
    for i in range(0, len(t)):
        t[(i, 0)] = -1
        t[(i, len(t) - 1)] = -1
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
    v1 = ((a + 1), b)
    c1 = t[((a + 1), b)] != -1
    v2 = ((a - 1), b)
    c2 = t[((a - 1), b)] != -1
    v3 = (a, (b + 1))
    c3 = t[(a, (b + 1))] != -1
    v4 = (a, (b - 1))
    c4 = t[(a, (b - 1))] != -1
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
def desbordar_valle(t, debug=False):
    cantidad_filas = t.shape[0]
    cantidad_columnas = t.shape[1]
    for i in range(1, cantidad_filas - 1):
        for j in range(1, cantidad_columnas - 1):
            if t[(i, j)] >= 4:
                t = desbrodar_pocision(t, (i, j))
    if debug:
        print(t)
    return t
# %% 13. LUGARES A DESBORDAR devuelve True si hay alguna posición en el tablero que hay que desbordar, y False si no.
def hay_que_desbordar(t, debug=False):
    cantidad_filas = t.shape[0]
    cantidad_columnas = t.shape[1]
    falta = False
    for i in range(1, cantidad_filas - 1):
        for j in range(1, cantidad_columnas - 1):
            if t[i, j] >= 4:
                falta = True
    if debug:
        print(falta)
    return falta
# %% ESTABILIZAR mientras haya alguna posición que tenga al menos cuatro copos, llame a desbordar_valle.
def estabilizar(t, debug=False):
    while hay_que_desbordar(t):
        desbordar_valle(t)
    if debug:
        print(t)
    return t
# %% COPO EN EL MEDIO:
def paso(t, debug=False):
    filas = t.shape[0]
    columnas = t.shape[1]
    punto_medio = ((int(filas / 2)), (int(columnas / 2)))
    tirar_copo(t, (punto_medio))
    estabilizar(t)
    if debug:
        print(t)
    return t
# %% VIDEO:
def guardar_foto(t, paso):
    dir_name = "output"
    if not os.path.exists(dir_name):  # me fijo si no existe el directorio
        os.mkdir(dir_name)  # si no existe lo creo
    ax = plt.gca()
    file_name = os.path.join(dir_name, "out{:05}.png".format(paso))
    plt.imshow(t, vmin=-1, vmax=3)
    ax.set_title("Copos tirados: {}".format(paso + 1))  # titulo
    plt.savefig(file_name)
def hacer_video(cant_fotos):
    dir_name = "output"
    lista_fotos = []
    for i in range(cant_fotos):
        file_name = os.path.join(dir_name, "out{:05}.png".format(i))
        lista_fotos.append(imageio.imread(file_name))
    video_name = os.path.join(dir_name, "avalancha.mp4")
    # genero el video con 10 Copos por segundo. Explorar otros valores:
    imageio.mimsave(video_name, lista_fotos, fps=10)
    print("Estamos trabajando en el directorio", os.getcwd())
    print("y se guardo el video:", video_name)
def probar(n, pasos):
    t = crear_tablero(n)
    for i in range(pasos):
        paso(t)
        guardar_foto(t, i)
    hacer_video(pasos)
    return t
# %% PARAMETROS:
n = 7
cant_fotos = 200
pasos = 200

# %% LLAMADAS:
# t1 = tablero_base(7)
# %% 
probar(n, pasos)
