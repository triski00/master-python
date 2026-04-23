# Capturar excepciones y manejar errorres en código
# susceptibles a fallos/errorres
"""
try:

    nombre = input("¿Cual es tu nombre?: ")


    if len(nombre) > 1:
     
     nombre_usuario = "El nombre es " + nombre
     print(nombre_usuario)
    
except:

  print("Ha ocurrido un error, mete bien el nombre cazurro ")

else:
  print("Todo ha ido bien")
finally:
  print("Fin de la interaccion!!")

  """

# Multiples excepciones

"""

try:

  numero = int(input("Dime el numero para elevarlo al cuadrado: "))
  print("El cuadrado es: "+str(numero*numero))

except typeError:
     print("Debes convertir tus cadenas a enteros !!")
except ValueError:
     print("Introduce un numero correcto !!")
except Exception as error:
    print("Ha ocurrido un error:", error)

    """

# Excepciones personalizadas
try:


  nombre = input("Introduce el nombre: ")
  edad = int(input("Introduce la edad: "))

  if edad < 5 or edad > 110:
    raise ValueError(" La edad introducida no es real")
  elif len(nombre) <= 1:
    raise ValueError("El nombre no está completo")

    print(f"Bienvenido al master de python {nombre} !!")
     
except ValueError as e:
 print("Introduce los datos correctamente $$$$")



