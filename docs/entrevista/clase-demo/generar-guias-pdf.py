#!/usr/bin/env python3
"""
Genera 3 PDFs completos de preparación — uno por opción de clase demo
Cubre: conocimiento, Q&A, timing, evaluador, todo lo que necesitas saber
"""

import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

# ─── Estilos ─────────────────────────────────────────────────────────────────

styles = getSampleStyleSheet()

TEAL   = colors.HexColor("#0f3d3e")
ORANGE = colors.HexColor("#ff6b35")
GREEN  = colors.HexColor("#2e7d32")
RED    = colors.HexColor("#c62828")
GRAY   = colors.HexColor("#f5f5f5")
DARK   = colors.HexColor("#212121")

s_title = ParagraphStyle("title", parent=styles["Title"],
    fontSize=26, textColor=TEAL, spaceAfter=6)
s_cover_sub = ParagraphStyle("cover_sub", parent=styles["Normal"],
    fontSize=14, textColor=ORANGE, spaceAfter=4)
s_h1 = ParagraphStyle("h1", parent=styles["Heading1"],
    fontSize=16, textColor=TEAL, spaceBefore=14, spaceAfter=6,
    borderPad=4)
s_h2 = ParagraphStyle("h2", parent=styles["Heading2"],
    fontSize=13, textColor=ORANGE, spaceBefore=10, spaceAfter=4)
s_h3 = ParagraphStyle("h3", parent=styles["Heading3"],
    fontSize=11, textColor=DARK, spaceBefore=6, spaceAfter=3, fontName="Helvetica-Bold")
s_body = ParagraphStyle("body", parent=styles["BodyText"],
    fontSize=10, spaceAfter=5, leading=14)
s_q = ParagraphStyle("q", parent=styles["BodyText"],
    fontSize=10, spaceAfter=2, leftIndent=8,
    fontName="Helvetica-Bold", textColor=DARK)
s_a = ParagraphStyle("a", parent=styles["BodyText"],
    fontSize=10, spaceAfter=8, leftIndent=20, textColor=GREEN)
s_tip = ParagraphStyle("tip", parent=styles["BodyText"],
    fontSize=10, spaceAfter=4, leftIndent=12,
    backColor=colors.HexColor("#e8f5e9"), leading=14)
s_warn = ParagraphStyle("warn", parent=styles["BodyText"],
    fontSize=10, spaceAfter=4, leftIndent=12,
    backColor=colors.HexColor("#fff3e0"), leading=14)
s_code = ParagraphStyle("code", parent=styles["BodyText"],
    fontSize=9, fontName="Courier", leftIndent=20,
    backColor=colors.HexColor("#f0f0f0"), spaceAfter=6, leading=12)

def hr():
    return HRFlowable(width="100%", thickness=1, color=TEAL, spaceAfter=8)

def tabla_timing(filas, col_widths=(1.2*inch, 1.0*inch, 4.5*inch)):
    """Tabla de timing con formato."""
    data = [["Minuto", "Tiempo", "Actividad"]] + filas
    t = Table(data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), TEAL),
        ("TEXTCOLOR",  (0,0), (-1,0), colors.white),
        ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",   (0,0), (-1,0), 10),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, GRAY]),
        ("FONTSIZE",   (0,1), (-1,-1), 9),
        ("GRID",       (0,0), (-1,-1), 0.5, colors.HexColor("#cccccc")),
        ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]))
    return t

def tabla_rubrica():
    data = [
        ["Criterio", "Lo que el evaluador ve", "Cómo destacar"],
        ["Claridad",      "¿Explicas sin confundir?",         "Analogías simples antes del código"],
        ["Conocimiento",  "¿Dominas profundidad?",            "Relaciona conceptos, da contexto"],
        ["Pedagogía",     "¿Sabes enseñar, no solo saber?",   "Verifica comprensión, adapta el ritmo"],
        ["Timing",        "¿Respetas los 45 min?",            "Reloj visible, corta si se alarga"],
        ["Engagement",    "¿Mantienes interés online?",       "Preguntas, demos en vivo, pausas"],
        ["Profesional",   "¿Presencia online correcta?",      "Cámara, audio, fondo, sin distracciones"],
        ["Improvisación", "¿Manejas preguntas inesperadas?",  "Honestidad + redirigir si no sabes"],
    ]
    t = Table(data, colWidths=[1.3*inch, 2.5*inch, 2.9*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), TEAL),
        ("TEXTCOLOR",  (0,0), (-1,0), colors.white),
        ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",   (0,0), (-1,-1), 9),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, GRAY]),
        ("GRID",       (0,0), (-1,-1), 0.5, colors.HexColor("#cccccc")),
        ("VALIGN",     (0,0), (-1,-1), "TOP"),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]))
    return t


# ─────────────────────────────────────────────────────────────────────────────
# OPCIÓN 1 — VISUALIZACIÓN (CLASE 6)
# ─────────────────────────────────────────────────────────────────────────────

