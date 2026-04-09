"""Pruebas de humo para la capa HTTP de la app Flask.

Este archivo verifica que la interfaz principal y las APIs básicas del sistema
respondan con la estructura esperada para clases, quizzes y ejecución remota.
"""

from __future__ import annotations

import sys
from pathlib import Path

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
    assert "Bootcamp Python" in response.get_data(as_text=True)


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
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["X-Frame-Options"] == "SAMEORIGIN"
    assert response.headers["Referrer-Policy"] == "no-referrer"
    assert "default-src 'self'" in response.headers["Content-Security-Policy"]


def test_api_class_detail_valid():
    client = _client()
    response = client.get("/api/class/01-python-fundamentos")
    assert response.status_code == 200
    data = response.get_json()
    assert "html" in data
    assert "README.md" in data["html"]
    assert "teoria.md" in data["html"]
    assert data["quiz"] is None
    assert data["assets"]["pdf"]["path"] == "classes/01-python-fundamentos/guia-explicativa.pdf"
    assert data["assets"]["pptx"]["path"] == "classes/01-python-fundamentos/presentacion.pptx"


def test_api_class_detail_includes_quiz_for_class_zero():
    client = _client()
    response = client.get("/api/class/00-diagnostico-inicial")
    assert response.status_code == 200
    data = response.get_json()
    assert data["quiz"] is not None
    assert data["quiz"]["id"] == "class-0-diagnostic"
    assert len(data["quiz"]["questions"]) == 30
    assert data["assets"]["pdf"]["url"].endswith("/downloads/class/00-diagnostico-inicial/pdf")


def test_download_class_pdf():
    client = _client()
    response = client.get("/downloads/class/01-python-fundamentos/pdf")
    assert response.status_code == 200
    assert response.mimetype == "application/pdf"


def test_download_class_pptx():
    client = _client()
    response = client.get("/downloads/class/01-python-fundamentos/pptx")
    assert response.status_code == 200
    assert (
        response.mimetype
        == "application/vnd.openxmlformats-officedocument.presentationml.presentation"
    )


def test_download_class_asset_rejects_invalid_kind():
    client = _client()
    response = client.get("/downloads/class/01-python-fundamentos/docx")
    assert response.status_code == 400


def test_api_class_detail_invalid_slug():
    client = _client()
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
        json={"notebook_id": "api-test-print", "code": 'print("hola bootcamp")'},
    )
    data = response.get_json()
    assert "hola bootcamp" in data["stdout"]


def test_execute_api_handles_syntax_error():
    client = _client()
    response = client.post("/api/execute", json={"notebook_id": "api-err", "code": "def broken(:"})
    data = response.get_json()
    assert response.status_code == 200
    assert data["error"] is not None


def test_execute_api_rejects_oversized_code():
    client = _client()
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
