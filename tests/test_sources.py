"""Tests del aparato de fuentes: extracción de citas y forma de los localizadores.

Qué resuelve:
    `scripts/verify-sources` comprueba el registro contra las clases, pero nadie
    comprueba al verificador. Si la extracción de citas se rompe en silencio —un
    encabezado que deja de reconocerse, una viñeta con dos enlaces que se cuenta
    una vez— el verificador seguiría en verde mientras deja de mirar la mitad del
    material.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import sources_lib as sl  # noqa: E402

# ─────────────────────────────────────────────────────────────────────────────
# Localizadores
# ─────────────────────────────────────────────────────────────────────────────


@pytest.mark.parametrize(
    "isbn",
    ["9781098107963", "9780262039246", "9781492056355"],
)
def test_isbn13_valido(isbn):
    assert sl.isbn13_is_valid(isbn)


@pytest.mark.parametrize(
    "isbn",
    [
        "9781098107964",  # dígito de control cambiado
        "978109810796",  # 12 dígitos
        "97810981079631",  # 14 dígitos
        "978-1-0981-0796-3",  # con guiones
        "",
        None,
    ],
)
def test_isbn13_invalido(isbn):
    assert not sl.isbn13_is_valid(isbn)


@pytest.mark.parametrize(
    "doi,ok",
    [
        ("10.48550/arXiv.1810.03993", True),
        ("10.1145/3287560.3287596", True),
        ("doi:10.1145/3287560", False),
        ("https://doi.org/10.1145/3287560", False),
        ("11.1145/3287560", False),
    ],
)
def test_doi_bien_formado(doi, ok):
    assert sl.doi_is_wellformed(doi) is ok


def test_locator_canonico_por_tipo():
    libro = {"type": "book", "isbn13": "9781098107963"}
    articulo = {"type": "paper", "doi": "10.48550/arXiv.1810.03993"}
    assert sl.expected_locator(libro) == "https://openlibrary.org/isbn/9781098107963"
    assert sl.expected_locator(articulo) == "https://doi.org/10.48550/arXiv.1810.03993"
    assert sl.expected_locator({"type": "reference"}) is None


# ─────────────────────────────────────────────────────────────────────────────
# Extracción de citas
# ─────────────────────────────────────────────────────────────────────────────

CLASE = """# Clase de prueba

Texto con un enlace en prosa a https://ejemplo.org/prosa que no es una cita.

```python
requests.get("https://api.ejemplo.org/no-es-una-fuente")
```

## 🔗 Referencias

- [Docs de algo](https://scikit-learn.org/1.8/modules/tree.html) — base del ejercicio 3.
- Géron, *Hands-On ML*, **cap. 7**.
- Dos enlaces: [a](https://a.example/x) y [b](https://b.example/y)

## 📥 Material descargable

- [PDF](./guia.pdf)
"""


@pytest.fixture()
def clase(tmp_path):
    path = tmp_path / "README.md"
    path.write_text(CLASE, encoding="utf-8")
    return path


def test_bloque_termina_en_el_siguiente_h2(clase):
    _, block = sl.extract_block(clase.read_text(encoding="utf-8"))
    assert "Material descargable" not in block
    assert "guia.pdf" not in block
    assert "Géron" in block


def test_una_cita_por_enlace_y_una_por_obra_sin_enlace(monkeypatch, clase):
    monkeypatch.setattr(sl, "ROOT", clase.parent)
    refs = sl.parse_class(clase)
    kinds = [c.kind for c in refs.citations]
    assert kinds.count("link") == 3  # dos viñetas con enlace, una con dos enlaces
    assert kinds.count("work") == 1  # Géron
    urls = {c.url for c in refs.citations if c.kind == "link"}
    assert "https://ejemplo.org/prosa" not in urls  # prosa: no es del bloque
    assert "https://api.ejemplo.org/no-es-una-fuente" not in urls  # código: tampoco


def test_la_glosa_de_uso_se_extrae(monkeypatch, clase):
    monkeypatch.setattr(sl, "ROOT", clase.parent)
    refs = sl.parse_class(clase)
    glosas = {c.gloss for c in refs.citations if c.gloss}
    assert "base del ejercicio 3." in glosas


def test_fold_normaliza_acentos_y_mayusculas():
    assert sl.fold("GÉRON, A.") == sl.fold("geron a")
    assert sl.fold("*Hands-On ML*") == "hands on ml"


def test_marcador_flotante():
    assert sl.floating_marker("https://scikit-learn.org/stable/modules/tree.html") == "/stable/"
    assert sl.floating_marker("https://scikit-learn.org/1.8/modules/tree.html") is None


# ─────────────────────────────────────────────────────────────────────────────
# El registro real del repo
# ─────────────────────────────────────────────────────────────────────────────


def test_el_registro_parsea_y_declara_su_regla():
    registry = json.loads(sl.REGISTRY_PATH.read_text(encoding="utf-8"))
    assert registry["schema_version"] == sl.SCHEMA_VERSION
    assert registry["policy"]
    assert registry["entries"]


def test_toda_entrada_verificada_tiene_localizador_canonico():
    registry = json.loads(sl.REGISTRY_PATH.read_text(encoding="utf-8"))
    for entry in registry["entries"]:
        if entry["status"] != "verificada":
            continue
        canonical = sl.expected_locator(entry)
        if canonical:
            assert entry["locator"] == canonical, entry["id"]
        assert entry["locator"].startswith("https://"), entry["id"]
        assert sl.is_iso_date(entry["accessed"]), entry["id"]


def test_toda_entrada_pendiente_declara_su_motivo():
    registry = json.loads(sl.REGISTRY_PATH.read_text(encoding="utf-8"))
    sin_motivo = [
        e["id"]
        for e in registry["entries"]
        if e["status"] == "pendiente" and not e.get("pending_reason")
    ]
    assert not sin_motivo


def test_las_232_clases_tienen_bloque_de_fuentes():
    referencias = sl.iter_class_references()
    assert len(referencias) == 232
    assert all(r.block for r in referencias)
