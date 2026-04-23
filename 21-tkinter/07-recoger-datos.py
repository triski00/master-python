from tkinter import *

ventana = Tk()
ventana.geometry("700x700")
ventana.config(
    bd=50,
    bg="#ccc"
)

# Variables
dato = StringVar()
resultado = StringVar()

# Función que recoge el dato
def getDato():
    resultado.set(dato.get())

    if len(resultado.get()) >= 1:
        texto_recogido.config(
            bg="green",
            fg="white"
        )

# Etiqueta y campo de entrada
Label(ventana, text="Mete un texto: ").pack(anchor=NW)
Entry(ventana, textvariable=dato).pack(anchor=W)

# Etiqueta para mostrar el resultado
Label(ventana, text="Dato recogido: ").pack(anchor=NW)
texto_recogido = Label(ventana, textvariable=resultado)
texto_recogido.pack(anchor=NW)

# Botón
Button(ventana, text="Mostrar dato", command=getDato).pack(anchor=NW)

ventana.mainloop()

