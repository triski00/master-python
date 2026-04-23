"""

Modulos: Funcionalidades ya hechas para reutilizar.
https://docs.python.org/3/py-modindex.html

Podemos conseguir modulos que ya vienen en el lenguaje,
modulos en internet, y tambien podemos crearlos.
"""
# Inportar mpodulo propio

#from mimodulo import hola_mundo
from mimodulo import *

#print(hola_mundo("Mario Avila"))
#print(mimodulo.calculadora(3, 5, True))

print(hola_mundo("Mario Avila"))

# Modulo de fechas

import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, ")
print("Mi fecha personalizada", fecha_personalizada)

print(datetime.datetime.now().timestamp())


# Modulo matematicas

import math

print("Raiz Cuadrada de 10: ", math.sqrt(10))
print("Numero pi: ", float(math.pi))

print("Redondear: ", math.ceil(6.16798))

# Modulo random

import random

print("Numero aleatorio entre 15 y 67: ", random.randint(15, 67))

