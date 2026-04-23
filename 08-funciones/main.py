"""
FUNCIONES:
Una funcion es un conjunto de instrucciones agrupadas bajo
un nombre concreto que pueden reutilizarse invocando a 
la funcion tantas veces como sea necesario.

def nomnbredemifuncion(parametros):
# BLOQUE  / CONJUNTO DE INSTRUCCIONES
nombre demifuncion(mi_parametro)
nombre demifuncion(mi_parametro)


"""
"""
#Ejemplo 1

print("####### EJEMPLO 1 #######")
      
      #Definir funcion
def muestranombre():
       print("Mario")
       print("Victor")
       print("Marco")
       print("Mosca")
       print("Tio Fill")
       print("\n")

#Invocar funciones
muestranombre()
muestranombre()


#Ejemplo 2 : Parametros
print("####### EJEMPLO 2 #######")


def mostartunomnbre(nombre, edad):
       print(f"Tu Nombre es: {nombre}")

       if edad >=18:
              print("Ya eres mayor de edad")
              

nombre = input("Introduce tu Nombre: ")
edad = int(input("Introduce tu edad: "))

mostartunomnbre(nombre, edad)

"""

#Ejemplo 3

print("####### EJEMPLO 3 #######")


def tabla(numero):
    print(f"Tabla de multiplicar del numero:  {numero}")
       
    for contador in range(11):
              operacion = numero*contador
              print(f"{numero} x {contador}  {operacion}")

              print("\n")

tabla(3)
tabla(7)
tabla(12)

#Ejemplo 3.1

print("--------------------------------")
for numero_tabla in range(1, 11):
       tabla(numero_tabla)


# Ejemplo 4

print("####### EJEMPLO 4 #######")

# Parametros opcionales

def getEmpleado(nombre, dni=None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")

    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Mario", "08940810C")


#Ejemplo 5: Parametros opcionales y return o devolver datos

def saludame(nombre):
       saludo = f"Hola, saludos {nombre}"

       return saludo
print(saludame("Mario"))

# Ejemplo 6 

def calculadora(numero1, numero2, basicas=False):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    if basicas:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "División: " + str(division)

    return cadena


print(calculadora(80, 5))

#Ejemplo 7

print("\n####### EJEMPLO 7 ######")


def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto


def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto


def devuelvetodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto


print(devuelvetodo("Mario", "Avila"))

#Ejemplo 8: Funciones Lambda
print ("\n##### EJEMPLO 8 ######")

dime_el_year = lambda year:f"El año es {year *50}"

print(dime_el_year(2034))










