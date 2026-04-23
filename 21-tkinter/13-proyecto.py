"""
Crear un programa que tenga:
listo-Ventana
listo-Tamaño fijo
listo-No redimensionable
listo-Un menú (inicio,información,salir)
listo-Diferentes pantallas
listo-Formulario de añadir productos
listo-Guardar datos tamporales
listo-Mostrar datos listados en la pantalla home
listo-Opcion de salir
"""

from tkinter import *

# -------------------------
#   VARIABLES GLOBALES
# -------------------------
productos = []

# -------------------------
#   VENTANA PRINCIPAL
# -------------------------
ventana = Tk()
ventana.title("Proyecto Tkinter - Master en Python")
ventana.geometry("500x500")
ventana.resizable(False, False)

# -------------------------
#   VARIABLES DE FORMULARIO
# -------------------------
name_data = StringVar()
price_data = StringVar()

# -------------------------
#   FUNCIONES
# -------------------------

def home():
    add_label.grid_remove()
    ad_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    home_label.config(
        text="Inicio",
        bg="black",
        fg="white",
        font=("Arial", 30),
        padx=80,
        pady=20
    )
    home_label.grid(row=0, column=0, sticky="w")

    # Construir texto con formato
    texto = ""
    for nombre, precio, descripcion in productos:
        texto += f"{nombre}\n{precio}\n{descripcion}\n----------\n"

    home_products_label.config(text=texto)
    home_products_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")


def add():
    home_label.grid_remove()
    home_products_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    add_label.config(
        text="Añadir producto",
        bg="black",
        fg="white",
        font=("Arial", 30),
        padx=80,
        pady=20
    )
    add_label.grid(row=0, column=0, sticky="w")

    ad_frame.grid(row=1, column=0, padx=20, pady=20, sticky="w")

    add_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    add_name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    add_price_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    add_price_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    add_desc_label.grid(row=2, column=0, padx=5, pady=5, sticky="ne")
    add_description_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    boton.grid(row=3, column=1, padx=5, pady=15, sticky="e")


def info():
    home_label.grid_remove()
    home_products_label.grid_remove()
    add_label.grid_remove()
    ad_frame.grid_remove()

    info_label.grid(row=0, column=0, sticky="w")
    data_label.grid(row=1, column=0, sticky="w")


def add_products():
    nombre = name_data.get()
    precio = price_data.get()
    descripcion = add_description_entry.get("1.0", "end-1c")

    productos.append((nombre, precio, descripcion))

    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", "end")

    home()  # Volver a inicio automáticamente


# -------------------------
#   MENÚ SUPERIOR
# -------------------------
menu_superior = Menu(ventana)
ventana.config(menu=menu_superior)

menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

# -------------------------
#   WIDGETS
# -------------------------

# HOME
home_label = Label(ventana)
home_products_label = Label(ventana, text="", font=("Arial", 12), justify="left")

# ADD
add_label = Label(ventana)
ad_frame = Frame(ventana)


add_name_label = Label(ad_frame, text="Nombre:")
add_name_entry = Entry(ad_frame, textvariable=name_data)

add_price_label = Label(ad_frame, text="Precio:")
add_price_entry = Entry(ad_frame, textvariable=price_data)

add_desc_label = Label(ad_frame, text="Descripción:")
add_description_entry = Text(ad_frame, width=40, height=5)

boton = Button(ad_frame, text="Guardar", bg="green", fg="white", command=add_products)

# INFO
info_label = Label(ventana, text="Información", font=("Arial", 20))
data_label = Label(ventana, text="Creado por Mario - 2026", font=("Arial", 12))

# -------------------------
#   INICIAR EN HOME
# -------------------------
home()

ventana.mainloop()

ventana.mainloop()


