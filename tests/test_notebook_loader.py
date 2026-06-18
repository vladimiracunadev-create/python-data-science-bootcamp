"""Pruebas del loader de notebooks reales del currículo.

Validan que el árbol Parte → Clase exponga los 232 contenidos del programa
en el orden correcto y que cada notebook se entregue con celdas estables,
markdown renderizado a HTML y blindajes ante slugs inválidos.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.notebook_loader import list_curriculum, load_notebook


def test_list_curriculum_returns_9_parts():
    curriculum = list_curriculum()
    assert len(curriculum) == 9
    assert [p["part_number"] for p in curriculum] == list(range(9))


def test_list_curriculum_includes_232_classes():
    curriculum = list_curriculum()
    total = sum(len(p["classes"]) for p in curriculum)
    assert total == 232


def test_list_curriculum_classes_sorted_numerically():
    curriculum = list_curriculum()
    parte_1 = next(p for p in curriculum if p["part_number"] == 1)
    numbers = [c["number"] for c in parte_1["classes"]]
    assert numbers == sorted(numbers)
    # Sanidad: orden numérico, no lexicográfico. Si fuera lexicográfico,
    # "100" iría antes que "50" — verificamos lo contrario.
    if 50 in numbers and 100 in numbers:
        assert numbers.index(50) < numbers.index(100)


def test_load_notebook_basic_structure():
    nb = load_notebook("parte-0-prerrequisitos/006-python-tipos-estructuras-control-de-flujo")
    assert isinstance(nb, dict)
    assert "cells" in nb and isinstance(nb["cells"], list)
    assert "slug" in nb
    assert "title" in nb
    assert nb["metadata"]["n_cells"] == len(nb["cells"])


def test_load_notebook_cells_have_id_and_type():
    nb = load_notebook("parte-0-prerrequisitos/006-python-tipos-estructuras-control-de-flujo")
    assert nb["cells"], "el notebook debe tener al menos una celda"
    for cell in nb["cells"]:
        assert "id" in cell and cell["id"].startswith("cell-")
        assert cell["type"] in {"markdown", "code"}
        assert isinstance(cell["source"], str)


def test_load_notebook_markdown_rendered_to_html():
    nb = load_notebook("parte-0-prerrequisitos/006-python-tipos-estructuras-control-de-flujo")
    md_cells = [c for c in nb["cells"] if c["type"] == "markdown"]
    assert md_cells, "se espera al menos una celda markdown"
    assert any("<" in c.get("rendered_html", "") and ">" in c.get("rendered_html", "") for c in md_cells)


def test_load_notebook_code_has_source_string():
    nb = load_notebook("parte-0-prerrequisitos/006-python-tipos-estructuras-control-de-flujo")
    code_cells = [c for c in nb["cells"] if c["type"] == "code"]
    assert code_cells, "se espera al menos una celda de código"
    for cell in code_cells:
        assert isinstance(cell["source"], str)


def test_load_notebook_invalid_slug_raises_value_error():
    with pytest.raises((ValueError, PermissionError)):
        load_notebook("../etc/passwd")


def test_load_notebook_missing_class_raises_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_notebook("parte-0-prerrequisitos/999-no-existe")


def test_load_notebook_for_a_recent_class_223():
    nb = load_notebook("parte-7-etica-fairness-privacidad/223-tipos-de-sesgo-algoritmico-y-origenes")
    assert len(nb["cells"]) > 5
