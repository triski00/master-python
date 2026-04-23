from tkinter import *

ventana = Tk()
ventana.geometry("700x500")

texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
    height=3,
    font=("Arial", 30),
    fg="black",
    bg="yellow",
    padx=60,
    pady=20,
    cursor="spider"
)

texto.pack(anchor=SE)

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos}, veo que eres de {pais}"

texto2 = Label(ventana, text=pruebas(nombre="Mario", apellidos="Avila", pais="España"))
texto2.config(
    height=3,
    bg="green",
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="spider"
)

texto2.pack(anchor=NW)

ventana.mainloop()



