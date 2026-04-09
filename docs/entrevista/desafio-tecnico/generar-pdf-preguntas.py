#!/usr/bin/env python3
"""Genera PDF legible con las 1000 preguntas Python"""
import json
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer

styles = getSampleStyleSheet()

style_h1 = ParagraphStyle("H1", parent=styles["Heading1"], fontSize=18,
    textColor=colors.HexColor("#0f3d3e"), spaceAfter=10, spaceBefore=16)
style_h2 = ParagraphStyle("H2", parent=styles["Heading2"], fontSize=13,
    textColor=colors.HexColor("#ff6b35"), spaceAfter=6, spaceBefore=10)
style_q = ParagraphStyle("Q", parent=styles["BodyText"], fontSize=10,
    spaceAfter=3, leftIndent=10, textColor=colors.HexColor("#111111"))
style_a = ParagraphStyle("A", parent=styles["BodyText"], fontSize=10,
    spaceAfter=8, leftIndent=20, textColor=colors.HexColor("#2a6e2a"))

with open("1000_preguntas_python.json", encoding="utf-8") as f:
    preguntas = json.load(f)

# Agrupa por categoría
categorias = {}
for p in preguntas:
    cat = p["categoria"]
    if cat not in categorias:
        categorias[cat] = []
    categorias[cat].append(p)

doc = SimpleDocTemplate("1000_preguntas_python.pdf", pagesize=letter,
    rightMargin=0.75 * inch, leftMargin=0.75 * inch,
    topMargin=0.75 * inch, bottomMargin=0.75 * inch)

contenido = [
    Paragraph("1000 Preguntas Python — Estudio Intensivo", styles["Title"]),
    Paragraph("Cubre: Fundamentos, POO, Data Science, Full-Stack, Avanzado, Entorno", styles["Normal"]),
    Spacer(1, 0.3 * inch),
]

for cat, preg_list in sorted(categorias.items()):
    contenido.append(Paragraph(f"{cat.upper()} ({len(preg_list)} preguntas)", style_h1))
    niveles = {"Básica": [], "Intermedia": [], "Avanzada": []}
    for p in preg_list:
        niv = p.get("dificultad", "Básica")
        if niv in niveles:
            niveles[niv].append(p)

    for nivel, items in niveles.items():
        if not items:
            continue
        contenido.append(Paragraph(f"{nivel}", style_h2))
        for p in items:
            contenido.append(Paragraph(f"<b>P{p['id']}.</b> {p['pregunta']}", style_q))
            contenido.append(Paragraph(f"R: {p['respuesta']}", style_a))

    contenido.append(PageBreak())

doc.build(contenido)
print("[OK] 1000_preguntas_python.pdf generado")
