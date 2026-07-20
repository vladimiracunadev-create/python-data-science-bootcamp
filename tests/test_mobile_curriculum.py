"""Tests del currículo embebido en la app móvil (React Native).

``mobile/src/data/classes.js`` se genera desde ``classes/**/README.md`` con
``scripts/generate_mobile_curriculum.py``. La app lo embebe en el bundle, así
que si el archivo queda vacío o desincronizado el APK se instala sin contenido
— que es exactamente el fallo que traía la v3.8.0.

Estos tests cubren tres cosas:
  1. que el archivo generado tenga las 232 clases en las 9 partes,
  2. que ningún campo que la UI renderiza venga vacío,
  3. que el archivo no haya derivado respecto del markdown fuente.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "mobile" / "src" / "data" / "classes.js"
GENERATOR = ROOT / "scripts" / "generate_mobile_curriculum.py"

# Reparto real de clases por parte, verificado contra classes/.
EXPECTED_PER_PART = {
    "parte-0-prerrequisitos": 49,
    "parte-1-machine-learning-clasico": 50,
    "parte-2-deep-learning": 75,
    "parte-3-estadistica-inferencial": 19,
    "parte-4-mlops": 14,
    "parte-5-ingenieria-de-datos": 8,
    "parte-6-sistemas-de-recomendacion": 7,
    "parte-7-etica-fairness-privacidad": 6,
    "parte-8-capstones": 4,
}

TOTAL_CLASSES = 232


def _extract_array(source: str, name: str) -> list:
    """Extrae ``export const <name> = [...]`` del módulo generado.

    El generador emite JSON puro con ``json.dumps``, así que basta con recortar
    el array balanceando corchetes y pasarlo por ``json.loads``.
    """
    marker = f"export const {name} = "
    start = source.index(marker) + len(marker)
    assert source[start] == "[", f"{name} no es un array"

    depth = 0
    in_string = False
    escaped = False
    for i in range(start, len(source)):
        char = source[i]
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue
        if char == '"':
            in_string = True
        elif char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
            if depth == 0:
                return json.loads(source[start : i + 1])
    raise AssertionError(f"array {name} sin cerrar")


@pytest.fixture(scope="module")
def source() -> str:
    assert DATA_FILE.exists(), f"falta el archivo generado: {DATA_FILE}"
    return DATA_FILE.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def classes(source: str) -> list:
    return _extract_array(source, "CLASSES")


@pytest.fixture(scope="module")
def parts(source: str) -> list:
    return _extract_array(source, "PARTS")


def test_classes_no_esta_vacio(classes):
    """El stub vacío (``CLASSES = []``) es justo el bug que se reparó."""
    assert classes, "classes.js no expone ninguna clase — la app se instalaría sin contenido"


def test_total_de_clases_y_partes(classes, parts):
    assert len(classes) == TOTAL_CLASSES
    assert len(parts) == len(EXPECTED_PER_PART)


def test_reparto_por_parte(classes, parts):
    """Cada parte debe traer exactamente las clases que hay en classes/."""
    contados: dict[str, int] = {}
    for item in classes:
        contados[item["partSlug"]] = contados.get(item["partSlug"], 0) + 1
    assert contados == EXPECTED_PER_PART

    declarados = {part["id"]: part["classCount"] for part in parts}
    assert declarados == EXPECTED_PER_PART


def test_numeracion_contigua(classes):
    """Las clases van de la 1 a la 232 sin huecos ni repetidos."""
    numeros = sorted(item["number"] for item in classes)
    assert numeros == list(range(1, TOTAL_CLASSES + 1))


def test_ids_unicos(classes):
    ids = [item["id"] for item in classes]
    assert len(set(ids)) == len(ids)


@pytest.mark.parametrize(
    "campo",
    ["title", "description", "theory", "level", "duration", "colabUrl"],
)
def test_campos_de_texto_presentes(classes, campo):
    """Ningún campo que la UI pinta puede venir vacío."""
    vacios = [item["id"] for item in classes if not item.get(campo)]
    assert not vacios, f"{len(vacios)} clases sin '{campo}' (ej. {vacios[:3]})"


@pytest.mark.parametrize("campo", ["outcomes", "topics", "materials", "exercises"])
def test_listas_presentes(classes, campo):
    """ClassScreen recorre estas listas; una vacía deja una tarjeta en blanco."""
    vacias = [item["id"] for item in classes if not item.get(campo)]
    assert not vacias, f"{len(vacias)} clases sin '{campo}' (ej. {vacias[:3]})"


def test_colab_apunta_a_la_rama_real(classes):
    """La rama del remoto es ``main``; con ``master`` Colab devolvía 404."""
    malas = [item["id"] for item in classes if "/blob/main/" not in item["colabUrl"]]
    assert not malas, f"{len(malas)} enlaces de Colab no apuntan a main"


def test_colab_apunta_a_un_notebook_existente(classes):
    """El notebook referenciado debe existir en el repo, si no el link rompe."""
    faltantes = []
    for item in classes:
        ruta = item["colabUrl"].split("/blob/main/", 1)[1]
        if not (ROOT / ruta).exists():
            faltantes.append(item["id"])
    assert not faltantes, f"{len(faltantes)} notebooks inexistentes (ej. {faltantes[:3]})"


def test_niveles_reconocidos_por_el_theme(classes):
    """``levelColor`` solo mapea estos niveles; otro valor pintaría gris."""
    validos = {"Diagnostico", "Basico", "Intermedio", "Intermedio-Avanzado", "Avanzado", "Integrador"}
    desconocidos = {item["level"] for item in classes} - validos
    assert not desconocidos, f"niveles no soportados por el theme: {desconocidos}"


def test_sin_markdown_residual(classes):
    """La UI usa <Text> plano: ``**`` o ``[x](y)`` se verían como ruido."""
    sucias = [
        item["id"]
        for item in classes
        if "**" in item["theory"] or re.search(r"\[[^\]]+\]\([^)]+\)", item["theory"])
    ]
    assert not sucias, f"{len(sucias)} clases con markdown sin limpiar (ej. {sucias[:3]})"


def test_generado_esta_sincronizado_con_el_markdown(source):
    """Regenerar no debe producir diferencias: si las hay, el archivo derivó."""
    resultado = subprocess.run(
        [sys.executable, str(GENERATOR)],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    assert resultado.returncode == 0, f"el generador falló: {resultado.stderr}"
    assert DATA_FILE.read_text(encoding="utf-8") == source, (
        "mobile/src/data/classes.js está desincronizado de classes/**/README.md — "
        "corre: python scripts/generate_mobile_curriculum.py"
    )
