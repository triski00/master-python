"""

Diccionario:
Un tipo de datos que almacena un conjunto de datos.
En formato clave < valor.
Es parecido a un array asociativo o un objeto json.
"""
persona = {
    "nombre": "Mario",
    "apellidos": "Avila",
    "web": "mario.avila@gmail.com"
}

print(persona["apellidos"])

# Lista con diccionarios

contactos = [
    {
        'nombre': 'Antonio',
        'email': 'antonio@antonio.com'
    },
    {
        'nombre': 'Luis',
        'email': 'luis@luis.com'
    },
    {
        'nombre': 'Salvador',
        'email': 'salvador@salvador.com'
    }
]

contactos[0]['nombre'] = "Antoñito"
print(contactos[0]['nombre'])

print("\nListado de contactos: ")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("-------------------------------")








