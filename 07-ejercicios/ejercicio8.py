"""
Ejerciio8.
¿Cuanto es el x % de x numero?

"""


numero = int(input("Introduce el numero: "))
porcentaje = int(input(f"¿Que porcentaje quieres sacar de {numero}?"))

operacion = (numero * (porcentaje/100))

print(f"El {porcentaje}% de {numero} es: {operacion}")
