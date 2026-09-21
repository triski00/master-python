from datetime import date

import mysql.connector

import usuarios.conexion as conexion
import usuarios.seguridad as seguridad

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]


class Usuario:

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        # Fecha real de registro (el conector la convierte al formato AAAA-MM-DD)
        fecha = date.today()

        # Guardar la contraseña con hash y sal, nunca en claro
        cifrado = seguridad.hashear_password(self.password)

        sql = "INSERT INTO usuarios VALUES(NULL, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado, fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except mysql.connector.IntegrityError:
            # El email ya existe (restricción UNIQUE). Otros errores no se
            # ocultan: se propagan para poder verlos y corregirlos.
            database.rollback()
            result = [0, self]

        return result

    def identificar(self):
        # Se busca por email y la contraseña se verifica contra su hash con sal
        sql = "SELECT * FROM usuarios WHERE email = %s"
        cursor.execute(sql, (self.email,))
        fila = cursor.fetchone()

        # Columnas: id, nombre, apellidos, email, password, fecha
        if fila and seguridad.verificar_password(self.password, fila[4]):
            return fila

        return None
