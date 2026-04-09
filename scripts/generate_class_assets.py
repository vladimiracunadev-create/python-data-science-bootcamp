"""Genera PDFs explicativos y presentaciones PPTX para cada clase del bootcamp.

Responsabilidades:
    1. Reutilizar la fuente de verdad del currículo para evitar divergencias.
    2. Crear una guía PDF por clase con contexto, ruta, práctica y cierre.
    3. Crear una presentación PowerPoint por clase con una plantilla uniforme.

Qué resuelve:
    Permite compartir material imprimible y expositivo por clase sin preparar
    manualmente trece documentos y trece presentaciones cada vez.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import rebuild_curriculum as curriculum_source
from generar_pdf_documento import render_markdown_text
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_AUTO_SHAPE_TYPE
from pptx.enum.text import MSO_ANCHOR
from pptx.util import Inches, Pt

BASE_DIR = Path(__file__).resolve().parents[1]
PDF_OUTPUT_DIR = BASE_DIR / "docs" / "pdfs" / "classes"
PPTX_OUTPUT_DIR = BASE_DIR / "docs" / "presentaciones" / "classes"

COLOR_BG = RGBColor(15, 23, 42)
COLOR_PANEL = RGBColor(17, 24, 39)
COLOR_ACCENT = RGBColor(34, 197, 94)
COLOR_TEXT = RGBColor(241, 245, 249)
COLOR_MUTED = RGBColor(148, 163, 184)
COLOR_CODE = RGBColor(2, 6, 23)


def route_lines(number: int) -> list[str]:
    """Convierte la tabla de ruta de sesión en bullets compactos para PPTX."""
    rows = curriculum_source.route_table(number).splitlines()
    bullets: list[str] = []
    for row in rows:
        if not row.startswith("|") or "---" in row or "Tramo" in row:
            continue
        parts = [part.strip() for part in row.strip("|").split("|")]
        if len(parts) != 4:
            continue
        tramo, tiempo, enfoque, evidencia = parts
        bullets.append(f"{tramo}: {tiempo} | {enfoque} | Evidencia: {evidencia}")
    return bullets


def build_class_markdown(item: dict) -> str:
    """Construye una guía explicativa compacta para una clase concreta."""
    materials = "\n".join(f"- `{name}`" for name in curriculum_source.materials(item))
    outcomes = "\n".join(f"- {value}" for value in item["outcomes"])
    topics = "\n".join(f"- {value}" for value in item["topics"])
    route = curriculum_source.route_table(item["number"])

    if item["code"] is None:
        main_block = f"""## 🧩 Bloque de trabajo principal

{item['block_intro']}

**Qué hace:** {item['schema']}

**Para qué sirve:** {item['purpose']}
"""
    else:
        documented_code = curriculum_source.documented_code(item)
        main_block = f"""## 💻 Demostración guiada

### {item['block_title']}

{item['block_intro']}

**Qué hace:** {item['schema']}

**Para qué sirve:** {item['purpose']}

```python
{documented_code}
```
"""

    practice_notes = [
        "Pedir al estudiante que explique la pregunta antes de escribir código.",
        "Leer la salida en voz alta y conectar resultado con evidencia.",
        "Hacer una variación pequeña y justificar qué cambió y por qué.",
    ]
    if item["number"] == 0:
        practice_notes = [
            "Resolver el diagnóstico completo en 15 minutos sin ayuda externa.",
            "Leer la retroalimentación por pregunta para detectar vacíos reales.",
            "Cerrar con una meta breve de mejora para la clase siguiente.",
        ]

    homework_notes = [
        "Dejar código o desarrollo ordenado.",
        "Escribir una conclusión breve con evidencia.",
        "Mantener comentarios en los bloques que no sean obvios.",
    ]
    if item["number"] == 0:
        homework_notes = [
            "Registrar fortalezas iniciales.",
            "Anotar dudas que quieras resolver en la primera semana.",
            "Definir un compromiso concreto de estudio para el arranque.",
        ]

    practice = "\n".join(f"- {value}" for value in practice_notes)
    homework = "\n".join(f"- {value}" for value in homework_notes)

    return f"""# {item['icon']} {curriculum_source.class_label(item['number'])}: {item['title']}

> 📘 Guía explicativa para conducir, estudiar o presentar esta clase con claridad.

## 🎯 Objetivo de aprendizaje

{item['objective']}

## ⏱️ Perfil de la sesión

- Duración sugerida: `{item['duration']}`
- Nivel: `{item['level']}`
- Dataset base: `{item['dataset']}`

## ✅ Resultados esperados

{outcomes}

## 🧠 Temas que deben quedar claros

{topics}

## 💡 Idea central

{item['idea']}

## ❓ Por qué importa este módulo

{item['why']}

## 🧭 Ruta sugerida de la clase

{route}

{main_block}
## 🧪 Práctica guiada

{practice}

## 📝 Tarea o evidencia de cierre

{homework}

## 📚 Materiales del módulo

{materials}

## 🔗 Continuidad

