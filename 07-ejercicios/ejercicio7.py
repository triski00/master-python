"""
Ejercicio7.
Hacer un programa que muestre todos los numeros impares
entre dos numeros que elija el usuario.
"""
numero1 = int(input("introduce un numero: "))
numero2 = int(input("introduce el siguiente numero: "))

if numero1 < numero2:

    for x in range(numero1, (numero2 + 1)):

        if x%2 == 0:
           print(f"{x} es par")
        else:
            print(f"{x} en Inpar")

else:
    print("El numero 1 debe ser mayor al 2")

