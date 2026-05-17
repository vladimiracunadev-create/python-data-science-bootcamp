export const CLASSES = [
  {
    "id": "00-diagnostico-inicial",
    "number": 0,
    "title": "Diagnóstico inicial y orientación",
    "description": "Prueba diagnóstica de 30 preguntas para estimar la base técnica del grupo y ordenar el arranque del bootcamp.",
    "duration": "15 min",
    "level": "Diagnóstico",
    "colabUrl": null,
    "topics": [
      "Python básico",
      "Lectura de tablas",
      "Gráficos",
      "Modelado inicial",
      "Hábitos de trabajo"
    ],
    "theory": "Diagnóstico breve, retroalimentación inmediata y acuerdo sobre la ruta de aprendizaje. Estimar el punto de partida del grupo antes de iniciar la ruta formal del bootcamp.",
    "outcomes": [
      "Identificar fortalezas iniciales.",
      "Detectar vacíos de apoyo.",
      "Alinear expectativas del recorrido."
    ],
    "materials": [
      "README.md",
      "slides.md",
      "teoria.md",
      "ejercicios.md",
      "homework.md",
      "quiz.json"
    ],
    "codeExamples": [],
    "quiz": {
      "id": "class-0-diagnostic",
      "title": "Diagnóstico inicial del bootcamp",
      "description": "30 preguntas de opción múltiple para estimar el nivel de entrada en 15 minutos.",
      "duration": "15 min",
      "questions": [
        {
          "id": "q01",
          "category": "Python",
          "prompt": "¿Qué imprime `print(2 + 3)`?",
          "options": [
            "23",
            "5",
            "2 + 3",
            "Error"
          ],
          "correctIndex": 1,
          "explanation": "`+` suma ambos enteros antes de imprimir."
        },
        {
          "id": "q02",
          "category": "Python",
          "prompt": "¿Qué tipo de dato es `[1, 2, 3]`?",
          "options": [
            "Diccionario",
            "Tupla",
            "Lista",
            "Cadena"
          ],
          "correctIndex": 2,
          "explanation": "Los corchetes crean una lista."
        },
        {
          "id": "q03",
          "category": "Python",
          "prompt": "¿Qué devuelve `len([10, 20, 30])`?",
          "options": [
            "2",
            "3",
            "30",
            "Error"
          ],
          "correctIndex": 1,
          "explanation": "`len()` cuenta elementos."
        },
        {
          "id": "q04",
          "category": "Python",
          "prompt": "Si `x = 4`, ¿qué imprime `if x > 5: print(\"A\") else: print(\"B\")`?",
          "options": [
            "A",
            "B",
            "A y B",
            "Error"
          ],
          "correctIndex": 1,
          "explanation": "Como `4 > 5` es falso, entra al `else`."
        },
        {
          "id": "q05",
          "category": "Python",
          "prompt": "¿Cómo accedes a `nombre` en `{\"nombre\": \"Ana\"}`?",
          "options": [
            "`dato.nombre`",
            "`dato[\"nombre\"]`",
            "`nombre[dato]`",
            "`dato(\"nombre\")`"
          ],
          "correctIndex": 1,
          "explanation": "En diccionarios se accede por clave."
        },
        {
          "id": "q06",
          "category": "Python",
          "prompt": "¿Qué imprime `for n in range(3): print(n)`?",
          "options": [
            "1, 2, 3",
            "0, 1, 2",
            "0, 1, 2, 3",
            "Nada"
          ],
          "correctIndex": 1,
          "explanation": "`range(3)` produce 0, 1 y 2."
        },
        {
          "id": "q07",
          "category": "Python",
          "prompt": "¿Para qué sirve una función?",
          "options": [
            "Solo para gráficos",
            "Para reutilizar lógica",
            "Para borrar archivos",
            "Para crear CSV"
          ],
          "correctIndex": 1,
          "explanation": "Una función encapsula una tarea reutilizable."
        },
        {
          "id": "q08",
          "category": "Python",
          "prompt": "¿Qué hace `#` en Python?",
          "options": [
            "Crea una lista",
            "Marca un comentario",
            "Define un bucle",
            "Convierte texto"
          ],
          "correctIndex": 1,
          "explanation": "Todo lo que sigue a `#` no se ejecuta."
        },
        {
          "id": "q09",
          "category": "Datos",
          "prompt": "¿Qué hace `pd.read_csv(\"archivo.csv\")`?",
          "options": [
            "Dibuja un gráfico",
            "Carga un CSV en un DataFrame",
            "Borra nulos",
            "Convierte fechas"
          ],
          "correctIndex": 1,
          "explanation": "Es la forma estándar de abrir un CSV en pandas."
        },
        {
          "id": "q10",
          "category": "Datos",
          "prompt": "Un valor nulo suele indicar que:",
          "options": [
            "Todo está roto",
            "Falta información",
            "La fila sobra siempre",
            "La tabla no sirve"
          ],
          "correctIndex": 1,
          "explanation": "Un nulo indica ausencia de dato, no necesariamente error fatal."
        },
        {
          "id": "q11",
          "category": "Datos",
          "prompt": "¿Qué muestra `df.head()`?",
          "options": [
            "Últimas filas",
            "Primeras filas",
            "Solo columnas",
            "Solo tipos"
          ],
          "correctIndex": 1,
          "explanation": "Sirve para inspeccionar el inicio de la tabla."
        },
        {
          "id": "q12",
          "category": "Datos",
          "prompt": "¿Para qué sirve `groupby()`?",
          "options": [
            "Ordenar alfabéticamente",
            "Agrupar y resumir por categoría",
            "Crear gráficos",
            "Renombrar columnas"
          ],
          "correctIndex": 1,
          "explanation": "Agrupa filas para resumirlas por segmento."
        },
        {
          "id": "q13",
          "category": "Datos",
          "prompt": "¿Qué hace `dropna()`?",
          "options": [
            "Duplica nulos",
            "Elimina filas o columnas con nulos",
            "Pone cero automáticamente",
            "Convierte nulos en texto"
          ],
          "correctIndex": 1,
          "explanation": "Elimina datos incompletos cuando esa decisión tiene sentido."
        },
        {
          "id": "q14",
          "category": "Datos",
          "prompt": "¿Qué representa la mediana?",
          "options": [
            "El valor más repetido",
            "El valor central al ordenar",
            "La mitad de la suma",
            "El valor máximo"
          ],
          "correctIndex": 1,
          "explanation": "La mediana es el centro de la distribución ordenada."
        },
        {
          "id": "q15",
          "category": "Datos",
          "prompt": "Si quieres quedarte solo con ventas mayores a 100, primero debes:",
          "options": [
            "Filtrar filas",
            "Agrupar por categoría",
            "Renombrar columnas",
            "Resetear índices"
          ],
          "correctIndex": 0,
          "explanation": "Antes de resumir, seleccionas solo las filas relevantes."
        },
        {
          "id": "q16",
          "category": "Visualizacion",
          "prompt": "¿Qué gráfico suele servir mejor para comparar categorías?",
          "options": [
            "Barras",
            "Mapa de calor",
            "Boxplot",
            "Dispersión"
          ],
          "correctIndex": 0,
          "explanation": "Las barras comparan magnitudes entre grupos discretos."
        },
        {
          "id": "q17",
          "category": "Visualizacion",
          "prompt": "¿Qué gráfico suele servir mejor para una evolución en el tiempo?",
          "options": [
            "Línea",
            "Torta",
            "Histograma",
            "Tabla"
          ],
          "correctIndex": 0,
          "explanation": "La línea ayuda a seguir tendencia en series temporales."
        },
        {
          "id": "q18",
          "category": "Visualizacion",
          "prompt": "¿Para qué sirve un histograma?",
          "options": [
            "Para mapas",
            "Para ver distribución de una variable numérica",
            "Para jerarquías",
            "Para tablas"
          ],
          "correctIndex": 1,
          "explanation": "Resume frecuencias por rangos."
        },
        {
          "id": "q19",
          "category": "Visualizacion",
          "prompt": "¿Qué relación comunica mejor un gráfico de dispersión?",
          "options": [
            "Dos variables numéricas",
            "Carpetas del proyecto",
            "Errores de sintaxis",
            "Colores"
          ],
          "correctIndex": 0,
          "explanation": "El scatter plot muestra relación entre dos variables numéricas."
        },
        {
          "id": "q20",
          "category": "Visualizacion",
          "prompt": "¿Qué mejora la lectura de un gráfico?",
          "options": [
            "Quitar etiquetas",
            "Agregar título y ejes claros",
            "Usar todos los colores posibles",
            "Evitar leyendas siempre"
          ],
          "correctIndex": 1,
          "explanation": "El contexto visual ayuda a interpretar rápido."
        },
        {
          "id": "q21",
          "category": "Modelado",
          "prompt": "En ML supervisado, el target es:",
          "options": [
            "La variable a predecir",
            "El archivo CSV",
            "La librería",
            "La fecha"
          ],
          "correctIndex": 0,
          "explanation": "El target es la salida esperada."
        },
        {
          "id": "q22",
          "category": "Modelado",
          "prompt": "¿Por qué se separan train y testá",
          "options": [
            "Para usar menos memoria",
            "Para medir generalización",
            "Para graficar más",
            "Para ordenar datos"
          ],
          "correctIndex": 1,
          "explanation": "Si pruebas con train, la evaluación engaña."
        },
        {
          "id": "q23",
          "category": "Modelado",
          "prompt": "¿Qué describe mejor el overfitting?",
          "options": [
            "Falla en train y test",
            "Memoriza train y falla fuera de muestra",
            "Usa pocas columnas",
            "Entrena muy rápido"
          ],
          "correctIndex": 1,
          "explanation": "Overfitting es aprender demasiado el entrenamiento."
        },
        {
          "id": "q24",
          "category": "Modelado",
          "prompt": "¿Para qué sirve un pipeline?",
          "options": [
            "Para dashboards",
            "Para encadenar preprocesamiento y modelo sin leakage",
            "Para guardar CSV",
            "Para traducir errores"
          ],
          "correctIndex": 1,
          "explanation": "Organiza el flujo y evita mezclar información."
        },
        {
          "id": "q25",
          "category": "Modelado",
          "prompt": "Si el MAE baja, normalmente significa que:",
          "options": [
            "El modelo empeoró",
            "El error promedio disminuyó",
            "Se borraron filas",
            "Cambió el target"
          ],
          "correctIndex": 1,
          "explanation": "En métricas de error, menor suele ser mejor."
        },
        {
          "id": "q26",
          "category": "Trabajo",
          "prompt": "Antes de escribir código, conviene:",
          "options": [
            "Entender la pregunta y revisar datos",
            "Elegir colores",
            "Instalar más librerías",
            "Copiar una solución"
          ],
          "correctIndex": 0,
          "explanation": "Sin una pregunta clara, el análisis se desordena."
        },
        {
          "id": "q27",
          "category": "Trabajo",
          "prompt": "Si usas IA o internet en clase, la mejor práctica es:",
          "options": [
            "Pegar sin leer",
            "Verificar, adaptar y explicar",
            "Cambiar colores",
            "Ocultarlo"
          ],
          "correctIndex": 1,
          "explanation": "La herramienta ayuda, pero el criterio sigue siendo humano."
        },
        {
          "id": "q28",
          "category": "Trabajo",
          "prompt": "¿Qué describe un buen comentario educativo?",
          "options": [
            "Repite la línea",
            "Explica qué hace el bloque y por qué se usa",
            "Oculta errores",
            "Reemplaza pruebas"
          ],
          "correctIndex": 1,
          "explanation": "Un comentario útil agrega contexto, no ruido."
        },
        {
          "id": "q29",
          "category": "Trabajo",
          "prompt": "Si un gráfico se ve raro, primero revisa:",
          "options": [
            "Columnas, tipos y orden del código",
            "Cerrar el notebook",
            "Cambiar la paleta",
            "Eliminar el dataset"
          ],
          "correctIndex": 0,
          "explanation": "Muchos errores visuales nacen de datos o pasos mal elegidos."
        },
        {
          "id": "q30",
          "category": "Trabajo",
          "prompt": "¿Cuál es el objetivo principal del bootcamp?",
          "options": [
            "Memorizar comandos",
            "Leer problemas, trabajar con datos y explicar resultados",
            "Solo aprobar pruebas",
            "Usar muchas librerías"
          ],
          "correctIndex": 1,
          "explanation": "El foco es criterio aplicado, no solo sintaxis."
        }
      ]
    }
  },
  {
    "id": "01-python-fundamentos",
    "number": 1,
    "title": "Fundamentos de Python aplicados a datos",
    "description": "Variables, tipos, estructuras y control de flujo aplicados a datos simples.",
    "duration": "90 min",
    "level": "Básico",
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-bootcamp/blob/master/classes/01-python-fundamentos/notebook.ipynb",
    "topics": [
      "Variables y tipos",
      "Listas y diccionarios",
      "Funciones",
      "Control de flujo"
    ],
    "theory": "Python se presenta como herramienta para ordenar y transformar información, no como teoría abstracta. Comprender los elementos básicos de Python y aplicarlos a ejemplos pequeños relacionados con datos.",
    "outcomes": [
      "Crear variables claras y expresivas.",
      "Usar listas y diccionarios para representar información.",
      "Escribir funciones simples con propósito evidente."
    ],
    "materials": [
      "README.md",
      "slides.md",
      "teoria.md",
      "ejercicios.md",
      "homework.md",
      "notebook.ipynb",
      "soluciones.ipynb"
    ],
    "codeExamples": [
      {
        "id": "01-python-fundamentos-code",
        "title": "Función para calcular ingreso bruto",
        "explanation": "Encapsular una operación en una función evita repetir lógica y facilita explicar cada paso.",
        "schema": "entrada → calcular → devolver → reutilizar",
        "language": "python",
        "code": "# Qué hace: entrada → calcular → devolver → reutilizar.\n# Para qué sirve: Sirve para introducir reutilización, parámetros y retorno usando un ejemplo cercano al análisis de ventas.\ndef calcular_total_bruto(unidades, precio_unitario):\n    # Multiplicamos cantidad por precio para estimar el ingreso bruto.\n    return unidades * precio_unitario\n\n\nventas = [\n    {\"producto\": \"Mouse\", \"unidades\": 3, \"precio_unitario\": 8990},\n    {\"producto\": \"Teclado\", \"unidades\": 2, \"precio_unitario\": 15990},\n]\n\ntotales = [calcular_total_bruto(v[\"unidades\"], v[\"precio_unitario\"]) for v in ventas]\nprint(totales)"
      }
    ],
    "quiz": null
  },
  {
    "id": "02-pandas-limpieza-datos",
    "number": 2,
    "title": "Pandas y limpieza de datos",
    "description": "Carga de CSV, inspección inicial y limpieza de tablas para preparar análisis confiables.",
    "duration": "90 min",
    "level": "Básico",
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-bootcamp/blob/master/classes/02-pandas-limpieza-datos/notebook.ipynb",
    "topics": [
      "DataFrame",
      "Inspección inicial",
      "Nulos",
      "Estandarización básica"
    ],
    "theory": "No se analiza una tabla seria sin inspeccionarla y documentar primero sus problemas. Usar pandas para cargar, inspeccionar y limpiar tablas antes de analizarlas.",
    "outcomes": [
      "Cargar un CSV y revisar su estructura.",
      "Detectar problemas simples de calidad.",
      "Aplicar limpiezas justificadas y documentadas."
    ],
    "materials": [
      "README.md",
      "slides.md",
      "teoria.md",
      "ejercicios.md",
      "homework.md",
      "notebook.ipynb",
      "soluciones.ipynb"
    ],
    "codeExamples": [
      {
        "id": "02-pandas-limpieza-datos-code",
        "title": "Carga e inspección de un CSV",
        "explanation": "El primer paso no es graficar: es entender qué columnas existen, cómo vienen escritas y si podemos confiar en ellas.",
        "schema": "cargar → inspeccionar → limpiar → verificar",
        "language": "python",
        "code": "# Qué hace: cargar → inspeccionar → limpiar → verificar.\n# Para qué sirve: Sirve para instalar una rutina mínima de calidad antes de cualquier análisis o visualización.\nimport pandas as pd\n\ndf = pd.read_csv(\"datasets/ventas_tienda.csv\")\n\n# Revisamos primeras filas, tipos y valores faltantes antes de seguir.\nprint(df.head())\nprint(df.info())\nprint(df.isna().sum())\n\n# Ejemplo simple de limpieza visible.\ndf[\"medio_pago\"] = df[\"medio_pago\"].str.strip()"
      }
    ],
    "quiz": null
  },
  {
    "id": "03-visualizacion-exploratoria",
    "number": 3,
    "title": "Visualización exploratoria",
    "description": "Gráficos iniciales para describir patrones, comparar categorías y abrir preguntas de análisis.",
    "duration": "90 min",
    "level": "Básico",
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-bootcamp/blob/master/classes/03-visualizacion-exploratoria/notebook.ipynb",
    "topics": [
      "Agrupación",
      "Barras",
      "Lectura visual",
      "Preguntas exploratorias"
    ],
    "theory": "La visualización exploratoria ayuda a mirar mejor y a formular preguntas más útiles. Usar visualizaciones exploratorias para describir patrones y abrir nuevas preguntas de análisis.",
    "outcomes": [
      "Construir un resumen por categoría o sucursal.",
      "Elegir un gráfico simple y legible.",
      "Explicar qué pregunta responde la visualización."
    ],
    "materials": [
      "README.md",
      "slides.md",
      "teoria.md",
      "ejercicios.md",
      "homework.md",
      "notebook.ipynb",
      "soluciones.ipynb"
    ],
    "codeExamples": [
      {
        "id": "03-visualizacion-exploratoria-code",
        "title": "Ventas netas por categoría",
        "explanation": "Antes de graficar conviene preparar un resumen que reduzca el ruido de filas individuales.",
        "schema": "calcular métrica → agrupar → ordenar → graficar",
        "language": "python",
        "code": "# Qué hace: calcular métrica → agrupar → ordenar → graficar.\n# Para qué sirve: Sirve para mostrar cómo un gráfico nace de una decisión previa de agregación y no de un clic automático.\nimport pandas as pd\nimport matplotlib.pyplot as plt\n\ndf = pd.read_csv(\"datasets/ventas_tienda.csv\")\ndf[\"total_neto\"] = df[\"unidades\"] * df[\"precio_unitario\"] * (1 - df[\"descuento_pct\"])\n\nresumen = (\n    df.groupby(\"categoria\", as_index=False)[\"total_neto\"]\n    .sum()\n    .sort_values(\"total_neto\", ascending=False)\n)\n\nplt.figure(figsize=(8, 4))\nplt.bar(resumen[\"categoria\"], resumen[\"total_neto\"])\nplt.title(\"Ventas netas por categoría\")\nplt.ylabel(\"CLP\")\nplt.xticks(rotation=20)\nplt.tight_layout()"
      }
    ],
    "quiz": null
  },
  {
    "id": "04-estadistica-descriptiva",
    "number": 4,
    "title": "Estadística descriptiva",
    "description": "Medidas descriptivas para resumir variables y sostener interpretaciones básicas.",
    "duration": "90 min",
    "level": "Básico",
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-bootcamp/blob/master/classes/04-estadistica-descriptiva/notebook.ipynb",
    "topics": [
      "Media",
      "Mediana",
      "Dispersión",
      "Interpretación"
    ],
    "theory": "La estadística descriptiva resume poblaciones, pero siempre debe volver a una pregunta concreta. Interpretar medidas descriptivas simples y relacionarlas con preguntas reales.",
    "outcomes": [
      "Calcular medidas de tendencia central.",
      "Leer una dispersión básica sin perder contexto.",
      "Evitar conclusiones apoyadas en un solo número."
    ],
    "materials": [
      "README.md",
      "slides.md",
      "teoria.md",
      "ejercicios.md",
      "homework.md",
      "notebook.ipynb",
      "soluciones.ipynb"
    ],
    "codeExamples": [
      {
        "id": "04-estadistica-descriptiva-code",
        "title": "Resumen de asistencia del curso",
        "explanation": "Usar varias medidas a la vez evita depender de un único número y mejora la interpretación.",
        "schema": "seleccionar variable → calcular resumen → interpretar",
        "language": "python",
        "code": "# Qué hace: seleccionar variable → calcular resumen → interpretar.\n# Para qué sirve: Sirve para conectar conceptos estadísticos con decisiones pedagógicas o de seguimiento académico.\nimport pandas as pd\n\ndf = pd.read_csv(\"datasets/estudiantes.csv\")\nasistencia = df[\"asistencia_pct\"]\n\nprint(\"Media:\", asistencia.mean())\nprint(\"Mediana:\", asistencia.median())\nprint(\"Desviación estándar:\", asistencia.std())\nprint(asistencia.describe())"
      }
    ],
    "quiz": null
  },
  {
    "id": "05-visualizacion-con-matplotlib",
    "number": 5,
    "title": "Visualización con matplotlib",
    "description": "Construcción de gráficos más controlados y legibles usando matplotlib.",
    "duration": "90 min",
    "level": "Intermedio",
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-bootcamp/blob/master/classes/05-visualizacion-con-matplotlib/notebook.ipynb",
    "topics": [
      "Figure y axes",
      "Rotulado",
      "Legibilidad",
      "Ajuste visual"
    ],
    "theory": "No basta con que el gráfico funcione: debe poder leerse sin fricción. Crear gráficos más controlados con matplotlib y mejorar su legibilidad.",
    "outcomes": [
      "Crear una figura explícita con tamaño controlado.",
      "Rotular ejes y títulos con intención.",
      "Mejorar la lectura visual de un gráfico temporal."
    ],
    "materials": [
      "README.md",
      "slides.md",
      "teoria.md",
      "ejercicios.md",
      "homework.md",
      "notebook.ipynb",
      "soluciones.ipynb"
    ],
    "codeExamples": [
      {
        "id": "05-visualizacion-con-matplotlib-code",
        "title": "Serie temporal de clientes activos",
        "explanation": "Crear una figura explícita permite controlar tamaño, etiquetas y orden visual con intención.",
        "schema": "crear figura → dibujar → rotular → ajustar",
        "language": "python",
        "code": "# Qué hace: crear figura → dibujar → rotular → ajustar.\n# Para qué sirve: Sirve para pasar de una visualización funcional a una visualización comunicable.\nimport pandas as pd\nimport matplotlib.pyplot as plt\n\ndf = pd.read_csv(\"datasets/retencion_clientes.csv\")\n\nfig, ax = plt.subplots(figsize=(9, 4))\nax.plot(df[\"mes\"], df[\"clientes_activos\"], marker=\"o\", linewidth=2)\nax.set_title(\"Clientes activos por mes\")\nax.set_xlabel(\"Mes\")\nax.set_ylabel(\"Clientes activos\")\nax.tick_params(axis=\"x\", rotation=45)\nax.grid(alpha=0.2)\nplt.tight_layout()"
      }
    ],
    "quiz": null
  },
  {
    "id": "06-texto-fechas-y-transformaciones",
    "number": 6,
    "title": "Texto, fechas y transformaciones",
    "description": "Transformación de columnas de texto y fecha para hacerlas útiles en análisis y modelado inicial.",
    "duration": "90 min",
    "level": "Intermedio",
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-bootcamp/blob/master/classes/06-texto-fechas-y-transformaciones/notebook.ipynb",
    "topics": [
      "Fechas",
      "Texto",
      "Columnas derivadas",
      "Normalización"
    ],
    "theory": "Muchas preguntas nuevas aparecen cuando una columna se transforma bien. Transformar columnas de texto y fecha para volverlas útiles en análisis y modelado inicial.",
    "outcomes": [
      "Convertir una columna a fecha real.",
      "Crear variables derivadas con sentido analítico.",
      "Normalizar texto para evitar duplicados de categoría."
    ],
    "materials": [
      "README.md",
      "slides.md",
      "teoria.md",
      "ejercicios.md",
      "homework.md",
      "notebook.ipynb",
      "soluciones.ipynb"
    ],
    "codeExamples": [
      {
        "id": "06-texto-fechas-y-transformaciones-code",
        "title": "Fechas y texto listos para analizar",
        "explanation": "Convertir y normalizar columnas no es maquillaje: cambia lo que se puede preguntar después.",
        "schema": "convertir → derivar → normalizar → reutilizar",
        "language": "python",
        "code": "# Qué hace: convertir → derivar → normalizar → reutilizar.\n# Para qué sirve: Sirve para preparar columnas que luego alimentan gráficos, filtros o variables de modelado.\nimport pandas as pd\n\ndf = pd.read_csv(\"datasets/ventas_tienda.csv\")\ndf[\"fecha\"] = pd.to_datetime(df[\"fecha\"])\n\n# Creamos columnas nuevas para responder preguntas posteriores.\ndf[\"mes\"] = df[\"fecha\"].dt.to_period(\"M\").astype(str)\ndf[\"dia_semana\"] = df[\"fecha\"].dt.day_name()\ndf[\"producto_normalizado\"] = df[\"producto\"].str.strip().str.lower()\n\nprint(df[[\"fecha\", \"mes\", \"dia_semana\", \"producto_normalizado\"]].head())"
      }
    ],
    "quiz": null
  },
  {
    "id": "07-mini-proyecto-guiado",
    "number": 7,
    "title": "Mini proyecto guiado",
    "description": "Integración guiada de lectura, limpieza, análisis y comunicación en una sola secuencia corta.",
    "duration": "90 min",
    "level": "Integrador",
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-bootcamp/blob/master/classes/07-mini-proyecto-guiado/notebook.ipynb",
    "topics": [
      "Pregunta de análisis",
      "Recorte",
      "Secuencia de trabajo",
      "Evidencia"
    ],
    "theory": "El proyecto ordena técnicas sueltas dentro de un proceso con sentido. Integrar las habilidades vistas hasta ahora en un mini proyecto guiado de principio a fin.",
    "outcomes": [
      "Formular una pregunta concreta de proyecto.",
      "Armar una base de trabajo con columnas útiles.",
      "Seguir una secuencia coherente de análisis."
    ],
    "materials": [
      "README.md",
      "slides.md",
      "teoria.md",
      "ejercicios.md",
      "homework.md",
      "notebook.ipynb",
      "soluciones.ipynb"
    ],
    "codeExamples": [
      {
        "id": "07-mini-proyecto-guiado-code",
        "title": "Definición de pregunta y base de trabajo",
        "explanation": "Antes de calcular, conviene dejar escrita la pregunta y recortar solo las columnas necesarias.",
        "schema": "pregunta → recorte → base de trabajo → análisis",
        "language": "python",
        "code": "# Qué hace: pregunta → recorte → base de trabajo → análisis.\n# Para qué sirve: Sirve para evitar notebooks dispersos y para mostrar que el proyecto comienza delimitando el problema.\nimport pandas as pd\n\ndf = pd.read_csv(\"datasets/ventas_tienda.csv\")\ndf[\"total_neto\"] = df[\"unidades\"] * df[\"precio_unitario\"] * (1 - df[\"descuento_pct\"])\n\npregunta = \"¿Qué categoría concentra mayor ingreso neto?\"\ncolumnas = [\"fecha\", \"sucursal\", \"categoria\", \"producto\", \"medio_pago\", \"total_neto\"]\nproyecto = df[columnas].copy()\n\nprint(pregunta)\nprint(proyecto.head())"
      }
    ],
    "quiz": null
  },
  {
    "id": "08-presentacion-de-hallazgos",
    "number": 8,
    "title": "Presentación de hallazgos",
    "description": "Traducción de resultados técnicos a mensajes cortos, claros y defendibles.",
    "duration": "90 min",
    "level": "Integrador",
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-bootcamp/blob/master/classes/08-presentacion-de-hallazgos/notebook.ipynb",
    "topics": [
      "Storytelling con datos",
      "Resumen ejecutivo",
      "Mensajes clave",
      "Visuales de apoyo"
    ],
    "theory": "La calidad del análisis también depende de cómo se explica y a quién se dirige. Transformar resultados técnicos en una historia corta, clara y defendible.",
    "outcomes": [
      "Ordenar una historia de análisis.",
      "Elegir visuales que sostengan un mensaje.",
      "Escribir conclusiones ejecutivas sin perder rigor."
    ],
    "materials": [
      "README.md",
      "slides.md",
      "teoria.md",
      "ejercicios.md",
      "homework.md",
      "notebook.ipynb",
      "soluciones.ipynb"
    ],
    "codeExamples": [
      {
        "id": "08-presentacion-de-hallazgos-code",
        "title": "Resumen ejecutivo en tres líneas",
        "explanation": "No todo hallazgo se comunica con un gráfico; a veces conviene escribir un mensaje breve y accionable.",
        "schema": "hallazgo → evidencia → recomendación",
        "language": "python",
        "code": "# Qué hace: hallazgo → evidencia → recomendación.\n# Para qué sirve: Sirve para entrenar una salida ejecutiva que conecte el dato con una decisión posible.\nhallazgo = \"La categoría Accesorios concentra el mayor ingreso neto del periodo.\"\nevidencia = \"El resumen por categoría la ubica en el primer lugar del ranking.\"\nrecomendacion = \"Conviene revisar margen, stock y campañas antes de ampliar la oferta.\"\n\nprint(hallazgo)\nprint(evidencia)\nprint(recomendacion)"
      }
    ],
    "quiz": null
  },
  {
    "id": "09-machine-learning-intro",
    "number": 9,
    "title": "Introducción a machine learning",
    "description": "Primer acercamiento a aprendizaje supervisado usando un problema de regresión simple.",
    "duration": "90 min",
    "level": "Intermedio avanzado",
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-bootcamp/blob/master/classes/09-machine-learning-intro/notebook.ipynb",
    "topics": [
      "X e y",
      "Train/test split",
      "Regresión",
      "Predicción"
    ],
    "theory": "Machine learning se presenta como una extensión del análisis, no como magia negra. Comprender qué es un modelo supervisado y construir una primera regresión simple con scikit-learn.",
    "outcomes": [
      "Distinguir variables de entrada y objetivo.",
      "Construir un train/test split reproducible.",
      "Entrenar una regresión simple y revisar sus predicciones."
    ],
    "materials": [
      "README.md",
      "slides.md",
      "teoria.md",
      "ejercicios.md",
      "homework.md",
      "notebook.ipynb",
      "soluciones.ipynb"
    ],
    "codeExamples": [
      {
        "id": "09-machine-learning-intro-code",
        "title": "Primera regresión con variables académicas",
        "explanation": "Antes de entrenar, conviene declarar con claridad qué queremos predecir y qué datos usaremos como entrada.",
        "schema": "problema → X / y → split → entrenar → predecir",
        "language": "python",
        "code": "# Qué hace: problema → X / y → split → entrenar → predecir.\n# Para qué sirve: Sirve para mostrar la estructura mínima de un flujo supervisado sin saturar al estudiante con complejidad.\nimport pandas as pd\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn.model_selection import train_test_split\n\ndf = pd.read_csv(\"datasets/estudiantes.csv\")\nX = df[[\"asistencia_pct\", \"evaluacion_python\", \"edad\"]]\ny = df[\"evaluacion_pandas\"]\n\nX_train, X_test, y_train, y_test = train_test_split(\n    X, y, test_size=0.2, random_state=42\n)\n\nmodelo = LinearRegression()\nmodelo.fit(X_train, y_train)\npredicciones = modelo.predict(X_test)\nprint(predicciones[:5])"
      }
    ],
    "quiz": null
  },
  {
    "id": "10-modelos-supervisados",
    "number": 10,
    "title": "Modelos supervisados",
    "description": "Comparación de modelos supervisados básicos y elección de métricas según el problema.",
    "duration": "90 min",
    "level": "Intermedio avanzado",
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-bootcamp/blob/master/classes/10-modelos-supervisados/notebook.ipynb",
    "topics": [
      "Clasificación",
      "Árboles",
      "Etiquetas",
      "Métricas"
    ],
    "theory": "El modelo y la métrica se eligen por la pregunta, no por popularidad. Comparar modelos supervisados básicos y elegir métricas según el tipo de problema.",
    "outcomes": [
      "Transformar un problema en una etiqueta supervisada.",
      "Entrenar un clasificador simple e interpretable.",
      "Relacionar modelo y métrica con la pregunta del problema."
    ],
    "materials": [
      "README.md",
      "slides.md",
      "teoria.md",
      "ejercicios.md",
      "homework.md",
      "notebook.ipynb",
      "soluciones.ipynb"
    ],
    "codeExamples": [
      {
        "id": "10-modelos-supervisados-code",
        "title": "Clasificación binaria con árbol",
        "explanation": "Primero definimos una etiqueta supervisada simple y luego entrenamos un modelo interpretable.",
        "schema": "crear etiqueta → separar variables → entrenar → revisar",
        "language": "python",
        "code": "# Qué hace: crear etiqueta → separar variables → entrenar → revisar.\n# Para qué sirve: Sirve para introducir clasificación sin perder transparencia en la lógica del modelo.\nimport pandas as pd\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.tree import DecisionTreeClassifier\n\ndf = pd.read_csv(\"datasets/estudiantes.csv\")\ndf[\"alto_desempeno\"] = (\n    (df[\"evaluacion_python\"] >= 75) & (df[\"evaluacion_pandas\"] >= 75)\n).astype(int)\n\nX = df[[\"asistencia_pct\", \"evaluacion_python\", \"edad\"]]\ny = df[\"alto_desempeno\"]\n\nX_train, X_test, y_train, y_test = train_test_split(\n    X, y, test_size=0.2, random_state=42\n)\n\nmodelo = DecisionTreeClassifier(max_depth=3, random_state=42)\nmodelo.fit(X_train, y_train)\nprint(modelo.predict(X_test[:5]))"
      }
    ],
    "quiz": null
  },
  {
    "id": "11-evaluacion-y-pipelines",
    "number": 11,
    "title": "Evaluación y pipelines",
    "description": "Evaluación más rigurosa de modelos y uso de pipelines para evitar fugas y pasos inconsistentes.",
    "duration": "90 min",
    "level": "Intermedio avanzado",
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-bootcamp/blob/master/classes/11-evaluacion-y-pipelines/notebook.ipynb",
    "topics": [
      "Validación cruzada",
      "Pipelines",
      "Leakage",
      "Comparación de score"
    ],
    "theory": "Pasar de un modelo que parece funcionar a un flujo de evaluación más confiable. Evaluar modelos con mayor rigor y evitar leakage o sobreajuste.",
    "outcomes": [
      "Explicar por qué un score único puede ser frágil.",
      "Usar un pipeline con preprocesamiento y modelo.",
      "Leer un score medio de validación cruzada con más criterio."
    ],
    "materials": [
      "README.md",
      "slides.md",
      "teoria.md",
      "ejercicios.md",
      "homework.md",
      "notebook.ipynb",
      "soluciones.ipynb"
    ],
    "codeExamples": [
      {
        "id": "11-evaluacion-y-pipelines-code",
        "title": "Pipeline con validación cruzada",
        "explanation": "El pipeline encapsula el preprocesamiento junto con el modelo y evita pasos manuales inconsistentes.",
        "schema": "preprocesar + modelar → validar → comparar",
        "language": "python",
        "code": "# Qué hace: preprocesar + modelar → validar → comparar.\n# Para qué sirve: Sirve para introducir una práctica más robusta sin perder claridad sobre cada componente.\nimport pandas as pd\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.model_selection import cross_val_score\nfrom sklearn.pipeline import Pipeline\nfrom sklearn.preprocessing import StandardScaler\n\ndf = pd.read_csv(\"datasets/estudiantes.csv\")\ndf[\"alto_desempeno\"] = (\n    (df[\"evaluacion_python\"] >= 75) & (df[\"evaluacion_pandas\"] >= 75)\n).astype(int)\n\nX = df[[\"asistencia_pct\", \"evaluacion_python\", \"evaluacion_pandas\", \"edad\"]]\ny = df[\"alto_desempeno\"]\n\npipeline = Pipeline(\n    [(\"scaler\", StandardScaler()), (\"model\", LogisticRegression(max_iter=300))]\n)\nscores = cross_val_score(pipeline, X, y, cv=5, scoring=\"f1\")\nprint(scores.mean())"
      }
    ],
    "quiz": null
  },
  {
    "id": "12-proyecto-final-y-cierre",
    "number": 12,
    "title": "Proyecto final y cierre",
    "description": "Integración final del recorrido con un proyecto breve, defendible y bien estructurado.",
    "duration": "90 min",
    "level": "Integrador",
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-bootcamp/blob/master/classes/12-proyecto-final-y-cierre/notebook.ipynb",
    "topics": [
      "Estructura del notebook",
      "Pregunta final",
      "Evidencia",
      "Cierre de aprendizaje"
    ],
    "theory": "El cierre del bootcamp debe mostrar integración, criterio y claridad de comunicación. Integrar las habilidades del bootcamp en un proyecto final acotado y defendible.",
    "outcomes": [
      "Formular una pregunta final defendible.",
      "Ordenar el notebook por etapas comprensibles.",
      "Cerrar con evidencia de aprendizaje integrado."
    ],
    "materials": [
      "README.md",
      "slides.md",
      "teoria.md",
      "ejercicios.md",
      "homework.md",
      "notebook.ipynb",
      "soluciones.ipynb"
    ],
    "codeExamples": [
      {
        "id": "12-proyecto-final-y-cierre-code",
        "title": "Esqueleto inicial del proyecto final",
        "explanation": "Organizar el proyecto por etapas hace que otra persona pueda seguir el razonamiento sin perderse.",
        "schema": "contexto → carga → análisis → conclusión",
        "language": "python",
        "code": "# Qué hace: contexto → carga → análisis → conclusión.\n# Para qué sirve: Sirve para modelar una estructura mínima que haga legible el trabajo final ante docentes y compañeros.\nimport pandas as pd\n\n# 1. Cargar datos y dejar una copia de trabajo.\ndf = pd.read_csv(\"datasets/ventas_tienda.csv\")\ntrabajo = df.copy()\ntrabajo[\"total_neto\"] = trabajo[\"unidades\"] * trabajo[\"precio_unitario\"] * (1 - trabajo[\"descuento_pct\"])\n\n# 2. Formular la pregunta antes de seguir.\npregunta = \"¿Qué sucursal conviene reforzar en la próxima campaña?\"\nprint(pregunta)\n\n# 3. Generar una evidencia inicial.\nresumen = (\n    trabajo.groupby(\"sucursal\", as_index=False)[\"total_neto\"]\n    .sum()\n    .sort_values(\"total_neto\", ascending=False)\n)\nprint(resumen.head())"
      }
    ],
    "quiz": null
  }
];
