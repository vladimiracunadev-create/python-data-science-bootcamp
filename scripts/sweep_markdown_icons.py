"""Corrige detalles editoriales repetitivos en los Markdown del repositorio.

Responsabilidades:
    1. Reparar mojibake común cuando un archivo fue guardado con una
       decodificación incorrecta (`CatÃ¡logo`, `ðŸ§ `, etc.).
    2. Asegurar que los documentos importantes tengan un icono visible en el H1
       para conservar la identidad visual que usa el repositorio.

Qué resuelve:
    Evita correcciones manuales repetitivas en README, documentación operativa
    y materiales de apoyo cuando se pierde el icono del título o aparecen
    secuencias rotas por encoding.
"""

from __future__ import annotations

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

try:
    from ftfy import fix_text
except ImportError:  # pragma: no cover - fallback defensivo
    fix_text = None

SKIP_PARTS = {
    ".git",
    ".venv",
    "node_modules",
    "dist",
    "build",
    ".pytest_cache",
    ".ruff_cache",
    ".expo",
}

TITLE_ICONS = {
    Path("README.md"): "🧭",
    Path("CHANGELOG.md"): "📝",
    Path("CONTRIBUTING.md"): "🤝",
    Path("ROADMAP.md"): "🗺️",
    Path("RECRUITER.md"): "🎯",
    Path("RUNBOOK.md"): "🛠️",
    Path("SECURITY.md"): "🔐",
    Path("datasets/README.md"): "📦",
    Path("mobile/README.md"): "📱",
    Path("docs/ARQUITECTURA_PRODUCTO.md"): "🏗️",
    Path("docs/BUILD_INSTALLER.md"): "🪟",
    Path("docs/INDEX.md"): "🧭",
    Path("docs/MOBILE_APP.md"): "📱",
    Path("docs/entorno-interactivo.md"): "🧪",
}

SUSPICIOUS_TOKENS = ("Ã", "ðŸ", "â€”", "â€", "Â")
KNOWN_ICONS = {
    "🧭",
    "📝",
    "🤝",
    "🗺️",
    "🎯",
    "🛠️",
    "🔐",
    "📦",
    "📱",
    "🏗️",
    "🪟",
    "🧪",
    "🧠",
    "🖥️",
    "📚",
    "🎤",
    "💡",
    "⚙️",
    "🧩",
    "🧱",
}


def should_skip(path: Path) -> bool:
    """Indica si una ruta está fuera del barrido editorial."""
    return any(part in SKIP_PARTS for part in path.parts)


def suspicious_count(text: str) -> int:
    """Cuenta marcadores típicos de encoding roto para comparar mejoras."""
    return sum(text.count(token) for token in SUSPICIOUS_TOKENS)


def repair_mojibake(text: str) -> str:
    """Intenta reparar un archivo si parece haber sido recodificado mal.

    Qué resuelve:
        Muchos archivos dañados por UTF-8/latin-1 incorrecto se recuperan al
        volver a bytes latin-1 y decodificarlos como UTF-8. Solo se acepta el
        cambio si reduce los marcadores sospechosos.
    """
    if suspicious_count(text) == 0:
        return text

    candidates = [text]

    if fix_text is not None:
        candidates.append(fix_text(text))

    try:
        candidates.append(text.encode("latin-1").decode("utf-8"))
    except UnicodeError:
        pass

    best = min(candidates, key=suspicious_count)
    return best


def title_has_icon(title: str) -> bool:
    """Detecta si el H1 ya parte con uno de los iconos estándar del repo."""
    stripped = title.strip()
    return any(stripped.startswith(f"{icon} ") or stripped == icon for icon in KNOWN_ICONS)


def ensure_h1_icon(relative_path: Path, text: str) -> str:
    """Añade el icono esperado al H1 si el documento principal no lo tiene."""
    icon = TITLE_ICONS.get(relative_path)
    if not icon:
        return text

    lines = text.splitlines()
    in_code = False
    for index, line in enumerate(lines):
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if line.startswith("# "):
            title = line[2:]
            if not title_has_icon(title):
                lines[index] = f"# {icon} {title}"
            break
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def main() -> None:
    """Recorre el repo y aplica correcciones editoriales seguras."""
    updated = 0
    for path in sorted(BASE_DIR.rglob("*.md")):
        if should_skip(path):
            continue

        original = path.read_text(encoding="utf-8")
        fixed = repair_mojibake(original)
        fixed = ensure_h1_icon(path.relative_to(BASE_DIR), fixed)

        if fixed != original:
            path.write_text(fixed, encoding="utf-8")
            updated += 1
            print(f"[OK] {path.relative_to(BASE_DIR)}")

    print(f"Archivos actualizados: {updated}")


if __name__ == "__main__":
    main()
