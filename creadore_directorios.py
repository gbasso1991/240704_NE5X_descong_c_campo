#%%/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:37:54 2024

@author: giuliano
"""

import os
import shutil

def procesar_directorio(directorio):
    # Comprobamos si el directorio existe
    if not os.path.exists(directorio):
        print(f"El directorio '{directorio}' no existe.")
        return

    # Recorremos todos los elementos del directorio
    for elemento in os.listdir(directorio):
        ruta_elemento = os.path.join(directorio, elemento)

        # Si es un directorio, procesamos recursivamente
        if os.path.isdir(ruta_elemento):
            procesar_directorio(ruta_elemento)
        else:
            # Si es un archivo, movemos si es necesario
            mover_archivos(ruta_elemento)

def mover_archivos(archivo):
    # Obtenemos el nombre del directorio del archivo
    directorio = os.path.dirname(archivo)

    # Creamos la carpeta 'aux' si no existe
    carpeta_aux = os.path.join(directorio, 'aux')
    if not os.path.exists(carpeta_aux):
        os.makedirs(carpeta_aux)

    # Obtenemos la lista de archivos en el directorio
    archivos = os.listdir(directorio)
    # Ordenamos los archivos
    archivos.sort()
    
    # Movemos los archivos a 'aux' si están entre el 15 y el -15
    for i, archivo_actual in enumerate(archivos):
        if 20 <= i < len(archivos) - 20:
            shutil.move(os.path.join(directorio, archivo_actual), carpeta_aux)

#%% Directorio principal a procesar
directorio_principal = os.getcwd()

# Llamamos a la función principal para procesar el directorio
procesar_directorio(directorio_principal)
#%%


# import os

# # Directorio donde se encuentran los archivos
# directorio = os.path.join(os.getcwd(),'240306_125811_265_150_2')

# # Obtener la lista de archivos en el directorio
# archivos = os.listdir(directorio)

# # Ordenar la lista de archivos
# archivos.sort()

# # Número inicial para XXX
# numero_inicial = 43

# # Iterar sobre los archivos y renombrarlos
# for i, archivo in enumerate(archivos):
#     nuevo_nombre = f"265kHz_150dA_100Mss_NE{numero_inicial + i:03d}.txt"
#     # Renombrar el archivo
#     os.rename(os.path.join(directorio, archivo), os.path.join(directorio, nuevo_nombre))
#     print(f"Renombrado {archivo} a {nuevo_nombre}")





