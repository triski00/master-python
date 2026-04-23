"""

Ejercicio 4. 
Crear un script que tenga 4 variables, una ista, un string,
un entero y un booleano y que imprima un mensaje
segun el tipo de datos de cada variable. Usar funciones.
"""

def traducirTipo(Tipo):
    if tipo == list:
        result = "Lista"
    elif tipo == str:
        result = "CADENA DE TEXTO"
    elif tipo == int:
        result = "NUMERO ENTERO"
    elif tipo == boll:
        result = "BOOLEANO"

        return result


def comprobarTipado(dato, tipo):
    result = ""
    test = isinstance(dato, tipo)

    if test:
        print(f"Este dato es de tipo {type(dato)}")
    else:
        result = "El tipo de dato no corresponde"

        return result



mi_lista = ["hola mundo", 77]
titulo = "Master en Python"
numero = 100
verdadero = True

print(comprobarTipado(mi_lista, list))
print(comprobarTipado(titulo, str))
print(comprobarTipado(verdadero, bool))
print(comprobarTipado(numero, int))






