import os

import mysql.connector


def conectar():
    """Abre la conexión a MySQL.

    Los datos de conexión se leen de variables de entorno (con valores por
    defecto pensados para un MySQL local de pruebas):
        MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE, MYSQL_PORT
    """
    database = mysql.connector.connect(
        host=os.environ.get("MYSQL_HOST", "localhost"),
        user=os.environ.get("MYSQL_USER", "root"),
        password=os.environ.get("MYSQL_PASSWORD", ""),
        database=os.environ.get("MYSQL_DATABASE", "master_python"),
        port=int(os.environ.get("MYSQL_PORT", "3306")),
    )

    cursor = database.cursor(buffered=True)

    return [database, cursor]
