"""

Ejercicio. 3 Programa que compruebe si una variable sesta vacia y 
si esta vacia , rellenarla con texto en minusculas y mostarrlo en mayusculas.

"""

texto = " "

if len(texto.strip()) <= 0:

    texto  = "hola soy un texto en misnusculas"
    print(texto.upper())

else:
    print(f"La variable tiene contenido {texto}")

    