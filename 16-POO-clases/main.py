# Programacion orientada a objetos (POO)

# Definir una clase (molde para crear mas objetos
#(Coche) con caracteristicas similares)

class Coche:

    def __init__(self):
        self.__color = "Rojo"
        self.__marca = "Ferrari"
        self.__modelo = "Aventador"
        self.__velocidad = 300
        self.__caballaje = 5
        self.__plazas = 2

    # Getters
    def getColor(self):
        return self.__color

    def getModelo(self):
        return self.__modelo

    def getVelocidad(self):
        return self.__velocidad

    # Setters
    def setColor(self, color):
        self.__color = color

    def setModelo(self, modelo):
        self.__modelo = modelo

    # Acciones
    def acelerar(self):
        self.__velocidad += 1

    def frenar(self):
        self.__velocidad -= 1


# Crear objeto
coche = Coche()

print("COCHE 1: ")

coche.setColor("amarillo")
coche.setModelo("Murcielago")

print(coche.getColor(), coche.getModelo())
print("Velocidad actual:", coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()

print("Velocidad nueva:", coche.getVelocidad())

print("---------------------")

# Crear mas objetos

coche2 = Coche()

coche2.setColor("Verde")
coche2.setModelo("Gallardo")

print("COCHE 2:")
print(coche2.getModelo(), coche2.getColor())


