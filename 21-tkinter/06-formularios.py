from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.title("Formularios en Tkinter | Victor Robles")

# Encabezado
encabezado = Label(ventana, text="Formularios con Tkinter - VR")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans", 18),
    padx=10,
    pady=10
)
encabezado.grid(row=0, column=0, columnspan=2, sticky=W)

# Campo: Nombre
label_nombre = Label(ventana, text="Nombre")
label_nombre.grid(row=1, column=0, sticky=W, padx=5, pady=5)

campo_nombre = Entry(ventana)
campo_nombre.grid(row=1, column=1, sticky=W, padx=5, pady=5)
campo_nombre.config(justify="left", state="normal")

# Campo: Apellidos
label_apellidos = Label(ventana, text="Apellidos")
label_apellidos.grid(row=2, column=0, sticky=W, padx=5, pady=5)

campo_apellidos = Entry(ventana)
campo_apellidos.grid(row=2, column=1, sticky=W, padx=5, pady=5)
campo_apellidos.config(justify="left", state="normal")

# Campo: descripción
label_apellidos = Label(ventana, text="Descripcion")
label_apellidos.grid(row=3, column=0, sticky=N, padx=5, pady=5)
# Campo texto grande
campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1)
campo_grande.config(
    width=30,
    height=5,
    font=("Arial", 12),
    padx=15,
    pady=15
)

# Botón
Label(ventana).grid(row=4, column=1)

boton = Button(ventana, text="Envia")
boton.grid(row=5, column=1, sticky=W)
boton.config(padx=15, pady=15, bg="green", fg="white")

ventana.mainloop()



