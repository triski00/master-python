"""
Ejercicio3
Escribir un programa que muestre los cuadrados
(un numiro multiplicado por simismo) de los 60 primeros numeros naturales.
Resolverso con for y con while.
"""

#while
"""
contador = 0
while contador <= 60:

    cuadrado = contador*contador
    print(f"El cuadrado de {contador} es {cuadrado}")

    contador += 1
"""
    #for

for numero in range(61):
        cuadrado = numero*numero
        print(f"El cuadrado de {numero} es {cuadrado}")