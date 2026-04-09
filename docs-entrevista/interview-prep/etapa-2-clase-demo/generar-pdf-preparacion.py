#!/usr/bin/env python3
"""
Generador de PDF: Guía de Preparación para enseñar Clase 11
Contiene todo lo que necesitas saber para dar la clase exitosamente
"""

import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer

# ============================================================================
# CONFIGURACIÓN
# ============================================================================

FILENAME = "GUIA_PREPARACION_Clase_11_Evaluacion_y_Pipelines.pdf"
TITLE = "Guía de Preparación — Clase 11: Evaluación y Pipelines"
AUTHOR = "Vladimir Acuña / Bootcamp Python DS"
CREATED = datetime.datetime.now().strftime("%d de %B de %Y")

# ============================================================================
# ESTILOS
# ============================================================================

styles = getSampleStyleSheet()

style_title = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=colors.HexColor('#0f3d3e'),
    spaceAfter=30,
    alignment=1,
)

style_h1 = ParagraphStyle(
    'CustomH1',
    parent=styles['Heading1'],
    fontSize=16,
    textColor=colors.HexColor('#0f3d3e'),
    spaceAfter=12,
    spaceBefore=12,
)

style_h2 = ParagraphStyle(
    'CustomH2',
    parent=styles['Heading2'],
    fontSize=13,
    textColor=colors.HexColor('#ff6b35'),
    spaceAfter=8,
    spaceBefore=8,
)

style_body = ParagraphStyle(
    'CustomBody',
    parent=styles['BodyText'],
    fontSize=10,
    spaceAfter=6,
    leading=14,
)

style_code = ParagraphStyle(
    'Code',
    parent=styles['Normal'],
    fontSize=8,
    fontName='Courier',
    leftIndent=20,
    spaceAfter=6,
)

# ============================================================================
# CONTENIDO DEL PDF
# ============================================================================

