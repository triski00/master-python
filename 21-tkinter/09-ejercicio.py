# CALCULADORA
# Con operaciones básicas
# Usando la librería tkinter
# Mostrar el resultado en una alerta

from tkinter import *
from tkinter import messagebox

# Crear ventana
ventana = Tk()
ventana.title("Ejercicio completo con Tkinter | Marlon")
ventana.geometry("400x300")

# Variables
primer_numero = StringVar()
segundo_numero = StringVar()
resultado = StringVar()

# Validar datos
def validar_datos():
    if not primer_numero.get() or not segundo_numero.get():
        messagebox.showerror("Error", "¡Debes llenar los datos!")
        return False
    
    # Validar que sean números
    try:
        float(primer_numero.get())
        float(segundo_numero.get())
        return True
    except:
        messagebox.showerror("Error", "Debes introducir números válidos")
        return False

# Operaciones
def sumar():
    if validar_datos():
        resultado.set(float(primer_numero.get()) + float(segundo_numero.get()))
        mostrar_resultado()

def restar():
    if validar_datos():
        resultado.set(float(primer_numero.get()) - float(segundo_numero.get()))
        mostrar_resultado()

def multiplicar():
    if validar_datos():
        resultado.set(float(primer_numero.get()) * float(segundo_numero.get()))
        mostrar_resultado()

def dividir():
    if validar_datos():
        try:
            resultado.set(float(primer_numero.get()) / float(segundo_numero.get()))
            mostrar_resultado()
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir entre cero")

# Mostrar resultado
def mostrar_resultado():
    messagebox.showinfo("Resultado", f"El resultado de la operación es: {resultado.get()}")

# Primer número
Label(ventana, text="Primer número:").grid(row=0, column=0, padx=10, pady=10)
Entry(ventana, textvariable=primer_numero).grid(row=0, column=1)

# Segundo número
Label(ventana, text="Segundo número:").grid(row=1, column=0, padx=10, pady=10)
Entry(ventana, textvariable=segundo_numero).grid(row=1, column=1)

# Botones
frame_botones = Frame(ventana)
frame_botones.grid(row=2, column=0, columnspan=2, pady=20)

Button(frame_botones, text="Sumar", width=10, command=sumar).grid(row=0, column=0, padx=5)
Button(frame_botones, text="Restar", width=10, command=restar).grid(row=0, column=1, padx=5)
Button(frame_botones, text="Multiplicar", width=10, command=multiplicar).grid(row=1, column=0, padx=5)
Button(frame_botones, text="Dividir", width=10, command=dividir).grid(row=1, column=1, padx=5)

# Resultado
Label(ventana, text="Resultado:").grid(row=3, column=0)
Entry(ventana, textvariable=resultado, state="readonly").grid(row=3, column=1)

ventana.mainloop()
