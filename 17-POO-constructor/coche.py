class Coche:
        
        # Atributos o propiedades ( variables)

        # Caracteristicas dell coche

    soy_publico = "Hola soy un atributo publico"
    __soy_privado = "Hola soy un atributo privado"

    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
    
        self.__color = color
        self.__marca = marca
        self.__modelo = modelo
        self.__velocidad = velocidad
        self.__caballaje = caballaje
        self.__plazas = plazas

       

        

               

    # Getters
    def getColor(self):
        return self.__color

    def getModelo(self):
        return self.__modelo
    
    def getMarca(self):
        return self.__marca

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

    def getInfo(self):
        info = "---- Información del coche  -----"
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str(self.getVelocidad())

        return info






# Crear objeto
datos = "Ferrari, Aventador, 300, 500, 2".split(", ")

coche = Coche("Amarillo", datos[0], datos[1], int(datos[2]), int(datos[3]), int(datos[4]))

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
carro = Coche("Amarillo", "Renault", "Clio", 150, 200, 4)

coche2 = Coche("Amarillo", datos[0], datos[1], int(datos[2]), int(datos[3]), int(datos[4]))

coche2.setColor("Amarillo")
coche2.setModelo("Renault")

print("COCHE 2:")
print(coche2.getModelo(), coche2.getColor())

