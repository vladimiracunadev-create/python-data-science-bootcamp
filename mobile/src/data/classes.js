export const CLASSES = [
  {
    "id": "00-diagnostico-inicial",
    "number": 0,
    "title": "Diagnostico inicial y orientacion",
    "description": "Prueba corta de 30 preguntas para medir base tecnica y ordenar el arranque del bootcamp.",
    "duration": "15 min",
    "level": "Diagnostico",
    "colabUrl": null,
    "topics": [
      "Python basico",
      "Lectura de tablas",
      "Graficos",
      "Modelado inicial",
      "Habitos de trabajo"
    ],
    "theory": "Diagnostico breve, correccion inmediata y acuerdo sobre la ruta de aprendizaje. Estimar el punto de partida del grupo antes de iniciar la ruta formal.",
    "outcomes": [
      "Identificar fortalezas iniciales.",
      "Detectar vacios de apoyo.",
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
      "title": "Diagnostico inicial del bootcamp",
      "description": "30 preguntas de opcion multiple para estimar el nivel de entrada en 15 minutos.",
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
          "prompt": "¿Por qué se separan train y test?",
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
    "title": "Python fundamentos",
    "description": "Variables, tipos, colecciones y control de flujo aplicados a datos simples.",
    "duration": "90 min",
    "level": "Basico",
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-bootcamp/blob/master/classes/01-python-fundamentos/notebook.ipynb",
    "topics": [
      "Variables y tipos",
      "Listas y diccionarios",
      "Funciones",
      "Control de flujo"
    ],
    "theory": "Construir confianza en la sintaxis y conectar cada estructura con un uso real. Comprender los bloques basicos de Python y usarlos en tareas pequenas con datos.",
    "outcomes": [
      "Crear variables claras.",
      "Usar listas y diccionarios.",
      "Escribir funciones simples."
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
        "title": "Funcion con validacion simple",
        "explanation": "La funcion encapsula una tarea reutilizable y evita errores con una validacion minima.",
        "schema": "entrada -> validar -> calcular -> devolver",
        "language": "python",
        "code": "def calcular_promedio(notas):\n    # Evitamos dividir por cero si la lista esta vacia.\n    if len(notas) == 0:\n        return 0\n\n    total = sum(notas)\n    return total / len(notas)\n\nprint(calcular_promedio([6.0, 6.5, 7.0]))"
      }
    ],
    "quiz": null
  },
  {
    "id": "02-pandas-limpieza-datos",
    "number": 2,
    "title": "Pandas y limpieza de datos",
    "description": "Carga de CSV, inspeccion inicial y limpieza de tablas para preparar analisis confiables.",
    "duration": "90 min",
    "level": "Basico",
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-bootcamp/blob/master/classes/02-pandas-limpieza-datos/notebook.ipynb",
    "topics": [
      "DataFrame",
      "head/info",
      "Nulos",
      "Renombrado de columnas"
    ],
    "theory": "Instalar la idea de que no se analiza una tabla sin revisarla primero. Usar pandas para cargar, inspeccionar y limpiar tablas antes de analizarlas.",
    "outcomes": [
      "Cargar un CSV.",
      "Detectar problemas de calidad.",
      "Aplicar limpiezas justificadas."
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
        "title": "Carga e inspeccion de un CSV",
        "explanation": "Primero abrimos el archivo y luego lo inspeccionamos para saber si podemos confiar en su estructura.",
        "schema": "cargar -> mirar forma -> revisar columnas",
        "language": "python",
        "code": "import pandas as pd\n\n# Cargamos el CSV en un DataFrame para trabajar por columnas.\ndf = pd.read_csv(\"datasets/ventas_tienda.csv\")\n\nprint(df.head())\nprint(df.shape)\nprint(df.info())"
      }
    ],
    "quiz": null
  },
  {
    "id": "03-visualizacion-exploratoria",
    "number": 3,
    "title": "Visualizacion exploratoria",
    "description": "Graficos iniciales para detectar patrones y abrir preguntas nuevas a partir de una tabla limpia.",
    "duration": "90 min",
    "level": "Basico",
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-bootcamp/blob/master/classes/03-visualizacion-exploratoria/notebook.ipynb",
    "topics": [
      "Barras",
      "Histogramas",
      "Series temporales basicas",
      "Lectura de patrones"
    ],
    "theory": "La visualizacion exploratoria ayuda a mirar y preguntar mejor. Usar visualizaciones exploratorias para describir patrones y abrir nuevas preguntas de analisis.",
    "outcomes": [
      "Elegir un grafico inicial adecuado.",
      "Comparar categorias.",
      "Describir hallazgos sin exagerar."
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
        "title": "Ventas por categoria",
        "explanation": "Agrupamos antes de graficar porque queremos comparar categorias, no filas sueltas.",
        "schema": "agrupar -> ordenar -> graficar",
        "language": "python",
        "code": "import pandas as pd\nimport matplotlib.pyplot as plt\n\ndf = pd.read_csv(\"datasets/ventas_tienda.csv\")\nresumen = df.groupby(\"categoria\", as_index=False)[\"total_neto\"].sum()\nresumen = resumen.sort_values(\"total_neto\", ascending=False)\n\nresumen.plot.bar(x=\"categoria\", y=\"total_neto\", legend=False)\nplt.title(\"Ventas netas por categoria\")\nplt.tight_layout()"
      }
    ],
    "quiz": null
  },
  {
    "id": "04-estadistica-descriptiva",
    "number": 4,
    "title": "Estadistica descriptiva",
    "description": "Medidas de tendencia central y dispersion para apoyar decisiones iniciales.",
    "duration": "90 min",
    "level": "Intermedio",
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-bootcamp/blob/master/classes/04-estadistica-descriptiva/notebook.ipynb",
    "topics": [
      "Media y mediana",
      "Conteos",
      "Dispersion simple",
      "Resumen por grupo"
    ],
    "theory": "Pasar de mirar valores sueltos a resumir poblaciones con una pregunta clara. Interpretar medidas descriptivas simples y relacionarlas con preguntas reales.",
    "outcomes": [
      "Calcular resumenes utiles.",
      "Comparar segmentos.",
      "Explicar que aporta cada medida."
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
        "title": "Resumen general de una columna",
        "explanation": "Usamos varias medidas juntas para no depender de un unico numero.",
        "schema": "seleccionar variable -> calcular resumen -> interpretar",
        "language": "python",
        "code": "import pandas as pd\n\ndf = pd.read_csv(\"datasets/retencion_clientes.csv\")\ncolumna = df[\"clientes_activos\"]\n\nprint(\"Media:\", columna.mean())\nprint(\"Mediana:\", columna.median())\nprint(\"Desv. estandar:\", columna.std())"
      }
    ],
    "quiz": null
  },
  {
    "id": "05-visualizacion-con-matplotlib",
    "number": 5,
    "title": "Visualizacion con matplotlib",
    "description": "Graficos mas controlados con titulos, ejes y anotaciones pensadas para comunicar.",
    "duration": "90 min",
    "level": "Intermedio",
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-bootcamp/blob/master/classes/05-visualizacion-con-matplotlib/notebook.ipynb",
    "topics": [
      "Figure y Axes",
      "Titulos y ejes",
      "Subplots",
      "Anotaciones"
    ],
    "theory": "Pasar de la grafica funcional a la grafica comunicable. Crear graficos mas controlados con matplotlib y mejorar su legibilidad.",
    "outcomes": [
      "Construir figuras manualmente.",
      "Rotular con sentido.",
      "Comparar paneles sin ruido."
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
        "title": "Grafico de linea legible",
        "explanation": "Creamos una figura explicita para controlar tamano, titulo y ejes.",
        "schema": "crear figure -> dibujar -> rotular",
        "language": "python",
        "code": "import pandas as pd\nimport matplotlib.pyplot as plt\n\ndf = pd.read_csv(\"datasets/transporte.csv\")\nresumen = df.groupby(\"mes\", as_index=False)[\"pasajeros\"].sum()\n\nfig, ax = plt.subplots(figsize=(10, 4))\nax.plot(resumen[\"mes\"], resumen[\"pasajeros\"], marker=\"o\")\nax.set_title(\"Pasajeros por mes\")\nax.set_xlabel(\"Mes\")\nax.set_ylabel(\"Pasajeros\")\nplt.tight_layout()"
      }
    ],
    "quiz": null
  },
  {
    "id": "06-texto-fechas-y-transformaciones",
    "number": 6,
    "title": "Texto, fechas y transformaciones",
    "description": "Limpieza de texto, manejo de fechas y variables derivadas para enriquecer analisis.",
    "duration": "90 min",
    "level": "Intermedio",
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-bootcamp/blob/master/classes/06-texto-fechas-y-transformaciones/notebook.ipynb",
    "topics": [
      "Strings con pandas",
      "to_datetime",
      "Componentes de fecha",
      "Variables derivadas"
    ],
    "theory": "Muchas preguntas nuevas aparecen cuando una columna se transforma bien. Transformar columnas de texto y fecha para volverlas utiles en analisis y modelado inicial.",
    "outcomes": [
      "Normalizar texto.",
      "Convertir fechas.",
      "Crear columnas derivadas utiles."
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
        "title": "Conversion de fechas y variables derivadas",
        "explanation": "Convertir a fecha habilita nuevas preguntas como comportamiento por mes o dia de semana.",
        "schema": "convertir fecha -> extraer componente -> usar",
        "language": "python",
        "code": "import pandas as pd\n\ntickets = pd.read_csv(\"datasets/soporte_tickets.csv\")\ntickets[\"fecha_creacion\"] = pd.to_datetime(tickets[\"fecha_creacion\"])\n\n# Creamos columnas nuevas para responder preguntas posteriores.\ntickets[\"mes\"] = tickets[\"fecha_creacion\"].dt.month\ntickets[\"dia_semana\"] = tickets[\"fecha_creacion\"].dt.day_name()\n\nprint(tickets[[\"fecha_creacion\", \"mes\", \"dia_semana\"]].head())"
      }
    ],
    "quiz": null
  },
  {
    "id": "07-mini-proyecto-guiado",
    "number": 7,
    "title": "Mini proyecto guiado",
    "description": "Primer flujo completo: definir pregunta, limpiar, analizar, visualizar y concluir.",
    "duration": "90 min",
    "level": "Intermedio",
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-bootcamp/blob/master/classes/07-mini-proyecto-guiado/notebook.ipynb",
    "topics": [
      "Pregunta analitica",
      "Flujo reproducible",
      "Seleccion de variables",
      "Conclusiones"
    ],
    "theory": "Dejar de pensar la clase como tecnicas sueltas y verla como un proceso coherente. Integrar las habilidades vistas hasta ahora en un mini proyecto guiado de principio a fin.",
    "outcomes": [
      "Definir una pregunta acotada.",
      "Organizar un flujo claro.",
      "Cerrar con evidencia."
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
        "title": "Pregunta y recorte de trabajo",
        "explanation": "Antes de calcular, recortamos columnas y dejamos visible la pregunta del proyecto.",
        "schema": "pregunta -> columnas utiles -> base de trabajo",
        "language": "python",
        "code": "import pandas as pd\n\ndf = pd.read_csv(\"datasets/ventas_tienda.csv\")\n\n# Pregunta del proyecto: ¿que categorias concentran mayor venta neta?\ncolumnas = [\"fecha\", \"categoria\", \"region\", \"total_neto\"]\nproyecto = df[columnas].copy()\nprint(proyecto.head())"
      }
    ],
    "quiz": null
  },
  {
    "id": "08-presentacion-de-hallazgos",
    "number": 8,
    "title": "Presentacion de hallazgos",
    "description": "Conversion de analisis en mensajes claros y defendibles para otras personas.",
    "duration": "90 min",
    "level": "Intermedio",
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-bootcamp/blob/master/classes/08-presentacion-de-hallazgos/notebook.ipynb",
    "topics": [
      "Storytelling con datos",
      "Resumen ejecutivo",
      "Mensajes clave",
      "Visuales de apoyo"
    ],
    "theory": "La calidad del analisis tambien depende de como se explica y a quien se dirige. Transformar resultados tecnicos en una historia corta, clara y defendible.",
    "outcomes": [
      "Ordenar una historia de analisis.",
      "Elegir visuales que sostengan un mensaje.",
      "Escribir conclusiones ejecutivas."
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
        "title": "Resumen ejecutivo en pocas lineas",
        "explanation": "Aunque no sea un grafico, este bloque muestra como traducir el analisis a una salida legible.",
        "schema": "hallazgo -> importancia -> recomendacion",
        "language": "python",
        "code": "hallazgo = \"La region norte concentra la mayor venta neta del periodo.\"\nimportancia = \"Esto sugiere una oportunidad para profundizar disponibilidad y promocion.\"\nrecomendacion = \"Comparar margen y stock antes de escalar la decision.\"\n\nprint(hallazgo)\nprint(importancia)\nprint(recomendacion)"
      }
    ],
    "quiz": null
  },
  {
    "id": "09-machine-learning-intro",
    "number": 9,
    "title": "Introduccion a machine learning",
    "description": "Primer modelo predictivo con scikit-learn para entender features, target y evaluacion inicial.",
    "duration": "90 min",
    "level": "Intermedio",
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-bootcamp/blob/master/classes/09-machine-learning-intro/notebook.ipynb",
    "topics": [
      "Aprendizaje supervisado",
      "Features y target",
      "train/test split",
      "Regresion lineal"
    ],
    "theory": "Mostrar machine learning como extension del analisis, no como magia negra. Comprender que es un modelo supervisado y construir una primera regresion simple con scikit-learn.",
    "outcomes": [
      "Identificar X e y.",
      "Separar train y test.",
      "Leer una metrica de error inicial."
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
        "title": "Preparacion de variables y split",
        "explanation": "Definimos columnas de entrada y la variable objetivo antes de entrenar.",
        "schema": "problema -> X / y -> train/test",
        "language": "python",
        "code": "import pandas as pd\nfrom sklearn.model_selection import train_test_split\n\ndf = pd.read_csv(\"datasets/ventas_tienda.csv\")\nX = df[[\"precio_unitario\", \"unidades_vendidas\", \"descuento_pct\"]]\ny = df[\"total_neto\"]\n\nX_train, X_test, y_train, y_test = train_test_split(\n    X, y, test_size=0.2, random_state=42\n)"
      }
    ],
    "quiz": null
  },
  {
    "id": "10-modelos-supervisados",
    "number": 10,
    "title": "Modelos supervisados",
    "description": "Comparacion inicial entre regresion y clasificacion, con metricas acordes al problema.",
    "duration": "90 min",
    "level": "Intermedio-Avanzado",
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-bootcamp/blob/master/classes/10-modelos-supervisados/notebook.ipynb",
    "topics": [
      "Regresion vs clasificacion",
      "Arboles",
      "Regresion logistica",
      "Metricas"
    ],
    "theory": "Elegir modelo y metrica por la pregunta, no por popularidad. Comparar modelos supervisados basicos y elegir metricas segun el tipo de problema.",
    "outcomes": [
      "Diferenciar familias de problema.",
      "Entrenar un modelo simple.",
      "Interpretar metricas clave."
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
        "title": "Clasificacion basica con arbol",
        "explanation": "Convertimos un problema en una etiqueta binaria y entrenamos un modelo simple e interpretable.",
        "schema": "crear etiqueta -> entrenar -> predecir",
        "language": "python",
        "code": "import pandas as pd\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.tree import DecisionTreeClassifier\n\ndf = pd.read_csv(\"datasets/ventas_tienda.csv\")\ndf[\"venta_alta\"] = (df[\"total_neto\"] >= df[\"total_neto\"].median()).astype(int)\n\nX = df[[\"precio_unitario\", \"unidades_vendidas\", \"descuento_pct\"]]\ny = df[\"venta_alta\"]\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n\narbol = DecisionTreeClassifier(max_depth=4, random_state=42)\narbol.fit(X_train, y_train)"
      }
    ],
    "quiz": null
  },
  {
    "id": "11-evaluacion-y-pipelines",
    "number": 11,
    "title": "Evaluacion y pipelines",
    "description": "Validacion cruzada, pipeline y busqueda de hiperparametros para medir modelos con mas rigor.",
    "duration": "90 min",
    "level": "Avanzado",
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-bootcamp/blob/master/classes/11-evaluacion-y-pipelines/notebook.ipynb",
    "topics": [
      "Cross-validation",
      "Overfitting",
      "Pipelines",
      "GridSearchCV"
    ],
    "theory": "Pasar de un modelo que parece funcionar a un flujo de evaluacion mas confiable. Evaluar modelos con mayor rigor y evitar leakage o sobreajuste.",
    "outcomes": [
      "Detectar overfitting inicial.",
      "Aplicar validacion cruzada.",
      "Construir un pipeline simple."
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
        "title": "Pipeline con validacion cruzada",
        "explanation": "El pipeline encapsula escalado y modelo, y la validacion cruzada entrega una medida menos fragil.",
        "schema": "pipeline -> CV -> score medio",
        "language": "python",
        "code": "import pandas as pd\nfrom sklearn.model_selection import cross_val_score\nfrom sklearn.pipeline import Pipeline\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.linear_model import LogisticRegression\n\ndf = pd.read_csv(\"datasets/retencion_clientes.csv\")\nX = df[[\"clientes_activos\", \"clientes_perdidos\"]]\ny = (df[\"clientes_perdidos\"] > df[\"clientes_perdidos\"].median()).astype(int)\n\npipe = Pipeline([(\"scaler\", StandardScaler()), (\"model\", LogisticRegression(max_iter=300))])\nscores = cross_val_score(pipe, X, y, cv=5, scoring=\"f1\")\nprint(scores.mean())"
      }
    ],
    "quiz": null
  },
  {
    "id": "12-proyecto-final-y-cierre",
    "number": 12,
    "title": "Proyecto final y cierre",
    "description": "Integracion de todo el bootcamp en un caso final con entregable claro, defensa breve y proyeccion.",
    "duration": "90 min",
    "level": "Integrador",
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-bootcamp/blob/master/classes/12-proyecto-final-y-cierre/notebook.ipynb",
    "topics": [
      "Pregunta final",
      "Flujo completo",
      "Entregable integrador",
      "Defensa breve"
    ],
    "theory": "Cerrar con evidencia de aprendizaje integrado, no con una lista de tecnicas desconectadas. Integrar las habilidades del bootcamp en un proyecto final acotado y defendible.",
    "outcomes": [
      "Definir una pregunta final realista.",
      "Ordenar notebook y entregables.",
      "Justificar decisiones tecnicas."
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
        "title": "Esqueleto del proyecto final",
        "explanation": "El codigo organiza el proyecto por etapas para que otra persona siga el razonamiento sin perderse.",
        "schema": "contexto -> carga -> analisis -> conclusion",
        "language": "python",
        "code": "import pandas as pd\n\n# 1. Cargar datos y dejar una copia de trabajo.\ndf = pd.read_csv(\"datasets/ventas_tienda.csv\")\ntrabajo = df.copy()\n\n# 2. Formular una pregunta visible antes de seguir.\npregunta = \"¿Que categoria conviene reforzar en la proxima campana?\"\nprint(pregunta)"
      }
    ],
    "quiz": null
  }
];
