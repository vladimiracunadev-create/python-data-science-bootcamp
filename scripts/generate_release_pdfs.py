"""Genera los 3 PDFs de release para el bootcamp Python para Data Science."""

# Uso: python scripts/generate_release_pdfs.py
# Salida: release_artifacts/{portal-alumno,guia-rapida,temario}-*.pdf
# Requiere: pip install reportlab

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

# ── Paleta ──────────────────────────────────────────────────────────────────
# Paleta visual alineada con el theme del portal GitHub Pages (site/styles.css).
# Mantener coherencia entre la web y los PDFs imprimibles.
TEAL       = colors.HexColor("#0f766e")
TEAL_DARK  = colors.HexColor("#0b4f4a")
TEAL_LIGHT = colors.HexColor("#ccfbf1")
GOLD       = colors.HexColor("#d9a441")
GOLD_LIGHT = colors.HexColor("#fef3c7")
PURPLE     = colors.HexColor("#7c3aed")
PURPLE_L   = colors.HexColor("#ede9fe")
GREEN      = colors.HexColor("#16a34a")
GREEN_L    = colors.HexColor("#dcfce7")
INK        = colors.HexColor("#102a43")
INK_SOFT   = colors.HexColor("#39536c")
BG_WARM    = colors.HexColor("#f5efe3")
WHITE      = colors.white
BORDER     = colors.HexColor("#d8cdbd")

OUT_DIR    = Path("release_artifacts")
PORTAL_URL = "https://vladimiracunadev-create.github.io/python-data-science-bootcamp/"
W, H       = A4   # 595 x 842 pts

# ── Estilos comunes ──────────────────────────────────────────────────────────
def make_styles():
    # Devuelve un dict de estilos reutilizados por los 3 PDFs para garantizar
    # coherencia tipográfica entre portal, guía rápida y temario.
    return {
        "title": ParagraphStyle("title",
            fontName="Helvetica-Bold", fontSize=26,
            textColor=INK, leading=30, spaceAfter=4),
        "subtitle": ParagraphStyle("subtitle",
            fontName="Helvetica", fontSize=13,
            textColor=INK_SOFT, leading=18, spaceAfter=12),
        "eyebrow": ParagraphStyle("eyebrow",
            fontName="Helvetica-Bold", fontSize=8,
            textColor=TEAL, leading=10, spaceBefore=4, spaceAfter=2,
            letterSpacing=1.5),
        "h2": ParagraphStyle("h2",
            fontName="Helvetica-Bold", fontSize=16,
            textColor=INK, leading=20, spaceBefore=18, spaceAfter=6),
        "h3": ParagraphStyle("h3",
            fontName="Helvetica-Bold", fontSize=11,
            textColor=INK, leading=14, spaceBefore=4, spaceAfter=3),
        "body": ParagraphStyle("body",
            fontName="Helvetica", fontSize=9.5,
            textColor=INK_SOFT, leading=14, spaceAfter=4),
        "small": ParagraphStyle("small",
            fontName="Helvetica", fontSize=8,
            textColor=INK_SOFT, leading=11),
        "url": ParagraphStyle("url",
            fontName="Helvetica", fontSize=8.5,
            textColor=TEAL_DARK, leading=12),
        "footer": ParagraphStyle("footer",
            fontName="Helvetica", fontSize=7.5,
            textColor=INK_SOFT, leading=10, alignment=TA_CENTER),
        "num_big": ParagraphStyle("num_big",
            fontName="Helvetica-Bold", fontSize=22,
            textColor=TEAL, leading=26),
        "class_title": ParagraphStyle("class_title",
            fontName="Helvetica-Bold", fontSize=10.5,
            textColor=INK, leading=13, spaceAfter=2),
        "class_desc": ParagraphStyle("class_desc",
            fontName="Helvetica", fontSize=8.5,
            textColor=INK_SOFT, leading=12, spaceAfter=3),
        "topic": ParagraphStyle("topic",
            fontName="Helvetica", fontSize=8,
            textColor=INK_SOFT, leading=11,
            leftIndent=8),
    }


