"""Pruebas de humo para la capa HTTP de la app Flask.

Este archivo verifica que la interfaz principal y las APIs básicas del sistema
respondan con la estructura esperada para clases, quizzes y ejecución remota.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.app import app


def _client():
    """Crea un cliente Flask de pruebas aislado para los endpoints."""
    app.config["TESTING"] = True
    return app.test_client()


def test_index_loads():
    client = _client()
    response = client.get("/")
    assert response.status_code == 200
    assert "Python Data Science Program" in response.get_data(as_text=True)


def test_api_classes_returns_list():
    client = _client()
    response = client.get("/api/classes")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "slug" in data[0]
    assert "title" in data[0]


def test_health_endpoint():
    client = _client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_ready_endpoint():
    client = _client()
    response = client.get("/ready")
    data = response.get_json()
    assert response.status_code == 200
    assert data["status"] == "ready"
    assert data["classes"] > 0
    assert data["notebooks"] > 0


def test_security_headers_present():
    client = _client()
    response = client.get("/")
    # La app ejecuta código arbitrario del alumno en el navegador vía iframe/eval.
    # Sin estos tres headers un atacante puede inyectar scripts (XSS), montar
    # clickjacking o filtrar información por referer a dominios externos.
    # nosniff evita que el browser reinterprete el MIME de la respuesta.
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    # SAMEORIGIN impide que la app sea embebida en páginas de terceros (clickjacking).
    assert response.headers["X-Frame-Options"] == "SAMEORIGIN"
    assert response.headers["Referrer-Policy"] == "no-referrer"
    # CSP con default-src 'self' bloquea scripts externos no declarados explícitamente.
    assert "default-src 'self'" in response.headers["Content-Security-Policy"]


def test_api_class_detail_valid():
    client = _client()
    # Currículo v2: las clases viven en parte-N/NNN-tema/, el slug usa "/".
    # Se usa la primera clase de la Parte 0 como ejemplo estable.
    slug = "parte-0-prerrequisitos/006-python-tipos-estructuras-control-de-flujo"
    response = client.get(f"/api/class/{slug}")
    assert response.status_code == 200
    data = response.get_json()
    # El payload tiene cuatro secciones clave que el frontend consume por separado:
    #   "html"   → diccionario con el HTML renderizado de cada .md de la clase
    #   "quiz"   → objeto con preguntas, o None si la clase no tiene quiz
    #   "assets" → rutas y URLs de descarga para PDF y PPTX
    # Si cualquiera de estas claves desaparece el frontend rompe en silencio.
    assert "html" in data
    # README.md es el único markdown obligatorio en el stub v2; teoria/slides/etc. se agregan
    # conforme se desarrolla cada clase.
    assert "README.md" in data["html"]
    # Los stubs v2 aún no traen quiz; cuando se desarrolle el contenido, este assert deberá moverse.
    assert data["quiz"] is None


@pytest.mark.skip(reason="Currículo v2 aún no incluye quiz para la clase de diagnóstico; reactivar cuando se agregue quiz.json a la clase correspondiente.")
def test_api_class_detail_includes_quiz_for_class_zero():
    pass


@pytest.mark.skip(reason="Currículo v2 no trae PDFs generados todavía; reactivar tras correr generar_pdfs.py sobre las clases nuevas.")
def test_download_class_pdf():
    pass


@pytest.mark.skip(reason="Currículo v2 no trae PPTX generados todavía; reactivar tras correr generate_class_assets.py sobre las clases nuevas.")
def test_download_class_pptx():
    pass


def test_download_class_asset_rejects_invalid_kind():
    client = _client()
    # El endpoint solo debe servir "pdf" y "pptx". Aceptar tipos arbitrarios como
    # "docx" o "zip" abriría la puerta a enumerar archivos del servidor o forzar
    # la descarga de archivos internos no destinados a los alumnos.
    response = client.get("/downloads/class/parte-0-prerrequisitos/006-python-tipos-estructuras-control-de-flujo/docx")
    assert response.status_code == 400


def test_api_class_detail_invalid_slug():
    client = _client()
    # Path traversal clásico: un atacante intenta salir del directorio de clases
    # usando "../" para leer archivos arbitrarios del sistema (p.ej. /etc/passwd).
    # El servidor debe rechazar cualquier slug que no sea un nombre de carpeta plano.
    response = client.get("/api/class/../etc/passwd")
    assert response.status_code in (400, 404)


def test_api_class_detail_not_found():
    client = _client()
    response = client.get("/api/class/clase-que-no-existe")
    assert response.status_code == 404


def test_execute_api_runs_code():
    client = _client()
    response = client.post("/api/execute", json={"notebook_id": "api-test", "code": "2 + 3"})
    data = response.get_json()
    assert response.status_code == 200
    assert data["result"] == "5"


def test_execute_api_captures_print():
    client = _client()
    response = client.post(
        "/api/execute",
        json={"notebook_id": "api-test-print", "code": 'print("hola programa")'},
    )
    data = response.get_json()
    assert "hola programa" in data["stdout"]


def test_execute_api_handles_syntax_error():
    client = _client()
    # El alumno enviará código incompleto o incorrecto con frecuencia durante el laboratorio.
    # El engine debe capturar SyntaxError internamente y devolver 200 con "error" poblado,
    # no propagar una excepción que haga caer el proceso Flask o retornar un 500 al cliente.
    response = client.post("/api/execute", json={"notebook_id": "api-err", "code": "def broken(:"})
    data = response.get_json()
    assert response.status_code == 200
    assert data["error"] is not None


def test_execute_api_rejects_oversized_code():
    client = _client()
    # 5 000 líneas de "x = 1\n" generan ~30 KB; el límite del engine es 20 KB.
    # Sin este rechazo, un alumno podría enviar un script enorme con un loop infinito
    # y saturar la CPU o la memoria del servidor compartido durante toda la sesión.
    response = client.post("/api/execute", json={"notebook_id": "api-big", "code": "x = 1\n" * 5000})
    assert response.status_code in (200, 400)
    data = response.get_json()
    assert data.get("error") is not None


def test_api_notebooks_returns_list():
    client = _client()
    response = client.get("/api/notebooks")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)


def test_api_reset_session():
    client = _client()
    client.post("/api/execute", json={"notebook_id": "reset-test", "code": "x = 99"})
    response = client.post("/api/reset", json={"notebook_id": "reset-test"})
    assert response.status_code == 200
    assert response.get_json()["ok"] is True
