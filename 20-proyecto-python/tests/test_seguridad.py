from usuarios import seguridad


def test_el_hash_no_contiene_la_password_en_claro():
    guardado = seguridad.hashear_password("secreto123")
    assert "secreto123" not in guardado
    assert guardado.startswith("pbkdf2_sha256$")


def test_verifica_password_correcta_e_incorrecta():
    guardado = seguridad.hashear_password("secreto123")
    assert seguridad.verificar_password("secreto123", guardado) is True
    assert seguridad.verificar_password("otra-cosa", guardado) is False


def test_misma_password_genera_hashes_distintos_por_la_sal():
    assert seguridad.hashear_password("igual") != seguridad.hashear_password("igual")


def test_formato_invalido_devuelve_false_sin_lanzar_error():
    assert seguridad.verificar_password("x", "no-es-un-hash") is False
    assert seguridad.verificar_password("x", None) is False
