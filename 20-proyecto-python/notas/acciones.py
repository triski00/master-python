import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"\nOk {usuario[1]}!!! Vamos a crear una nueva nota...")
        titulo = input("Introduce el título de tu nota: ")
        descripcion = input("Mete el contenido de tu nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto, has guardado la nota: {nota.titulo}")
        else:
            print(f"No se ha guardado la nota, lo siento {usuario[1]}")

    def mostrar(self, usuario):
        print(f"\nVale {usuario[1]}!! Aquí tienes tus notas:")

        nota = modelo.Nota(usuario[0], "", "")
        notas = nota.listar()

        for n in notas:
            print("\n----------------------------------")
            print(f"Título: {n[2]}")
            print(f"Descripción: {n[3]}")
            print("----------------------------------")

        input("\nPulsa ENTER para volver al menú...")

    def borrar(self, usuario):
        print(f"\nOk {usuario[1]}!!! Vamos a borrar una nota...")

        titulo = input("Introduce el título de la nota a borrar: ")

        nota = modelo.Nota(usuario[0], titulo, "")
        borrar = nota.borrar()

        if borrar[0] >= 1:
            print(f"\nPerfecto, has borrado la nota: {titulo}")
        else:
            print(f"No se ha borrado la nota, lo siento {usuario[1]}")


                