def guia_opcion1():
    e = []

    # Portada
    e += [Spacer(1, 1*inch),
          Paragraph("GUÍA COMPLETA DE PREPARACIÓN", s_title),
          Paragraph("Opción 1 — Clase 6: Visualización con Matplotlib", s_cover_sub),
          Paragraph("Presentación online · 45 minutos · Con evaluador", s_cover_sub),
          Spacer(1, 0.3*inch),
          Paragraph(f"Generado: {datetime.date.today().strftime('%d/%m/%Y')}", styles["Normal"]),
          PageBreak()]

    # 1. Por qué esta clase es la indicada para demostrar
    e += [Paragraph("1. POR QUÉ ESTA CLASE ES ESTRATÉGICA", s_h1), hr(),
          Paragraph("La Clase 6 de Visualización es la más accesible visualmente para un evaluador. "
                    "Un gráfico bien ejecutado en vivo comunica más que 10 minutos de teoría. "
                    "Además, demuestra que conectas datos crudos con conclusiones — la esencia del Data Science.", s_body),
          Paragraph("✅ Ideal si quieres destacar por: claridad, comunicación visual, bajo riesgo técnico.", s_tip),
          Paragraph("⚠️ Riesgo a controlar: que parezca básica. Profundiza siempre con el 'por qué'.", s_warn),
          Spacer(1, 0.15*inch)]

    # 2. Conocimiento que debes dominar
    e += [Paragraph("2. CONOCIMIENTO QUE DEBES DOMINAR", s_h1), hr()]

    temas = [
        ("¿Qué es Matplotlib?",
         "Librería de visualización estándar de Python, basada en MATLAB. Permite crear gráficos "
         "estáticos, animados e interactivos. Base de otras librerías como Seaborn y Pandas plot."),
        ("Anatomía de una figura",
         "Figure (contenedor principal) > Axes (área de graficado) > Axis (ejes X/Y) > Artists (líneas, texto, etc.). "
         "Entender esta jerarquía evita confusión entre plt.figure() y plt.subplot()."),
        ("plt vs axes API",
         "plt.plot() es la API de estado (rápida, menos control). ax.plot() es la API orientada a objetos "
         "(recomendada para gráficos complejos o subplots)."),
        ("Cuándo usar cada tipo",
         "Scatter: relación entre 2 variables continuas. Line: tendencia temporal. Bar: comparar categorías. "
         "Histogram: distribución. Box: detectar outliers. Heatmap: correlaciones."),
        ("Anscombe's Quartet",
         "4 datasets con mismas estadísticas (media, varianza, correlación) pero gráficamente diferentes. "
         "Prueba que SIEMPRE hay que visualizar antes de reportar."),
        ("DPI y guardado",
         "plt.savefig('archivo.png', dpi=300, bbox_inches='tight'). DPI 300 = calidad de impresión. "
         "bbox_inches='tight' evita que se corten los labels."),
    ]

    for t, c in temas:
        e += [Paragraph(f"<b>{t}</b>", s_h3),
              Paragraph(c, s_body)]

    e.append(PageBreak())

    # 3. Q&A
    e += [Paragraph("3. PREGUNTAS Y RESPUESTAS DEL TEMA", s_h1), hr()]

    qa = [
        ("¿Qué diferencia hay entre plt.show() y plt.savefig()?",
         "show() muestra el gráfico en pantalla (Jupyter/IDE). savefig() lo guarda en disco. "
         "Se puede usar savefig() antes de show(). Si se usa show() primero, la figura se limpia y savefig() queda vacío."),
        ("¿Por qué mi gráfico aparece vacío después de plt.show()?",
         "plt.show() limpia el estado. Solución: usar savefig() ANTES de show(), o usar la API orientada a objetos (fig, ax)."),
        ("¿Qué es figsize?",
         "Es el tamaño en pulgadas: plt.figure(figsize=(10, 6)) = 10 pulgadas de ancho × 6 de alto. "
         "Para presentaciones: (12, 7). Para reportes: (8, 5)."),
        ("¿Cómo diferencio series en un scatter por color?",
         "Usando el parámetro c= con una lista de colores o un array de valores + cmap. "
         "Ejemplo: plt.scatter(x, y, c=labels, cmap='viridis')."),
        ("¿Cuándo uso Seaborn en lugar de Matplotlib?",
         "Seaborn es mejor para gráficos estadísticos (distribuciones, correlaciones, regresiones). "
         "Matplotlib es más flexible para gráficos personalizados. Ambos coexisten."),
        ("¿Qué hace tight_layout()?",
         "Ajusta automáticamente el espaciado entre subplots para que no se superpongan títulos y labels."),
        ("¿Cómo añado leyenda a un gráfico?",
         "Usando plt.legend() o ax.legend(). Necesitas label= en cada serie: plt.plot(x, y, label='Serie A')."),
        ("¿Qué es un subplot?",
         "fig, axes = plt.subplots(filas, columnas) crea una cuadrícula de gráficos dentro de una figura. "
         "Útil para comparar múltiples variables en una sola imagen."),
        ("¿Por qué mi texto sale cortado en el gráfico guardado?",
         "Usar bbox_inches='tight' en savefig(). También puedes ajustar márgenes con plt.subplots_adjust()."),
        ("¿Cómo cambio el estilo general de todos los gráficos?",
         "plt.style.use('seaborn') o plt.style.use('ggplot'). Ejecutar una sola vez al inicio del notebook."),
        ("¿Qué hace alpha= en un gráfico?",
         "Controla la transparencia: 0 = invisible, 1 = sólido. Útil en scatter plots densos para ver superposición."),
        ("¿Cómo grafico datos de un DataFrame de pandas directamente?",
         "df.plot(kind='bar') o df['columna'].hist(). Pandas tiene una API de plot integrada que usa Matplotlib internamente."),
        ("¿Cuál es la diferencia entre bar y barh?",
         "bar = barras verticales (comparar valores). barh = barras horizontales (mejor cuando los labels son largos)."),
        ("¿Cómo agrego anotaciones a un gráfico?",
         "plt.annotate('texto', xy=(x,y), xytext=(x2,y2), arrowprops=dict(arrowstyle='->')). "
         "También ax.text(x, y, 'texto') para texto simple sin flecha."),
        ("¿Qué pasa si no llamo a plt.show()?",
         "En Jupyter con %matplotlib inline se muestra automáticamente al final de cada celda. "
         "En scripts .py es necesario llamar show() para que aparezca."),
    ]

    for p, r in qa:
        e += [Paragraph(f"P: {p}", s_q),
              Paragraph(f"R: {r}", s_a)]

    e.append(PageBreak())

    # 4. Timing exacto
    e += [Paragraph("4. PLANIFICACIÓN Y USO DEL TIEMPO — 45 MINUTOS", s_h1), hr()]
    e.append(tabla_timing([
        ["00:00",  "1 min",  "Apertura: '¿Han visto alguna vez cómo un gráfico revela lo que los números ocultan?'"],
        ["01:00",  "4 min",  "Anscombe's Quartet — por qué visualizar siempre. Dibuja o muestra imagen."],
        ["05:00",  "5 min",  "Tipos de gráficos y cuándo usar cada uno (tabla visual en slide)."],
        ["10:00",  "8 min",  "DEMO 1: primer gráfico (sin(x)) — explicar anatomía, título, labels, grid."],
        ["18:00",  "5 min",  "Personalización: colores, estilos, alpha, savefig. Show rápido."],
        ["23:00",  "7 min",  "DEMO 2: subplots 2×2 con datos Iris — scatter + histogram."],
        ["30:00",  "5 min",  "DEMO 3: estilo seaborn + barras comparativas (opcional, si hay tiempo)."],
        ["35:00",  "8 min",  "EJERCICIO EN VIVO: alumnos crean gráfico propio. Docente guía paso a paso."],
        ["43:00",  "2 min",  "Resumen de la clase + vista previa Clase 7."],
        ["45:00",  "—",      "FIN"],
    ]))
    e.append(Spacer(1, 0.2*inch))
    e += [Paragraph("⏱️ Puntos de control (mira el reloj sin que se note):", s_h3),
          Paragraph("Minuto 10: ¿Ya mostraste Anscombe y los tipos de gráficos?", s_body),
          Paragraph("Minuto 23: ¿Ya hiciste el primer demo en vivo?", s_body),
          Paragraph("Minuto 35: ¿Ya terminaste los demos y empezaste el ejercicio?", s_body),
          Paragraph("Si vas lento: omite DEMO 3 (barras). Si vas rápido: expande el ejercicio con más variantes.", s_tip),
          PageBreak()]

    # 5. Lo que el evaluador mide
    e += [Paragraph("5. LO QUE EL EVALUADOR MIDE — CÓMO SER SU MEJOR OPCIÓN", s_h1), hr()]
    e.append(tabla_rubrica())
    e.append(Spacer(1, 0.2*inch))

    e += [Paragraph("Momentos que dejan huella:", s_h2),
          Paragraph("🌟 <b>Anscombe's Quartet</b> — muestra la imagen. El evaluador recordará que abriste con impacto.", s_tip),
          Paragraph("🌟 <b>Demo en vivo limpia</b> — no copies, escribe (o ejecuta celdas preparadas). "
                    "El evaluador ve que dominas el entorno.", s_tip),
          Paragraph("🌟 <b>Explica el output</b> — no solo ejecutes. Di '¿ven este pico? Significa que…' "
                    "Eso separa a quien enseña de quien muestra código.", s_tip),
          Paragraph("🌟 <b>Pregunta al alumno</b> — 'Antes de ejecutar, ¿qué forma creen que tendrá el gráfico?' "
                    "El evaluador ve que activas pensamiento, no solo recepción.", s_tip),
          Paragraph("🌟 <b>Cierre con propósito</b> — 'La visualización no es decoración, es comunicación de datos. "
                    "Ustedes ya pueden comunicar con datos. Eso vale.'", s_tip),
          PageBreak()]

    # 6. Errores comunes y cómo evitarlos
    e += [Paragraph("6. ERRORES COMUNES — Y CÓMO EVITARLOS", s_h1), hr()]
    errores = [
        ("Leer el código en voz alta sin explicar",
         "Habla del concepto, no de la sintaxis. 'Aquí le digo que el eje X es…' no 'aquí pongo plt.xlabel'."),
        ("Ejecutar todo de golpe sin pausas",
         "Celda por celda. Después de cada output, pregunta '¿qué observan?'"),
        ("Gráficos sin título ni labels",
         "Siempre título, xlabel, ylabel. Demuestra que sabes que un gráfico sin contexto no comunica nada."),
        ("Ignorar preguntas del evaluador",
         "Si pregunta algo, detente, responde y vuelve. No digas 'lo veremos más adelante'."),
        ("Tiempo libre al final",
         "Si terminas antes de minuto 43, agrega variantes al ejercicio o invita reflexión."),
    ]
    for err, sol in errores:
        e += [Paragraph(f"❌ {err}", s_warn),
              Paragraph(f"✅ Solución: {sol}", s_tip)]

    e.append(Spacer(1, 0.2*inch))

    # 7. Lo que nadie te dice
    e += [Paragraph("7. LO QUE NADIE TE DICE (PERO EL EVALUADOR VE)", s_h1), hr(),
          Paragraph("<b>Tu actitud frente al error importa más que no errar.</b> "
                    "Si algo falla en el demo, no te pongas nervioso. Di 'interesante, veamos qué pasó aquí…' "
                    "y arréglalo. El evaluador valora cómo manejas la presión.", s_body),
          Paragraph("<b>El silencio pedagógico es una herramienta.</b> "
                    "Después de ejecutar un gráfico, guarda silencio 3 segundos. "
                    "Deja que lo miren. Eso demuestra confianza.", s_body),
          Paragraph("<b>La transición entre slides importa.</b> "
                    "No digas 'siguiente slide'. Di 'Ahora que entendemos X, veamos cómo se traduce en código…'", s_body),
          Paragraph("<b>El evaluador también evalúa cómo tratas a los 'alumnos' imaginarios.</b> "
                    "Usa 'nosotros', no 'ustedes'. 'Vamos a crear…', no 'hagan esto'.", s_body),
          Paragraph("<b>El cierre es tan importante como la apertura.</b> "
                    "No termines con '…y eso es todo'. Cierra con un mensaje que motive.", s_body),
          Spacer(1, 0.2*inch)]

    # 8. Checklist
    e += [Paragraph("8. CHECKLIST FINAL — EL DÍA ANTERIOR", s_h1), hr(),
          Paragraph("□ Ejecuté los 3 demos al menos 5 veces cada uno", s_body),
          Paragraph("□ Hice una carrera completa de 45 min con reloj", s_body),
          Paragraph("□ Tengo Jupyter abierto con las celdas listas", s_body),
          Paragraph("□ Guardé screenshots de cada demo como backup", s_body),
          Paragraph("□ Practiqué la explicación de Anscombe's Quartet en voz alta", s_body),
          Paragraph("□ Preparé 2 preguntas para hacer a los alumnos", s_body),
          Paragraph("□ Revisé micrófono, cámara y fondo", s_body),
          Paragraph("□ Cerré notificaciones y apps innecesarias", s_body),
          Paragraph("□ Dormí bien (en serio, importa)", s_body),
          Paragraph("□ El día de la presentación, respiro 3 veces y confío en lo que preparé", s_body)]

    return e


