"""Pruebas de humo de la capa HTTP del laboratorio.

Verifican el árbol del currículo, el detalle de clase, la carga de notebooks
reales y el lifecycle de kernels. La ejecución sobre kernels reales vive en
``test_kernel_manager.py`` para mantener este archivo rápido.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.app import app


def _client():
    """Crea un cliente Flask de pruebas aislado."""
    app.config["TESTING"] = True
    return app.test_client()


# ---------------------------------------------------------------------------
# Vistas básicas
# ---------------------------------------------------------------------------

def test_index_loads():
    response = _client().get("/")
    assert response.status_code == 200
    assert "Python Data Science Program" in response.get_data(as_text=True)


def test_health_endpoint():
    response = _client().get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_ready_endpoint():
    response = _client().get("/ready")
    data = response.get_json()
    assert response.status_code == 200
    assert data["status"] == "ready"
    # 9 partes y 232 clases es el estado del currículo v3.5.0 — si la cifra cambia,
    # actualizar ambos lados (memoria del proyecto + este test) y no aflojar el assert.
    assert data["parts"] == 9
    assert data["classes"] == 232


def test_security_headers_present():
    response = _client().get("/")
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["X-Frame-Options"] == "SAMEORIGIN"
    assert response.headers["Referrer-Policy"] == "no-referrer"
    # CSP con default-src 'self' bloquea CDNs no declarados — todo asset es local.
    assert "default-src 'self'" in response.headers["Content-Security-Policy"]


# ---------------------------------------------------------------------------
# Currículo (loader)
# ---------------------------------------------------------------------------

def test_api_curriculum_tree():
    response = _client().get("/api/curriculum")
    data = response.get_json()
    assert response.status_code == 200
    assert len(data) == 9  # 9 partes
    # Cada parte tiene su lista de clases ordenadas por número.
    total = sum(len(p["classes"]) for p in data)
    assert total == 232


def test_api_classes_compat_list():
    response = _client().get("/api/classes")
    data = response.get_json()
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0
    assert "slug" in data[0]


def test_api_notebook_real_class():
    # Clase real del Parte 7 (recién desarrollada).
    slug = "parte-7-etica-fairness-privacidad/223-tipos-de-sesgo-algoritmico-y-origenes"
    response = _client().get(f"/api/notebook/{slug}")
    assert response.status_code == 200
    data = response.get_json()
    # El loader devuelve celdas reales del .ipynb del currículo, no plantillas.
    # Sin esto el alumno nunca ejecutaría el contenido docente que justifica el curso.
    assert "cells" in data
    assert len(data["cells"]) > 5
    assert all("type" in c for c in data["cells"])


def test_api_notebook_invalid_slug():
    # Path traversal: el slug "../" debe rechazarse antes de tocar el disco.
    response = _client().get("/api/notebook/../../etc/passwd")
    assert response.status_code in (400, 404)


def test_api_notebook_not_found():
    response = _client().get("/api/notebook/parte-0-prerrequisitos/999-no-existe")
    assert response.status_code == 404


def test_api_class_detail_real_class():
    slug = "parte-0-prerrequisitos/006-python-tipos-estructuras-control-de-flujo"
    response = _client().get(f"/api/class/{slug}")
    assert response.status_code == 200
    data = response.get_json()
    assert "html" in data
    assert "README.md" in data["html"]


def test_api_class_detail_invalid_slug():
    response = _client().get("/api/class/../etc/passwd")
    assert response.status_code in (400, 404)


def test_download_class_asset_rejects_invalid_kind():
    # El endpoint solo debe servir "pdf" y "pptx" para evitar enumerar archivos.
    response = _client().get(
        "/downloads/class/parte-0-prerrequisitos/006-python-tipos-estructuras-control-de-flujo/docx"
    )
    assert response.status_code == 400


# ---------------------------------------------------------------------------
# Kernel lifecycle (rutas HTTP — la ejecución viva está cubierta en
# test_kernel_manager.py; aquí solo validamos validación y enrutado).
# ---------------------------------------------------------------------------

def test_kernel_start_returns_id():
    response = _client().post("/api/kernel/start")
    assert response.status_code == 200
    kid = response.get_json()["kernel_id"]
    assert len(kid) == 32  # uuid4().hex
    # Cleanup para no dejar procesos vivos entre tests.
    _client().delete(f"/api/kernel/{kid}")


def test_kernel_execute_with_invalid_id_404():
    bogus = "0" * 32  # válido en formato pero no existe en el gestor.
    response = _client().post(
        f"/api/kernel/{bogus}/execute",
        json={"code": "1+1"},
    )
    assert response.status_code == 404


def test_kernel_execute_rejects_bad_id_format():
    response = _client().post("/api/kernel/not-a-uuid/execute", json={"code": "1+1"})
    assert response.status_code == 400


def test_kernel_interrupt_returns_204_on_unknown():
    bogus = "1" * 32
    response = _client().post(f"/api/kernel/{bogus}/interrupt")
    assert response.status_code == 404


@pytest.mark.skipif(
    True, reason="end-to-end con kernel real corre en test_kernel_manager.py para no duplicar costos"
)
def test_kernel_end_to_end_via_http():
    pass
