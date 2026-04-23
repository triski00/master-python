import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Nota:

    def __init__(self, usuario_id, titulo="", descripcion=""):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    def guardar(self):
        sql = "INSERT INTO notas VALUES (NULL, %s, %s, %s, NOW())"
        datos = (self.usuario_id, self.titulo, self.descripcion)

        cursor.execute(sql, datos)
        database.commit()

        return [cursor.rowcount, self]

    def listar(self):
        sql = "SELECT * FROM notas WHERE usuario_id = %s"
        cursor.execute(sql, (self.usuario_id,))
        return cursor.fetchall()

    def borrar(self):
        sql = "DELETE FROM notas WHERE usuario_id = %s AND titulo = %s"
        datos = (self.usuario_id, self.titulo)

        cursor.execute(sql, datos)
        database.commit()

        return [cursor.rowcount, self]

    def eliminar(self, titulo):
        sql = "DELETE FROM notas WHERE usuario_id = %s AND titulo LIKE %s"
        datos = (self.usuario_id, f"%{titulo}%")

        cursor.execute(sql, datos)
        database.commit()

        return [cursor.rowcount, self]