# ─────────────────────────────────────────────────────────────────────────────
# OPCIÓN 2 — ML INTRO (CLASE 9)
# ─────────────────────────────────────────────────────────────────────────────

def guia_opcion2():
    e = []

    e += [Spacer(1, 1*inch),
          Paragraph("GUÍA COMPLETA DE PREPARACIÓN", s_title),
          Paragraph("Opción 2 — Clase 9: Machine Learning Intro", s_cover_sub),
          Paragraph("Presentación online · 45 minutos · Con evaluador", s_cover_sub),
          Spacer(1, 0.3*inch),
          Paragraph(f"Generado: {datetime.date.today().strftime('%d/%m/%Y')}", styles["Normal"]),
          PageBreak()]

    e += [Paragraph("1. POR QUÉ ESTA CLASE ES ESTRATÉGICA", s_h1), hr(),
          Paragraph("La Clase 9 es la puerta de entrada al Machine Learning. "
                    "Un evaluador que busca a alguien para enseñar Data Science quiere ver que sabes "
                    "explicar conceptos de ML desde cero con claridad y ejemplos reales, sin asumir conocimiento previo. "
                    "Esta clase demuestra amplitud conceptual y rigor pedagógico.", s_body),
          Paragraph("✅ Ideal si quieres mostrar: solidez conceptual, capacidad de simplificar lo complejo.", s_tip),
          Paragraph("⚠️ Riesgo a controlar: volverse abstracto. Cada concepto necesita un ejemplo concreto.", s_warn)]

    e += [Paragraph("2. CONOCIMIENTO QUE DEBES DOMINAR", s_h1), hr()]

    temas = [
        ("¿Qué es Machine Learning?",
         "Rama de la IA donde los sistemas aprenden patrones de datos sin ser programados explícitamente. "
         "Arthur Samuel (1959): 'Campo que da a los computadores la capacidad de aprender sin ser programados explícitamente.'"),
        ("Supervised Learning",
         "Aprende de datos etiquetados (X → y). Se entrena con pares (input, output conocido). "
         "Ejemplos: regresión (predice número), clasificación (predice categoría)."),
        ("Unsupervised Learning",
         "Encuentra patrones en datos sin etiquetas. No hay 'respuesta correcta'. "
         "Ejemplos: clustering (agrupar clientes), reducción de dimensiones (PCA)."),
        ("Reinforcement Learning",
         "Un agente aprende tomando acciones en un entorno para maximizar una recompensa. "
         "Ejemplo: AlphaGo, robots, juegos de video."),
        ("El flujo de ML",
         "1. Obtener datos → 2. Explorar → 3. Limpiar → 4. Preparar features → "
         "5. Entrenar modelo → 6. Evaluar → 7. Optimizar → 8. Desplegar."),
        ("Overfitting",
         "El modelo memorizó el training set. Alta accuracy en train, baja en test. "
         "Causas: modelo muy complejo, poco dato. Solución: regularización, más datos, cross-validation."),
        ("Underfitting",
         "El modelo es demasiado simple. Baja accuracy en train Y test. "
         "Causas: modelo muy simple, features irrelevantes. Solución: modelo más complejo."),
        ("Train/Test Split",
         "Dividir datos: 80% entrenamiento, 20% prueba. El test set NUNCA se toca durante el entrenamiento. "
         "Así se simula cómo el modelo se comportará con datos nunca vistos."),
        ("Score en regresión: R²",
         "Mide qué porcentaje de la varianza explica el modelo. 1.0 = perfecto, 0 = igual que predecir la media. "
         "Negativo = peor que la media (modelo muy malo)."),
        ("Feature vs Target",
         "Features (X): variables de entrada, lo que usamos para predecir. "
         "Target (y): lo que queremos predecir. Ejemplo: features=horas_estudio, target=nota_examen."),
    ]

    for t, c in temas:
        e += [Paragraph(f"<b>{t}</b>", s_h3),
              Paragraph(c, s_body)]

    e.append(PageBreak())

    e += [Paragraph("3. PREGUNTAS Y RESPUESTAS DEL TEMA", s_h1), hr()]

    qa = [
        ("¿Cuál es la diferencia entre AI, ML y Deep Learning?",
         "AI es el campo más amplio (cualquier comportamiento inteligente de máquinas). "
         "ML es un subconjunto de AI (aprende de datos). Deep Learning es un subconjunto de ML (redes neuronales profundas)."),
        ("¿Por qué necesitamos dividir en train y test?",
         "Para evaluar la generalización. Si evaluamos en los mismos datos de entrenamiento, "
         "el modelo parece perfecto pero puede fallar en datos nuevos (overfitting)."),
        ("¿Qué pasa si no limpio los datos antes de entrenar?",
         "Garbage in, garbage out. Valores nulos, outliers o escalas inconsistentes degradan el modelo. "
         "La limpieza es 60-70% del trabajo real en Data Science."),
        ("¿LinearRegression puede hacer clasificación?",
         "No directamente. Para clasificación se usa LogisticRegression (que a pesar del nombre, clasifica). "
         "LinearRegression predice valores continuos."),
        ("¿Por qué mi modelo tiene 95% accuracy pero funciona mal en producción?",
         "Posibles causas: overfitting, data leakage, distribución diferente en producción, "
         "o accuracy no es la métrica correcta (dataset desbalanceado)."),
        ("¿Qué es data leakage?",
         "Cuando información del futuro (test set) filtra al entrenamiento. Causa accuracy irreal. "
         "Ejemplo: normalizar con stats del dataset completo antes de hacer split."),
        ("¿Cuántos datos necesito para entrenar un modelo?",
         "Depende de la complejidad del problema y del modelo. Regla general: mínimo 10× el número de features. "
         "Redes neuronales necesitan miles o millones."),
        ("¿Qué es un hiperparámetro?",
         "Parámetro que tú defines antes del entrenamiento (no lo aprende el modelo). "
         "Ejemplos: learning rate, max_depth de un árbol, número de capas en una red neuronal."),
        ("¿Cuál es la diferencia entre parámetro e hiperparámetro?",
         "Parámetros: los aprende el modelo durante el entrenamiento (pesos, coeficientes). "
         "Hiperparámetros: los defines tú antes (profundidad del árbol, regularización)."),
        ("¿Por qué sklearn usa siempre fit/predict?",
         "Es la API estándar (Estimator API). fit() entrena el modelo, predict() hace predicciones. "
         "Todos los modelos la implementan, lo que facilita cambiar de algoritmo sin reescribir el pipeline."),
        ("¿Qué hace random_state en train_test_split?",
         "Fija la semilla aleatoria para reproducibilidad. Con el mismo random_state siempre obtienes "
         "la misma división de datos."),
        ("¿Por qué normalizar los datos?",
         "Algoritmos sensibles a escala (KNN, SVM, redes neuronales) necesitan que las features "
         "estén en rangos similares. StandardScaler → media 0, std 1."),
        ("¿Qué es una feature de alta cardinalidad?",
         "Una variable categórica con muchos valores únicos (ej: ID de usuario). "
         "Difícil de codificar con one-hot encoding sin explotar la dimensionalidad."),
        ("¿Cuándo usar regresión vs clasificación?",
         "Regresión: target es continuo (precio, temperatura, ventas). "
         "Clasificación: target es categórico (spam/no spam, enfermo/sano, tipo de flor)."),
        ("¿Qué significa que un modelo 'no converge'?",
         "El algoritmo de optimización no encontró el mínimo. Causas: learning rate muy alto, "
         "datos mal escalados, demasiadas iteraciones necesarias."),
    ]

    for p, r in qa:
        e += [Paragraph(f"P: {p}", s_q),
              Paragraph(f"R: {r}", s_a)]

    e.append(PageBreak())

    e += [Paragraph("4. PLANIFICACIÓN Y USO DEL TIEMPO — 45 MINUTOS", s_h1), hr()]
    e.append(tabla_timing([
        ["00:00", "1 min",  "Hook: '¿Cómo sabe Netflix qué serie recomendarte? → Machine Learning'"],
        ["01:00", "5 min",  "¿Qué es ML? AI vs ML vs DL. Supervised / Unsupervised / Reinforcement."],
        ["06:00", "5 min",  "El flujo de ML (diagrama). De datos crudos a modelo desplegado."],
        ["11:00", "9 min",  "DEMO: LinearRegression en vivo. train_test_split + fit + score. Iris dataset."],
        ["20:00", "8 min",  "Overfitting vs Underfitting. Dibuja curvas en pantalla o pizarra."],
        ["28:00", "5 min",  "Algoritmos comunes (overview rápido). DecisionTree, KNN, RandomForest."],
        ["33:00", "7 min",  "DEMO: DecisionTree en Iris. Comparar scores con LinearRegression."],
        ["40:00", "4 min",  "Resumen del flujo + motivación para Clase 10 (profundización)."],
        ["44:00", "1 min",  "Preguntas abiertas."],
        ["45:00", "—",      "FIN"],
    ]))
    e.append(Spacer(1, 0.2*inch))
    e += [Paragraph("⏱️ Puntos de control:", s_h3),
          Paragraph("Minuto 11: ¿Ya explicaste los 3 tipos de ML y el flujo?", s_body),
          Paragraph("Minuto 20: ¿Ya ejecutaste el primer demo?", s_body),
          Paragraph("Minuto 33: ¿Ya cubriste overfitting?", s_body),
          Paragraph("Si vas lento: omite DEMO con DecisionTree, solo menciona los algoritmos.", s_tip),
          PageBreak()]

    e += [Paragraph("5. LO QUE EL EVALUADOR MIDE — CÓMO SER SU MEJOR OPCIÓN", s_h1), hr()]
    e.append(tabla_rubrica())
    e.append(Spacer(1, 0.2*inch))

    e += [Paragraph("Momentos que dejan huella:", s_h2),
          Paragraph("🌟 <b>El hook de apertura</b> — La pregunta de Netflix es universal. Todos la han vivido.", s_tip),
          Paragraph("🌟 <b>Diagrama del flujo dibujado en tiempo real</b> — No solo slides estáticos.", s_tip),
          Paragraph("🌟 <b>Analogía de overfitting</b> — 'Como un estudiante que memoriza las respuestas "
                    "del examen anterior en lugar de entender la materia.'", s_tip),
          Paragraph("🌟 <b>Comparar 2 modelos en vivo</b> — LinearRegression vs DecisionTree. "
                    "Demuestra que sabes que no hay un único algoritmo.", s_tip),
          Paragraph("🌟 <b>Conectar con el mundo real</b> — Spotify, Google, Uber usan ML. "
                    "El evaluador ve que enseñas con propósito.", s_tip),
          PageBreak()]

    e += [Paragraph("6. ERRORES COMUNES — Y CÓMO EVITARLOS", s_h1), hr()]
    errores = [
        ("Explicar ML sin ejemplos del mundo real",
         "Cada concepto debe tener un caso real: 'Supervised = detectar spam (tienes emails etiquetados)'."),
        ("No dibujar el flujo",
         "El flujo de ML es abstracto si solo se menciona. Dibújalo en pizarra o en una slide animada."),
        ("No explicar qué hace train_test_split internamente",
         "Di que shuffle=True por defecto, que se puede usar stratify= para clases desbalanceadas."),
        ("Decir 'el modelo aprende' sin explicar qué aprende",
         "En LinearRegression aprende los coeficientes (pesos). En DecisionTree aprende los umbrales de corte."),
        ("No conectar Clase 9 con Clase 10",
         "Al cerrar, menciona: 'Hoy vimos el panorama. La próxima clase entramos en profundidad con "
         "clasificación, árboles de decisión y evaluación avanzada.'"),
    ]
    for err, sol in errores:
        e += [Paragraph(f"❌ {err}", s_warn),
              Paragraph(f"✅ Solución: {sol}", s_tip)]

    e.append(Spacer(1, 0.2*inch))

    e += [Paragraph("7. LO QUE NADIE TE DICE (PERO EL EVALUADOR VE)", s_h1), hr(),
          Paragraph("<b>El evaluador sabe la materia.</b> No intentes impresionarlo con vocabulario técnico sin explicar. "
                    "Lo que sí lo impresiona es que sepas enseñarla con claridad.", s_body),
          Paragraph("<b>La velocidad de avance dice mucho.</b> Si vas muy rápido, el evaluador asume que no verificas comprensión. "
                    "Pausa, pregunta, confirma.", s_body),
          Paragraph("<b>Los errores en demos no son un problema si los manejas bien.</b> "
                    "Tener un error y debuggear en vivo demuestra maestría. Tener un error y ponerse nervioso no.", s_body),
          Paragraph("<b>Menciona limitaciones.</b> Un buen docente dice 'esta métrica no siempre es suficiente'. "
                    "Eso demuestra pensamiento crítico.", s_body),
          Spacer(1, 0.2*inch)]

    e += [Paragraph("8. CHECKLIST FINAL — EL DÍA ANTERIOR", s_h1), hr(),
          Paragraph("□ Practiqué la analogía de Netflix + el hook de apertura", s_body),
          Paragraph("□ Dibujé el flujo de ML de memoria sin mirar notas", s_body),
          Paragraph("□ Ejecuté LinearRegression y DecisionTree 5+ veces", s_body),
          Paragraph("□ Puedo explicar overfitting con al menos 2 analogías distintas", s_body),
          Paragraph("□ Cronometré la carrera completa (±2 min de 45 min)", s_body),
          Paragraph("□ Preparé backup: screenshots de demos por si Jupyter falla", s_body),
          Paragraph("□ Revisé setup técnico (cámara, audio, Jupyter arriba)", s_body)]

    return e