def footer_cb(canvas, doc):
    """Pie de página en cada hoja.

    Al registrarse como callback de SimpleDocTemplate (onFirstPage/onLaterPages),
    ReportLab lo ejecuta automáticamente en cada página sin necesidad de llamarlo
    de forma explícita desde el story.
    """
    canvas.saveState()
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(INK_SOFT)
    canvas.drawString(20*mm, 12*mm, "Bootcamp Python para Data Science")
    canvas.drawRightString(W - 20*mm, 12*mm, PORTAL_URL)
    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(0.5)
    canvas.line(20*mm, 15*mm, W - 20*mm, 15*mm)
    canvas.restoreState()


# ── Datos de las clases ──────────────────────────────────────────────────────
# Fuente de verdad para los 3 PDFs. Si cambia el temario del bootcamp,
# se actualiza aquí y los PDFs generados reflejan el cambio automáticamente.
CLASSES = [
    {
        "num": "00", "icon": "◎", "title": "Diagnóstico inicial",
        "desc": "Quiz de entrada para estimar el punto de partida del grupo y orientar el ritmo del bootcamp.",
        "topics": ["Quiz diagnóstico de 30 preguntas", "Presentación del programa y herramientas", "Configuración del entorno"],
        "color": GOLD, "bg": GOLD_LIGHT,
    },
    {
        "num": "01", "icon": "⬡", "title": "Fundamentos de Python",
        "desc": "Variables, tipos, estructuras de control y funciones aplicadas a datos desde el primer día.",
        "topics": ["Variables y tipos de dato", "Listas, diccionarios, loops", "Funciones básicas"],
        "color": TEAL, "bg": TEAL_LIGHT,
    },
    {
        "num": "02", "icon": "▦", "title": "Pandas y limpieza de datos",
        "desc": "Carga, inspección, limpieza y transformación de DataFrames con pandas.",
        "topics": ["DataFrames y Series", "Valores nulos y duplicados", "Filtros y selección de columnas"],
        "color": TEAL, "bg": TEAL_LIGHT,
    },
    {
        "num": "03", "icon": "▣", "title": "Visualización exploratoria",
        "desc": "Gráficos para entender distribuciones, relaciones y anomalías en los datos.",
        "topics": ["Histogramas y boxplots", "Scatter plots", "Interpretación visual de datos"],
        "color": TEAL, "bg": TEAL_LIGHT,
    },
    {
        "num": "04", "icon": "△", "title": "Estadística descriptiva",
        "desc": "Media, mediana, desviación estándar, correlaciones y cómo leerlas correctamente.",
        "topics": ["Medidas de tendencia central", "Dispersión y varianza", "Correlación e interpretación"],
        "color": TEAL, "bg": TEAL_LIGHT,
    },
    {
        "num": "05", "icon": "◈", "title": "Visualización con Matplotlib",
        "desc": "Control preciso de gráficos: títulos, ejes, colores y múltiples subplots.",
        "topics": ["Figure y Axes", "Personalización de gráficos", "Subplots y layouts"],
        "color": TEAL, "bg": TEAL_LIGHT,
    },
    {
        "num": "06", "icon": "◎", "title": "Texto, fechas y transformaciones",
        "desc": "Procesamiento de strings, manejo de fechas y transformaciones avanzadas de columnas.",
        "topics": ["Operaciones con strings", "Parsing y cálculo de fechas", "Apply y funciones lambda"],
        "color": TEAL, "bg": TEAL_LIGHT,
    },
    {
        "num": "07", "icon": "◉", "title": "Mini proyecto guiado",
        "desc": "Análisis completo de un dataset real: desde carga hasta conclusiones documentadas.",
        "topics": ["Pipeline end-to-end", "Limpieza, análisis y gráficos", "Redacción de conclusiones"],
        "color": TEAL, "bg": TEAL_LIGHT,
    },
    {
        "num": "08", "icon": "◆", "title": "Presentación de hallazgos",
        "desc": "Cómo comunicar resultados a audiencias no técnicas con claridad y evidencia.",
        "topics": ["Narrativa de datos", "Selección de gráficos para presentar", "Práctica de exposición"],
        "color": TEAL, "bg": TEAL_LIGHT,
    },
    {
        "num": "09", "icon": "◧", "title": "Machine Learning — Intro",
        "desc": "Qué es ML, cómo dividir datos y entrenar un primer modelo de regresión lineal.",
        "topics": ["Conceptos: train/test split", "LinearRegression con sklearn", "Métricas: MAE, RMSE, R2"],
        "color": PURPLE, "bg": PURPLE_L,
    },
    {
        "num": "10", "icon": "◨", "title": "Modelos supervisados",
        "desc": "Clasificación con árboles de decisión y regresión logística. Evaluación y métricas.",
        "topics": ["DecisionTree y LogisticRegression", "Matriz de confusión", "Precision, recall, F1"],
        "color": PURPLE, "bg": PURPLE_L,
    },
    {
        "num": "11", "icon": "◩", "title": "Evaluación y Pipelines",
        "desc": "Validación cruzada, Pipelines de sklearn y búsqueda de hiperparámetros con GridSearchCV.",
        "topics": ["cross_val_score", "Pipeline: preproceso + modelo", "GridSearchCV"],
        "color": PURPLE, "bg": PURPLE_L,
    },
    {
        "num": "12", "icon": "★", "title": "Proyecto final y cierre",
        "desc": "Análisis integrador con dataset real: exploración, modelo y presentación de resultados.",
        "topics": ["Dataset a elección del alumno", "Pipeline completo end-to-end", "Presentación y defensa"],
        "color": GREEN, "bg": GREEN_L,
    },
]


