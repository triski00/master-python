from tkinter import *

ventana = Tk()
ventana.title("Marcos | Master en Python")
ventana.geometry("700x700")
ventana.config(bg="#d9d9d9")

# ---------------------------
# CONTENEDOR PRINCIPAL
# ---------------------------
contenedor = Frame(ventana, bg="#d9d9d9")
contenedor.pack(expand=True, pady=40)

# ---------------------------
# FILA 1
# ---------------------------
marco1 = Frame(contenedor, bg="blue", width=180, height=120, highlightbackground="black", highlightthickness=2)
marco1.grid(row=0, column=0, padx=10, pady=10)
marco1.pack_propagate(False)

texto1 = Label(marco1, text="Primer marco")
texto1.config(
    bg="blue",
    fg="white",
    font=("Arial", 16),
    anchor=CENTER
)
texto1.pack(expand=True, fill="both")


marco2 = Frame(contenedor, bg="lightblue", width=180, height=120, highlightbackground="black", highlightthickness=2)
marco2.grid(row=0, column=1, padx=10, pady=10)



marco3 = Frame(contenedor, bg="orange", width=180, height=120, highlightbackground="black", highlightthickness=2)
marco3.grid(row=0, column=2, padx=10, pady=10)

# ---------------------------
# FILA 2
# ---------------------------
marco4 = Frame(contenedor, bg="red", width=180, height=120, highlightbackground="black", highlightthickness=2)
marco4.grid(row=1, column=0, padx=10, pady=10)
marco4.pack_propagate(False)

texto4 = Label(marco4, text="Cuarto marco")
texto4.config(
    bg="red",
    fg="white",
    font=("Arial", 16),
    anchor=CENTER
)
texto4.pack(expand=True, fill="both")





marco5 = Frame(contenedor, bg="lightblue", width=180, height=120, highlightbackground="black", highlightthickness=2)
marco5.grid(row=1, column=1, padx=10, pady=10)



marco6 = Frame(contenedor, bg="green", width=180, height=120, highlightbackground="black", highlightthickness=2)
marco6.grid(row=1, column=2, padx=10, pady=10)

# Evitar que los marcos se colapsen
for marco in (marco1, marco2, marco3, marco4, marco5, marco6):
    marco.grid_propagate(False)

ventana.mainloop()
