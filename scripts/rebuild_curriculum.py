"""Genera y sincroniza el contenido estructural del plan de clases del bootcamp.

Este script resuelve la consistencia entre el catálogo docente, los markdown de
cada clase y los datos que consume la app móvil. Cuando cambia el plan de
clases, aquí se actualiza la fuente única para evitar divergencias.
"""

from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
CLASSES_DIR = BASE_DIR / "classes"
MOBILE_PATH = BASE_DIR / "mobile" / "src" / "data" / "classes.js"


CURRICULUM = [
    {
        "slug": "00-diagnostico-inicial",
        "number": 0,
        "icon": "\U0001F9ED",
        "title": "Diagn\u00f3stico inicial y orientaci\u00f3n",
        "description": "Prueba diagn\u00f3stica de 30 preguntas para estimar la base t\u00e9cnica del grupo y ordenar el arranque del bootcamp.",
        "duration": "15 minutos",
        "duration_short": "15 min",
        "level": "Diagn\u00f3stico",
        "objective": "Estimar el punto de partida del grupo antes de iniciar la ruta formal del bootcamp.",
        "dataset": "No requiere dataset.",
        "topics": ["Python b\u00e1sico", "Lectura de tablas", "Gr\u00e1ficos", "Modelado inicial", "H\u00e1bitos de trabajo"],
        "outcomes": ["Identificar fortalezas iniciales.", "Detectar vac\u00edos de apoyo.", "Alinear expectativas del recorrido."],
        "idea": "Diagn\u00f3stico breve, retroalimentaci\u00f3n inmediata y acuerdo sobre la ruta de aprendizaje.",
        "note": "Usa el resultado para ajustar ritmo, apoyos y ejemplos de las primeras clases.",
        "why": "Permite decidir desde d\u00f3nde conviene partir y qu\u00e9 apoyos necesita cada estudiante.",
        "block_title": "Lectura del resultado diagn\u00f3stico",
        "block_intro": "La meta no es etiquetar al estudiante, sino traducir el resultado en una ruta de trabajo concreta.",
        "schema": "resultado \u2192 lectura por \u00e1rea \u2192 acci\u00f3n de apoyo",
        "purpose": "Sirve para priorizar repaso, nivelar expectativas y organizar el acompa\u00f1amiento docente desde la primera semana.",
        "code": None,
        "next": "La siguiente parada es la clase 01: Fundamentos de Python aplicados a datos.",
    },
    {
        "slug": "01-python-fundamentos",
        "number": 1,
        "icon": "\U0001F4D8",
        "title": "Fundamentos de Python aplicados a datos",
        "description": "Variables, tipos, estructuras y control de flujo aplicados a datos simples.",
        "duration": "90 minutos",
        "duration_short": "90 min",
        "level": "B\u00e1sico",
        "objective": "Comprender los elementos b\u00e1sicos de Python y aplicarlos a ejemplos peque\u00f1os relacionados con datos.",
        "dataset": "datasets/ventas_tienda.csv",
        "topics": ["Variables y tipos", "Listas y diccionarios", "Funciones", "Control de flujo"],
        "outcomes": ["Crear variables claras y expresivas.", "Usar listas y diccionarios para representar informaci\u00f3n.", "Escribir funciones simples con prop\u00f3sito evidente."],
        "idea": "Python se presenta como herramienta para ordenar y transformar informaci\u00f3n, no como teor\u00eda abstracta.",
        "note": "Modela en voz alta c\u00f3mo leer un error simple y convertirlo en una acci\u00f3n concreta.",
        "why": "Es la base para que el estudiante pueda leer, modificar y comentar c\u00f3digo con confianza.",
        "block_title": "Funci\u00f3n para calcular ingreso bruto",
        "block_intro": "Encapsular una operaci\u00f3n en una funci\u00f3n evita repetir l\u00f3gica y facilita explicar cada paso.",
        "schema": "entrada \u2192 calcular \u2192 devolver \u2192 reutilizar",
        "purpose": "Sirve para introducir reutilizaci\u00f3n, par\u00e1metros y retorno usando un ejemplo cercano al an\u00e1lisis de ventas.",
        "code": """def calcular_total_bruto(unidades, precio_unitario):
    # Multiplicamos cantidad por precio para estimar el ingreso bruto.
    return unidades * precio_unitario


ventas = [
    {"producto": "Mouse", "unidades": 3, "precio_unitario": 8990},
    {"producto": "Teclado", "unidades": 2, "precio_unitario": 15990},
]

totales = [calcular_total_bruto(v["unidades"], v["precio_unitario"]) for v in ventas]
print(totales)""",
        "next": "La clase 02 traslada estas bases a tablas con pandas.",
    },
    {
        "slug": "02-pandas-limpieza-datos",
        "number": 2,
        "icon": "\U0001F9F9",
        "title": "Pandas y limpieza de datos",
        "description": "Carga de CSV, inspecci\u00f3n inicial y limpieza de tablas para preparar an\u00e1lisis confiables.",
        "duration": "90 minutos",
        "duration_short": "90 min",
        "level": "B\u00e1sico",
        "objective": "Usar pandas para cargar, inspeccionar y limpiar tablas antes de analizarlas.",
        "dataset": "datasets/ventas_tienda.csv",
        "topics": ["DataFrame", "Inspecci\u00f3n inicial", "Nulos", "Estandarizaci\u00f3n b\u00e1sica"],
        "outcomes": ["Cargar un CSV y revisar su estructura.", "Detectar problemas simples de calidad.", "Aplicar limpiezas justificadas y documentadas."],
        "idea": "No se analiza una tabla seria sin inspeccionarla y documentar primero sus problemas.",
        "note": "Haz expl\u00edcita la diferencia entre limpiar por costumbre y limpiar con criterio.",
        "why": "Pandas es la puerta de entrada al trabajo real con datos tabulares y a la toma de decisiones sobre calidad.",
        "block_title": "Carga e inspecci\u00f3n de un CSV",
        "block_intro": "El primer paso no es graficar: es entender qu\u00e9 columnas existen, c\u00f3mo vienen escritas y si podemos confiar en ellas.",
        "schema": "cargar \u2192 inspeccionar \u2192 limpiar \u2192 verificar",
        "purpose": "Sirve para instalar una rutina m\u00ednima de calidad antes de cualquier an\u00e1lisis o visualizaci\u00f3n.",
        "code": """import pandas as pd

df = pd.read_csv("datasets/ventas_tienda.csv")

# Revisamos primeras filas, tipos y valores faltantes antes de seguir.
print(df.head())
print(df.info())
print(df.isna().sum())

# Ejemplo simple de limpieza visible.
df["medio_pago"] = df["medio_pago"].str.strip()""",
        "next": "La clase 03 usa tablas m\u00e1s confiables para explorar patrones visuales.",
    },
    {
        "slug": "03-visualizacion-exploratoria",
        "number": 3,
        "icon": "\U0001F4CA",
        "title": "Visualizaci\u00f3n exploratoria",
        "description": "Gr\u00e1ficos iniciales para describir patrones, comparar categor\u00edas y abrir preguntas de an\u00e1lisis.",
        "duration": "90 minutos",
        "duration_short": "90 min",
        "level": "B\u00e1sico",
        "objective": "Usar visualizaciones exploratorias para describir patrones y abrir nuevas preguntas de an\u00e1lisis.",
        "dataset": "datasets/ventas_tienda.csv",
        "topics": ["Agrupaci\u00f3n", "Barras", "Lectura visual", "Preguntas exploratorias"],
        "outcomes": ["Construir un resumen por categor\u00eda o sucursal.", "Elegir un gr\u00e1fico simple y legible.", "Explicar qu\u00e9 pregunta responde la visualizaci\u00f3n."],
        "idea": "La visualizaci\u00f3n exploratoria ayuda a mirar mejor y a formular preguntas m\u00e1s \u00fatiles.",
        "note": "Insiste en que un gr\u00e1fico no reemplaza la pregunta: la hace visible.",
        "why": "El estudiante necesita aprender a comparar categor\u00edas y detectar patrones antes de avanzar a an\u00e1lisis m\u00e1s complejos.",
        "block_title": "Ventas netas por categor\u00eda",
        "block_intro": "Antes de graficar conviene preparar un resumen que reduzca el ruido de filas individuales.",
        "schema": "calcular m\u00e9trica \u2192 agrupar \u2192 ordenar \u2192 graficar",
        "purpose": "Sirve para mostrar c\u00f3mo un gr\u00e1fico nace de una decisi\u00f3n previa de agregaci\u00f3n y no de un clic autom\u00e1tico.",
        "code": """import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/ventas_tienda.csv")
df["total_neto"] = df["unidades"] * df["precio_unitario"] * (1 - df["descuento_pct"])

resumen = (
    df.groupby("categoria", as_index=False)["total_neto"]
    .sum()
    .sort_values("total_neto", ascending=False)
)

plt.figure(figsize=(8, 4))
plt.bar(resumen["categoria"], resumen["total_neto"])
plt.title("Ventas netas por categor\u00eda")
plt.ylabel("CLP")
plt.xticks(rotation=20)
plt.tight_layout()""",
        "next": "La clase 04 profundiza en c\u00f3mo resumir datos con medidas descriptivas.",
    },
    {
        "slug": "04-estadistica-descriptiva",
        "number": 4,
        "icon": "\U0001F4D0",
        "title": "Estad\u00edstica descriptiva",
        "description": "Medidas descriptivas para resumir variables y sostener interpretaciones b\u00e1sicas.",
        "duration": "90 minutos",
        "duration_short": "90 min",
        "level": "B\u00e1sico",
        "objective": "Interpretar medidas descriptivas simples y relacionarlas con preguntas reales.",
        "dataset": "datasets/estudiantes.csv",
        "topics": ["Media", "Mediana", "Dispersi\u00f3n", "Interpretaci\u00f3n"],
        "outcomes": ["Calcular medidas de tendencia central.", "Leer una dispersi\u00f3n b\u00e1sica sin perder contexto.", "Evitar conclusiones apoyadas en un solo n\u00famero."],
        "idea": "La estad\u00edstica descriptiva resume poblaciones, pero siempre debe volver a una pregunta concreta.",
        "note": "Haz que el grupo compare media y mediana con lenguaje simple antes de pasar a f\u00f3rmulas.",
        "why": "Permite pasar de mirar filas sueltas a resumir comportamientos de un grupo con criterio.",
        "block_title": "Resumen de asistencia del curso",
        "block_intro": "Usar varias medidas a la vez evita depender de un \u00fanico n\u00famero y mejora la interpretaci\u00f3n.",
        "schema": "seleccionar variable \u2192 calcular resumen \u2192 interpretar",
        "purpose": "Sirve para conectar conceptos estad\u00edsticos con decisiones pedag\u00f3gicas o de seguimiento acad\u00e9mico.",
        "code": """import pandas as pd

df = pd.read_csv("datasets/estudiantes.csv")
asistencia = df["asistencia_pct"]

print("Media:", asistencia.mean())
print("Mediana:", asistencia.median())
print("Desviaci\u00f3n est\u00e1ndar:", asistencia.std())
print(asistencia.describe())""",
        "next": "La clase 05 convierte estos res\u00famenes en gr\u00e1ficos m\u00e1s controlados con matplotlib.",
    },
    {
        "slug": "05-visualizacion-con-matplotlib",
        "number": 5,
        "icon": "\U0001F3A8",
        "title": "Visualizaci\u00f3n con matplotlib",
        "description": "Construcci\u00f3n de gr\u00e1ficos m\u00e1s controlados y legibles usando matplotlib.",
        "duration": "90 minutos",
        "duration_short": "90 min",
        "level": "Intermedio",
        "objective": "Crear gr\u00e1ficos m\u00e1s controlados con matplotlib y mejorar su legibilidad.",
        "dataset": "datasets/retencion_clientes.csv",
        "topics": ["Figure y axes", "Rotulado", "Legibilidad", "Ajuste visual"],
        "outcomes": ["Crear una figura expl\u00edcita con tama\u00f1o controlado.", "Rotular ejes y t\u00edtulos con intenci\u00f3n.", "Mejorar la lectura visual de un gr\u00e1fico temporal."],
        "idea": "No basta con que el gr\u00e1fico funcione: debe poder leerse sin fricci\u00f3n.",
        "note": "Haz comparar un gr\u00e1fico improvisado con otro bien rotulado para que la mejora sea visible.",
        "why": "Matplotlib permite controlar detalle visual y comunicar mejor una conclusi\u00f3n.",
        "block_title": "Serie temporal de clientes activos",
        "block_intro": "Crear una figura expl\u00edcita permite controlar tama\u00f1o, etiquetas y orden visual con intenci\u00f3n.",
        "schema": "crear figura \u2192 dibujar \u2192 rotular \u2192 ajustar",
        "purpose": "Sirve para pasar de una visualizaci\u00f3n funcional a una visualizaci\u00f3n comunicable.",
        "code": """import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/retencion_clientes.csv")

fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(df["mes"], df["clientes_activos"], marker="o", linewidth=2)
ax.set_title("Clientes activos por mes")
ax.set_xlabel("Mes")
ax.set_ylabel("Clientes activos")
ax.tick_params(axis="x", rotation=45)
ax.grid(alpha=0.2)
plt.tight_layout()""",
        "next": "La clase 06 ampl\u00eda el repertorio con texto, fechas y transformaciones.",
    },
    {
        "slug": "06-texto-fechas-y-transformaciones",
        "number": 6,
        "icon": "\U0001F5D3\uFE0F",
        "title": "Texto, fechas y transformaciones",
        "description": "Transformaci\u00f3n de columnas de texto y fecha para hacerlas \u00fatiles en an\u00e1lisis y modelado inicial.",
        "duration": "90 minutos",
        "duration_short": "90 min",
        "level": "Intermedio",
        "objective": "Transformar columnas de texto y fecha para volverlas \u00fatiles en an\u00e1lisis y modelado inicial.",
        "dataset": "datasets/ventas_tienda.csv",
        "topics": ["Fechas", "Texto", "Columnas derivadas", "Normalizaci\u00f3n"],
        "outcomes": ["Convertir una columna a fecha real.", "Crear variables derivadas con sentido anal\u00edtico.", "Normalizar texto para evitar duplicados de categor\u00eda."],
        "idea": "Muchas preguntas nuevas aparecen cuando una columna se transforma bien.",
        "note": "Pide siempre que el grupo diga para qu\u00e9 sirve la nueva columna antes de crearla.",
        "why": "Las transformaciones abren preguntas m\u00e1s \u00fatiles y preparan mejor la base de trabajo.",
        "block_title": "Fechas y texto listos para analizar",
        "block_intro": "Convertir y normalizar columnas no es maquillaje: cambia lo que se puede preguntar despu\u00e9s.",
        "schema": "convertir \u2192 derivar \u2192 normalizar \u2192 reutilizar",
        "purpose": "Sirve para preparar columnas que luego alimentan gr\u00e1ficos, filtros o variables de modelado.",
        "code": """import pandas as pd

df = pd.read_csv("datasets/ventas_tienda.csv")
df["fecha"] = pd.to_datetime(df["fecha"])

# Creamos columnas nuevas para responder preguntas posteriores.
df["mes"] = df["fecha"].dt.to_period("M").astype(str)
df["dia_semana"] = df["fecha"].dt.day_name()
df["producto_normalizado"] = df["producto"].str.strip().str.lower()

print(df[["fecha", "mes", "dia_semana", "producto_normalizado"]].head())""",
        "next": "La clase 07 usa estas habilidades dentro de un mini proyecto guiado.",
    },
    {
        "slug": "07-mini-proyecto-guiado",
        "number": 7,
        "icon": "\U0001F9E9",
        "title": "Mini proyecto guiado",
        "description": "Integraci\u00f3n guiada de lectura, limpieza, an\u00e1lisis y comunicaci\u00f3n en una sola secuencia corta.",
        "duration": "90 minutos",
        "duration_short": "90 min",
        "level": "Integrador",
        "objective": "Integrar las habilidades vistas hasta ahora en un mini proyecto guiado de principio a fin.",
        "dataset": "datasets/ventas_tienda.csv",
        "topics": ["Pregunta de an\u00e1lisis", "Recorte", "Secuencia de trabajo", "Evidencia"],
        "outcomes": ["Formular una pregunta concreta de proyecto.", "Armar una base de trabajo con columnas \u00fatiles.", "Seguir una secuencia coherente de an\u00e1lisis."],
        "idea": "El proyecto ordena t\u00e9cnicas sueltas dentro de un proceso con sentido.",
        "note": "Haz visible la pregunta central durante toda la sesi\u00f3n para evitar que el grupo se disperse.",
        "why": "Este m\u00f3dulo ayuda a unir an\u00e1lisis, limpieza y visualizaci\u00f3n en un flujo coherente y comunicable.",
        "block_title": "Definici\u00f3n de pregunta y base de trabajo",
        "block_intro": "Antes de calcular, conviene dejar escrita la pregunta y recortar solo las columnas necesarias.",
        "schema": "pregunta \u2192 recorte \u2192 base de trabajo \u2192 an\u00e1lisis",
        "purpose": "Sirve para evitar notebooks dispersos y para mostrar que el proyecto comienza delimitando el problema.",
        "code": """import pandas as pd

df = pd.read_csv("datasets/ventas_tienda.csv")
df["total_neto"] = df["unidades"] * df["precio_unitario"] * (1 - df["descuento_pct"])

pregunta = "\u00bfQu\u00e9 categor\u00eda concentra mayor ingreso neto?"
columnas = ["fecha", "sucursal", "categoria", "producto", "medio_pago", "total_neto"]
proyecto = df[columnas].copy()

print(pregunta)
print(proyecto.head())""",
        "next": "La clase 08 convierte ese trabajo en una presentaci\u00f3n breve de hallazgos.",
    },
    {
        "slug": "08-presentacion-de-hallazgos",
        "number": 8,
        "icon": "\U0001F5E3\uFE0F",
        "title": "Presentaci\u00f3n de hallazgos",
        "description": "Traducci\u00f3n de resultados t\u00e9cnicos a mensajes cortos, claros y defendibles.",
        "duration": "90 minutos",
        "duration_short": "90 min",
        "level": "Integrador",
        "objective": "Transformar resultados t\u00e9cnicos en una historia corta, clara y defendible.",
        "dataset": "Reutiliza el dataset del mini proyecto o uno equivalente del bootcamp.",
        "topics": ["Storytelling con datos", "Resumen ejecutivo", "Mensajes clave", "Visuales de apoyo"],
        "outcomes": ["Ordenar una historia de an\u00e1lisis.", "Elegir visuales que sostengan un mensaje.", "Escribir conclusiones ejecutivas sin perder rigor."],
        "idea": "La calidad del an\u00e1lisis tambi\u00e9n depende de c\u00f3mo se explica y a qui\u00e9n se dirige.",
        "note": "Haz ensayar respuestas a la pregunta: \u00ab\u00bfpor qu\u00e9 esto importa?\u00bb.",
        "why": "Sin una traducci\u00f3n clara, un buen an\u00e1lisis pierde impacto frente a docentes, alumnos o stakeholders.",
        "block_title": "Resumen ejecutivo en tres l\u00edneas",
        "block_intro": "No todo hallazgo se comunica con un gr\u00e1fico; a veces conviene escribir un mensaje breve y accionable.",
        "schema": "hallazgo \u2192 evidencia \u2192 recomendaci\u00f3n",
        "purpose": "Sirve para entrenar una salida ejecutiva que conecte el dato con una decisi\u00f3n posible.",
        "code": """hallazgo = "La categor\u00eda Accesorios concentra el mayor ingreso neto del periodo."
evidencia = "El resumen por categor\u00eda la ubica en el primer lugar del ranking."
recomendacion = "Conviene revisar margen, stock y campa\u00f1as antes de ampliar la oferta."

print(hallazgo)
print(evidencia)
print(recomendacion)""",
        "next": "La clase 09 introduce modelado predictivo como extensi\u00f3n del an\u00e1lisis.",
    },
    {
        "slug": "09-machine-learning-intro",
        "number": 9,
        "icon": "\U0001F916",
        "title": "Introducci\u00f3n a machine learning",
        "description": "Primer acercamiento a aprendizaje supervisado usando un problema de regresi\u00f3n simple.",
        "duration": "90 minutos",
        "duration_short": "90 min",
        "level": "Intermedio avanzado",
        "objective": "Comprender qu\u00e9 es un modelo supervisado y construir una primera regresi\u00f3n simple con scikit-learn.",
        "dataset": "datasets/estudiantes.csv",
        "topics": ["X e y", "Train/test split", "Regresi\u00f3n", "Predicci\u00f3n"],
        "outcomes": ["Distinguir variables de entrada y objetivo.", "Construir un train/test split reproducible.", "Entrenar una regresi\u00f3n simple y revisar sus predicciones."],
        "idea": "Machine learning se presenta como una extensi\u00f3n del an\u00e1lisis, no como magia negra.",
        "note": "Vuelve siempre a la pregunta predictiva antes de mencionar el modelo.",
        "why": "Ayuda a entender c\u00f3mo un conjunto de variables puede apoyar una predicci\u00f3n supervisada b\u00e1sica.",
        "block_title": "Primera regresi\u00f3n con variables acad\u00e9micas",
        "block_intro": "Antes de entrenar, conviene declarar con claridad qu\u00e9 queremos predecir y qu\u00e9 datos usaremos como entrada.",
        "schema": "problema \u2192 X / y \u2192 split \u2192 entrenar \u2192 predecir",
        "purpose": "Sirve para mostrar la estructura m\u00ednima de un flujo supervisado sin saturar al estudiante con complejidad.",
        "code": """import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("datasets/estudiantes.csv")
X = df[["asistencia_pct", "evaluacion_python", "edad"]]
y = df["evaluacion_pandas"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

modelo = LinearRegression()
modelo.fit(X_train, y_train)
predicciones = modelo.predict(X_test)
print(predicciones[:5])""",
        "next": "La clase 10 compara modelos supervisados y sus m\u00e9tricas m\u00e1s comunes.",
    },
    {
        "slug": "10-modelos-supervisados",
        "number": 10,
        "icon": "\U0001F333",
        "title": "Modelos supervisados",
        "description": "Comparaci\u00f3n de modelos supervisados b\u00e1sicos y elecci\u00f3n de m\u00e9tricas seg\u00fan el problema.",
        "duration": "90 minutos",
        "duration_short": "90 min",
        "level": "Intermedio avanzado",
        "objective": "Comparar modelos supervisados b\u00e1sicos y elegir m\u00e9tricas seg\u00fan el tipo de problema.",
        "dataset": "datasets/estudiantes.csv",
        "topics": ["Clasificaci\u00f3n", "\u00c1rboles", "Etiquetas", "M\u00e9tricas"],
        "outcomes": ["Transformar un problema en una etiqueta supervisada.", "Entrenar un clasificador simple e interpretable.", "Relacionar modelo y m\u00e9trica con la pregunta del problema."],
        "idea": "El modelo y la m\u00e9trica se eligen por la pregunta, no por popularidad.",
        "note": "Pide que cada estudiante diga qu\u00e9 error ser\u00eda m\u00e1s costoso antes de hablar de m\u00e9tricas.",
        "why": "Ayuda a comparar enfoques y a entender qu\u00e9 cambia entre predecir valores y predecir clases.",
        "block_title": "Clasificaci\u00f3n binaria con \u00e1rbol",
        "block_intro": "Primero definimos una etiqueta supervisada simple y luego entrenamos un modelo interpretable.",
        "schema": "crear etiqueta \u2192 separar variables \u2192 entrenar \u2192 revisar",
        "purpose": "Sirve para introducir clasificaci\u00f3n sin perder transparencia en la l\u00f3gica del modelo.",
        "code": """import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("datasets/estudiantes.csv")
df["alto_desempeno"] = (
    (df["evaluacion_python"] >= 75) & (df["evaluacion_pandas"] >= 75)
).astype(int)

X = df[["asistencia_pct", "evaluacion_python", "edad"]]
y = df["alto_desempeno"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

modelo = DecisionTreeClassifier(max_depth=3, random_state=42)
modelo.fit(X_train, y_train)
print(modelo.predict(X_test[:5]))""",
        "next": "La clase 11 endurece la evaluaci\u00f3n con validaci\u00f3n cruzada y pipelines.",
    },
    {
        "slug": "11-evaluacion-y-pipelines",
        "number": 11,
        "icon": "\U0001F9EA",
        "title": "Evaluaci\u00f3n y pipelines",
        "description": "Evaluaci\u00f3n m\u00e1s rigurosa de modelos y uso de pipelines para evitar fugas y pasos inconsistentes.",
        "duration": "90 minutos",
        "duration_short": "90 min",
        "level": "Intermedio avanzado",
        "objective": "Evaluar modelos con mayor rigor y evitar leakage o sobreajuste.",
        "dataset": "datasets/estudiantes.csv",
        "topics": ["Validaci\u00f3n cruzada", "Pipelines", "Leakage", "Comparaci\u00f3n de score"],
        "outcomes": ["Explicar por qu\u00e9 un score \u00fanico puede ser fr\u00e1gil.", "Usar un pipeline con preprocesamiento y modelo.", "Leer un score medio de validaci\u00f3n cruzada con m\u00e1s criterio."],
        "idea": "Pasar de un modelo que parece funcionar a un flujo de evaluaci\u00f3n m\u00e1s confiable.",
        "note": "Haz visible el riesgo de mezclar preprocesamiento y evaluaci\u00f3n fuera de un pipeline.",
        "why": "La evaluaci\u00f3n rigurosa ayuda a distinguir entre una buena demostraci\u00f3n y un flujo que realmente generaliza mejor.",
        "block_title": "Pipeline con validaci\u00f3n cruzada",
        "block_intro": "El pipeline encapsula el preprocesamiento junto con el modelo y evita pasos manuales inconsistentes.",
        "schema": "preprocesar + modelar \u2192 validar \u2192 comparar",
        "purpose": "Sirve para introducir una pr\u00e1ctica m\u00e1s robusta sin perder claridad sobre cada componente.",
        "code": """import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("datasets/estudiantes.csv")
df["alto_desempeno"] = (
    (df["evaluacion_python"] >= 75) & (df["evaluacion_pandas"] >= 75)
).astype(int)

X = df[["asistencia_pct", "evaluacion_python", "evaluacion_pandas", "edad"]]
y = df["alto_desempeno"]

pipeline = Pipeline(
    [("scaler", StandardScaler()), ("model", LogisticRegression(max_iter=300))]
)
scores = cross_val_score(pipeline, X, y, cv=5, scoring="f1")
print(scores.mean())""",
        "next": "La clase 12 integra todo el recorrido en un proyecto final con cierre.",
    },
    {
        "slug": "12-proyecto-final-y-cierre",
        "number": 12,
        "icon": "\U0001F3C1",
        "title": "Proyecto final y cierre",
        "description": "Integraci\u00f3n final del recorrido con un proyecto breve, defendible y bien estructurado.",
        "duration": "90 minutos",
        "duration_short": "90 min",
        "level": "Integrador",
        "objective": "Integrar las habilidades del bootcamp en un proyecto final acotado y defendible.",
        "dataset": "datasets/ventas_tienda.csv o el dataset trabajado por el grupo.",
        "topics": ["Estructura del notebook", "Pregunta final", "Evidencia", "Cierre de aprendizaje"],
        "outcomes": ["Formular una pregunta final defendible.", "Ordenar el notebook por etapas comprensibles.", "Cerrar con evidencia de aprendizaje integrado."],
        "idea": "El cierre del bootcamp debe mostrar integraci\u00f3n, criterio y claridad de comunicaci\u00f3n.",
        "note": "Eval\u00faa no solo el resultado final, sino tambi\u00e9n si el proceso qued\u00f3 explicado con orden.",
        "why": "El proyecto final permite ver si el estudiante integra an\u00e1lisis, c\u00f3digo y comunicaci\u00f3n con una l\u00f3gica completa.",
        "block_title": "Esqueleto inicial del proyecto final",
        "block_intro": "Organizar el proyecto por etapas hace que otra persona pueda seguir el razonamiento sin perderse.",
        "schema": "contexto \u2192 carga \u2192 an\u00e1lisis \u2192 conclusi\u00f3n",
        "purpose": "Sirve para modelar una estructura m\u00ednima que haga legible el trabajo final ante docentes y compa\u00f1eros.",
        "code": """import pandas as pd

# 1. Cargar datos y dejar una copia de trabajo.
df = pd.read_csv("datasets/ventas_tienda.csv")
trabajo = df.copy()
trabajo["total_neto"] = trabajo["unidades"] * trabajo["precio_unitario"] * (1 - trabajo["descuento_pct"])

# 2. Formular la pregunta antes de seguir.
pregunta = "\u00bfQu\u00e9 sucursal conviene reforzar en la pr\u00f3xima campa\u00f1a?"
print(pregunta)

# 3. Generar una evidencia inicial.
resumen = (
    trabajo.groupby("sucursal", as_index=False)["total_neto"]
    .sum()
    .sort_values("total_neto", ascending=False)
)
print(resumen.head())""",
        "next": "Despu\u00e9s del cierre, el estudiante deber\u00eda salir con un siguiente paso de aprendizaje claro.",
    },
]