# ─────────────────────────────────────────────────────────────────────────────
# OPCIÓN 3 — PIPELINES (CLASE 11)
# ─────────────────────────────────────────────────────────────────────────────

def guia_opcion3():
    e = []

    e += [Spacer(1, 1*inch),
          Paragraph("GUÍA COMPLETA DE PREPARACIÓN", s_title),
          Paragraph("Opción 3 — Clase 11: Evaluación y Pipelines", s_cover_sub),
          Paragraph("Presentación online · 45 minutos · Con evaluador", s_cover_sub),
          Spacer(1, 0.3*inch),
          Paragraph(f"Generado: {datetime.date.today().strftime('%d/%m/%Y')}", styles["Normal"]),
          PageBreak()]

    e += [Paragraph("1. POR QUÉ ESTA CLASE ES ESTRATÉGICA", s_h1), hr(),
          Paragraph("La Clase 11 demuestra que sabes llevar ML a producción. "
                    "CrossValidation, GridSearchCV y Pipelines son las herramientas que diferencian "
                    "a un junior (que hace train/test simple) de un profesional. "
                    "Elegir esta clase le dice al evaluador: 'No solo sé ML, sé ML que funciona en el mundo real.'", s_body),
          Paragraph("✅ Ideal si quieres mostrar: profundidad técnica, pensamiento productivo, rigor profesional.", s_tip),
          Paragraph("⚠️ Riesgo a controlar: densidad. 4 conceptos en 45 min exige ritmo ágil y conexiones claras.", s_warn)]

    e += [Paragraph("2. CONOCIMIENTO QUE DEBES DOMINAR", s_h1), hr()]

    temas = [
        ("Problema del train/test split simple",
         "Con un solo split, el score depende de qué datos cayeron en test (varianza alta). "
         "Si los datos son 'fáciles' en test, score alto irreal. Si son difíciles, score bajo injusto."),
        ("K-Fold Cross-Validation",
         "Divide datos en k partes iguales. Itera k veces: usa k-1 como train, 1 como validation. "
         "Cada muestra se usa exactamente 1 vez para validación. Resultado: k scores → promedio + std."),
        ("StratifiedKFold",
         "Versión de KFold que mantiene la proporción de clases en cada fold. "
         "Esencial en datasets desbalanceados."),
        ("Confusion Matrix",
         "Tabla 2×2 para clasificación binaria: TP, TN, FP, FN. "
         "FP = error tipo 1 (dije sí, era no). FN = error tipo 2 (dije no, era sí)."),
        ("Precision, Recall, F1",
         "Precision = TP/(TP+FP). Recall = TP/(TP+FN). F1 = 2PR/(P+R). "
         "Cuándo usar: Precision si FP caro (spam). Recall si FN caro (diagnóstico). F1 si ambos importan."),
        ("ROC-AUC",
         "Curva ROC: True Positive Rate vs False Positive Rate a distintos umbrales. "
         "AUC = área bajo la curva. 1.0 = perfecto, 0.5 = aleatorio. Mejor que accuracy en datasets desbalanceados."),
        ("GridSearchCV",
         "Busca exhaustivamente las mejores combinaciones de hiperparámetros usando cross-validation interna. "
         "Prueba param1 × param2 × ... × cv_folds entrenamientos. "
         "Retorna best_params_, best_score_, best_estimator_."),
        ("RandomizedSearchCV",
         "Muestrea aleatoriamente combinaciones en lugar de probar todas. "
         "Más rápido que GridSearchCV cuando el espacio de hiperparámetros es grande."),
        ("Pipeline",
         "Cadena de transformadores + estimador final. fit() aplica transformaciones en orden y entrena el modelo. "
         "predict() aplica transformaciones a nuevos datos y predice."),
        ("Por qué Pipeline evita data leakage",
         "Con Pipeline, los transformadores (ej: StandardScaler) se fitean SOLO con datos de train en cada fold "
         "de cross-validation. Sin Pipeline, puedes fitear el scaler con todo el dataset, filtrando info del test."),
        ("Notación de hiperparámetros en Pipeline",
         "'paso__hiperparámetro'. Ejemplo: 'clf__max_depth': [3, 5, 10]. "
         "El doble guion bajo (__) separa el nombre del paso del nombre del parámetro."),
        ("ColumnTransformer",
         "Aplica diferentes transformaciones a diferentes columnas. "
         "Ejemplo: StandardScaler a columnas numéricas + OneHotEncoder a columnas categóricas."),
    ]

    for t, c in temas:
        e += [Paragraph(f"<b>{t}</b>", s_h3),
              Paragraph(c, s_body)]

    e.append(PageBreak())

    e += [Paragraph("3. PREGUNTAS Y RESPUESTAS DEL TEMA", s_h1), hr()]

    qa = [
        ("¿Por qué cross_val_score puede dar scores diferentes a score() en test set?",
         "cross_val_score usa múltiples splits y reporta el promedio. score() usa un único split fijo. "
         "cross_val_score es más representativo de la performance real del modelo."),
        ("¿Qué significa un std alto en cross-validation?",
         "Alta varianza entre folds. El modelo es sensible al subset de datos. Puede indicar poco dato "
         "o modelo inestable. Std bajo = modelo robusto."),
        ("¿GridSearchCV hace data leakage?",
         "No, si usas Pipeline. Sin Pipeline, podrías fitear el scaler con todos los datos antes del grid. "
         "Con Pipeline, cada fold fittea el scaler solo con su training data."),
        ("¿Cuál es la diferencia entre GridSearchCV y RandomizedSearchCV?",
         "GridSearchCV prueba TODAS las combinaciones. RandomizedSearchCV prueba n_iter combinaciones aleatorias. "
         "RandomizedSearchCV es más eficiente con espacios de búsqueda grandes."),
        ("¿Cómo accedo al mejor modelo de GridSearchCV?",
         "grid.best_estimator_ retorna el modelo ya entrenado con los mejores parámetros. "
         "grid.best_params_ solo retorna el diccionario de parámetros."),
        ("¿Puedo usar Pipeline con modelos de regresión?",
         "Sí, Pipeline funciona igual para regresión y clasificación. La diferencia es el último estimador."),
        ("¿Por qué F1 es la media armónica y no la aritmética?",
         "La media armónica penaliza valores muy dispares entre Precision y Recall. "
         "Si P=0.9 y R=0.1, media aritmética=0.5 (parece OK), media armónica=0.18 (refleja que algo está muy mal)."),
        ("¿Cuándo es ROC-AUC mejor que accuracy?",
         "En datasets desbalanceados. Con 95% de clase negativa, un modelo que siempre predice negativo "
         "tiene 95% accuracy pero AUC=0.5 (inútil). ROC-AUC revela la verdad."),
        ("¿Cuántos folds usar en cross-validation?",
         "5 o 10 son estándar. Con k muy alto: más tiempo, menos varianza. "
         "Con k muy bajo: más varianza, menos tiempo. Para datasets pequeños, usa k=10."),
        ("¿Pipeline puede incluir selección de features?",
         "Sí. SelectKBest, PCA, u otros transformadores se pueden incluir como pasos. "
         "También puedes tunear sus parámetros con GridSearchCV via 'paso__parámetro'."),
        ("¿Qué pasa si GridSearchCV tarda mucho?",
         "Usa n_jobs=-1 para paralelizar. Reduce el grid (menos valores). "
         "Usa RandomizedSearchCV. O usa HalvingGridSearchCV (sklearn >= 0.24)."),
        ("¿Qué es el parámetro scoring en GridSearchCV?",
         "Define la métrica usada para comparar configuraciones. Default: accuracy para clasificación, R² para regresión. "
         "Puedes usar: 'f1', 'roc_auc', 'precision', 'recall', etc."),
        ("¿Cómo hago validación cruzada estratificada con GridSearchCV?",
         "GridSearchCV usa StratifiedKFold automáticamente para clasificación (cv=5). "
         "Para forzarlo: cv=StratifiedKFold(n_splits=5, shuffle=True)."),
        ("¿Diferencia entre fit() y fit_transform() en un transformer?",
         "fit() aprende parámetros (ej: media para StandardScaler). "
         "transform() aplica la transformación. fit_transform() hace ambas en una sola llamada."),
        ("¿Debo fitear el Pipeline con todos los datos después de GridSearchCV?",
         "GridSearchCV ya reentrenó el mejor modelo con todos los datos de train (refit=True por defecto). "
         "Solo necesitas hacer grid.best_estimator_.predict(X_test)."),
    ]

    for p, r in qa:
        e += [Paragraph(f"P: {p}", s_q),
              Paragraph(f"R: {r}", s_a)]

    e.append(PageBreak())

    e += [Paragraph("4. PLANIFICACIÓN Y USO DEL TIEMPO — 45 MINUTOS", s_h1), hr()]
    e.append(tabla_timing([
        ["00:00", "1 min",  "Hook: '95% train, 62% test. ¿Qué salió mal? — Hoy lo resolvemos.'"],
        ["01:00", "6 min",  "Cross-Validation: concepto + diagrama de folds. Por qué es mejor que split simple."],
        ["07:00", "5 min",  "DEMO: cross_val_score en Iris. Mostrar scores, media y std."],
        ["12:00", "7 min",  "Confusion matrix + Precision/Recall/F1. Ejemplo médico (FN caro)."],
        ["19:00", "5 min",  "DEMO: classification_report en vivo. Interpretar cada número."],
        ["24:00", "5 min",  "GridSearchCV: concepto. Cuántas combinaciones prueba (multiplicar en voz alta)."],
        ["29:00", "6 min",  "DEMO: GridSearchCV con param_grid. Mostrar best_params_ y best_score_."],
        ["35:00", "6 min",  "Pipeline: concepto + por qué evita errores. DEMO: Pipeline + GridSearchCV."],
        ["41:00", "3 min",  "Resumen: CV + métricas + GridSearch + Pipeline = ML profesional."],
        ["44:00", "1 min",  "Preguntas."],
        ["45:00", "—",      "FIN"],
    ]))
    e.append(Spacer(1, 0.2*inch))
    e += [Paragraph("⏱️ Puntos de control:", s_h3),
          Paragraph("Minuto 12: ¿Ya hiciste el demo de cross_val_score?", s_body),
          Paragraph("Minuto 24: ¿Ya cubriste métricas y classification_report?", s_body),
          Paragraph("Minuto 35: ¿Ya mostraste GridSearchCV?", s_body),
          Paragraph("Si vas lento: omite el DEMO de classification_report (solo muestra el código). "
                    "Pipeline es el cierre fuerte — no lo omitas.", s_tip),
          PageBreak()]

    e += [Paragraph("5. LO QUE EL EVALUADOR MIDE — CÓMO SER SU MEJOR OPCIÓN", s_h1), hr()]
    e.append(tabla_rubrica())
    e.append(Spacer(1, 0.2*inch))

    e += [Paragraph("Momentos que dejan huella:", s_h2),
          Paragraph("🌟 <b>El hook de overfitting</b> — Mostrar el gap 95%/62% al abrir genera tensión narrativa. "
                    "El evaluador quiere ver cómo lo resuelves.", s_tip),
          Paragraph("🌟 <b>Multiplicar las combinaciones en voz alta</b> — '4 valores × 3 valores × 5 folds = 60 entrenamientos. "
                    "GridSearchCV los hace todos por ti.' El evaluador ve que entiendes qué pasa bajo el capó.", s_tip),
          Paragraph("🌟 <b>El ejemplo médico de Recall</b> — 'Si el modelo dice No tienes cáncer pero sí lo tienes, "
                    "ese Falso Negativo es gravísimo.' El evaluador ve que conectas técnica con consecuencias reales.", s_tip),
          Paragraph("🌟 <b>Demo limpio de Pipeline</b> — Un pipeline de 3 pasos ejecutado en 2 líneas impresiona. "
                    "Muestra la comparación antes/después (código manual vs Pipeline).", s_tip),
          Paragraph("🌟 <b>Cerrar con propósito</b> — 'Ahora saben hacer ML que funciona en producción. "
                    "Eso es lo que las empresas buscan.'", s_tip),
          PageBreak()]

    e += [Paragraph("6. ERRORES COMUNES — Y CÓMO EVITARLOS", s_h1), hr()]
    errores = [
        ("Explicar Pipeline sin mostrar el 'antes'",
         "Muestra primero cómo es sin Pipeline (scaler.fit(X_train), scaler.transform(X_train), model.fit...). "
         "Luego muestra Pipeline. El contraste hace obvia la ventaja."),
        ("No explicar la notación clf__max_depth",
         "Di explícitamente: 'El doble guion bajo conecta el nombre del paso con su parámetro interno'. "
         "Escríbelo en pantalla, no solo lo digas."),
        ("Pasar muy rápido por las métricas",
         "Precision y Recall son el corazón. Tómate 2 minutos extra si hace falta. "
         "El evaluador puede preguntar sobre esto."),
        ("GridSearchCV tarda y hay silencio incómodo",
         "Mientras ejecuta, explica qué está haciendo internamente. '¿Cuántas combinaciones calcula? "
         "4 × 3 = 12 configuraciones × 5 folds = 60 entrenamientos ahora mismo…'"),
        ("No conectar CV con Pipeline",
         "Explícitamente: 'Con Pipeline, cross-validation aplica el scaler correctamente en cada fold. "
         "Sin Pipeline, podrías estar cometiendo data leakage sin saberlo.'"),
    ]
    for err, sol in errores:
        e += [Paragraph(f"❌ {err}", s_warn),
              Paragraph(f"✅ Solución: {sol}", s_tip)]

    e.append(Spacer(1, 0.2*inch))

    e += [Paragraph("7. LO QUE NADIE TE DICE (PERO EL EVALUADOR VE)", s_h1), hr(),
          Paragraph("<b>Esta clase tiene el mayor potencial de impresionar Y el mayor riesgo de confundir.</b> "
                    "La diferencia está en las transiciones. Cada concepto nuevo debe conectarse explícitamente al anterior.", s_body),
          Paragraph("<b>Los números importan.</b> Cuando ejecutes GridSearchCV y veas best_score_=0.947, "
                    "no sigas. Di: '0.947 vs el 0.88 que teníamos antes — mejoramos 7 puntos. "
                    "Eso lo hizo el grid automáticamente.' El evaluador ve que interpretas, no solo ejecutas.", s_body),
          Paragraph("<b>La notación clf__ es un detalle que revela dominio.</b> "
                    "Si la explicas bien, el evaluador sabe que has trabajado con Pipelines de verdad.", s_body),
          Paragraph("<b>El ritmo de esta clase debe ser más ágil.</b> "
                    "4 conceptos en 45 min. Si te atasca en uno, perderás el resto. "
                    "Practica con reloj hasta que el timing sea natural.", s_body),
          Spacer(1, 0.2*inch)]

    e += [Paragraph("8. CHECKLIST FINAL — EL DÍA ANTERIOR", s_h1), hr(),
          Paragraph("□ Puedo explicar cross-validation dibujando los folds de memoria", s_body),
          Paragraph("□ Puedo calcular la confusion matrix manualmente para un ejemplo simple", s_body),
          Paragraph("□ Ejecuté GridSearchCV y sé interpretar best_params_, best_score_", s_body),
          Paragraph("□ Hice el Pipeline completo (scaler + clf) + GridSearchCV de una sola vez", s_body),
          Paragraph("□ Practiqué la explicación de clf__max_depth en voz alta", s_body),
          Paragraph("□ Cronometré la carrera completa: ±2 min de 45 min", s_body),
          Paragraph("□ Tengo backup (screenshots) de todos los demos por si Jupyter falla", s_body),
          Paragraph("□ Preparé la frase de cierre de memoria", s_body)]

    return e


# ─────────────────────────────────────────────────────────────────────────────
# GENERAR LOS 3 PDF
# ─────────────────────────────────────────────────────────────────────────────

OPCIONES = [
    ("opcion-1-visualizacion/doc/GUIA_opcion1_Visualizacion.pdf", guia_opcion1),
    ("opcion-2-ml-intro/doc/GUIA_opcion2_ML_Intro.pdf",          guia_opcion2),
    ("opcion-3-pipelines/doc/GUIA_opcion3_Pipelines.pdf",        guia_opcion3),
]

for path, fn in OPCIONES:
    doc = SimpleDocTemplate(path, pagesize=letter,
        rightMargin=0.75*inch, leftMargin=0.75*inch,
        topMargin=0.75*inch, bottomMargin=0.75*inch)
    doc.build(fn())
    print(f"[OK] {path}")

print("\n[OK] 3 guias PDF generadas")
