# tkinter:
# Módulo para crear interfaces gráficas de usuario

from tkinter import *
import os.path

class Programa:
    def __init__(self):
        self.title = "Master python con VR"
        self.icono = "./imagenes/favicon.ico"
        self.icon_alt = "./21-tkinter/imagenes/favicon.ico"
        self.size = "800x800"
        self.resizable = False

    def cargar(self):
        ventana = Tk()
        self.ventana = ventana
        ventana.title(self.title)
        # ... resto del código ...
    
    def addTexto(self, dato):
        texto = Label(self.ventana, text=dato)
        texto.pack()

    def mostrar(self):
        self.ventana.mainloop()


# Ejecución del programa
programa = Programa()
programa.cargar()
programa.addTexto("Hola")
programa.addTexto("soy un texto")
programa.addTexto("Bienvenido al master de python")
programa.addTexto("Tus muelas")
programa.mostrar()