def write_text(path: Path, content: str) -> None:
    """Escribe archivos de salida con salto de línea final estable.

    Qué resuelve:
        Mantiene consistencia entre markdown generados y evita diferencias de
        formato triviales al regenerar el currículo.
    """
    path.write_text(content.strip() + "\n", encoding="utf-8")


def class_label(number: int) -> str:
    """Devuelve la etiqueta estándar con formato de dos dígitos."""
    return f"Clase {number:02d}" if number else "Clase 00"


def materials(item: dict) -> list[str]:
    """Lista los materiales esperados para cada clase del bootcamp.

    Qué resuelve:
        Hace explícito qué archivos deben existir por módulo y qué cambia entre
        una clase diagnóstica y una clase con notebook completo.
    """
    base = ["README.md", "slides.md", "teoria.md", "ejercicios.md", "homework.md"]
    if item["number"] == 0:
        base.append("quiz.json")
    else:
        base.extend(["notebook.ipynb", "soluciones.ipynb"])
    return base


def route_table(number: int) -> str:
    """Devuelve una tabla breve con la secuencia sugerida de la sesión.

    Qué resuelve:
        Mantiene el mismo nivel de detalle pedagógico entre módulos y evita que
        cada clase describa su ritmo con criterios distintos.
    """
    if number == 0:
        return """| Tramo | Tiempo sugerido | Enfoque | Evidencia |
|---|---|---|---|
| Inicio | 3 min | Contexto del diagnóstico | Criterio entendido |
| Resolución | 10 min | Responder el quiz | Diagnóstico completo |
| Cierre | 2 min | Retroalimentación inicial | Foco de mejora definido |"""
    return """| Tramo | Tiempo sugerido | Enfoque | Evidencia |
|---|---|---|---|
| Inicio | 10 min | Activar contexto y objetivo | Pregunta inicial visible |
| Desarrollo 1 | 20 min | Demostración guiada | Primer bloque entendido |
| Desarrollo 2 | 25 min | Lectura de código y explicación | Salida interpretada |
| Práctica | 25 min | Ejercicio o quiz del módulo | Entregable corto |
| Cierre | 10 min | Síntesis y siguiente paso | Autoevaluación breve |"""


