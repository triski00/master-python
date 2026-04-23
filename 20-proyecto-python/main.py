from usuarios import acciones  

print("""
      Acciones disponibles:
      -registro
      -login
      """)

hazEl = acciones.Acciones()  

accion = input("¿Qué quieres hacer? (registro/login): ")

if accion == "registro":
     hazEl.registro()

elif accion == "login":
    hazEl.login()