contenido = [
    # Portada
    Spacer(1, 1.5 * inch),
    Paragraph("GUÍA DE PREPARACIÓN", style_title),
    Paragraph("Clase 11: Evaluación y Pipelines", styles['Heading2']),
    Spacer(1, 0.5 * inch),
    Paragraph("Demostración Pedagógica — Etapa 2", styles['Normal']),
    Spacer(1, 0.3 * inch),
    Paragraph("Preparado por: Vladimir Acuña", styles['Normal']),
    Paragraph(f"Fecha: {CREATED}", styles['Normal']),
    PageBreak(),

    # ÍNDICE
    Paragraph("ÍNDICE", style_title),
    Paragraph("1. Descripción general de la clase", style_h2),
    Paragraph("2. Objetivos de aprendizaje", style_h2),
    Paragraph("3. Conceptos clave que debes dominar", style_h2),
    Paragraph("4. Estructura y timing de la clase", style_h2),
    Paragraph("5. Indicaciones para enseñar", style_h2),
    Paragraph("6. Ejemplos prácticos en vivo", style_h2),
    Paragraph("7. Respuestas a preguntas frecuentes", style_h2),
    Paragraph("8. Checklist de preparación", style_h2),
    PageBreak(),

    # DESCRIPCIÓN GENERAL
    Paragraph("1. DESCRIPCIÓN GENERAL DE LA CLASE", style_title),
    Paragraph("<b>Clase 11: Evaluación y Pipelines</b>", style_h1),
    Paragraph(
        "Esta es la penúltima clase del bootcamp. Los alumnos ya conocen algoritmos de ML "
        "(LinearRegression, DecisionTree, LogisticRegression). Ahora aprenderán a: "
        "(1) evaluarlos correctamente sin overfitting, "
        "(2) optimizar hiperparámetros automáticamente, "
        "(3) automatizar workflows con Pipelines.",
        style_body
    ),
    Spacer(1, 0.15 * inch),
    Paragraph("<b>Por qué es importante:</b>", style_h2),
    Paragraph(
        "• En producción NO puedes hacer train/test split simple — es muy propenso a overfitting.\n"
        "• GridSearchCV es el estándar de la industria para encontrar hiperparámetros óptimos.\n"
        "• Pipelines evitan errores comunes (olvidar normalizar, fitear dos veces, etc.).\n"
        "• Un modelo bien evaluado es más confiable que uno con 'accuracy alto'.",
        style_body
    ),
    Spacer(1, 0.2 * inch),

    # OBJETIVOS
    Paragraph("2. OBJETIVOS DE APRENDIZAJE", style_title),
    Paragraph("Al finalizar la clase, los alumnos serán capaces de:", style_h2),
    Paragraph(
        "□ Entender por qué el train/test split simple puede ser insuficiente (overfitting).\n"
        "□ Implementar cross-validation (k-fold) correctamente.\n"
        "□ Interpretar y usar métricas: Precision, Recall, F1, ROC-AUC.\n"
        "□ Usar GridSearchCV para automatizar la búsqueda de hiperparámetros.\n"
        "□ Construir Pipelines para encadenar pasos de preprocesamiento y modelado.\n"
        "□ Aplicar todo esto en un ejercicio práctico real.",
        style_body
    ),
    PageBreak(),

    # CONCEPTOS CLAVE
    Paragraph("3. CONCEPTOS CLAVE QUE DEBES DOMINAR", style_title),

    Paragraph("3.1 OVERFITTING", style_h1),
    Paragraph(
        "Train accuracy: 95% | Test accuracy: 62%<br/>"
        "Esto significa que el modelo 'aprendió de memoria' el training set "
        "pero no generaliza a datos nuevos.",
        style_body
    ),
    Paragraph(
        "<b>Causas comunes:</b><br/>"
        "• Modelo muy complejo (ej: árbol muy profundo)<br/>"
        "• Pocos datos de entrenamiento<br/>"
        "• Falta de regularización",
        style_body
    ),
    Paragraph(
        "<b>Cómo detectarlo:</b><br/>"
        "• training_score >> test_score (gap grande)<br/>"
        "• Graficar learning curves (entrenamiento baja, validación no mejora)",
        style_body
    ),
    Spacer(1, 0.15 * inch),

    Paragraph("3.2 CROSS-VALIDATION (K-FOLD)", style_h1),
    Paragraph(
        "Divide el dataset en k partes (típicamente k=5). "
        "Itera k veces: usa k-1 partes para entrenar, 1 para validar. "
        "Retorna promedio de k scores → estimación más confiable.",
        style_body
    ),
    Paragraph(
        "<b>Ventaja sobre train/test simple:</b><br/>"
        "• Usa más datos para entrenamiento en cada fold<br/>"
        "• Cada muestra se usa para validación exactamente una vez<br/>"
        "• Reducción de varianza en el score estimado",
        style_body
    ),
    Spacer(1, 0.15 * inch),

    Paragraph("3.3 CONFUSION MATRIX", style_h1),
    Paragraph(
        "En clasificación binaria, hay 4 casos posibles:<br/>"
        "<br/>"
        "TN (Verdadero Negativo): Predije No, era No ✓<br/>"
        "TP (Verdadero Positivo): Predije Sí, era Sí ✓<br/>"
        "FP (Falso Positivo): Predije Sí, era No ✗ (error tipo 1)<br/>"
        "FN (Falso Negativo): Predije No, era Sí ✗ (error tipo 2)<br/>",
        style_body
    ),
    Paragraph(
        "<b>Importante:</b> El tipo de error depende del contexto.\n"
        "Diagnóstico médico: FN es peligroso (paciente enfermo sin detectar).\n"
        "Spam detection: FP es costoso (email importante marcado como spam).",
        style_body
    ),
    Spacer(1, 0.15 * inch),

    Paragraph("3.4 MÉTRICAS: PRECISION, RECALL, F1", style_h1),
    Paragraph(
        "Precision = TP / (TP + FP) → de los que predije Sí, cuántos eran correctos<br/>"
        "Recall = TP / (TP + FN) → de los Sí reales, cuántos atrapé<br/>"
        "F1 = 2 × (P × R) / (P + R) → media armónica (balance P y R)<br/>",
        style_body
    ),
    Paragraph(
        "<b>Cuándo usar cada una:</b><br/>"
        "• Precision: falsos positivos son caros (ej: ads targeting)<br/>"
        "• Recall: falsos negativos son caros (ej: detección fraude)<br/>"
        "• F1: ambos errores importan igual",
        style_body
    ),
    Spacer(1, 0.15 * inch),

    Paragraph("3.5 GRIDSEARCHCV", style_h1),
    Paragraph(
        "Prueba automáticamente TODAS las combinaciones de hiperparámetros "
        "que especifiques. Usa cross-validation internamente. Retorna los mejores parámetros.",
        style_body
    ),
    Paragraph(
        "<b>Ejemplo:</b> Si especificas max_depth=[3,5,7,10] y min_samples_split=[2,5,10], "
        "GridSearchCV prueba 4 × 3 = 12 combinaciones × 5 folds = 60 entrenamientos.",
        style_body
    ),
    Spacer(1, 0.15 * inch),

    Paragraph("3.6 PIPELINES", style_h1),
    Paragraph(
        "Encadena pasos de preprocesamiento + modelo en un único objeto. "
        "Ventajas:<br/>"
        "• Código limpio y reproducible<br/>"
        "• Evita errores comunes (normalizar test con stats de train)<br/>"
        "• Compatible con GridSearchCV",
        style_body
    ),
    PageBreak(),

    # ESTRUCTURA Y TIMING
    Paragraph("4. ESTRUCTURA Y TIMING DE LA CLASE", style_title),
    Paragraph(
        "Total: 90 minutos aproximadamente<br/>"
        "<br/>"
        "00:00 — 05:00 (5 min): Apertura + Agenda<br/>"
        "         ¿Qué aprenderemos hoy? ¿Por qué es importante?<br/>"
        "<br/>"
        "05:00 — 15:00 (10 min): Problema del overfitting<br/>"
        "         Dibuja gráficos de learning curves. Muestra ejemplos reales.<br/>"
        "<br/>"
        "15:00 — 25:00 (10 min): Cross-Validation<br/>"
        "         Explicación + código simple en Jupyter.<br/>"
        "<br/>"
        "25:00 — 35:00 (10 min): Métricas (Confusion Matrix, Precision, Recall)<br/>"
        "         Usa casos clínicos (diagnóstico) para intuición.<br/>"
        "<br/>"
        "35:00 — 45:00 (10 min): GridSearchCV<br/>"
        "         Demostración interactiva. Explica qué está pasando 'bajo el capó'.<br/>"
        "<br/>"
        "45:00 — 60:00 (15 min): Pipelines<br/>"
        "         Código paso a paso. Muestra por qué es mejor que hacer todo manual.<br/>"
        "<br/>"
        "60:00 — 75:00 (15 min): Ejercicio en vivo con dataset Iris<br/>"
        "         Los alumnos escriben conmigo. Puedes ir más lento.<br/>"
        "<br/>"
        "75:00 — 85:00 (10 min): Resumen + preguntas<br/>"
        "<br/>"
        "85:00 — 90:00 (5 min): Vista previa de Clase 12 (Proyecto Final)",
        style_body
    ),
    PageBreak(),

    # INDICACIONES
    Paragraph("5. INDICACIONES PARA ENSEÑAR", style_title),

    Paragraph("5.1 ENERGÍA Y TONO", style_h2),
    Paragraph(
        "• Abre con energía. Esta es la penúltima clase — genera entusiasmo.<br/>"
        "• Mantén un tono conversacional. No leas slides, úsalos como guía.<br/>"
        "• Haz pausas. Deja tiempo para que asimilen.<br/>"
        "• Sonríe. Los alumnos captan tu genuino interés por enseñar.",
        style_body
    ),
    Spacer(1, 0.1 * inch),

    Paragraph("5.2 EJEMPLOS CONCRETOS", style_h2),
    Paragraph(
        "• No importa si es teórico, debe tener un contexto real.<br/>"
        "• Precision/Recall: usa diagnóstico médico (intuitive).<br/>"
        "• Overfitting: dibuja en la pizarra dos curvas (train vs test).<br/>"
        "• Pipelines: muestra el 'antes y después' (manual vs Pipeline).",
        style_body
    ),
    Spacer(1, 0.1 * inch),

    Paragraph("5.3 DEMOSTRACIÓN EN VIVO", style_h2),
    Paragraph(
        "• Ejecuta todo en Jupyter. Los alumnos ven los resultados en tiempo real.<br/>"
        "• Si cometes un error, corrígelo en vivo. Muestra que es normal.<br/>"
        "• Habla mientras codeas ('Ahora estoy creando el grid con estos valores...').<br/>"
        "• Deja los outputs visibles — son la prueba de que funciona.",
        style_body
    ),
    Spacer(1, 0.1 * inch),

    Paragraph("5.4 INTERACTIVIDAD", style_h2),
    Paragraph(
        "• Haz preguntas retóricas. ('¿Qué creen que pasaría si...?')<br/>"
        "• Pide a alumnos que predigan resultados antes de ejecutar código.<br/>"
        "• Ejercicio en vivo: que escriban conmigo, no que solo miren.<br/>"
        "• Deja espacios para preguntas. No tengas miedo del silencio.",
        style_body
    ),
    Spacer(1, 0.1 * inch),

    Paragraph("5.5 GESTIÓN DEL TIEMPO", style_h2),
    Paragraph(
        "• Si vas lento en conceptos, acorta el ejercicio al final.<br/>"
        "• Si vas rápido, expande preguntas y casos de uso.<br/>"
        "• Cuenta con que Jupyter puede ser lento — ten código preparado de backup.<br/>"
        "• Si algo falla (error en código), muestra cómo debuggear (error > solución).",
        style_body
    ),
    PageBreak(),

    # EJEMPLOS PRÁCTICOS
    Paragraph("6. EJEMPLOS PRÁCTICOS EN VIVO", style_title),

    Paragraph("6.1 CROSS-VALIDATION", style_h2),
    Paragraph("Código a ejecutar:", style_h2),
    Paragraph(
        "from sklearn.datasets import load_iris<br/>"
        "from sklearn.model_selection import cross_val_score<br/>"
        "from sklearn.tree import DecisionTreeClassifier<br/>"
        "<br/>"
        "X, y = load_iris(return_X_y=True)<br/>"
        "clf = DecisionTreeClassifier()<br/>"
        "scores = cross_val_score(clf, X, y, cv=5)<br/>"
        "<br/>"
        "print(f'Scores: {scores}')<br/>"
        "print(f'Media: {scores.mean():.3f}')<br/>"
        "print(f'Std: {scores.std():.3f}')",
        style_code
    ),
    Paragraph(
        "Resultado esperado: 5 scores (uno por fold) + media ~0.95 + std ~0.02",
        style_body
    ),
    Spacer(1, 0.15 * inch),

    Paragraph("6.2 CLASSIFICATION_REPORT", style_h2),
    Paragraph("Código a ejecutar:", style_h2),
    Paragraph(
        "from sklearn.model_selection import train_test_split<br/>"
        "from sklearn.metrics import classification_report<br/>"
        "<br/>"
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)<br/>"
        "clf = DecisionTreeClassifier()<br/>"
        "clf.fit(X_train, y_train)<br/>"
        "<br/>"
        "y_pred = clf.predict(X_test)<br/>"
        "print(classification_report(y_test, y_pred))",
        style_code
    ),
    Spacer(1, 0.15 * inch),

    Paragraph("6.3 GRIDSEARCHCV", style_h2),
    Paragraph("Código a ejecutar:", style_h2),
    Paragraph(
        "from sklearn.model_selection import GridSearchCV<br/>"
        "<br/>"
        "param_grid = {<br/>"
        "    'max_depth': [3, 5, 7, 10],<br/>"
        "    'min_samples_split': [2, 5, 10]<br/>"
        "}<br/>"
        "<br/>"
        "grid = GridSearchCV(DecisionTreeClassifier(), param_grid, cv=5)<br/>"
        "grid.fit(X_train, y_train)<br/>"
        "<br/>"
        "print(f'Mejores parámetros: {grid.best_params_}')<br/>"
        "print(f'Mejor score: {grid.best_score_:.3f}')",
        style_code
    ),
    Spacer(1, 0.15 * inch),

    Paragraph("6.4 PIPELINES", style_h2),
    Paragraph("Código a ejecutar:", style_h2),
    Paragraph(
        "from sklearn.pipeline import Pipeline<br/>"
        "from sklearn.preprocessing import StandardScaler<br/>"
        "from sklearn.decomposition import PCA<br/>"
        "from sklearn.linear_model import LogisticRegression<br/>"
        "<br/>"
        "pipe = Pipeline([<br/>"
        "    ('scaler', StandardScaler()),<br/>"
        "    ('pca', PCA()),<br/>"
        "    ('clf', LogisticRegression())<br/>"
        "])<br/>"
        "<br/>"
        "param_grid = {'pca__n_components': [2, 5, 10]}<br/>"
        "grid = GridSearchCV(pipe, param_grid, cv=5)<br/>"
        "grid.fit(X_train, y_train)",
        style_code
    ),
    Paragraph(
        "Nota: Usa 'pca__n_components' (con __ doble) para acceder parámetros de pasos dentro del Pipeline.",
        style_body
    ),
    PageBreak(),

    # FAQ
    Paragraph("7. RESPUESTAS A PREGUNTAS FRECUENTES", style_title),

    Paragraph("<b>P: ¿Cuántos folds debo usar en cross-validation?</b>", style_h2),
    Paragraph(
        "R: Típicamente 5 o 10. Con menos datos, usa 5. Con mucho volumen, 10 está bien. "
        "No hay regla estricta — varía según contexto.",
        style_body
    ),
    Spacer(1, 0.1 * inch),

    Paragraph("<b>P: ¿GridSearchCV es lento?</b>", style_h2),
    Paragraph(
        "R: Sí, prueba muchas combinaciones. Usa n_jobs=-1 para paralelizar. "
        "Si aún es lento, reduce el grid (menos hiperparámetros a probar).",
        style_body
    ),
    Spacer(1, 0.1 * inch),

    Paragraph("<b>P: ¿Pipeline es solo para clasificación?</b>", style_h2),
    Paragraph(
        "R: No, funciona igual para regresión. La diferencia es el estimador final (Classifier vs Regressor).",
        style_body
    ),
    Spacer(1, 0.1 * inch),

    Paragraph("<b>P: Si train_score = 0.95 y cross_val_score = 0.88, ¿estoy overfitting?</b>", style_h2),
    Paragraph(
        "R: Un poco, pero es normal. Una diferencia de 7% es aceptable. Si fuera 20%+, ahí sí preocúpate.",
        style_body
    ),
    Spacer(1, 0.1 * inch),

    Paragraph("<b>P: ¿Debo usar ROC-AUC o F1?</b>", style_h2),
    Paragraph(
        "R: ROC-AUC es mejor si tu dataset está desbalanceado. F1 si clases están balanceadas. "
        "Lo ideal: reporta ambas.",
        style_body
    ),
    PageBreak(),

    # CHECKLIST
    Paragraph("8. CHECKLIST DE PREPARACIÓN", style_title),
    Paragraph(
        "□ Leí esta guía completa<br/>"
        "□ Entiendo los 6 conceptos clave (overfitting, CV, confusion matrix, métricas, GridSearchCV, Pipelines)<br/>"
        "□ Practiqué los 4 ejemplos de código en mi máquina<br/>"
        "□ Tengo Jupyter abierto con Iris dataset precargado<br/>"
        "□ Preparé ejemplos alternativos por si algo falla<br/>"
        "□ Leí las indicaciones de enseñanza (energía, ejemplos, timing)<br/>"
        "□ Estoy preparado para responder preguntas (sección FAQ)<br/>"
        "□ Duración total: 90 minutos (seguir el timing)<br/>"
        "□ Tengo agua/descanso previsto<br/>"
        "□ La clase tiene un final claro (resumen + proyección a Clase 12)",
        style_body
    ),
    Spacer(1, 0.3 * inch),

    Paragraph("¡ÉXITO EN TU DEMOSTRACIÓN!", style_title),
    Paragraph(
        "Recuerda: no se trata de ser perfecto. Se trata de demostrar que sabes enseñar "
        "con claridad, paciencia, y genuino interés por que tus alumnos aprendan. "
        "¡Confía en tu preparación!",
        styles['Normal']
    ),
]

# ============================================================================
# GENERAR PDF
# ============================================================================

doc = SimpleDocTemplate(
    FILENAME,
    pagesize=letter,
    rightMargin=0.75 * inch,
    leftMargin=0.75 * inch,
    topMargin=0.75 * inch,
    bottomMargin=0.75 * inch,
)

doc.build(contenido)
print(f"[OK] PDF generado: {FILENAME}")