def documented_code(item: dict) -> str:
    """Antepone comentarios explicativos al bloque Python principal del módulo.

    Qué resuelve:
        Hace explícito, dentro del propio código mostrado al alumno, qué hace el
        bloque y para qué sirve dentro de la secuencia didáctica.
    """
    if item["code"] is None:
        raise ValueError("El módulo no tiene bloque de código asociado")

    schema = item["schema"].strip()
    purpose = item["purpose"].strip()
    if schema and schema[-1] not in ".!?":
        schema += "."
    if purpose and purpose[-1] not in ".!?":
        purpose += "."

    header = [
        f"# Qué hace: {schema}",
        f"# Para qué sirve: {purpose}",
        "",
    ]
    return "\n".join(header) + item["code"]


def render_readme(item: dict) -> str:
    """Genera la ficha resumida de cada clase para navegación rápida."""
    return f"""# {item['icon']} {class_label(item['number'])}: {item['title']}

> 🎯 Ficha de clase con objetivo, materiales y foco de aprendizaje.

## 🎯 Objetivo

{item['objective']}

## ⏱️ Duración sugerida

{item['duration']}

## 📦 Dataset base

- `{item['dataset']}`

## ✅ Resultados esperados

Al finalizar, el estudiante podrá:

{chr(10).join(f"- {value}" for value in item['outcomes'])}

## 🧭 Temas clave

{chr(10).join(f"- {value}" for value in item['topics'])}

## 🧰 Materiales del módulo

{chr(10).join(f"- `{value}`" for value in materials(item))}

## 💻 Cómo leer el código de esta clase

- Cada bloque debe responder una pregunta concreta.
- Los comentarios deben explicar qué hace el bloque y para qué sirve.
- Antes de pasar al siguiente paso, verifica que entiendes la salida.

## 💡 Idea central

{item['idea']}

## 👩‍🏫 Nota para el docente

{item['note']}
"""


