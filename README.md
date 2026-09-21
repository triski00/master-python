# Máster en Python

Repositorio de aprendizaje del **Máster en Python**: ejercicios y proyectos ordenados por temas, desde los fundamentos del lenguaje hasta una aplicación web con Django.

![Tests](https://github.com/triski00/master-python/actions/workflows/python-package.yml/badge.svg)

> ## ⚠️ Proyecto didáctico
> Este código se ha escrito **para aprender**. No está pensado para producción.
> Algunas cosas están simplificadas a propósito:
>
> - **`20-proyecto-python`**: app de consola sin interfaz ni capa de servicio. La contraseña se guarda con PBKDF2 y sal, implementado a mano con `hashlib` para entender cómo funciona; en un proyecto real habría que usar una solución probada (autenticación de Django, bcrypt o argon2). La conexión a MySQL es una única conexión global, sin pool.
> - **`22-django`**: usa SQLite y `django-ckeditor`, que incluye CKEditor 4, una versión sin soporte y con vulnerabilidades conocidas (Django lo avisa al arrancar). Para un sitio real habría que cambiar de editor y de base de datos, y preparar el despliegue (archivos estáticos, servidor, HTTPS).
> - Los ejercicios sueltos (`01` a `19`) son prácticas de clase y no tienen tests.

## Contenido

| Carpeta | Tema |
|---|---|
| `01` – `06` | Fundamentos: hola mundo, variables y tipos, operadores, entrada/salida, condicionales y bucles |
| `07`, `11` | Ejercicios de repaso |
| `08` – `10` | Funciones, listas, sets y diccionarios |
| `12` – `13` | Módulos y paquetes |
| `14` – `15` | Sistema de archivos y manejo de errores |
| `16` – `18` | Programación orientada a objetos: clases, constructor y herencia |
| `19-bases-datos` | Bases de datos con SQLite |
| `20-proyecto-python` | **Proyecto:** gestor de notas por consola con usuarios y MySQL |
| `21-tkinter` | Interfaces gráficas con tkinter |
| `22-django` | Django: `AprendiendoDjango` (primeros pasos) y **`ProyectoDjango2`** (blog y páginas con panel de administración) |

## Requisitos

- Python 3.12 o superior (Django 6.0 lo exige)
- MySQL o MariaDB, solo para `20-proyecto-python`

## Puesta en marcha

Los comandos son para **Windows (PowerShell)**. En Linux o macOS: `source venv/bin/activate` para activar el entorno y `export VARIABLE=valor` para las variables de entorno.

```powershell
git clone https://github.com/triski00/master-python.git
cd master-python
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### `20-proyecto-python` (notas por consola con MySQL)

Registro y login de usuarios, y crear, listar y borrar notas propias.

1. Crea la base de datos y las tablas ejecutando `20-proyecto-python/basedatos.sql` en tu servidor MySQL.
2. Define la conexión con variables de entorno (los valores por defecto son `localhost`, `root`, sin contraseña, base `master_python` y puerto `3306`):

```powershell
$env:MYSQL_USER = "mi_usuario"
$env:MYSQL_PASSWORD = "mi_contraseña"
# Opcionales: MYSQL_HOST, MYSQL_DATABASE, MYSQL_PORT
```

3. Ejecuta la aplicación desde su carpeta:

```powershell
cd 20-proyecto-python
python main.py
```

### `22-django/ProyectoDjango2` (blog y páginas)

Blog con artículos y categorías (relación muchos a muchos), imágenes y editor de texto enriquecido; páginas dinámicas con URL amigable, orden y visibilidad, cuyo menú se genera con un *context processor*. Todo se gestiona desde el panel de administración.

```powershell
cd 22-django\ProyectoDjango2
$env:DJANGO_DEBUG = "1"          # modo desarrollo local
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

| Ruta | Qué muestra |
|---|---|
| `/` | Inicio |
| `/articulos/` | Lista de artículos |
| `/pagina/<slug>/` | Página dinámica creada desde el admin |
| `/admin/` | Panel de administración |

`AprendiendoDjango` se arranca igual desde `22-django\AprendiendoDjango`.

#### Variables de entorno de Django

| Variable | Uso |
|---|---|
| `DJANGO_DEBUG` | `1` activa el modo desarrollo. Sin ella, `DEBUG` está desactivado |
| `DJANGO_SECRET_KEY` | Clave secreta. Obligatoria si `DJANGO_DEBUG` no es `1` |
| `DJANGO_ALLOWED_HOSTS` | Hosts permitidos separados por comas (con `DEBUG` desactivado) |

La clave secreta y la base de datos local **no se suben al repositorio** (`.gitignore`).

## Tests

```powershell
# En la raíz: tests de 20-proyecto-python
pytest

# Tests de ProyectoDjango2 (con DJANGO_DEBUG=1 o DJANGO_SECRET_KEY definida)
cd 22-django\ProyectoDjango2
python manage.py test
```

- `pytest` comprueba el hash y la verificación de contraseñas de `20-proyecto-python`.
- `manage.py test` cubre modelos y vistas de `mainapp`, `pages` y `blog`.

## Integración continua

El workflow `.github/workflows/python-package.yml` ejecuta en cada push y pull request a `main`:
lint con **flake8**, los tests con **pytest** y los tests de **Django**, en Python 3.12 y 3.13.

## Autor

Mario Ávila Hueso
