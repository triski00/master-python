"""Utilidades para guardar contraseñas de forma segura.

Las contraseñas nunca se guardan en claro: se guarda un hash PBKDF2-SHA256
con una sal aleatoria distinta para cada usuario.

Formato guardado en la base de datos:
    pbkdf2_sha256$<iteraciones>$<sal en hex>$<hash en hex>

Nota didáctica: está implementado con la librería estándar (hashlib) para
entender cómo funciona. En un proyecto real conviene usar una solución
probada (por ejemplo, el sistema de autenticación de Django, bcrypt o argon2).
"""
import hashlib
import hmac
import os

ALGORITMO = "pbkdf2_sha256"
ITERACIONES = 600_000


def hashear_password(password, iteraciones=ITERACIONES):
    """Devuelve el hash con sal de una contraseña, listo para guardar."""
    sal = os.urandom(16)
    derivada = hashlib.pbkdf2_hmac("sha256", password.encode("utf8"), sal, iteraciones)
    return f"{ALGORITMO}${iteraciones}${sal.hex()}${derivada.hex()}"


def verificar_password(password, guardado):
    """Comprueba una contraseña contra el hash guardado."""
    try:
        algoritmo, iteraciones, sal_hex, hash_hex = guardado.split("$")
        if algoritmo != ALGORITMO:
            return False
        derivada = hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf8"), bytes.fromhex(sal_hex), int(iteraciones)
        )
    except (ValueError, AttributeError):
        return False
    return hmac.compare_digest(derivada.hex(), hash_hex)