def render_slides(item: dict) -> str:
    return f"""# 🖥️ Diapositivas sugeridas — {class_label(item['number'])}

> 🖥️ Guion visual breve para conducir la sesión sin sobrecargar la clase.

## 🚪 Apertura

- Presentar el objetivo y la pregunta central del módulo.
- Conectar la sesión con el recorrido general del bootcamp.

## 🛤️ Ruta de la sesión

{route_table(item['number'])}

## 📌 Puntos que deben quedar claros

{chr(10).join(f"- {value}" for value in item['topics'])}

## 🏁 Cierre esperado

{item['next']}
"""


def render_theory(item: dict) -> str:
    """Genera el documento teórico que acompaña a cada clase."""
    if item["code"] is None:
        main_block = f"""## 🧩 Bloque de trabajo principal

{item['block_intro']}

**Qué hace:** {item['schema']}

**Para qué sirve:** {item['purpose']}"""
    else:
        main_block = f"""## 💻 Bloque de código documentado

### {item['block_title']}

{item['block_intro']}

**Qué hace:** {item['schema']}

**Para qué sirve:** {item['purpose']}

```python
{documented_code(item)}
```"""
    return f"""# 🧠 Documento teórico — {class_label(item['number'])}: {item['title']}

> 🧠 Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## 💡 Idea central

{item['idea']}

## ❓ Por qué importa este módulo

{item['why']}

{main_block}

## ⚠️ Errores frecuentes a vigilar

- Saltar al código sin aclarar la pregunta.
- Ejecutar bloques sin leer la salida.
- Dejar bloques importantes sin comentarios o sin explicación oral.

## 🔗 Conexión con el siguiente módulo

{item['next']}
"""


