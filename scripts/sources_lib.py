"""Extracción y normalización del aparato de fuentes de las 232 clases.

Qué resuelve:
    El programa cita 232 bloques de fuentes distintos y hasta ahora no existía
    ningún sitio donde se pudiera comprobar qué obra hay detrás de cada cita.
    Este módulo es la capa común —sin red, determinista— que usan los dos
    verificadores:

      scripts/verify-sources    offline, bloquea en CI
      scripts/refresh-sources   con red, manual, no bloquea

    Define una sola cosa: qué cuenta como "fuente usada". La unidad es la
    **cita**, y se extrae exclusivamente del bloque `## 🔗 Referencias` de cada
    `classes/<parte>/<clase>/README.md`:

      - cada URL del bloque es una cita de tipo `link`
      - cada viñeta SIN URL es una cita de tipo `work` (libro, paper, charla)

    Una viñeta con URL no genera además una cita `work`: el texto que rodea al
    enlace describe la misma obra que el enlace localiza, y contarlo dos veces
    inflaría la cobertura sin añadir trazabilidad.

Uso:
    from sources_lib import iter_citations, load_registry, isbn13_is_valid

Salida: este módulo no imprime nada ni toca la red.
"""

from __future__ import annotations

import json
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLASSES_DIR = ROOT / "classes"
SOURCES_DIR = ROOT / "sources"
REGISTRY_PATH = SOURCES_DIR / "bibliography.json"
LIBRARY_VERSIONS_PATH = SOURCES_DIR / "library_versions.json"
README_PATH = ROOT / "README.md"

#: Encabezado exacto del bloque de fuentes. Las 232 clases usan este mismo.
REFERENCES_HEADING = "## 🔗 Referencias"

#: Marcadores de la generación del README que produce el verificador. Todo lo
#: que quede entre ambos se reescribe entero: nadie edita cifras a mano.
README_BEGIN = "<!-- BEGIN:fuentes -->"
README_END = "<!-- END:fuentes -->"

SCHEMA_VERSION = 1

ENTRY_TYPES = ("book", "paper", "standard", "reference", "dataset")
ENTRY_STATUS = ("verificada", "pendiente")

#: Rutas de documentación que se mueven bajo los pies del lector: el mismo
#: enlace apunta a una API distinta cada vez que la librería publica. Un enlace
#: así no es una fuente comprobable.
FLOATING_MARKERS = ("/stable/", "/latest/", "/en/latest/", "/en/stable/")

_URL_RE = re.compile(r"https?://[^\s)>\]\"'`]+")
_MD_LINK_RE = re.compile(r"\[([^\]]*)\]\((<?)(https?://[^)\s]+)>?(?:\s+\"[^\"]*\")?\)")
_BULLET_RE = re.compile(r"^\s*-\s+(.*\S)\s*$")
_DOI_RE = re.compile(r"^10\.\d{4,9}/[-._;()/:a-zA-Z0-9]+$")
_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
_ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

#: Puntuación final que arrastran las citas y que no forma parte de la URL.
_TRAILING = ".,;:>)]}»”'\"`"


# ─────────────────────────────────────────────────────────────────────────────
# Normalización
# ─────────────────────────────────────────────────────────────────────────────


def strip_markdown(text: str) -> str:
    """Devuelve el texto de una viñeta sin marcas de énfasis ni sintaxis de enlace."""
    text = _MD_LINK_RE.sub(r"\1", text)
    text = _URL_RE.sub(" ", text)
    text = re.sub(r"[*_`~]", "", text)
    text = text.replace("<", " ").replace(">", " ")
    return re.sub(r"\s+", " ", text).strip()


def fold(text: str) -> str:
    """Normaliza para comparar: sin acentos, en minúsculas, sin puntuación suelta.

    Qué resuelve:
        Las mismas obras aparecen como "Géron", "Geron" o "GÉRON, A." según la
        clase. El emparejamiento con el registro tiene que ser estable frente a
        esa variación sin recurrir a coincidencias difusas.
    """
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def clean_url(url: str) -> str:
    """Recorta la puntuación de cierre que la prosa pega al final de una URL."""
    return url.rstrip(_TRAILING)


def slugify(text: str, max_words: int = 9) -> str:
    """Construye un identificador kebab-case estable a partir de un texto."""
    words = fold(text).split()
    return "-".join(words[:max_words]) or "sin-titulo"


def isbn13_is_valid(isbn: str) -> bool:
    """Valida un ISBN-13 con su dígito de control (norma ISO 2108)."""
    if not isinstance(isbn, str) or not re.fullmatch(r"\d{13}", isbn):
        return False
    total = sum(int(d) * (1 if i % 2 == 0 else 3) for i, d in enumerate(isbn[:12]))
    return (10 - total % 10) % 10 == int(isbn[12])


def doi_is_wellformed(doi: str) -> bool:
    """Comprueba la forma de un DOI (prefijo 10.x + sufijo)."""
    return isinstance(doi, str) and bool(_DOI_RE.match(doi))


def is_iso_date(value: str) -> bool:
    return isinstance(value, str) and bool(_ISO_DATE_RE.match(value))


def is_kebab_id(value: str) -> bool:
    return isinstance(value, str) and bool(_ID_RE.match(value))


# ─────────────────────────────────────────────────────────────────────────────
# Extracción de citas
# ─────────────────────────────────────────────────────────────────────────────