# ════════════════════════════════════════════════════════════════════════════
# PDF 1 — PORTAL DEL ALUMNO
# ════════════════════════════════════════════════════════════════════════════
def build_portal_alumno():
    # Produce: portal-alumno-bootcamp.pdf (~3 páginas).
    # Audiencia: alumno que recibe el PDF al inicio del bootcamp.
    # Propósito: punto de entrada oficial con temario completo, metodología y
    # recursos; complementa la versión web del portal GitHub Pages.
    path = OUT_DIR / "portal-alumno-bootcamp.pdf"
    doc = SimpleDocTemplate(
        str(path), pagesize=A4,
        leftMargin=20*mm, rightMargin=20*mm,
        topMargin=22*mm, bottomMargin=22*mm,
    )
    S = make_styles()
    story = []

    # ── Hero banner ──
    hero_data = [[
        Paragraph("PORTAL DEL ALUMNO", S["eyebrow"]),
        Paragraph(PORTAL_URL, S["url"]),
    ]]
    hero_tbl = Table(hero_data, colWidths=[(W - 40*mm) * 0.6, (W - 40*mm) * 0.4])
    hero_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), TEAL),
        ("TEXTCOLOR", (0, 0), (-1, -1), WHITE),
        ("PADDING", (0, 0), (-1, -1), 10),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
    ]))
    story.append(hero_tbl)
    story.append(Spacer(1, 8))

    story.append(Paragraph("Bootcamp Python para Data Science", S["title"]))
    story.append(Paragraph(
        "Tu punto de entrada oficial al programa. 13 clases modulares, laboratorio interactivo y recursos por sesión.",
        S["subtitle"]
    ))

    # estadísticas rápidas
    stats_data = [
        [Paragraph("<b>13</b><br/>clases", ParagraphStyle("sc", fontName="Helvetica-Bold", fontSize=14, textColor=TEAL, leading=18, alignment=TA_CENTER)),
         Paragraph("<b>12</b><br/>notebooks", ParagraphStyle("sc", fontName="Helvetica-Bold", fontSize=14, textColor=TEAL, leading=18, alignment=TA_CENTER)),
         Paragraph("<b>1</b><br/>proyecto final", ParagraphStyle("sc", fontName="Helvetica-Bold", fontSize=14, textColor=TEAL, leading=18, alignment=TA_CENTER)),
         Paragraph("<b>40</b><br/>tests CI/CD", ParagraphStyle("sc", fontName="Helvetica-Bold", fontSize=14, textColor=TEAL, leading=18, alignment=TA_CENTER))],
    ]
    cw = (W - 40*mm) / 4
    stats_tbl = Table(stats_data, colWidths=[cw]*4)
    stats_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), TEAL_LIGHT),
        ("BOX", (0, 0), (-1, -1), 0.5, TEAL),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, TEAL),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("PADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(stats_tbl)
    story.append(Spacer(1, 16))

    # ── Temario ──
    story.append(HRFlowable(width="100%", thickness=1, color=BORDER))
    story.append(Paragraph("TEMARIO COMPLETO", S["eyebrow"]))
    story.append(Paragraph("Las 13 clases del bootcamp", S["h2"]))
    story.append(Spacer(1, 6))

    for cls in CLASSES:
        row_data = [
            [
                Paragraph(f"<b>{cls['num']}</b>", ParagraphStyle("n", fontName="Helvetica-Bold", fontSize=16, textColor=cls["color"], alignment=TA_CENTER)),
                [
                    Paragraph(f"{cls['icon']}  {cls['title']}", S["class_title"]),
                    Paragraph(cls["desc"], S["class_desc"]),
                    *[Paragraph(f"· {t}", S["topic"]) for t in cls["topics"]],
                ],
            ]
        ]
        tbl = Table(row_data, colWidths=[18*mm, W - 40*mm - 18*mm])
        tbl.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (0, 0), cls["bg"]),
            ("BACKGROUND", (1, 0), (1, 0), WHITE),
            ("BOX", (0, 0), (-1, -1), 0.5, BORDER),
            ("LINEAFTER", (0, 0), (0, 0), 1.5, cls["color"]),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("ALIGN", (0, 0), (0, 0), "CENTER"),
            ("PADDING", (0, 0), (0, 0), 8),
            ("PADDING", (1, 0), (1, 0), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]))
        story.append(KeepTogether(tbl))
        story.append(Spacer(1, 3))

    story.append(Spacer(1, 16))
    story.append(HRFlowable(width="100%", thickness=1, color=BORDER))

    # ── Metodología ──
    story.append(Paragraph("METODOLOGÍA", S["eyebrow"]))
    story.append(Paragraph("Cómo trabajamos en cada clase", S["h2"]))

    steps = [
        ("01", "Entender", "Se presenta el objetivo del bloque y por qué sirve en un problema real."),
        ("02", "Practicar", "Se trabaja con ejemplos cortos, ejercicios guiados y variaciones."),
        ("03", "Interpretar", "El resultado se traduce a una conclusión clara y comunicable."),
        ("04", "Consolidar", "Se revisan errores, se guarda evidencia y se deja una tarea breve."),
    ]
    step_rows = [[
        Paragraph(f"<b>{n}</b>", ParagraphStyle("sn", fontName="Helvetica-Bold", fontSize=14, textColor=WHITE, alignment=TA_CENTER)),
        [Paragraph(title, S["h3"]), Paragraph(desc, S["class_desc"])],
    ] for n, title, desc in steps]

    step_tbl = Table(step_rows, colWidths=[14*mm, W - 40*mm - 14*mm])
    step_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), TEAL),
        ("BACKGROUND", (1, 0), (1, -1), BG_WARM),
        ("BOX", (0, 0), (-1, -1), 0.5, BORDER),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, BORDER),
        ("ALIGN", (0, 0), (0, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("PADDING", (0, 0), (-1, -1), 9),
    ]))
    story.append(Spacer(1, 6))
    story.append(step_tbl)
    story.append(Spacer(1, 14))

    # ── Recursos ──
    story.append(HRFlowable(width="100%", thickness=1, color=BORDER))
    story.append(Paragraph("RECURSOS", S["eyebrow"]))
    story.append(Paragraph("Lo que debes tener a mano como alumno", S["h2"]))
    story.append(Spacer(1, 6))

    resources = [
        ("Repositorio del curso", "Materiales, clases, datasets y estructura general del bootcamp.", "github.com/vladimiracunadev-create/python-data-science-bootcamp"),
        ("Datasets de práctica", "Casos sintéticos para trabajar Python, pandas, gráficos e interpretación.", "github.com/.../datasets"),
        ("Notebooks y clases", "Clases, notebooks, ejercicios y guías liberados en sala.", "github.com/.../classes"),
        ("Vista institucional", "Resumen del producto educativo, implementación y hoja de ruta.", PORTAL_URL + "product/"),
    ]
    res_data = [[
        [Paragraph(f"<b>{name}</b>", S["h3"]), Paragraph(desc, S["class_desc"]), Paragraph(url, S["url"])]
        for name, desc, url in resources[:2]
    ], [
        [Paragraph(f"<b>{name}</b>", S["h3"]), Paragraph(desc, S["class_desc"]), Paragraph(url, S["url"])]
        for name, desc, url in resources[2:]
    ]]
    cw2 = (W - 40*mm) / 2 - 2*mm
    for row in res_data:
        tbl = Table([row], colWidths=[cw2, cw2], rowHeights=None)
        tbl.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), BG_WARM),
            ("BOX", (0, 0), (-1, -1), 0.5, BORDER),
            ("INNERGRID", (0, 0), (-1, -1), 0.5, BORDER),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("PADDING", (0, 0), (-1, -1), 10),
        ]))
        story.append(tbl)
        story.append(Spacer(1, 4))

    # ── Uso de tecnología ──
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=1, color=BORDER))
    story.append(Paragraph("USO DE TECNOLOGÍA", S["eyebrow"]))
    story.append(Paragraph("Cómo usar herramientas digitales sin perder aprendizaje", S["h2"]))
    story.append(Spacer(1, 6))

    rules = [
        ("01 Piensa primero", "Antes de buscar una respuesta, formula tu propia hipótesis."),
        ("02 Consulta después", "Usa herramientas digitales para comparar, aclarar o depurar."),
        ("03 Verifica siempre", "Revisa si la respuesta recibida responde al objetivo real del ejercicio."),
        ("04 Explica al final", "Si no puedes explicarlo con tus palabras, aún no está aprendido."),
    ]
    rule_rows = [[Paragraph(f"<b>{r}</b>", S["h3"]), Paragraph(d, S["class_desc"])] for r, d in rules]
    rule_tbl = Table(rule_rows, colWidths=[55*mm, W - 40*mm - 55*mm])
    rule_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), GOLD_LIGHT),
        ("BACKGROUND", (1, 0), (1, -1), WHITE),
        ("BOX", (0, 0), (-1, -1), 0.5, BORDER),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, BORDER),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("PADDING", (0, 0), (-1, -1), 9),
        ("LINEAFTER", (0, 0), (0, -1), 1.5, GOLD),
    ]))
    story.append(rule_tbl)

    doc.build(story, onFirstPage=footer_cb, onLaterPages=footer_cb)
    print(f"  OK  {path}")