def render_exercises(item: dict) -> str:
    return f"""# 🧪 Ejercicios — {class_label(item['number'])}

> 🧪 Práctica guiada para trabajar en clase y consolidar el aprendizaje.

## 🧱 Antes de empezar

- Lee la consigna completa antes de escribir código.
- Comenta los bloques que no sean obvios.
- Explica qué hace cada transformación relevante y para qué sirve.

## 🧭 Trabajo guiado

1. Resume con tus palabras la pregunta principal del módulo.
2. Ejecuta o revisa el bloque principal y explica la salida.
3. Realiza una variación pequeña y anota qué cambió y por qué.

## ✅ Criterios de autocorrección

- El resultado responde a la pregunta planteada.
- El código está ordenado y comentado en los puntos clave.
- La salida se puede explicar con lenguaje simple.
"""


def render_homework(item: dict) -> str:
    assignment = "Deja una versión corta y ordenada del trabajo de este módulo, incluyendo una conclusión breve y comentarios en los bloques clave."
    deliverables = [
        "Código o desarrollo ordenado.",
        "Conclusión breve conectada con evidencia.",
        "Comentarios que expliquen qué hace y para qué sirve cada bloque importante.",
    ]
    checks = [
        "Entendí la pregunta del módulo.",
        "Puedo explicar la salida sin leer el código completo.",
        "Dejé comentarios útiles en los pasos clave.",
    ]
    if item["number"] == 0:
        assignment = "Deja una breve reflexión sobre tu punto de partida y el tipo de apoyo que te ayudaría a avanzar con más seguridad."
        deliverables = [
            "Reflexión breve sobre fortalezas y vacíos.",
            "Compromiso de trabajo para la clase siguiente.",
            "Dudas iniciales que quieras resolver con el docente.",
        ]
        checks = [
            "Entendí la lógica general del diagnóstico.",
            "Puedo identificar en qué áreas necesito refuerzo.",
            "Sé cuál será mi foco de mejora en la clase siguiente.",
        ]
    return f"""# 📝 Tarea — {class_label(item['number'])}

> 📝 Trabajo autónomo para consolidar lo visto y practicar con más calma.

## 🎯 Encargo

{assignment}

## 📦 Entregables

{chr(10).join(f"- {value}" for value in deliverables)}

## 🔍 Autoevaluación final

{chr(10).join(f"- {value}" for value in checks)}
"""


