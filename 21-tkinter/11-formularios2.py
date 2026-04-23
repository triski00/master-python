from tkinter import *

def mostrarProfesion():
    texto = ""
    if web.get():
        texto += "Desarrollo web\n"
    if movil.get():
        texto += "Desarrollo móvil"
    resultado.config(text=texto)

ventana = Tk()
ventana.geometry("800x500")

encabezado = Label(ventana, text="Formularios 2")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    font=("Consolas", 20),
    bg="green"
)
encabezado.grid(row=0, column=0, columnspan=5, sticky=W)

web = IntVar()
movil = IntVar()

Checkbutton(
    ventana,
    text="Desarrollo web",
    variable=web,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=2, column=0)

Checkbutton(
    ventana,
    text="Desarrollo móvil",
    variable=movil,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=3, column=0)

resultado = Label(ventana, text="", fg="blue", font=("Arial", 14))
resultado.grid(row=4, column=0, pady=20)

# Radio buttons
def marcar():
    marcado.config(text=opcion.get())

opcion = StringVar()
opcion.set(None)

Label(ventana, text="¿Cuál es tu género?").grid(row=5, column=0)

Radiobutton(
    ventana,
    text="Masculino",
    value="Masculino",
    variable=opcion,
    command=marcar
).grid(row=6, column=0)

Radiobutton(
    ventana,
    text="Femenino",
    value="Femenino",
    variable=opcion,
    command=marcar
).grid(row=7, column=0)

marcado = Label(ventana, text="", fg="purple", font=("Arial", 14))
marcado.grid(row=8, column=0, pady=10)

# Option Menú
opcionMenu = StringVar()
opcionMenu.set("Opcion 1")

Label(ventana, text="¿Selecciona una opcion?").grid(row=5, column=1)

select = OptionMenu(ventana, opcionMenu, "Opcion 1", "Opcion 2", "Opcion 3")
select.grid(row=6, column=1)



ventana.mainloop()
