"""

Una variable ed un contenedor de información que dentro guardará un dato
se pueden cre<r muchas variables y que cada una tenga un dato distinto.
"""

# Crear variables y asignar un valor
Texto = "Máster en Python por VictorR"
Texto2 = "con perraco"
numero = 45
decimal = 6.7

# Mostrar el valor de las variables
print(Texto)

print(Texto2)

print(numero)

print(decimal)

print("----------------------------------------------")

# Sustituir de algunas variables / reasignando valores
numero = 77
decimal =  8.9
print(numero)
print(decimal)


# Concatenación

nombre = "Mario"
apellidos = "Avila"
web = "pere.es"

print("------------------------------------------")

# Concatenacion

nombre = "Mario"
apellidos = "Avila"
web = "perraco.es"

print(nombre + " " + apellidos + " _ " + web)
print(f"{nombre} {apellidos} - {web}")
print("Hola me llamo {} {} y mi web es: {}".format(nombre, apellidos, web))