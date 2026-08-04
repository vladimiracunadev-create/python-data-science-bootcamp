"""Impide que vuelvan a colarse datos personales reales en el currículo.

Qué resuelve:
    El README de la clase 030 usaba una dirección de correo personal real como
    dato de ejemplo en un bloque de regex. Ese texto no se queda en el repo: se
    publica en GitHub Pages, se hornea en los PDF y PPTX de la clase, del bundle
    de la parte y del curso completo, y viaja dentro del bundle JS de la app
    Android y del ejecutable de escritorio. Sacarlo de un sitio y olvidarse de
    los otros deja el dato publicado igual.

    Este test bloquea el patrón en la fuente (README + notebook), que es de
    donde salen todos los derivados.

Nota sobre los ejemplos que SÍ usan proveedores reales:
    ``bob@gmail.com`` y ``dan@yahoo.com`` se conservan a propósito. Son nombres
    de fantasía y la clase 030 necesita justamente un abanico de dominios
    distintos (example.com, gmail.com, empresa.es, yahoo.com) para que el
    ejercicio de extraer el dominio tenga sentido. No son datos de nadie.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
CLASSES = ROOT / "classes"

#: Identificadores personales del autor. Si aparecen en el material de clase es
#: un dato real filtrado, no un ejemplo. Las URLs del repo
#: (``vladimiracunadev-create``) son legítimas y no matchean estos patrones.
PERSONAL_PATTERNS = [
    re.compile(r"vladimir[._-]?acu[nñ]a\s*@", re.IGNORECASE),
    re.compile(r"@vladimiracuna\.", re.IGNORECASE),
]

#: Dominios reservados por RFC 2606 / RFC 6761 para documentación y ejemplos.
SAFE_EXAMPLE_DOMAINS = ("example.com", "example.org", "example.net")


def _class_sources() -> list[Path]:
    return sorted(CLASSES.rglob("README.md")) + sorted(CLASSES.rglob("notebook.ipynb"))


def test_hay_material_de_clase_que_revisar():
    """Guardarraíl: si el glob se rompe, el test de abajo pasaría en vacío."""
    assert len(_class_sources()) > 400


@pytest.mark.parametrize("pattern", PERSONAL_PATTERNS, ids=lambda p: p.pattern)
def test_sin_datos_personales_en_el_curriculo(pattern: re.Pattern[str]):
    """Ningún README ni notebook debe traer una dirección personal real."""
    offenders: list[str] = []
    for path in _class_sources():
        text = path.read_text(encoding="utf-8", errors="replace")
        for i, line in enumerate(text.split("\n"), 1):
            if pattern.search(line):
                offenders.append(f"{path.relative_to(ROOT)}:{i}: {line.strip()[:120]}")

    assert not offenders, (
        "Dato personal real en el material de clase — usá un dominio reservado "
        f"({', '.join(SAFE_EXAMPLE_DOMAINS)}):\n  " + "\n  ".join(offenders)
    )


def test_la_clase_030_usa_un_dominio_de_ejemplo():
    """Regresión concreta: el mini-ejemplo de regex de la clase 030."""
    readme = (
        CLASSES
        / "parte-0-prerrequisitos"
        / "030-pandas-operaciones-vectorizadas-sobre-strings"
        / "README.md"
    )
    text = readme.read_text(encoding="utf-8")
    assert "ana.garcia@example.com" in text
    # El ejemplo tiene que seguir enseñando lo suyo: un usuario CON punto, para
    # que se vea que `[\w.]+` lo captura.
    assert 'print(m.group("usuario"))  # ana.garcia' in text
