"""
Ejercicio6
Mostarar todas las tablas de multiplicar del 1 al 10.
Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10.
"""
for cabecera in range(1, 11):
 print("#####################")
 print(f"###### tabla del {cabecera} ######")
 print("#####################")

 for numero in range(1, 11):
  print(f"{numero} x {cabecera}  {numero*cabecera}")

  print("\n")