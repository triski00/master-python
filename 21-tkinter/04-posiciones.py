from tkinter import *

ventana = Tk()
ventana.geometry("700x500")
ventana.config(bg="#d9d9d9")  # gris claro

# ---------------------------
# BANNER SUPERIOR (NEGRO)
# ---------------------------
banner = Label(
    ventana,
    text="Bienvenido a mi programa",
    fg="white",
    bg="black",
    font=("Arial", 22),
    padx=20,
    pady=20
)
banner.pack(fill=X)

# ---------------------------
# BANNER NARANJA (DEBAJO)
# ---------------------------
subtitulo = Label(
    ventana,
    text="Soy Victor Robles",
    fg="black",
    bg="orange",
    font=("Arial", 20),
    padx=20,
    pady=20
)
subtitulo.pack(fill=X)

# ---------------------------
# BLOQUES INFERIORES (3)
# ---------------------------
bloques = Frame(ventana, bg="#d9d9d9")
bloques.pack(fill=X, pady=20)

Label(
    bloques,
    text="Basico 1",
    bg="green",
    fg="white",
    font=("Arial", 18),
    padx=40,
    pady=20
).pack(side=LEFT, expand=True, padx=10)

Label(
    bloques,
    text="Basico 2",
    bg="red",
    fg="white",
    font=("Arial", 18),
    padx=40,
    pady=20
).pack(side=LEFT, expand=True, padx=10)

Label(
    bloques,
    text="Basico 3",
    bg="pink",
    fg="black",
    font=("Arial", 18),
    padx=40,
    pady=20
).pack(side=LEFT, expand=True, padx=10)

ventana.mainloop()