# ════════════════════════════════════════════════════════════════════════════
# PDF 2 — GUÍA RÁPIDA (1-2 páginas)
# ════════════════════════════════════════════════════════════════════════════
def build_guia_rapida():
    path = OUT_DIR / "guia-rapida-alumno.pdf"
    doc = SimpleDocTemplate(
        str(path), pagesize=A4,
        leftMargin=18*mm, rightMargin=18*mm,
        topMargin=18*mm, bottomMargin=20*mm,
    )
    S = make_styles()
    story = []

    # Banner
    banner = Table([[
        Paragraph("BOOTCAMP PYTHON PARA DATA SCIENCE", ParagraphStyle(
            "bh", fontName="Helvetica-Bold", fontSize=13, textColor=WHITE, leading=16)),
        Paragraph("GUÍA RÁPIDA DEL ALUMNO", ParagraphStyle(
            "bsub", fontName="Helvetica", fontSize=9, textColor=colors.HexColor("#ccfbf1"), leading=12, alignment=TA_RIGHT)),
    ]], colWidths=[(W-36*mm)*0.65, (W-36*mm)*0.35])
    banner.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), TEAL_DARK),
        ("PADDING", (0, 0), (-1, -1), 12),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(banner)
    story.append(Spacer(1, 10))

    # Enlace oficial
    link_data = [[
        Paragraph("ENLACE OFICIAL DEL PORTAL", S["eyebrow"]),
        Paragraph(PORTAL_URL, ParagraphStyle("lurl", fontName="Helvetica-Bold", fontSize=10, textColor=TEAL_DARK)),
    ]]
    link_tbl = Table(link_data, colWidths=[52*mm, W-36*mm-52*mm])
    link_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), GOLD_LIGHT),
        ("BOX", (0, 0), (-1, -1), 1, GOLD),
        ("LEFTPADDING", (0, 0), (0, 0), 10),
        ("PADDING", (1, 0), (1, 0), 10),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LINEAFTER", (0, 0), (0, 0), 1.5, GOLD),
    ]))
    story.append(link_tbl)
    story.append(Spacer(1, 12))

    # Las 13 clases en grilla compacta
    story.append(Paragraph("LAS 13 CLASES", S["eyebrow"]))
    story.append(Spacer(1, 4))

    # 2 columnas
    left = CLASSES[:7]
    right = CLASSES[7:]

    def cls_cell(c):
        color = c["color"]
        return [
            Paragraph(f"<b>{c['num']}  {c['icon']}  {c['title']}</b>",
                ParagraphStyle("ct", fontName="Helvetica-Bold", fontSize=8.5, textColor=color, leading=11)),
            Paragraph(c["desc"],
                ParagraphStyle("cd", fontName="Helvetica", fontSize=7.5, textColor=INK_SOFT, leading=10, spaceAfter=1)),
        ]

    def build_col(classes):
        rows = []
        for c in classes:
            rows.append([cls_cell(c)])
        tbl = Table(rows, colWidths=[(W-36*mm)/2 - 3*mm])
        tbl.setStyle(TableStyle([
            ("BOX", (0, 0), (-1, -1), 0.5, BORDER),
            ("INNERGRID", (0, 0), (-1, -1), 0.5, BORDER),
            ("PADDING", (0, 0), (-1, -1), 7),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("BACKGROUND", (0, 0), (-1, -1), BG_WARM),
        ]))
        return tbl

    cols = Table([[build_col(left), build_col(right)]], colWidths=[(W-36*mm)/2]*2)
    cols.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("COLPADDING", (0, 0), (-1, -1), 3),
    ]))
    story.append(cols)
    story.append(Spacer(1, 12))

    # Metodología y Recursos lado a lado
    meto = [
        ("01 Entender", "Se presenta el objetivo y el porqué real."),
        ("02 Practicar", "Ejemplos cortos, guiados y con variaciones."),
        ("03 Interpretar", "El resultado se convierte en conclusión."),
        ("04 Consolidar", "Revisión de errores y tarea breve."),
    ]
    meto_rows = [[
        Paragraph(f"<b>{n}</b>", ParagraphStyle("mn", fontName="Helvetica-Bold", fontSize=8.5, textColor=TEAL, leading=11)),
        Paragraph(d, S["small"])
    ] for n, d in meto]
    meto_tbl = Table(
        [[Paragraph("METODOLOGÍA", S["eyebrow"])], *meto_rows],
        colWidths=[36*mm, (W-36*mm)/2 - 36*mm - 6*mm]
    )
    meto_tbl.setStyle(TableStyle([
        ("SPAN", (0, 0), (1, 0)),
        ("BACKGROUND", (0, 1), (-1, -1), BG_WARM),
        ("BOX", (0, 0), (-1, -1), 0.5, BORDER),
        ("INNERGRID", (0, 1), (-1, -1), 0.5, BORDER),
        ("PADDING", (0, 0), (-1, -1), 7),
        ("LINEAFTER", (0, 1), (0, -1), 1.5, TEAL),
    ]))

    res_items = [
        ("Repositorio", "github.com/vladimiracunadev-create/python-data-science-bootcamp"),
        ("Datasets", ".../tree/master/datasets"),
        ("Clases/Notebooks", ".../tree/master/classes"),
        ("Vista institucional", PORTAL_URL + "product/"),
    ]
    res_rows = [[
        Paragraph(f"<b>{n}</b>", ParagraphStyle("rn", fontName="Helvetica-Bold", fontSize=8.5, textColor=TEAL_DARK, leading=11)),
        Paragraph(u, S["small"])
    ] for n, u in res_items]
    res_tbl = Table(
        [[Paragraph("RECURSOS", S["eyebrow"])], *res_rows],
        colWidths=[30*mm, (W-36*mm)/2 - 30*mm - 6*mm]
    )
    res_tbl.setStyle(TableStyle([
        ("SPAN", (0, 0), (1, 0)),
        ("BACKGROUND", (0, 1), (-1, -1), BG_WARM),
        ("BOX", (0, 0), (-1, -1), 0.5, BORDER),
        ("INNERGRID", (0, 1), (-1, -1), 0.5, BORDER),
        ("PADDING", (0, 0), (-1, -1), 7),
        ("LINEAFTER", (0, 1), (0, -1), 1.5, GOLD),
    ]))

    bottom = Table([[meto_tbl, res_tbl]], colWidths=[(W-36*mm)/2]*2)
    bottom.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("COLPADDING", (0, 0), (-1, -1), 3),
    ]))
    story.append(bottom)

    doc.build(story, onFirstPage=footer_cb, onLaterPages=footer_cb)
    print(f"  OK  {path}")


