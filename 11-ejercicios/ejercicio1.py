"""

Ejercicio 1. Hacer un programa que tenga una lista
de 8 numeros enteros y haga lo siguiente:
-Recorrer la lista y mostrarla
-Hacer funcion que recorra lista de numeros y devuelva un string
-Ordenarla y mostrarla
-Mostarr su longitud
-Buscar algun elemento (que el usuario pida por teclado)
"""

# Crear la lista
numeros = [13, 64, 52, 73, 21, 7, 91, 63]

# Crear funcion que recorra lista y devuelva string
def mostrarLista(lista):
    resultado = ""

    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"

    return resultado

# Recorrer y mostrar
print("#### Recorrer y Mostrar ######")
"""
for numero in numeros:
    print(numero)
"""

print(mostrarLista(numeros))

# Ordenar y mostrar
print("##### Ordenar y mostrar #####")
numeros.sort()
print(mostrarLista(numeros))


# Mostar su longitud
print(len(numeros))

# Busqueda en la lista
print("##### Busqueda en la lista ######")

while True:
    try:
        busqueda = int(input("Introduce el numero: "))

        if busqueda <= 0:
            print("El numero debe ser mayor que 0")
            continue

        break  # Sale del bucle si todo está bien

    except ValueError:
        print("Debes introducir un numero valido")

print(f"Has introducido el {busqueda}")
print(f"##### Buscar en la lista el numero {busqueda} #####")

try:
    search = numeros.index(busqueda)
    print(f"El numero buscado existe en la lista, es el indice: {search}")
except ValueError:
    print("El numero no esta en la lista, sorry")
else:
    print("Todo ha funcionado correctamente")
finally:
    print("Fin de la interaccion !!")
    




    

