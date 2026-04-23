"""

# Condicional IF

Si_se_cumple_esta_condición:
  Ejecutargrupo de instrucciones
  SI NO:
  Se ejecutan otro grupo de instrucciones

  if condicion:
     instrucciones
     else:
         otras instruciones

"""
"""
# Operadores de comparacion
== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que 

"""

# Operadores logicos


"""
# Ejemplo 1

print("####### EJEMPLO 1 #######")

color =  input("Adivina cual es mi color favorito:")

if color == "rojo":
  print("Enhorabuena!!")
  print("El color es rojo")
        
else:
     print("El color es incorrecto")  

       # Ejemplo 2

print("####### EJEMPLO 2 #######")    
 
#year = 2020
year = int(input("¿En que año estamos? "))

if year >= 2021:
    print("Estamos de 2021 en adelante !!")
else:
    print("Es un año anterior a 2021")

     # Ejemplo 3

print("####### EJEMPLO 3 #######")

nombre = "Mario Avila"
ciudad = "Madrid"
continente = "Europa"
edad = 55
mayoria_edad = 18

if edad >= mayoria_edad:
        print(f"{nombre} es mayor de edad")

        if continente != "Europa":
           print("El usuario No es europeo")
        else:
            print(f"Es europeo y de {ciudad} !!")
   

     # instrucciones
     
else:
    print(f"{nombre} No es mayor de edad !!")


     # Ejemplo 4


print("\n###### EJEMPLO 4 #######")

dia = int(input("Introduce el numero del dia de la semana: "))

"""
"""
if dia == 1:
    print("Es viernes")
else:
    if dia == 2:
        print("Es sabado")
    else:
        if dia == 3:
            print("Es domingo")

   

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
else:
    print("Ya es fin de semana")

    """

    # Ejemplo 5

print("\n###### EJEMPLO 5 #######")
"""
    edad minima = 18
    edad_maxima = 65
    # edad_oficial = int(input("¿Tienes edad de trabajar? Introduce tu edad: "))
    edad_oficial = 18

    if edad_oficial >=18 and edad_oficial <= 65:
        print("Esta en la edad de trabar !!")
    else:
        print("No esta en la edad de trabajar")
                
"""

# Ejemplo 6

print("\n###### EJEMPLO 6 #######")

pais = "Italia"

if pais == "Mexico" or pais == "España" or pais == "Italia":
    print(f"{pais} es un pais de habla hispana !!")
else:
    print (f"{pais} no es un pais de habla hispana (")


    # Ejemplo 7

print("\n###### EJEMPLO 7 #######")

pais = "España"

if  not (pais == "Mexico" or pais == "España" or pais == "Italia"):
    print(f"{pais}  NO es un pais de habla hispana !!")
else:
    print (f"{pais} SI es un pais de habla hispana :(")


       # Ejemplo 8

print("\n###### EJEMPLO 8 #######")

pais = "USA"

if  pais != "Mexico" and pais != "España" and pais != "Italia":
    print(f"{pais}  NO es un pais de habla hispana !!")
else:
    print (f"{pais} SI es un pais de habla hispana :)")
