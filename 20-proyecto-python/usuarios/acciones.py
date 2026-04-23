import usuarios.usuario as modelo
import notas.acciones as accionesNotas

class Acciones:

    def registro(self):
        print("\nOk!! Vamos a registrarte en el sistema....")

        nombre = input("¿Cuál es tu nombre?: ")
        apellidos = input("¿Cuáles son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("No te has registrado correctamente!!!")

    def login(self):
        print("\nIdentifícate en el sistema....")

        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario("", "", email, password)
        login = usuario.identificar()

        if login:
            print(f"\nBienvenido {login[1]} {login[2]}")
            print(f"Te registraste en el sistema el {login[5]}")
            self.proximasAcciones(login)
        else:
            print("\nLogin incorrecto")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - crear
        - mostrar
        - borrar
        - salir
        """)

        accion = input("¿Qué quieres hacer?: ")
        hazEl = accionesNotas.Acciones()

        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "borrar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "salir":
            print("Hasta pronto")
            exit()






       