{item['next']}

## 👩‍🏫 Nota para el docente

{item['note']}
"""


def _add_background(slide) -> None:
    """Pinta fondo y barra superior para mantener identidad visual."""
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = COLOR_BG

    bar = slide.shapes.add_shape(
        MSO_AUTO_SHAPE_TYPE.RECTANGLE,
        0,
        0,
        Inches(13.333),
        Inches(0.45),
    )
    bar.fill.solid()
    bar.fill.fore_color.rgb = COLOR_PANEL
    bar.line.color.rgb = COLOR_PANEL

    accent = slide.shapes.add_shape(
        MSO_AUTO_SHAPE_TYPE.RECTANGLE,
        0,
        Inches(0.45),
        Inches(13.333),
        Inches(0.08),
    )
    accent.fill.solid()
    accent.fill.fore_color.rgb = COLOR_ACCENT
    accent.line.color.rgb = COLOR_ACCENT


def _add_title(slide, title: str, subtitle: str = "") -> None:
    """Crea un encabezado de slide consistente y legible."""
    _add_background(slide)

    title_box = slide.shapes.add_textbox(Inches(0.7), Inches(0.8), Inches(11.9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.clear()
    title_frame.word_wrap = True
    title_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
    paragraph = title_frame.paragraphs[0]
    paragraph.text = title
    paragraph.font.name = "Segoe UI Semibold"
    paragraph.font.size = Pt(24)
    paragraph.font.color.rgb = COLOR_TEXT

    if subtitle:
        subtitle_box = slide.shapes.add_textbox(Inches(0.72), Inches(1.45), Inches(11.9), Inches(0.5))
        subtitle_frame = subtitle_box.text_frame
        subtitle_frame.clear()
        subtitle_frame.word_wrap = True
        paragraph = subtitle_frame.paragraphs[0]
        paragraph.text = subtitle
        paragraph.font.name = "Segoe UI"
        paragraph.font.size = Pt(11)
        paragraph.font.color.rgb = COLOR_MUTED


def _add_bullets(slide, title: str, bullets: list[str], subtitle: str = "") -> None:
    """Agrega una slide con una lista de bullets compacta."""
    _add_title(slide, title, subtitle)
    box = slide.shapes.add_textbox(Inches(0.8), Inches(2.0), Inches(11.7), Inches(4.7))
    frame = box.text_frame
    frame.clear()
    frame.word_wrap = True

    for index, bullet in enumerate(bullets):
        paragraph = frame.paragraphs[0] if index == 0 else frame.add_paragraph()
        paragraph.text = bullet
        paragraph.level = 0
        paragraph.space_after = Pt(10)
        paragraph.font.name = "Segoe UI"
        paragraph.font.size = Pt(20 if len(bullets) <= 4 else 18)
        paragraph.font.color.rgb = COLOR_TEXT


def _add_two_column_slide(slide, title: str, left_title: str, left_values: list[str], right_title: str, right_values: list[str]) -> None:
    """Muestra dos columnas de contenido para temas y resultados."""
    _add_title(slide, title)

    for x, header, values in [
        (Inches(0.8), left_title, left_values),
        (Inches(6.8), right_title, right_values),
    ]:
        panel = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, x, Inches(1.95), Inches(5.1), Inches(4.4))
        panel.fill.solid()
        panel.fill.fore_color.rgb = COLOR_PANEL
        panel.line.color.rgb = COLOR_PANEL

        header_box = slide.shapes.add_textbox(x + Inches(0.2), Inches(2.15), Inches(4.7), Inches(0.4))
        header_frame = header_box.text_frame
        header_frame.clear()
        paragraph = header_frame.paragraphs[0]
        paragraph.text = header
        paragraph.font.name = "Segoe UI Semibold"
        paragraph.font.size = Pt(16)
        paragraph.font.color.rgb = COLOR_ACCENT

        body_box = slide.shapes.add_textbox(x + Inches(0.2), Inches(2.6), Inches(4.7), Inches(3.4))
        body_frame = body_box.text_frame
        body_frame.clear()
        body_frame.word_wrap = True
        for index, value in enumerate(values):
            paragraph = body_frame.paragraphs[0] if index == 0 else body_frame.add_paragraph()
            paragraph.text = value
            paragraph.font.name = "Segoe UI"
            paragraph.font.size = Pt(17)
            paragraph.font.color.rgb = COLOR_TEXT
            paragraph.space_after = Pt(8)


def _add_code_slide(slide, title: str, intro: str, code: str) -> None:
    """Agrega una slide para demo técnica o lectura guiada de código."""
    _add_title(slide, title, intro)

    box = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.0), Inches(11.7), Inches(4.6))
    box.fill.solid()
    box.fill.fore_color.rgb = COLOR_CODE
    box.line.color.rgb = COLOR_PANEL

    code_box = slide.shapes.add_textbox(Inches(1.0), Inches(2.25), Inches(11.2), Inches(4.1))
    frame = code_box.text_frame
    frame.clear()
    frame.word_wrap = True
    frame.vertical_anchor = MSO_ANCHOR.TOP
    paragraph = frame.paragraphs[0]
    paragraph.text = code
    paragraph.font.name = "Courier New"
    paragraph.font.size = Pt(12)
    paragraph.font.color.rgb = COLOR_TEXT


def create_presentation(item: dict, output_path: Path) -> None:
    """Construye una presentación PPTX breve y reutilizable por clase."""
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]

    slide = prs.slides.add_slide(blank)
    _add_title(
        slide,
        f"{item['icon']} {curriculum_source.class_label(item['number'])}: {item['title']}",
        f"{item['duration']} | Nivel {item['level']} | Dataset: {item['dataset']}",
    )
    intro_box = slide.shapes.add_textbox(Inches(0.8), Inches(2.15), Inches(11.7), Inches(3.2))
    intro_frame = intro_box.text_frame
    intro_frame.clear()
    intro_frame.word_wrap = True
    paragraph = intro_frame.paragraphs[0]
    paragraph.text = item["objective"]
    paragraph.font.name = "Segoe UI Semibold"
    paragraph.font.size = Pt(28)
    paragraph.font.color.rgb = COLOR_TEXT
    paragraph.space_after = Pt(18)
    paragraph = intro_frame.add_paragraph()
    paragraph.text = item["idea"]
    paragraph.font.name = "Segoe UI"
    paragraph.font.size = Pt(18)
    paragraph.font.color.rgb = COLOR_MUTED

    slide = prs.slides.add_slide(blank)
    _add_two_column_slide(
        slide,
        "🎯 Logros y focos del módulo",
        "Temas clave",
        item["topics"],
        "Resultados esperados",
        item["outcomes"],
    )

    slide = prs.slides.add_slide(blank)
    _add_bullets(slide, "🧭 Ruta sugerida de la sesión", route_lines(item["number"]))

    slide = prs.slides.add_slide(blank)
    _add_bullets(
        slide,
        "❓ Sentido pedagógico",
        [
            f"Por qué importa: {item['why']}",
            f"Qué hace: {item['schema']}",
            f"Para qué sirve: {item['purpose']}",
            f"Nota docente: {item['note']}",
        ],
    )

    slide = prs.slides.add_slide(blank)
    if item["code"] is None:
        _add_bullets(
            slide,
            f"🧩 {item['block_title']}",
            [
                item["block_intro"],
                f"Qué hace: {item['schema']}",
                f"Para qué sirve: {item['purpose']}",
            ],
        )
    else:
        _add_code_slide(slide, f"💻 {item['block_title']}", item["block_intro"], curriculum_source.documented_code(item))

    slide = prs.slides.add_slide(blank)
    _add_bullets(
        slide,
        "🧪 Práctica y cierre",
        [
            "Pedir explicación de la pregunta antes de ejecutar.",
            "Leer la salida y justificar cada decisión importante.",
            "Cerrar con una variación pequeña o conclusión breve.",
            item["next"],
        ],
    )

    slide = prs.slides.add_slide(blank)
    _add_bullets(
        slide,
        "📚 Materiales del módulo",
        [f"Disponible: {name}" for name in curriculum_source.materials(item)],
        "Archivos que conviene mostrar o entregar al grupo.",
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    prs.save(output_path)


def generate_assets(selected_classes: list[dict]) -> None:
    """Genera PDF y PPTX para el conjunto de clases solicitado."""
    for item in selected_classes:
        class_slug = item["slug"]
        class_number = f"{item['number']:02d}"
        markdown = build_class_markdown(item)

        pdf_path = PDF_OUTPUT_DIR / f"clase-{class_number}-{class_slug.split('-', 1)[1]}-guia-explicativa.pdf"
        pptx_path = PPTX_OUTPUT_DIR / f"clase-{class_number}-{class_slug.split('-', 1)[1]}-presentacion.pptx"

        render_markdown_text(
            markdown_text=markdown,
            output_path=pdf_path,
            title=f"{curriculum_source.class_label(item['number'])}: {item['title']}",
            subtitle="Guía explicativa lista para clase, repaso o presentación.",
        )
        create_presentation(item, pptx_path)
        print(f"[OK] {pdf_path.relative_to(BASE_DIR)}")
        print(f"[OK] {pptx_path.relative_to(BASE_DIR)}")


def main() -> None:
    """Procesa argumentos CLI y genera activos de una o varias clases."""
    parser = argparse.ArgumentParser(description="Genera PDF y PPTX para las clases del bootcamp.")
    parser.add_argument("--clase", help="Número de clase con dos dígitos, por ejemplo 01 o 12.")
    args = parser.parse_args()

    selected = curriculum_source.CURRICULUM
    if args.clase:
        selected = [item for item in curriculum_source.CURRICULUM if f"{item['number']:02d}" == args.clase]
        if not selected:
            raise SystemExit(f"No existe la clase {args.clase}.")

    generate_assets(selected)


if __name__ == "__main__":
    main()
