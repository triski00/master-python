"""

# FOR
for varialble in elemento_iterable (lista, rango, etc)
    BLOQUE DE INSTRUCCIONES

"""
"""
contador = 0
resultado = 0

for contador in range(0,10):
    print("voy por el "+ str(contador))

    resultado += contador

    print(f"El resultado es: {resultado}")

"""
# Ejemplo tablas de multiplicar

numero_usuario = int(input("¿De qué número quieres la tabla?: "))
limite = int(input("¿Hasta qué número quieres la tabla?: "))

# Control de valores mínimos
if numero_usuario < 1:
    numero_usuario = 1

if limite < 1:
    limite = 10

print(f"\n#### Tabla de multiplicar del número {numero_usuario} hasta {limite} ####\n")

for numero_tabla in range(1, limite + 1):
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario * numero_tabla}")

print("\nTabla finalizada.")