def render_mobile_data() -> str:
    """Genera el dataset JavaScript que consume la app móvil.

    Qué resuelve:
        Reutiliza la misma fuente de verdad del currículo para evitar diferencias
        entre lo que se publica en markdown y lo que ve el alumno en móvil.
    """
    quiz = json.loads((CLASSES_DIR / "00-diagnostico-inicial" / "quiz.json").read_text(encoding="utf-8"))
    payload = []
    for item in CURRICULUM:
        code_examples = []
        if item["code"] is not None:
            code_examples.append(
                {
                    "id": f"{item['slug']}-code",
                    "title": item["block_title"],
                    "explanation": item["block_intro"],
                    "schema": item["schema"],
                    "language": "python",
                    "code": documented_code(item),
                }
            )
        payload.append(
            {
                "id": item["slug"],
                "number": item["number"],
                "title": item["title"],
                "description": item["description"],
                "duration": item["duration_short"],
                "level": item["level"],
                "colabUrl": None
                if item["number"] == 0
                else f"https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-bootcamp/blob/master/classes/{item['slug']}/notebook.ipynb",
                "topics": item["topics"],
                "theory": f"{item['idea']} {item['objective']}",
                "outcomes": item["outcomes"],
                "materials": materials(item),
                "codeExamples": code_examples,
                "quiz": quiz if item["number"] == 0 else None,
            }
        )
    return "export const CLASSES = " + json.dumps(payload, ensure_ascii=False, indent=2) + ";\n"


def main() -> None:
    """Regenera markdown de clases y el catálogo móvil a partir del currículo."""
    for item in CURRICULUM:
        class_dir = CLASSES_DIR / item["slug"]
        class_dir.mkdir(parents=True, exist_ok=True)
        write_text(class_dir / "README.md", render_readme(item))
        write_text(class_dir / "slides.md", render_slides(item))
        write_text(class_dir / "teoria.md", render_theory(item))
        write_text(class_dir / "ejercicios.md", render_exercises(item))
        write_text(class_dir / "homework.md", render_homework(item))
    write_text(MOBILE_PATH, render_mobile_data())


if __name__ == "__main__":
    main()
