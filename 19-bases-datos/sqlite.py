# Import modulo
import sqlite3

# Conexion
conexion = sqlite3.connect('pruebas.db')

# crear cursor
cursor = conexion.cursor()


# crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  "titulo varchar(255),
  "descripcion text,
  "precio int(255)"
);
""")

# guardar cambios
conexion.commit()

# insertar datos
"""
cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'Descripcion de mi producto', 550)")
conexion.commit()
"""

# Borrar registros
cursor.execute("DELETE FROM productos")
conexion.commit()

# Insertar muchos registros de golpe

productos = [
    ("ordenador portatil", "BUEN PC", 700),
    ("Telefono movil", "BUEN telefono", 200),
    ("Placa base", "BUENA PLACA", 80),
    ("Monitor", "Pantalla grande", 300)
]

cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ?)", productos)
conexion.commit()

# Update
cursor.execute("UPDATE productos SET precio=600 WHERE precio=80")
 
# listar datos 
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()

for producto in productos:
    print("ID: ",producto[0])
    print("Titulo:", producto[1])
    print("Descripcion:", producto[2])
    print("Descripcion:", producto[3])
    print("/n")


# Cerrar conexion
conexion.close()