# ════════════════════════════════════════════════════════════════════════════
# PDF 3 — TEMARIO COMPLETO
# ════════════════════════════════════════════════════════════════════════════
def build_temario():
    path = OUT_DIR / "temario-bootcamp-python-ds.pdf"
    doc = SimpleDocTemplate(
        str(path), pagesize=A4,
        leftMargin=20*mm, rightMargin=20*mm,
        topMargin=22*mm, bottomMargin=22*mm,
    )
    S = make_styles()
    story = []

    # Portada de sección
    cover_data = [[
        Paragraph("BOOTCAMP PYTHON PARA DATA SCIENCE", ParagraphStyle(
            "ch", fontName="Helvetica-Bold", fontSize=11, textColor=colors.HexColor("#ccfbf1"), leading=14)),
        "",
    ], [
        Paragraph("Temario completo — 13 clases", ParagraphStyle(
            "ct", fontName="Helvetica-Bold", fontSize=22, textColor=WHITE, leading=26)),
        Paragraph(
            "<b>13</b> clases<br/><b>12</b> notebooks<br/><b>1</b> proyecto final",
            ParagraphStyle("cs", fontName="Helvetica", fontSize=10, textColor=colors.HexColor("#ccfbf1"), leading=16, alignment=TA_RIGHT)),
    ]]
    cover_tbl = Table(cover_data, colWidths=[(W-40*mm)*0.7, (W-40*mm)*0.3])
    cover_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), TEAL_DARK),
        ("PADDING", (0, 0), (-1, -1), 14),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 6),
        ("TOPPADDING", (0, 1), (-1, 1), 8),
    ]))
    story.append(cover_tbl)
    story.append(Spacer(1, 6))

    # Leyenda de colores
    legend = Table([[
        Paragraph("  Clase diagnóstica  ", ParagraphStyle("lg", fontName="Helvetica-Bold", fontSize=7.5, textColor=WHITE, alignment=TA_CENTER)),
        Paragraph("  Módulos Python & Datos  ", ParagraphStyle("lg2", fontName="Helvetica-Bold", fontSize=7.5, textColor=WHITE, alignment=TA_CENTER)),
        Paragraph("  Módulos Machine Learning  ", ParagraphStyle("lg3", fontName="Helvetica-Bold", fontSize=7.5, textColor=WHITE, alignment=TA_CENTER)),
        Paragraph("  Proyecto final  ", ParagraphStyle("lg4", fontName="Helvetica-Bold", fontSize=7.5, textColor=WHITE, alignment=TA_CENTER)),
    ]], colWidths=[(W-40*mm)/4]*4)
    legend.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), GOLD),
        ("BACKGROUND", (1, 0), (1, 0), TEAL),
        ("BACKGROUND", (2, 0), (2, 0), PURPLE),
        ("BACKGROUND", (3, 0), (3, 0), GREEN),
        ("PADDING", (0, 0), (-1, -1), 6),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ]))
    story.append(legend)
    story.append(Spacer(1, 12))

    # Clases detalladas
    for cls in CLASSES:
        header_data = [[
            Paragraph(f"CLASE {cls['num']}", ParagraphStyle(
                "cn", fontName="Helvetica-Bold", fontSize=8, textColor=WHITE, leading=10, letterSpacing=1)),
            Paragraph(f"<b>{cls['icon']}  {cls['title']}</b>", ParagraphStyle(
                "cth", fontName="Helvetica-Bold", fontSize=13, textColor=WHITE, leading=16)),
        ]]
        header_tbl = Table(header_data, colWidths=[22*mm, W-40*mm-22*mm])
        header_tbl.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), cls["color"]),
            ("PADDING", (0, 0), (-1, -1), 9),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LINEAFTER", (0, 0), (0, 0), 1.5, WHITE),
        ]))

        body_data = [[
            [
                Paragraph(cls["desc"], S["body"]),
                Spacer(1, 4),
                Paragraph("<b>Temas clave:</b>", S["h3"]),
                *[Paragraph(f"  {i+1}.  {t}", S["body"]) for i, t in enumerate(cls["topics"])],
            ]
        ]]
        body_tbl = Table(body_data, colWidths=[W-40*mm])
        body_tbl.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), cls["bg"]),
            ("BOX", (0, 0), (-1, -1), 0.5, cls["color"]),
            ("TOPPADDING", (0, 0), (-1, -1), 10),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
            ("LEFTPADDING", (0, 0), (-1, -1), 12),
            ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ]))

        block = KeepTogether([header_tbl, body_tbl, Spacer(1, 6)])
        story.append(block)

    # Notas finales
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=1, color=BORDER))
    notes_data = [[
        [
            Paragraph("SOBRE LOS NOTEBOOKS", S["eyebrow"]),
            Paragraph(
                "Cada clase (excepto la 00) tiene un notebook.ipynb y un soluciones.ipynb. "
                "El primero se trabaja en clase; el segundo se comparte después de la sesión.",
                S["body"]),
        ],
        [
            Paragraph("SOBRE LOS DATASETS", S["eyebrow"]),
            Paragraph(
                "Los datasets de práctica son sintéticos y están diseñados para ilustrar "
                "conceptos clave de cada clase sin depender de APIs externas.",
                S["body"]),
        ],
    ]]
    notes_tbl = Table(notes_data, colWidths=[(W-40*mm)/2]*2)
    notes_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BG_WARM),
        ("BOX", (0, 0), (-1, -1), 0.5, BORDER),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, BORDER),
        ("PADDING", (0, 0), (-1, -1), 10),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(notes_tbl)

    doc.build(story, onFirstPage=footer_cb, onLaterPages=footer_cb)
    print(f"  OK  {path}")


# ── Main ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    OUT_DIR.mkdir(exist_ok=True)
    print("Generando PDFs...")
    build_portal_alumno()
    build_guia_rapida()
    build_temario()
    print("Listo.")
