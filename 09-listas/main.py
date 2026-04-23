"""
LISTAS (arrays)
Son colecciones o conjuntos de datos/valores, bajo un unico
nombre.
Para acceder a esos valores podemos usar un indice numerico.
"""
# Definir una lista
pelicula = "Batman"
peliculas = ["Batman", "Spiderman", "Lord of the Ring"]
cantantes = list(("Tus Muelas", "Drake", "JL"))
year =list(range(2020, 2050))
variada = ["Mario", 30,4.4, 100, "texto"]
"""
print(pelicula)
print(cantantes)
print(year) 
print(variada)
"""

# Indices
pelicula = "otra cosa"
peliculas[1] = "Gran Torino"
peliculas[2] = "El condon Asesino"
print(peliculas)

print(peliculas[1])
print(cantantes[0:3])

# Añadir elementos a lista

cantantes.append("Ladilla Rusa")
print(cantantes)

#Recorrer Lista
"""
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")

    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

print("\n********LISTADO PELICULAS********")


for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")

"""
    #Listas multidimensionales

print("\n******** Listado de contactos ********")

contactos = [
    {"nombre": "Antonio", "email": "Antonio@antonio.com"},
    {"nombre": "Luis", "email": "luis@luis.com"}
]

for contacto in contactos:
    print("Nombre:", contacto["nombre"])
    print("Email:", contacto["email"])
    print("----------------------")
              



