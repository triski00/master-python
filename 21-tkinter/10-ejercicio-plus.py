# CALCULADORA
# Con operaciones básicas
# Usando la librería tkinter
# Mostrar el resultado en una alerta

from tkinter import *
from tkinter import messagebox

class Calculadora:

    def __init__(self, alertas):
        self.primer_numero = StringVar()
        self.segundo_numero = StringVar()
        self.resultado = StringVar()
        self.alertas = alertas

    # Validar datos
    def validar_datos(self):
        if not self.primer_numero.get() or not self.segundo_numero.get():
            self.alertas.showerror("Error", "Debes llenar los datos!")
            return False
        try:
            float(self.primer_numero.get())
            float(self.segundo_numero.get())
            return True
        except:
            self.alertas.showerror("Error", "Debes introducir números válidos")
            return False

    # Sumar
    def sumar(self):
        if self.validar_datos():
            self.resultado.set(
                float(self.primer_numero.get()) + float(self.segundo_numero.get())
            )
            self.mostrar_resultado()

    # Restar
    def restar(self):
        if self.validar_datos():
            self.resultado.set(
                float(self.primer_numero.get()) - float(self.segundo_numero.get())
            )
            self.mostrar_resultado()

    # Multiplicar
    def multiplicar(self):
        if self.validar_datos():
            self.resultado.set(
                float(self.primer_numero.get()) * float(self.segundo_numero.get())
            )
            self.mostrar_resultado()

    # Dividir
    def dividir(self):
        if self.validar_datos():
            try:
                self.resultado.set(
                    float(self.primer_numero.get()) / float(self.segundo_numero.get())
                )
                self.mostrar_resultado()
            except ZeroDivisionError:
                self.alertas.showerror("Error", "No se puede dividir entre cero")

    # Mostrar resultado
    def mostrar_resultado(self):
        self.alertas.showinfo("Resultado", f"El resultado es: {self.resultado.get()}")


# Crear ventana
ventana = Tk()
ventana.title("Ejercicio completo con Tkinter | Marlon")
ventana.geometry("400x300")
ventana.config(bd=25)

calculadora = Calculadora(messagebox)

# Primer número
Label(ventana, text="Primer número:").grid(row=0, column=0, padx=10, pady=10)
Entry(ventana, textvariable=calculadora.primer_numero).grid(row=0, column=1)

# Segundo número
Label(ventana, text="Segundo número:").grid(row=1, column=0, padx=10, pady=10)
Entry(ventana, textvariable=calculadora.segundo_numero).grid(row=1, column=1)

# Botones
frame_botones = Frame(ventana)
frame_botones.grid(row=2, column=0, columnspan=2, pady=20)

Button(frame_botones, text="Sumar", width=10, command=calculadora.sumar).grid(row=0, column=0, padx=5)
Button(frame_botones, text="Restar", width=10, command=calculadora.restar).grid(row=0, column=1, padx=5)
Button(frame_botones, text="Multiplicar", width=10, command=calculadora.multiplicar).grid(row=0, column=2, padx=5)
Button(frame_botones, text="Dividir", width=10, command=calculadora.dividir).grid(row=0, column=3, padx=5)

# Resultado
Label(ventana, text="Resultado:").grid(row=3, column=0)
Entry(ventana, textvariable=calculadora.resultado, state="readonly").grid(row=3, column=1)

ventana.mainloop()
