"""
Variables locales: Se definen de la función y no
se puede usar fuera de ella, solo solo estan disponibles dentro.
A no ser que hagamos un retrun.

Variables globales: Son las que se declaran fuera de una función 
y estan disponibles dentro y fuera de ellas.

"""

# variables global

frase = "Ni los genios son genios, ni los mediocre tan mediocres."
print(frase)

def HolaMundo():
 frase = "Hola Mundo!!"

 print(frase)

 year = 2026
 print(year)

 global website
 website = "marioweb.es"
 print("DENTRO: ", website)
  
 return "Dato devuelto " + str(year)


print(HolaMundo())
print("FUERA: ", website)