@dataclass
class Citation:
    """Una cita concreta: un enlace o una obra citada en una clase concreta."""

    class_path: str
    line: int
    bullet: str
    kind: str  # "link" | "work"
    url: str | None = None
    text: str = ""
    gloss: str = ""

    @property
    def key(self) -> str:
        """Clave de emparejamiento contra el registro."""
        return self.url if self.kind == "link" else fold(self.text)


@dataclass
class ClassReferences:
    """El bloque de fuentes de una clase, tal cual está en el README."""

    path: str
    heading_line: int
    block: str
    citations: list[Citation] = field(default_factory=list)


def iter_class_files() -> list[Path]:
    """Devuelve los README de clase en orden estable."""
    return sorted(CLASSES_DIR.glob("*/*/README.md"))


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def _split_gloss(plain: str) -> str:
    """Extrae la cláusula de uso de una viñeta (lo que sigue a un guion largo)."""
    parts = re.split(r"\s+[—–]\s+", plain, maxsplit=1)
    return parts[1].strip() if len(parts) == 2 else ""


def extract_block(text: str) -> tuple[int, str] | None:
    """Devuelve (línea del encabezado, contenido) del bloque de fuentes."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip() == REFERENCES_HEADING:
            body: list[str] = []
            for nxt in lines[i + 1 :]:
                if nxt.startswith("## "):
                    break
                body.append(nxt)
            return i + 1, "\n".join(body).strip("\n")
    return None


def parse_class(path: Path) -> ClassReferences | None:
    """Extrae y desglosa el bloque de fuentes de un README de clase."""
    text = path.read_text(encoding="utf-8")
    found = extract_block(text)
    if found is None:
        return None
    heading_line, block = found
    refs = ClassReferences(path=rel(path), heading_line=heading_line, block=block.strip())
    offset = heading_line
    for n, raw in enumerate(block.splitlines(), start=1):
        match = _BULLET_RE.match(raw)
        if not match:
            continue
        bullet = match.group(1)
        line_no = offset + n
        plain = strip_markdown(bullet)
        gloss = _split_gloss(plain)
        urls = [clean_url(u) for u in _URL_RE.findall(bullet)]
        if urls:
            for url in urls:
                refs.citations.append(
                    Citation(
                        class_path=refs.path,
                        line=line_no,
                        bullet=bullet,
                        kind="link",
                        url=url,
                        text=plain,
                        gloss=gloss,
                    )
                )
        else:
            refs.citations.append(
                Citation(
                    class_path=refs.path,
                    line=line_no,
                    bullet=bullet,
                    kind="work",
                    text=plain,
                    gloss=gloss,
                )
            )
    return refs


def iter_class_references() -> list[ClassReferences]:
    out = []
    for path in iter_class_files():
        parsed = parse_class(path)
        if parsed is not None:
            out.append(parsed)
    return out


def iter_citations() -> list[Citation]:
    return [c for refs in iter_class_references() for c in refs.citations]


# ─────────────────────────────────────────────────────────────────────────────
# Registro
# ─────────────────────────────────────────────────────────────────────────────


def load_registry(path: Path = REGISTRY_PATH) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_registry(registry: dict, path: Path = REGISTRY_PATH) -> None:
    """Escribe el registro con orden estable para que los diff sean legibles."""
    registry["entries"] = sorted(registry["entries"], key=lambda e: (e["type"], e["id"]))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(registry, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
    )


def load_library_versions(path: Path = LIBRARY_VERSIONS_PATH) -> dict:
    if not path.exists():
        return {"schema_version": SCHEMA_VERSION, "libraries": []}
    return json.loads(path.read_text(encoding="utf-8"))


def expected_locator(entry: dict) -> str | None:
    """Forma canónica del localizador según el tipo de entrada."""
    kind = entry.get("type")
    if kind == "book" and entry.get("isbn13"):
        return f"https://openlibrary.org/isbn/{entry['isbn13']}"
    if kind == "paper" and entry.get("doi"):
        return f"https://doi.org/{entry['doi']}"
    return None


def build_index(registry: dict) -> tuple[dict[str, dict], list[tuple[re.Pattern, dict]]]:
    """Indexa el registro para emparejar citas.

    Devuelve:
        (por_url, patrones_de_obra) — el primero empareja citas `link` por URL
        exacta; el segundo, citas `work` por expresión regular sobre el texto
        normalizado de la viñeta.
    """
    by_url: dict[str, dict] = {}
    patterns: list[tuple[re.Pattern, dict]] = []
    for entry in registry.get("entries", []):
        for url in entry.get("class_urls", []):
            by_url[url] = entry
        for alias in entry.get("aliases", []):
            patterns.append((re.compile(alias), entry))
    return by_url, patterns


def match_citation(
    citation: Citation,
    by_url: dict[str, dict],
    patterns: list[tuple[re.Pattern, dict]],
) -> list[dict]:
    """Devuelve las entradas del registro que reclaman esta cita."""
    if citation.kind == "link":
        entry = by_url.get(citation.url)
        return [entry] if entry else []
    folded = fold(citation.text)
    return [entry for rx, entry in patterns if rx.search(folded)]


def floating_marker(url: str) -> str | None:
    """Devuelve el marcador flotante que contiene la URL, si contiene alguno."""
    for marker in FLOATING_MARKERS:
        if marker in url:
            return marker
    return None


def host_of(url: str) -> str:
    match = re.match(r"https?://([^/]+)", url)
    return match.group(1).lower() if match else ""
