from pathlib import Path
import shutil

# Abrir archivo

ruta = Path().absolute() / "fichero_texto.txt"

with open(ruta, "a+") as archivo:
    archivo.write("Hola Mario\n")


    # Escribir dentro de un archivo

    archivo.write("*****Soy un texto metido desde un python******/n")

    # Cerrar archivo

    archivo.close()

    # Abrir archivo

    ruta = Path().absolute() / "fichero_texto.txt"
    archivo = open(ruta, "r")

    # Leer contenido
   # with open(ruta, "r") as archivo_lectura:
   #  contenido = archivo_lectura.read()
    #print(contenido)

    # Leer contenido y guardarlo en una lista

from pathlib import Path

ruta = Path().absolute() / "fichero_texto.txt"

with open(ruta, "r") as archivo_lectura:
    lista = archivo_lectura.readlines()
   # print(lista)

   # for frase in lista:
       # lista_frase = frase.split()
frase = "Hola Mario"

print("- " + frase.center(100))



# Copiar
"""
from pathlib import Path

ruta_original = Path().absolute() / "fichero_texto.txt"
from pathlib import Path

ruta_base = Path().absolute()
ruta_nueva = ruta_base / "fichero_copiado.txt"
shutil.copyfile(ruta_original, ruta_nueva)
"""

# Mover
"""

import time

if ruta_original.exists():
    try:
        shutil.move(ruta_original, ruta_nueva)
    except PermissionError:
        time.sleep(1)
        shutil.move(ruta_original, ruta_nueva)
else:
    print("El archivo no existe")

    """

# Crear carpeta
"""
import os

if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_cafrpeta")
    

else:
    print("Ya existe el directorio")

"""

    # Copiar 

ruta_original = "./mi_carpeta"
ruta_nueva = "./mi_carpeta_COPIADA"
shutil.copytree(ruta_original, ruta_nueva)
















