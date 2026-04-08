from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {".git", ".venv", "node_modules", ".pytest_cache"}

# Ordered from longer/more specific to shorter/more general.
REPLACEMENTS: list[tuple[str, str]] = [
    ("analisis", "análisis"),
    ("arquitectonica", "arquitectónica"),
    ("basica", "básica"),
    ("basicas", "básicas"),
    ("basico", "básico"),
    ("basicos", "básicos"),
    ("capacitacion", "capacitación"),
    ("categorias", "categorías"),
    ("categoria", "categoría"),
    ("coleccion", "colección"),
    ("colecciones", "colecciones"),
    ("comunicacion", "comunicación"),
    ("comprension", "comprensión"),
    ("configuracion", "configuración"),
    ("conexion", "conexión"),
    ("conexiones", "conexiones"),
    ("construccion", "construcción"),
    ("correccion", "corrección"),
    ("correcciones", "correcciones"),
    ("critica", "crítica"),
    ("critico", "crítico"),
    ("criticos", "críticos"),
    ("cuadricula", "cuadrícula"),
    ("codigo", "código"),
    ("codigos", "códigos"),
    ("diagnostico", "diagnóstico"),
    ("didactica", "didáctica"),
    ("dimension", "dimensión"),
    ("dinamica", "dinámica"),
    ("direccion", "dirección"),
    ("diseno", "diseño"),
    ("documentacion", "documentación"),
    ("ejecucion", "ejecución"),
    ("ensenanza", "enseñanza"),
    ("ensena", "enseña"),
    ("ensenan", "enseñan"),
    ("ensenar", "enseñar"),
    ("ensenarlo", "enseñarlo"),
    ("ensenarlo", "enseñarlo"),
    ("explicacion", "explicación"),
    ("explicaciones", "explicaciones"),
    ("evaluacion", "evaluación"),
    ("evaluaciones", "evaluaciones"),
    ("evolucion", "evolución"),
    ("funcion", "función"),
    ("funciones", "funciones"),
    ("grafico", "gráfico"),
    ("graficos", "gráficos"),
    ("guia", "guía"),
    ("guias", "guías"),
    ("hipotesis", "hipótesis"),
    ("informacion", "información"),
    ("institucion", "institución"),
    ("integracion", "integración"),
    ("introduccion", "introducción"),
    ("iteracion", "iteración"),
    ("linea", "línea"),
    ("lineas", "líneas"),
    ("logica", "lógica"),
    ("mas", "más"),
    ("metodologia", "metodología"),
    ("modulo", "módulo"),
    ("modulos", "módulos"),
    ("movil", "móvil"),
    ("numero", "número"),
    ("numeros", "números"),
    ("operacion", "operación"),
    ("opcion", "opción"),
    ("opciones", "opciones"),
    ("pedagogica", "pedagógica"),
    ("pedagogico", "pedagógico"),
    ("presentacion", "presentación"),
    ("progresion", "progresión"),
    ("practica", "práctica"),
    ("practicas", "prácticas"),
    ("rapida", "rápida"),
    ("rapido", "rápido"),
    ("relacion", "relación"),
    ("resolucion", "resolución"),
    ("retroalimentacion", "retroalimentación"),
    ("reunion", "reunión"),
    ("seccion", "sección"),
    ("secciones", "secciones"),
    ("segun", "según"),
    ("sesion", "sesión"),
    ("sesiones", "sesiones"),
    ("sintesis", "síntesis"),
    ("solucion", "solución"),
    ("soluciones", "soluciones"),
    ("tambien", "también"),
    ("tecnica", "técnica"),
    ("tecnicas", "técnicas"),
    ("tecnico", "técnico"),
    ("teorica", "teórica"),
    ("teorico", "teórico"),
    ("teoria", "teoría"),
    ("teorias", "teorías"),
    ("tecnologia", "tecnología"),
    ("titulo", "título"),
    ("titulos", "títulos"),
    ("transformacion", "transformación"),
    ("version", "versión"),
    ("visualizacion", "visualización"),
]


def preserve_case(source: str, replacement: str) -> str:
    if source.isupper():
        return replacement.upper()
    if source[:1].isupper():
        return replacement[:1].upper() + replacement[1:]
    return replacement


def apply_replacements(text: str) -> str:
    updated = text
    for wrong, right in REPLACEMENTS:
        pattern = re.compile(rf"\b{re.escape(wrong)}\b", re.IGNORECASE)
        updated = pattern.sub(lambda m: preserve_case(m.group(0), right), updated)
    return updated


LINK_TARGET_FIXES = {
    "docs/metodología-docente.md": "docs/metodologia-docente.md",
    "docs/plan-evaluación.md": "docs/plan-evaluacion.md",
    "docs/portal-estudiante-y-app-móvil.md": "docs/portal-estudiante-y-app-movil.md",
    "docs/despliegue-seguro-y-operación.md": "docs/despliegue-seguro-y-operacion.md",
    "portal-estudiante-y-app-móvil.md": "portal-estudiante-y-app-movil.md",
    "metodología-docente.md": "metodologia-docente.md",
    "plan-evaluación.md": "plan-evaluacion.md",
    "despliegue-seguro-y-operación.md": "despliegue-seguro-y-operacion.md",
    "entrevista/desafio-técnico-preparacion.md": "entrevista/desafio-tecnico-preparacion.md",
    "entrevista/entrevista-skillnest-presentación-v2.md": "entrevista/entrevista-skillnest-presentacion-v2.md",
    "entrevista/entrevista-skillnest-presentación.md": "entrevista/entrevista-skillnest-presentacion.md",
    "entrevista/reunión-pitch.md": "entrevista/reunion-pitch.md",
    "entrevista/demo-reunión-jueves.md": "entrevista/demo-reunion-jueves.md",
    "../despliegue-seguro-y-operación.md": "../despliegue-seguro-y-operacion.md",
    "desafio-técnico-preparacion.md": "desafio-tecnico-preparacion.md",
}


def repair_link_targets(text: str) -> str:
    updated = text
    for wrong, right in LINK_TARGET_FIXES.items():
        updated = updated.replace(f"]({wrong})", f"]({right})")
    return updated


def normalize_inline_segments(line: str) -> str:
    segments = re.split(r"(`[^`]*`|!?\[[^\]]+\]\([^)]+\))", line)
    for index in range(0, len(segments), 2):
        segments[index] = apply_replacements(segments[index])
    return "".join(segments)


def normalize_markdown(text: str) -> str:
    lines = text.splitlines(keepends=True)
    output: list[str] = []
    in_fence = False

    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            output.append(line)
            continue

        if in_fence:
            output.append(line)
            continue

        output.append(normalize_inline_segments(line))

    return "".join(output)


def should_skip(path: Path) -> bool:
    return any(part in SKIP_PARTS for part in path.parts)


def main() -> None:
    changed = 0
    for path in ROOT.rglob("*.md"):
        if should_skip(path):
            continue
        original = path.read_text(encoding="utf-8")
        normalized = repair_link_targets(normalize_markdown(original))
        if normalized != original:
            path.write_text(normalized, encoding="utf-8", newline="")
            changed += 1
            print(path.relative_to(ROOT))

    print(f"updated {changed} markdown files")


if __name__ == "__main__":
    main()
