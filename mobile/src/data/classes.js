// ============================================================
// CLASES DEL BOOTCAMP PYTHON DATA SCIENCE
// Archivo embebido: no requiere servidor. Todo el contenido
// esta aqui para uso offline.
// ============================================================

const BASE_COLAB = 'https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-bootcamp/blob/master/classes';

export const CLASSES = [
  // ─────────────────────────────────────────────────────────
  // CLASE 01 — PYTHON FUNDAMENTOS
  // ─────────────────────────────────────────────────────────
  {
    id: '01-python-fundamentos',
    number: 1,
    title: 'Python Fundamentos',
    description: 'Variables, tipos de datos, listas, diccionarios, funciones y control de flujo',
    duration: '90 min',
    level: 'Basico',
    colabUrl: `${BASE_COLAB}/01-python-fundamentos/notebook.ipynb`,
    topics: [
      'Variables y tipos de datos',
      'Listas y diccionarios',
      'Funciones basicas',
      'Control de flujo (if/for/while)',
    ],
    theory: `Python es un lenguaje interpretado de alto nivel, ideal para ciencia de datos. Su sintaxis es legible y concisa. No necesitas declarar tipos de variables: Python los infiere automaticamente segun el valor que asignes.\n\nEn esta clase aprenderemos los bloques fundamentales que usaremos en todo el bootcamp.`,
    codeExamples: [
      {
        id: 'c01-ex1',
        title: 'Variables y tipos de datos',
        explanation:
          'En Python no necesitas declarar el tipo. Python lo infiere automaticamente segun el valor asignado. Esto se llama tipado dinamico.',
        schema: 'variable = valor  →  Python infiere el tipo automaticamente',
        code: `# === VARIABLES Y TIPOS DE DATOS ===
# Python es dinamicamente tipado: el tipo se asigna segun el valor

nombre = "Ana"          # str: cadena de texto (entre comillas simples o dobles)
edad = 17               # int: numero entero (sin decimales)
promedio = 6.8          # float: numero con decimales
activo = True           # bool: verdadero o falso (mayuscula obligatoria)
sin_valor = None        # NoneType: representa ausencia de valor

# --- Verificar el tipo de una variable ---
# type() es una funcion integrada que devuelve la clase del objeto
print(type(nombre))     # → <class 'str'>
print(type(edad))       # → <class 'int'>
print(type(promedio))   # → <class 'float'>
print(type(activo))     # → <class 'bool'>

# --- Conversion entre tipos (casting) ---
# A veces necesitas convertir un tipo a otro explicitamente
edad_texto = str(edad)        # int → str: "17"
edad_decimal = float(edad)    # int → float: 17.0
texto_numero = int("42")      # str → int: 42 (solo si el string es numerico)

print(edad_texto, type(edad_texto))    # → "17" <class 'str'>
print(edad_decimal, type(edad_decimal))# → 17.0 <class 'float'>

# --- f-strings: la forma moderna de formatear texto ---
# Se usa f antes de las comillas, y las variables van entre {}
mensaje = f"Hola {nombre}, tienes {edad} años y tu promedio es {promedio}"
print(mensaje)  # → Hola Ana, tienes 17 años y tu promedio es 6.8`,
        language: 'python',
      },
      {
        id: 'c01-ex2',
        title: 'Listas y diccionarios',
        explanation:
          'Las listas guardan elementos en orden. Los diccionarios guardan pares clave-valor. Son las estructuras de datos mas usadas en Python.',
        schema: 'lista = [elem1, elem2]   /   diccionario = {"clave": valor}',
        code: `# === LISTAS ===
# Una lista es una coleccion ordenada y mutable (se puede modificar)
# Se define con corchetes []

notas = [6.5, 7.0, 5.8, 8.2, 6.0]   # lista de floats

# Acceder por indice (empieza en 0)
print(notas[0])    # → 6.5 (primer elemento)
print(notas[-1])   # → 6.0 (ultimo elemento, indice negativo)
print(notas[1:3])  # → [7.0, 5.8] (slice: desde indice 1 hasta 3 sin incluirlo)

# Metodos utiles de lista
notas.append(9.0)      # agrega al final: [6.5, 7.0, 5.8, 8.2, 6.0, 9.0]
notas.sort()           # ordena de menor a mayor: [5.8, 6.0, 6.5, 7.0, 8.2, 9.0]
print(len(notas))      # → 6 (cantidad de elementos)
print(sum(notas))      # → suma todos los numeros

# List comprehension: crear lista nueva con una expresion
aprobados = [n for n in notas if n >= 6.0]  # filtra notas >= 6
print(aprobados)  # → [6.0, 6.5, 7.0, 8.2, 9.0]

# === DICCIONARIOS ===
# Un diccionario almacena pares clave:valor, como un formulario
estudiante = {
    "nombre": "Ana",      # clave: "nombre", valor: "Ana"
    "edad": 17,           # clave: "edad", valor: 17
    "notas": [6.5, 7.0],  # el valor puede ser cualquier tipo, incluso una lista
    "activo": True
}

# Acceder por clave
print(estudiante["nombre"])          # → "Ana"
print(estudiante.get("edad", 0))     # → 17 (.get evita error si clave no existe)

# Agregar o modificar
estudiante["ciudad"] = "Concepcion"  # agrega nueva clave
estudiante["edad"] = 18              # modifica valor existente

# Iterar sobre el diccionario
for clave, valor in estudiante.items():
    print(f"  {clave}: {valor}")`,
        language: 'python',
      },
      {
        id: 'c01-ex3',
        title: 'Funciones basicas',
        explanation:
          'Las funciones agrupan codigo reutilizable. Se definen con def, reciben parametros y pueden devolver valores con return.',
        schema: 'def nombre_funcion(parametros):  →  bloque de codigo  →  return resultado',
        code: `# === FUNCIONES EN PYTHON ===
# Una funcion es un bloque de codigo reutilizable
# Se define con 'def', seguido del nombre y parentesis con parametros

def saludar(nombre):
    """
    Docstring: documentacion de la funcion (buena practica).
    Devuelve un saludo personalizado.
    """
    saludo = f"Hola, {nombre}!"  # crea el mensaje
    return saludo                 # devuelve el resultado (sin return = None)

# Llamar la funcion
mensaje = saludar("Ana")
print(mensaje)  # → "Hola, Ana!"

# --- Parametros con valor por defecto ---
# Si no se pasa el argumento, usa el valor por defecto
def calcular_promedio(notas, redondear=2):
    """Calcula el promedio de una lista de notas."""
    if len(notas) == 0:          # validacion: lista vacia
        return 0
    total = sum(notas)           # sum() suma todos los elementos
    promedio = total / len(notas) # len() cuenta los elementos
    return round(promedio, redondear)  # round() redondea decimales

mis_notas = [6.5, 7.0, 5.8, 8.2]
print(calcular_promedio(mis_notas))       # → 6.88 (redondea a 2 decimales)
print(calcular_promedio(mis_notas, 0))    # → 7.0 (sin decimales)

# --- Multiples valores de retorno ---
# Python puede devolver una tupla (varios valores a la vez)
def estadisticas(notas):
    """Devuelve maximo, minimo y promedio de una lista."""
    return max(notas), min(notas), sum(notas)/len(notas)

maximo, minimo, prom = estadisticas(mis_notas)
print(f"Max: {maximo}, Min: {minimo}, Prom: {prom:.2f}")`,
        language: 'python',
      },
      {
        id: 'c01-ex4',
        title: 'Control de flujo',
        explanation:
          'if/elif/else para condiciones, for para iterar sobre secuencias, while para repetir mientras se cumpla una condicion.',
        schema: 'if condicion:  /  for item in secuencia:  /  while condicion:',
        code: `# === CONTROL DE FLUJO ===

# --- IF / ELIF / ELSE ---
# Ejecuta bloques segun condiciones
nota = 6.8

if nota >= 7.0:
    calificacion = "Notable"         # se ejecuta si nota >= 7.0
elif nota >= 6.0:                    # si no, comprueba esta condicion
    calificacion = "Suficiente"      # nota entre 6.0 y 6.9
elif nota >= 4.0:
    calificacion = "Reprobado"       # nota entre 4.0 y 5.9
else:
    calificacion = "Muy deficiente"  # cualquier otro caso

print(f"Nota: {nota} → {calificacion}")  # → Nota: 6.8 → Suficiente

# --- FOR LOOP ---
# Itera sobre cada elemento de una secuencia (lista, string, range, etc.)
nombres = ["Ana", "Luis", "Maria", "Pedro"]

for nombre in nombres:              # 'nombre' toma el valor de cada elemento
    print(f"  Procesando: {nombre}")

# range(start, stop, step) genera una secuencia numerica
for i in range(0, 10, 2):          # 0, 2, 4, 6, 8 (de 0 a 9 de 2 en 2)
    print(i, end=" ")               # end=" " imprime en la misma linea
print()  # salto de linea al final

# enumerate: obtener indice y valor al mismo tiempo
for indice, nombre in enumerate(nombres, start=1):
    print(f"  {indice}. {nombre}")  # → 1. Ana, 2. Luis, ...

# --- WHILE LOOP ---
# Repite mientras la condicion sea True
contador = 0
while contador < 5:
    print(f"  Contador: {contador}")
    contador += 1    # equivale a contador = contador + 1

# CUIDADO: un while sin actualizacion = bucle infinito
# Siempre asegurate de que la condicion eventualmente sea False`,
        language: 'python',
      },
    ],
    exercises: [
      {
        id: 'c01-ej1',
        title: 'Calculadora de promedio',
        description:
          'Crea una funcion que reciba una lista de notas y devuelva: promedio, nota maxima, nota minima, y si el estudiante aprobo (promedio >= 6.0).',
        hint: 'Usa sum(), max(), min(), len() y un return con multiple valores.',
        starterCode: `def analizar_notas(notas):
    # Tu codigo aqui
    pass

# Prueba tu funcion
notas_ejemplo = [6.5, 7.0, 5.8, 8.2, 6.0]
resultado = analizar_notas(notas_ejemplo)
print(resultado)`,
      },
    ],
  },

  // ─────────────────────────────────────────────────────────
  // CLASE 02 — PANDAS Y LIMPIEZA DE DATOS
  // ─────────────────────────────────────────────────────────
  {
    id: '02-pandas-limpieza',
    number: 2,
    title: 'Pandas y Limpieza de Datos',
    description: 'Cargar, explorar y limpiar datasets con pandas: nulos, duplicados y transformaciones basicas',
    duration: '90 min',
    level: 'Basico',
    colabUrl: `${BASE_COLAB}/02-pandas-limpieza/notebook.ipynb`,
    topics: [
      'Cargar CSV con read_csv',
      'Explorar con info, describe, shape',
      'Manejar valores nulos (isnull, dropna, fillna)',
      'Eliminar duplicados',
    ],
    theory: `Pandas es la libreria principal para manipulacion de datos en Python. Su estructura central es el DataFrame, una tabla bidimensional con filas y columnas etiquetadas. Pandas permite cargar, explorar, limpiar y transformar datos de manera eficiente.\n\nLa limpieza de datos es el paso mas importante en cualquier analisis: datos sucios producen resultados erroneos.`,
    codeExamples: [
      {
        id: 'c02-ex1',
        title: 'Cargar y explorar un dataset',
        explanation:
          'El primer paso en cualquier analisis es cargar los datos y entender su estructura: cuantas filas, columnas, tipos de datos y si hay valores nulos.',
        schema: 'pd.read_csv("archivo.csv")  →  DataFrame  →  .info() / .describe() / .head()',
        code: `# === CARGAR Y EXPLORAR DATOS CON PANDAS ===
import pandas as pd   # convencion: alias 'pd' para pandas

# pd.read_csv lee un archivo CSV y lo convierte en un DataFrame
# Un DataFrame es como una hoja de Excel: filas = registros, columnas = variables
df = pd.read_csv("ventas_tienda.csv")

# .shape devuelve (filas, columnas) como tupla
print(f"Dimensiones: {df.shape}")    # → (500, 8): 500 filas, 8 columnas
print(f"Filas: {df.shape[0]}")       # accede al primer elemento de la tupla
print(f"Columnas: {df.shape[1]}")    # accede al segundo elemento

# .columns muestra los nombres de todas las columnas
print("Columnas:", df.columns.tolist())  # → ['fecha', 'producto', 'precio', ...]

# .head(n) muestra las primeras n filas (por defecto 5)
# Util para ver el formato y valores reales del dataset
print(df.head(5))

# .tail(n) muestra las ultimas n filas
print(df.tail(3))

# .info() da un resumen completo:
# - nombre y tipo de cada columna
# - cuantos valores no-nulos hay
# - uso de memoria del DataFrame
df.info()

# .describe() calcula estadisticas descriptivas de columnas numericas:
# count, mean, std, min, 25%, 50%, 75%, max
df.describe()`,
        language: 'python',
      },
      {
        id: 'c02-ex2',
        title: 'Detectar y manejar valores nulos',
        explanation:
          'Los valores nulos (NaN) son un problema comun en datasets reales. Pandas tiene funciones especificas para detectarlos, contarlos y manejarlos.',
        schema: 'isnull() → detectar  /  dropna() → eliminar  /  fillna(valor) → rellenar',
        code: `# === MANEJO DE VALORES NULOS (NaN) ===
# NaN = Not a Number: representa un valor ausente o desconocido

# --- Detectar nulos ---
# .isnull() devuelve True/False por cada celda
nulos = df.isnull()  # DataFrame de True/False

# .isnull().sum() cuenta los True (nulos) por columna
print("Nulos por columna:")
print(df.isnull().sum())  # → columna1: 0, columna2: 15, ...

# Porcentaje de nulos (mas informativo)
print("Porcentaje de nulos:")
porcentaje_nulos = (df.isnull().sum() / len(df)) * 100
print(porcentaje_nulos.round(2))   # redondea a 2 decimales

# --- Eliminar filas con nulos ---
# dropna() por defecto elimina cualquier fila que tenga al menos un NaN
df_sin_nulos = df.dropna()
print(f"Filas originales: {len(df)}")
print(f"Filas sin nulos: {len(df_sin_nulos)}")

# dropna(subset=['col']) solo elimina si esa columna especifica tiene NaN
df_sin_nulos_precio = df.dropna(subset=['precio'])

# --- Rellenar nulos con un valor ---
# fillna(valor) reemplaza NaN con el valor especificado
df['precio'] = df['precio'].fillna(0)           # reemplaza con 0
df['ciudad'] = df['ciudad'].fillna('Desconocida') # reemplaza con texto

# Rellenar con la media o mediana (muy comun en datos numericos)
media_precio = df['precio'].mean()               # calcula la media
df['precio'] = df['precio'].fillna(media_precio) # rellena con la media
print(f"Media usada para relleno: {media_precio:.2f}")`,
        language: 'python',
      },
      {
        id: 'c02-ex3',
        title: 'Eliminar duplicados y filtrar datos',
        explanation:
          'Los duplicados pueden sesgar el analisis. Pandas permite detectarlos y eliminarlos facilmente. Tambien podemos filtrar filas segun condiciones.',
        schema: 'duplicated() → detectar  /  drop_duplicates() → eliminar  /  df[condicion] → filtrar',
        code: `# === DUPLICADOS Y FILTROS ===

# --- Detectar duplicados ---
# .duplicated() devuelve True para filas repetidas (menos la primera)
duplicados = df.duplicated()
print(f"Filas duplicadas: {duplicados.sum()}")  # cuantas hay

# Ver las filas duplicadas
print(df[duplicados])  # muestra solo las filas duplicadas

# --- Eliminar duplicados ---
# .drop_duplicates() elimina filas que son identicas en TODAS las columnas
df_unico = df.drop_duplicates()
print(f"Antes: {len(df)} filas  |  Despues: {len(df_unico)} filas")

# drop_duplicates(subset=['col1','col2']) solo considera esas columnas
df_unico_id = df.drop_duplicates(subset=['id_venta'])

# --- Filtrar filas con condiciones ---
# Similar al WHERE en SQL
# Condicion simple: una columna cumple un criterio
ventas_caras = df[df['precio'] > 50000]    # precio mayor a 50000
print(f"Ventas sobre $50.000: {len(ventas_caras)}")

# Condicion multiple: usa & (AND) y | (OR) con parentesis
ventas_filtradas = df[
    (df['precio'] > 10000) &        # precio mayor a 10000 Y
    (df['categoria'] == 'Electro')  # categoria igual a 'Electro'
]
print(f"Ventas caras de Electro: {len(ventas_filtradas)}")

# .isin() filtra por una lista de valores permitidos
categorias_ok = ['Electro', 'Ropa', 'Hogar']
df_filtrado = df[df['categoria'].isin(categorias_ok)]`,
        language: 'python',
      },
      {
        id: 'c02-ex4',
        title: 'Seleccionar y renombrar columnas',
        explanation:
          'Podemos seleccionar subconjuntos de columnas para trabajar con menos datos, y renombrar columnas para que tengan nombres mas claros.',
        schema: 'df["col"]  →  Serie   /   df[["col1","col2"]]  →  DataFrame',
        code: `# === SELECCION Y RENOMBRADO DE COLUMNAS ===

# --- Seleccionar una columna ---
# Devuelve una Serie (como una lista con indice)
precios = df['precio']         # Serie con todos los precios
print(type(precios))           # → <class 'pandas.core.series.Series'>
print(precios.head())          # primeros 5 valores

# --- Seleccionar multiples columnas ---
# Devuelve un DataFrame (sub-tabla)
sub_df = df[['producto', 'precio', 'cantidad']]
print(sub_df.head())

# --- Renombrar columnas ---
# .rename() con un diccionario {nombre_viejo: nombre_nuevo}
df = df.rename(columns={
    'prod_name': 'producto',      # renombra 'prod_name' a 'producto'
    'unit_price': 'precio',       # renombra 'unit_price' a 'precio'
    'qty_sold': 'cantidad'        # renombra 'qty_sold' a 'cantidad'
})

# Renombrar TODAS las columnas de una vez con una lista
# (la lista debe tener el mismo numero de elementos que columnas)
df.columns = ['fecha', 'producto', 'precio', 'cantidad', 'categoria', 'ciudad']

# Convertir todos los nombres a minusculas (buena practica)
df.columns = df.columns.str.lower()    # .str aplica operaciones de string
df.columns = df.columns.str.strip()    # elimina espacios al inicio/fin

# --- Agregar columna calculada ---
# Podemos crear nuevas columnas a partir de las existentes
df['total_venta'] = df['precio'] * df['cantidad']  # nueva columna calculada
print(df[['producto', 'precio', 'cantidad', 'total_venta']].head())`,
        language: 'python',
      },
    ],
    exercises: [
      {
        id: 'c02-ej1',
        title: 'Pipeline de limpieza',
        description:
          'Carga el dataset, cuenta los nulos por columna, elimina las filas con mas del 50% de nulos, rellena los restantes con la media (numericos) o "Desconocido" (texto), y elimina duplicados.',
        hint: 'Combina isnull().sum(), dropna(thresh=...), fillna() y drop_duplicates()',
        starterCode: `import pandas as pd

df = pd.read_csv("datos_sucios.csv")

# Paso 1: Explorar nulos
# Tu codigo aqui

# Paso 2: Eliminar filas muy incompletas
# Tu codigo aqui

# Paso 3: Rellenar nulos restantes
# Tu codigo aqui

# Paso 4: Eliminar duplicados
# Tu codigo aqui

print("Limpieza completada:", df.shape)`,
      },
    ],
  },

  // ─────────────────────────────────────────────────────────
  // CLASE 03 — VISUALIZACION EXPLORATORIA
  // ─────────────────────────────────────────────────────────
  {
    id: '03-visualizacion-exploratoria',
    number: 3,
    title: 'Visualizacion Exploratoria',
    description: 'Scatter, histogramas y boxplots directamente con pandas para entender la distribucion de los datos',
    duration: '90 min',
    level: 'Basico',
    colabUrl: `${BASE_COLAB}/03-visualizacion-exploratoria/notebook.ipynb`,
    topics: [
      'Scatter plot (dispersion)',
      'Histograma (distribucion)',
      'Boxplot (cuartiles y outliers)',
      'Grafico de barras (categorias)',
    ],
    theory: `La visualizacion exploratoria (EDA - Exploratory Data Analysis) es fundamental para entender los datos antes de modelar. Los graficos permiten detectar patrones, outliers y relaciones que los numeros solos no muestran.\n\nPandas incluye metodos .plot() directamente en los DataFrames, haciendo muy sencillo crear visualizaciones rapidas.`,
    codeExamples: [
      {
        id: 'c03-ex1',
        title: 'Scatter plot: relacion entre variables',
        explanation:
          'El grafico de dispersion muestra si dos variables numericas estan relacionadas. Si los puntos forman una linea, hay correlacion.',
        schema: 'df.plot.scatter(x="col1", y="col2")  →  correlacion visual',
        code: `# === SCATTER PLOT (DISPERSION) ===
import pandas as pd
import matplotlib.pyplot as plt   # pyplot es el modulo de graficos

df = pd.read_csv("ventas_tienda.csv")

# --- Scatter basico ---
# .plot.scatter() grafica dos variables numericas
# x: variable del eje horizontal
# y: variable del eje vertical
df.plot.scatter(
    x='precio',         # eje X: precio del producto
    y='cantidad',       # eje Y: cantidad vendida
    figsize=(8, 5),     # tamaño del grafico: (ancho, alto) en pulgadas
    alpha=0.5,          # transparencia de los puntos (0=invisible, 1=solido)
    color='steelblue',  # color de los puntos
    title='Precio vs Cantidad vendida'
)
plt.xlabel('Precio ($)')    # etiqueta eje X
plt.ylabel('Cantidad')      # etiqueta eje Y
plt.tight_layout()          # ajusta margenes automaticamente
plt.show()                  # muestra el grafico (en Colab aparece solo)

# --- Scatter con color por categoria ---
# Usando matplotlib directamente para mas control
fig, ax = plt.subplots(figsize=(9, 6))  # crea figura y ejes

# Colores diferentes por categoria
colores = {'Electro': 'blue', 'Ropa': 'red', 'Hogar': 'green'}
for categoria, grupo in df.groupby('categoria'):
    ax.scatter(
        grupo['precio'],      # x de este grupo
        grupo['cantidad'],    # y de este grupo
        label=categoria,      # etiqueta para la leyenda
        alpha=0.6,
        color=colores.get(categoria, 'gray')
    )

ax.legend()                           # muestra la leyenda
ax.set_title('Precio vs Cantidad por Categoria')
plt.show()`,
        language: 'python',
      },
      {
        id: 'c03-ex2',
        title: 'Histograma: distribucion de una variable',
        explanation:
          'El histograma muestra como se distribuyen los valores de una variable. Permite ver si los datos son normales, sesgados o tienen varios picos.',
        schema: 'df["col"].plot.hist(bins=20)  →  distribucion de frecuencias',
        code: `# === HISTOGRAMA ===
# Un histograma agrupa los valores en intervalos (bins) y cuenta cuantos hay en cada uno

# --- Histograma simple ---
df['precio'].plot.hist(
    bins=20,            # numero de barras/intervalos (mas bins = mas detalle)
    figsize=(8, 5),
    color='steelblue',
    edgecolor='white',  # borde blanco entre barras (facilita lectura)
    title='Distribucion de Precios'
)
plt.xlabel('Precio ($)')
plt.ylabel('Frecuencia (cantidad de ventas)')
plt.show()

# --- Histograma con linea de densidad ---
# Para ver la forma de la distribucion mas suavemente
ax = df['precio'].plot.hist(bins=30, figsize=(8, 5), density=True, alpha=0.7)
# density=True normaliza para que el area = 1 (probabilidad)

# Agregar linea KDE (Kernel Density Estimate) encima
df['precio'].plot.kde(ax=ax, color='red', linewidth=2)
# KDE = estimacion suave de la distribucion

plt.title('Distribucion de Precios (con KDE)')
plt.xlabel('Precio ($)')
plt.show()

# --- Multiples histogramas ---
# Ver la distribucion de varias columnas a la vez
df[['precio', 'cantidad', 'total_venta']].plot.hist(
    bins=15,
    figsize=(12, 4),
    subplots=True,     # un subplot por columna
    layout=(1, 3),     # 1 fila, 3 columnas
    sharex=False       # cada grafico tiene su propio eje X
)
plt.tight_layout()
plt.show()`,
        language: 'python',
      },
      {
        id: 'c03-ex3',
        title: 'Boxplot: cuartiles y outliers',
        explanation:
          'El boxplot muestra la mediana, cuartiles y valores atipicos (outliers) de una variable. Es ideal para comparar distribuciones entre grupos.',
        schema: 'caja: Q1 a Q3  /  linea central: mediana  /  puntos: outliers',
        code: `# === BOXPLOT ===
# Anatomia del boxplot:
# - Linea central: mediana (Q2, percentil 50)
# - Caja inferior: Q1 (percentil 25)
# - Caja superior: Q3 (percentil 75)
# - Bigotes: hasta 1.5 * IQR (rango intercuartilico)
# - Puntos fuera de bigotes: OUTLIERS (valores atipicos)

# --- Boxplot simple ---
df['precio'].plot.box(
    figsize=(6, 6),
    title='Distribucion de Precios'
)
plt.ylabel('Precio ($)')
plt.show()

# --- Boxplot por grupos (muy informativo) ---
# Compara la distribucion del precio en cada categoria
df.boxplot(
    column='precio',        # variable a analizar
    by='categoria',         # variable de agrupacion
    figsize=(10, 6),
    grid=False              # sin grilla para un look mas limpio
)
plt.suptitle('')            # elimina el titulo automatico feo de pandas
plt.title('Precio por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Precio ($)')
plt.tight_layout()
plt.show()

# --- Detectar outliers con IQR ---
Q1 = df['precio'].quantile(0.25)   # percentil 25
Q3 = df['precio'].quantile(0.75)   # percentil 75
IQR = Q3 - Q1                      # rango intercuartilico

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers = df[(df['precio'] < limite_inferior) | (df['precio'] > limite_superior)]
print(f"Outliers detectados: {len(outliers)} ({len(outliers)/len(df)*100:.1f}%)")
print(f"Rango normal: ${limite_inferior:.0f} - ${limite_superior:.0f}")`,
        language: 'python',
      },
    ],
    exercises: [
      {
        id: 'c03-ej1',
        title: 'EDA completo',
        description:
          'Carga un dataset, crea un histograma de la variable principal, un boxplot por categoria, y un scatter entre dos variables relacionadas. Agrega titulos y etiquetas a cada grafico.',
        hint: 'Usa subplots para mostrar varios graficos en una sola figura.',
        starterCode: `import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ventas.csv")

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Histograma en axes[0]
# Tu codigo aqui

# Boxplot en axes[1]
# Tu codigo aqui

# Scatter en axes[2]
# Tu codigo aqui

plt.tight_layout()
plt.show()`,
      },
    ],
  },

  // ─────────────────────────────────────────────────────────
  // CLASE 04 — ESTADISTICA DESCRIPTIVA
  // ─────────────────────────────────────────────────────────
  {
    id: '04-estadistica-descriptiva',
    number: 4,
    title: 'Estadistica Descriptiva',
    description: 'Media, mediana, desviacion estandar, percentiles y correlacion entre variables',
    duration: '90 min',
    level: 'Basico',
    colabUrl: `${BASE_COLAB}/04-estadistica-descriptiva/notebook.ipynb`,
    topics: [
      'Tendencia central (media, mediana, moda)',
      'Dispersion (std, varianza, rango)',
      'Percentiles y cuartiles',
      'Correlacion (Pearson)',
    ],
    theory: `La estadistica descriptiva resume y describe las caracteristicas de un dataset. No busca hacer inferencias ni predicciones, solo describir lo que hay.\n\nLas dos preguntas clave son: donde estan los datos (tendencia central) y cuanto varian (dispersion).`,
    codeExamples: [
      {
        id: 'c04-ex1',
        title: 'Medidas de tendencia central',
        explanation:
          'La media es el promedio, la mediana es el valor del medio, y la moda es el mas frecuente. Cuando hay outliers, la mediana es mas representativa.',
        schema: 'mean() → promedio  /  median() → valor central  /  mode() → mas frecuente',
        code: `# === TENDENCIA CENTRAL ===
import pandas as pd
import numpy as np   # numpy: libreria de calculo numerico

df = pd.read_csv("ventas_tienda.csv")
precios = df['precio']

# --- MEDIA (promedio aritmetico) ---
# Suma todos los valores y divide por la cantidad
media = precios.mean()
print(f"Media: ${media:.2f}")     # → Media: $45.230,50

# --- MEDIANA (valor del medio) ---
# Ordena los valores y toma el del centro
# Si hay numero par de valores, promedia los dos centrales
mediana = precios.median()
print(f"Mediana: ${mediana:.2f}") # → Mediana: $32.000,00

# Si media > mediana → distribucion sesgada a la derecha (valores altos alejan la media)
# Si media ≈ mediana → distribucion simetrica (normal)
print(f"Sesgo: {'Derecha' if media > mediana else 'Izquierda o Simetrica'}")

# --- MODA (valor mas frecuente) ---
# Util para variables categoricas o discretas
moda = precios.mode()
print(f"Moda: {moda.values}")    # puede haber mas de una moda

# Para variables categoricas
moda_categoria = df['categoria'].mode()[0]  # [0] toma el primer resultado
print(f"Categoria mas vendida: {moda_categoria}")

# --- DESCRIBE: resumen completo ---
# Calcula varias estadisticas de una vez para columnas numericas
print(df.describe())
#        precio    cantidad  total_venta
# count  500.00     500.00      500.00
# mean  45230.50    3.20    144737.60
# std   38450.20    2.15    198520.30
# min    1200.00    1.00      1200.00
# 25%   12000.00    1.00     12000.00
# 50%   32000.00    3.00     72000.00
# 75%   68000.00    5.00    240000.00
# max  250000.00   10.00   2500000.00`,
        language: 'python',
      },
      {
        id: 'c04-ex2',
        title: 'Dispersion y percentiles',
        explanation:
          'La dispersion mide cuanto varian los datos respecto a la media. Los percentiles dividen los datos en partes iguales y son clave para detectar outliers.',
        schema: 'std() → desviacion  /  quantile(0.25) → Q1  /  quantile(0.75) → Q3',
        code: `# === DISPERSION Y PERCENTILES ===

precios = df['precio']

# --- DESVIACION ESTANDAR ---
# Mide cuanto se alejan los datos de la media en promedio
# Mayor std = datos mas dispersos/variados
std = precios.std()
media = precios.mean()
print(f"Media: ${media:.0f}  |  Std: ${std:.0f}")
print(f"Rango tipico: ${media-std:.0f} a ${media+std:.0f}")  # ±1 std

# --- VARIANZA ---
# Es el cuadrado de la desviacion estandar
# Menos intuitiva pero usada en formulas estadisticas
varianza = precios.var()
print(f"Varianza: {varianza:.0f}")  # mismo numero pero al cuadrado

# --- RANGO ---
rango = precios.max() - precios.min()  # diferencia entre extremos
print(f"Rango: ${precios.min():.0f} a ${precios.max():.0f} (diferencia: ${rango:.0f})")

# --- PERCENTILES ---
# El percentil P significa que P% de los datos estan por debajo de ese valor
p25 = precios.quantile(0.25)   # 25% de los precios estan por debajo de esto
p50 = precios.quantile(0.50)   # = mediana
p75 = precios.quantile(0.75)   # 75% de los precios estan por debajo
p90 = precios.quantile(0.90)   # 90% de los precios estan por debajo
p99 = precios.quantile(0.99)   # el 1% mas caro esta por encima de este precio

print(f"Q1 (P25): ${p25:.0f}")
print(f"Q2 (P50): ${p50:.0f}")
print(f"Q3 (P75): ${p75:.0f}")
print(f"P90:      ${p90:.0f}")
print(f"P99:      ${p99:.0f}")

# IQR = Rango Intercuartilico = Q3 - Q1
# Contiene el 50% central de los datos
IQR = p75 - p25
print(f"IQR: ${IQR:.0f}")

# Percentiles multiples de una vez
cuantiles = precios.quantile([0.1, 0.25, 0.5, 0.75, 0.9])
print(cuantiles)`,
        language: 'python',
      },
      {
        id: 'c04-ex3',
        title: 'Correlacion entre variables',
        explanation:
          'La correlacion de Pearson mide la relacion lineal entre dos variables numericas. Va de -1 (inversa perfecta) a +1 (directa perfecta). 0 = sin relacion lineal.',
        schema: 'r = 1: correlacion perfecta  /  r = 0: sin correlacion  /  r = -1: inversa',
        code: `# === CORRELACION ===
import seaborn as sns   # libreria para visualizaciones estadisticas

# --- Correlacion entre dos variables ---
# .corr() calcula el coeficiente de correlacion de Pearson
r = df['precio'].corr(df['cantidad'])
print(f"Correlacion precio-cantidad: {r:.4f}")
# r > 0.7: correlacion fuerte positiva
# r < -0.7: correlacion fuerte negativa
# |r| < 0.3: correlacion debil

# Interpretar el resultado
if abs(r) > 0.7:
    interpretacion = "FUERTE"
elif abs(r) > 0.4:
    interpretacion = "MODERADA"
else:
    interpretacion = "DEBIL"
print(f"La correlacion es {interpretacion} y {'POSITIVA' if r > 0 else 'NEGATIVA'}")

# --- Matriz de correlacion ---
# Calcula correlacion entre TODAS las columnas numericas a la vez
columnas_numericas = df.select_dtypes(include='number')  # solo numericas
matriz = columnas_numericas.corr()
print(matriz.round(3))

# --- Visualizar la matriz como mapa de calor (heatmap) ---
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
sns.heatmap(
    matriz,
    annot=True,       # muestra los numeros en cada celda
    fmt='.2f',        # formato: 2 decimales
    cmap='coolwarm',  # azul (negativo) → blanco (0) → rojo (positivo)
    center=0,         # 0 en el centro de la escala de color
    linewidths=0.5    # separador entre celdas
)
plt.title('Matriz de Correlacion')
plt.tight_layout()
plt.show()

# La diagonal siempre es 1.0 (cada variable correlaciona perfectamente consigo misma)
# Busca valores cercanos a 1 o -1 fuera de la diagonal`,
        language: 'python',
      },
    ],
    exercises: [
      {
        id: 'c04-ej1',
        title: 'Reporte estadistico',
        description:
          'Genera un reporte que muestre: media, mediana y moda de la columna precio; la correlacion entre precio y cantidad; y los 5 productos con precio mas alto.',
        hint: 'Usa .describe(), .corr() y .nlargest()',
        starterCode: `import pandas as pd

df = pd.read_csv("ventas.csv")

# 1. Estadisticas basicas de precio
# Tu codigo aqui

# 2. Correlacion precio-cantidad
# Tu codigo aqui

# 3. Top 5 productos mas caros
# Tu codigo aqui`,
      },
    ],
  },

  // ─────────────────────────────────────────────────────────
  // CLASE 05 — VISUALIZACION CON MATPLOTLIB
  // ─────────────────────────────────────────────────────────
  {
    id: '05-visualizacion-matplotlib',
    number: 5,
    title: 'Visualizacion con Matplotlib',
    description: 'Subplots, titulos, colores, estilos y guardar graficos profesionales con matplotlib',
    duration: '90 min',
    level: 'Intermedio',
    colabUrl: `${BASE_COLAB}/05-visualizacion-matplotlib/notebook.ipynb`,
    topics: [
      'Anatomia de una figura matplotlib',
      'Subplots (multiples graficos)',
      'Personalizar colores y estilos',
      'Guardar graficos como imagen',
    ],
    theory: `Matplotlib es la libreria de graficos mas usada en Python. Permite un control total sobre cada elemento del grafico: titulos, colores, fuentes, escalas, leyendas, etc.\n\nLa interfaz orientada a objetos (fig, ax) es la forma recomendada para graficos complejos.`,
    codeExamples: [
      {
        id: 'c05-ex1',
        title: 'Anatomia de una figura',
        explanation:
          'En matplotlib: Figure es el lienzo completo. Axes (ax) es cada area de graficado. Entender esta distincion es clave para personalizar graficos.',
        schema: 'plt.subplots() → (fig, ax)  /  ax.plot() → datos  /  ax.set_title() → titulo',
        code: `# === ANATOMIA DE MATPLOTLIB ===
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("ventas_tienda.csv")

# --- Interfaz orientada a objetos (recomendada) ---
# fig: la figura completa (el lienzo/canvas)
# ax: los ejes donde se grafica (puede haber varios en una figura)
fig, ax = plt.subplots(figsize=(9, 5))  # figsize en pulgadas (ancho, alto)

# Graficar datos en el eje
ventas_por_mes = df.groupby('mes')['total_venta'].sum()  # suma por mes
ax.plot(
    ventas_por_mes.index,   # eje X: meses
    ventas_por_mes.values,  # eje Y: total de ventas
    color='#22c55e',        # color en formato hex
    linewidth=2,            # grosor de la linea
    marker='o',             # marcador en cada punto
    markersize=6,           # tamaño del marcador
    linestyle='-'           # tipo de linea: '-', '--', ':', '-.'
)

# Personalizar el grafico
ax.set_title('Ventas Totales por Mes', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Mes', fontsize=12)
ax.set_ylabel('Total Ventas ($)', fontsize=12)
ax.tick_params(axis='x', rotation=45)  # rota etiquetas del eje X 45 grados
ax.grid(True, linestyle='--', alpha=0.5)  # grilla suave

# Agregar linea de referencia (promedio)
promedio = ventas_por_mes.mean()
ax.axhline(y=promedio, color='red', linestyle='--', label=f'Promedio: ${promedio:,.0f}')
ax.legend(fontsize=11)   # muestra la leyenda

fig.tight_layout()  # ajusta margenes para que nada se corte
plt.show()`,
        language: 'python',
      },
      {
        id: 'c05-ex2',
        title: 'Subplots: multiples graficos en una figura',
        explanation:
          'plt.subplots(nrows, ncols) crea una cuadricula de graficos. Ideal para comparar diferentes aspectos de los datos en un solo vistazo.',
        schema: 'fig, axes = plt.subplots(2, 2)  →  cuadricula de 4 graficos',
        code: `# === SUBPLOTS ===
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("ventas_tienda.csv")

# Crear figura con 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
# axes es un array de 2x2: axes[0,0], axes[0,1], axes[1,0], axes[1,1]

fig.suptitle('Analisis Exploratorio de Ventas', fontsize=18, fontweight='bold')

# --- Subplot 1: Histograma de precios ---
axes[0, 0].hist(df['precio'], bins=20, color='steelblue', edgecolor='white')
axes[0, 0].set_title('Distribucion de Precios')
axes[0, 0].set_xlabel('Precio ($)')
axes[0, 0].set_ylabel('Frecuencia')

# --- Subplot 2: Ventas por categoria ---
ventas_cat = df.groupby('categoria')['total_venta'].sum().sort_values()
axes[0, 1].barh(ventas_cat.index, ventas_cat.values, color='#22c55e')
# barh = barras horizontales (mejor cuando los nombres son largos)
axes[0, 1].set_title('Total Ventas por Categoria')
axes[0, 1].set_xlabel('Total ($)')

# --- Subplot 3: Scatter precio vs cantidad ---
axes[1, 0].scatter(df['precio'], df['cantidad'], alpha=0.3, color='#f59e0b', s=20)
# s=20 define el tamaño de cada punto
axes[1, 0].set_title('Precio vs Cantidad')
axes[1, 0].set_xlabel('Precio ($)')
axes[1, 0].set_ylabel('Cantidad vendida')

# --- Subplot 4: Linea temporal ---
ventas_dia = df.groupby('fecha')['total_venta'].sum()
axes[1, 1].plot(ventas_dia.index, ventas_dia.values, color='#ef4444', linewidth=1)
axes[1, 1].set_title('Ventas Diarias')
axes[1, 1].set_xlabel('Fecha')
axes[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('analisis_exploratorio.png', dpi=150, bbox_inches='tight')  # guarda el grafico
plt.show()`,
        language: 'python',
      },
      {
        id: 'c05-ex3',
        title: 'Estilos y graficos de barras',
        explanation:
          'Los graficos de barras son ideales para comparar categorias. Matplotlib permite personalizar colores, agregar etiquetas de valor y cambiar el estilo del fondo.',
        schema: 'ax.bar(x, height) → barras verticales  /  ax.barh(y, width) → horizontales',
        code: `# === GRAFICOS DE BARRAS PROFESIONALES ===
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("ventas_tienda.csv")

# Calcular datos para graficar
top_productos = df.groupby('producto')['total_venta'].sum().nlargest(8)
# nlargest(8) = los 8 productos con mayor total

# --- Estilo del grafico ---
plt.style.use('dark_background')  # tema oscuro (o 'seaborn-v0_8', 'ggplot', etc.)

fig, ax = plt.subplots(figsize=(10, 6))

# Barras con degradado de color (lista de colores)
colores = plt.cm.RdYlGn(  # paleta rojo-amarillo-verde
    [i/len(top_productos) for i in range(len(top_productos))]
)

barras = ax.barh(
    top_productos.index,    # etiquetas en eje Y
    top_productos.values,   # valores en eje X
    color=colores,
    height=0.6,             # grosor de las barras
    edgecolor='white',
    linewidth=0.5
)

# Agregar etiquetas con el valor exacto en cada barra
for barra, valor in zip(barras, top_productos.values):
    ax.text(
        valor + max(top_productos) * 0.01,  # posicion X: un poco despues de la barra
        barra.get_y() + barra.get_height() / 2,  # posicion Y: centro de la barra
        f'${valor/1e6:.1f}M',               # texto: formato millones
        va='center',                         # alineacion vertical
        fontsize=10,
        color='white'
    )

ax.set_title('Top 8 Productos por Ventas Totales', fontsize=15, fontweight='bold')
ax.set_xlabel('Total de Ventas ($)')
ax.spines['top'].set_visible(False)     # oculta borde superior
ax.spines['right'].set_visible(False)   # oculta borde derecho
plt.tight_layout()
plt.savefig('top_productos.png', dpi=150, bbox_inches='tight')
plt.show()`,
        language: 'python',
      },
    ],
    exercises: [
      {
        id: 'c05-ej1',
        title: 'Dashboard de ventas',
        description:
          'Crea una figura 2x2 con: grafico de linea (ventas por mes), grafico de barras (top 5 categorias), histograma (distribucion de precios) y pie chart (participacion de mercado por ciudad). Agrega titulos y colores consistentes.',
        hint: 'Usa ax.pie() para el pie chart. Los colores pueden ser una lista de strings hex.',
        starterCode: `import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("ventas.csv")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Dashboard de Ventas', fontsize=20, fontweight='bold')

# Grafico 1: linea temporal
# Tu codigo aqui

# Grafico 2: barras por categoria
# Tu codigo aqui

# Grafico 3: histograma de precios
# Tu codigo aqui

# Grafico 4: pie chart por ciudad
# Tu codigo aqui

plt.tight_layout()
plt.show()`,
      },
    ],
  },

  // ─────────────────────────────────────────────────────────
  // CLASE 06 — TEXTO, FECHAS Y TRANSFORMACIONES
  // ─────────────────────────────────────────────────────────
  {
    id: '06-texto-fechas-transformaciones',
    number: 6,
    title: 'Texto, Fechas y Transformaciones',
    description: 'Operaciones con strings, to_datetime, groupby/agg y transformaciones avanzadas de datos',
    duration: '90 min',
    level: 'Intermedio',
    colabUrl: `${BASE_COLAB}/06-texto-fechas-transformaciones/notebook.ipynb`,
    topics: [
      'Operaciones con strings (str accessor)',
      'Fechas con to_datetime',
      'groupby y agg',
      'apply y lambda',
    ],
    theory: `Muchos datasets del mundo real contienen fechas como texto y columnas de texto que necesitan limpieza. Pandas tiene dos accesorios especiales: .str para strings y .dt para fechas.\n\nGroupby es una de las herramientas mas poderosas: agrupa los datos y aplica funciones de agregacion (suma, promedio, conteo) a cada grupo.`,
    codeExamples: [
      {
        id: 'c06-ex1',
        title: 'Operaciones con strings',
        explanation:
          'El accessor .str de pandas permite aplicar operaciones de texto a toda una columna a la vez, sin usar bucles.',
        schema: 'df["col"].str.lower()  /  .str.contains()  /  .str.split()  /  .str.replace()',
        code: `# === OPERACIONES CON STRINGS ===
import pandas as pd

df = pd.read_csv("ventas_tienda.csv")

# El accessor .str permite operaciones de texto en toda la columna
# Similar a aplicar str.metodo() a cada elemento

# --- Limpieza basica ---
df['producto'] = df['producto'].str.lower()   # todo a minusculas
df['producto'] = df['producto'].str.strip()   # eliminar espacios inicio/fin
df['ciudad'] = df['ciudad'].str.upper()       # todo a mayusculas
df['ciudad'] = df['ciudad'].str.title()       # Primera Letra De Cada Palabra

# --- Buscar y reemplazar ---
# .contains() devuelve True/False para filtrar
electro_mask = df['producto'].str.contains('tv|computador|celular', case=False)
# case=False = no distingue mayusculas/minusculas
# '|' funciona como OR en expresiones regulares
df_electro = df[electro_mask]
print(f"Productos electronicos: {len(df_electro)}")

# .replace() reemplaza texto exacto
df['categoria'] = df['categoria'].str.replace('Electrodomesticos', 'Electro')

# --- Extraer partes del texto ---
# .split() divide por un separador
# expand=True crea columnas separadas
df[['dia', 'mes', 'año']] = df['fecha'].str.split('/', expand=True)

# .len() cuenta caracteres
df['largo_nombre'] = df['producto'].str.len()

# .startswith() / .endswith()
df_chile = df[df['ciudad'].str.startswith('San')]  # ciudades que empiezan con San

# --- Extraer con expresiones regulares ---
# .extract() captura grupos usando regex
df['cod_producto'] = df['sku'].str.extract(r'([A-Z]{3}-\\d{4})')
# r'...' = raw string (la barra invertida no se interpreta)
# [A-Z]{3} = 3 letras mayusculas
# \\d{4} = 4 digitos`,
        language: 'python',
      },
      {
        id: 'c06-ex2',
        title: 'Fechas con to_datetime',
        explanation:
          'Pandas puede convertir texto a fechas reales. Con el accessor .dt puedes extraer año, mes, dia, dia de la semana y mucho mas.',
        schema: 'pd.to_datetime("col") → datetime  /  .dt.year  /  .dt.month  /  .dt.dayofweek',
        code: `# === FECHAS Y TIEMPOS ===
import pandas as pd

df = pd.read_csv("ventas_tienda.csv")

# --- Convertir texto a fecha ---
# Sin conversion: la columna 'fecha' es texto (string)
print(df['fecha'].dtype)  # → object (texto)

# pd.to_datetime() convierte texto a tipo datetime
df['fecha'] = pd.to_datetime(df['fecha'])
print(df['fecha'].dtype)  # → datetime64[ns]

# Si el formato no es estandar, especificarlo
df['fecha'] = pd.to_datetime(df['fecha'], format='%d/%m/%Y')
# %d = dia, %m = mes, %Y = año con 4 digitos

# --- Extraer componentes con .dt ---
# .dt es el accessor para columnas de tipo datetime
df['año'] = df['fecha'].dt.year          # 2023, 2024, etc.
df['mes'] = df['fecha'].dt.month         # 1 a 12
df['dia'] = df['fecha'].dt.day           # 1 a 31
df['dia_semana'] = df['fecha'].dt.dayofweek  # 0=Lunes, 6=Domingo
df['nombre_mes'] = df['fecha'].dt.month_name()  # 'January', 'February', etc.
df['trimestre'] = df['fecha'].dt.quarter  # 1 a 4

# --- Operaciones con fechas ---
# Diferencia entre fechas (da un timedelta)
df['fecha_entrega'] = pd.to_datetime(df['fecha_entrega'])
df['dias_entrega'] = (df['fecha_entrega'] - df['fecha']).dt.days
print(f"Dias promedio de entrega: {df['dias_entrega'].mean():.1f}")

# Filtrar por rango de fechas
desde = pd.Timestamp('2024-01-01')
hasta = pd.Timestamp('2024-06-30')
df_h1 = df[(df['fecha'] >= desde) & (df['fecha'] <= hasta)]
print(f"Ventas primer semestre 2024: {len(df_h1)}")

# Agrupar por mes
ventas_mensuales = df.groupby(df['fecha'].dt.to_period('M'))['total_venta'].sum()
print(ventas_mensuales)  # indice: 2024-01, 2024-02, etc.`,
        language: 'python',
      },
      {
        id: 'c06-ex3',
        title: 'GroupBy y agregacion',
        explanation:
          'groupby divide el DataFrame en grupos segun una columna, y agg aplica funciones de agregacion a cada grupo. Es el equivalente del GROUP BY de SQL.',
        schema: 'df.groupby("col").agg({"num_col": ["sum","mean","count"]})',
        code: `# === GROUPBY Y AGG ===
import pandas as pd

df = pd.read_csv("ventas_tienda.csv")

# --- GroupBy simple ---
# Agrupa por categoria y calcula la suma de ventas en cada grupo
ventas_por_cat = df.groupby('categoria')['total_venta'].sum()
print(ventas_por_cat.sort_values(ascending=False))

# --- Multiples funciones de agregacion ---
# .agg() recibe un diccionario: columna → lista de funciones
resumen = df.groupby('categoria').agg(
    total_ventas=('total_venta', 'sum'),       # suma de ventas
    promedio_precio=('precio', 'mean'),        # precio promedio
    cantidad_total=('cantidad', 'sum'),        # cantidad total vendida
    num_transacciones=('id_venta', 'count'),   # cuantas ventas hay
    precio_max=('precio', 'max')               # precio maximo
)
print(resumen.round(2))

# --- GroupBy con multiples columnas ---
# Analizar por categoria Y mes
ventas_cat_mes = df.groupby(['categoria', 'mes'])['total_venta'].sum().reset_index()
# reset_index() convierte los grupos en columnas normales (no indices jerarquicos)
print(ventas_cat_mes.head(10))

# --- Pivot table: como una tabla dinamica de Excel ---
tabla = df.pivot_table(
    values='total_venta',    # que queremos calcular
    index='mes',             # filas
    columns='categoria',     # columnas
    aggfunc='sum',           # funcion de agregacion
    fill_value=0             # reemplaza NaN con 0 donde no hay datos
)
print(tabla)`,
        language: 'python',
      },
    ],
    exercises: [
      {
        id: 'c06-ej1',
        title: 'Analisis temporal',
        description:
          'Convierte la columna fecha a datetime, extrae mes y año, agrupa por mes para calcular total de ventas y ticket promedio, y grafica la evolucion mensual.',
        hint: 'Usa to_datetime(), .dt.month, groupby() y plot.bar()',
        starterCode: `import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ventas.csv")

# 1. Convertir fecha
# Tu codigo aqui

# 2. Extraer mes y año
# Tu codigo aqui

# 3. Agrupar por mes
# Tu codigo aqui

# 4. Graficar
# Tu codigo aqui`,
      },
    ],
  },

  // ─────────────────────────────────────────────────────────
  // CLASE 07 — MINI PROYECTO GUIADO
  // ─────────────────────────────────────────────────────────
  {
    id: '07-mini-proyecto-guiado',
    number: 7,
    title: 'Mini Proyecto Guiado',
    description: 'Analisis completo de datos de ventas: desde la carga hasta las conclusiones y recomendaciones',
    duration: '120 min',
    level: 'Intermedio',
    colabUrl: `${BASE_COLAB}/07-mini-proyecto-guiado/notebook.ipynb`,
    topics: [
      'Pipeline completo de EDA',
      'Preguntas de negocio',
      'Visualizaciones combinadas',
      'Conclusiones y recomendaciones',
    ],
    theory: `Este mini proyecto integra todo lo aprendido en las clases anteriores. Seguimos el proceso real de un analista de datos:\n\n1. Entender el negocio y formular preguntas\n2. Cargar y explorar los datos\n3. Limpiar y transformar\n4. Analizar y visualizar\n5. Concluir y recomendar\n\nEl dataset es ventas_tienda.csv con 500 registros de una tienda ficticia chilena.`,
    codeExamples: [
      {
        id: 'c07-ex1',
        title: 'Paso 1: Carga y exploracion inicial',
        explanation:
          'El primer paso es siempre entender que tenemos. Cargamos los datos y hacemos una inspeccion completa antes de tocar nada.',
        schema: 'Cargar → Dimensiones → Tipos → Nulos → Estadisticas → Primeras filas',
        code: `# === MINI PROYECTO: ANALISIS DE VENTAS TIENDA ===
# Dataset: ventas_tienda.csv
# Preguntas que queremos responder:
# 1. ¿Cuales son los productos mas vendidos?
# 2. ¿En que meses se vende mas?
# 3. ¿Que ciudad genera mas ingresos?
# 4. ¿Hay correlacion entre precio y cantidad vendida?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 50)
print("PASO 1: CARGA Y EXPLORACION")
print("=" * 50)

# Cargamos el dataset
df = pd.read_csv("ventas_tienda.csv")

# --- Inspeccion basica ---
print(f"\\nDimensiones: {df.shape[0]} filas x {df.shape[1]} columnas")
print(f"\\nColumnas: {list(df.columns)}")

# Tipos de datos de cada columna
print("\\nTipos de datos:")
print(df.dtypes)

# Valores nulos
print("\\nValores nulos por columna:")
nulos = df.isnull().sum()
print(nulos[nulos > 0])  # muestra solo columnas con nulos

# Estadisticas basicas de columnas numericas
print("\\nEstadisticas descriptivas:")
print(df.describe().round(2))

# Vista previa
print("\\nPrimeras 5 filas:")
print(df.head())

print("\\n✓ Exploracion completada")`,
        language: 'python',
      },
      {
        id: 'c07-ex2',
        title: 'Paso 2: Limpieza y preparacion',
        explanation:
          'Antes de analizar, limpiamos: nulos, tipos de datos incorrectos, y creamos columnas derivadas utiles para el analisis.',
        schema: 'Nulos → Tipos → Duplicados → Columnas derivadas → Dataset limpio',
        code: `# === PASO 2: LIMPIEZA Y PREPARACION ===
print("=" * 50)
print("PASO 2: LIMPIEZA DE DATOS")
print("=" * 50)

# --- Convertir tipos ---
df['fecha'] = pd.to_datetime(df['fecha'])         # texto → fecha
df['precio'] = pd.to_numeric(df['precio'], errors='coerce')  # texto → numero
# errors='coerce': si no puede convertir, pone NaN en vez de error

# --- Limpiar texto ---
df['categoria'] = df['categoria'].str.strip().str.title()  # espacios y capitalizar
df['ciudad'] = df['ciudad'].str.strip().str.title()

# --- Manejar nulos (despues de convertir tipos) ---
print(f"Nulos despues de conversion: {df.isnull().sum().sum()}")

# Rellenar precio nulo con la mediana por categoria (mas preciso que la media global)
df['precio'] = df.groupby('categoria')['precio'].transform(
    lambda x: x.fillna(x.median())  # para cada categoria, rellena con su mediana
)

# --- Eliminar duplicados ---
antes = len(df)
df = df.drop_duplicates()
print(f"Duplicados eliminados: {antes - len(df)}")

# --- Crear columnas derivadas ---
df['total_venta'] = df['precio'] * df['cantidad']  # valor total de cada transaccion
df['mes'] = df['fecha'].dt.month                   # numero de mes
df['mes_nombre'] = df['fecha'].dt.strftime('%b')   # nombre abreviado del mes
df['año'] = df['fecha'].dt.year                    # año

print(f"\\nDataset limpio: {df.shape}")
print("\\n✓ Limpieza completada")`,
        language: 'python',
      },
      {
        id: 'c07-ex3',
        title: 'Paso 3: Analisis y visualizacion',
        explanation:
          'Respondemos las preguntas de negocio con analisis concretos y graficos claros. Cada grafico debe responder una pregunta especifica.',
        schema: 'Pregunta → Calculo → Visualizacion → Conclusion',
        code: `# === PASO 3: ANALISIS Y VISUALIZACION ===
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Analisis de Ventas - Resumen Ejecutivo', fontsize=16, fontweight='bold')

# --- Pregunta 1: Productos mas vendidos ---
top5 = df.groupby('producto')['cantidad'].sum().nlargest(5)
axes[0, 0].barh(top5.index, top5.values, color='#22c55e')
axes[0, 0].set_title('Top 5 Productos por Cantidad')
axes[0, 0].set_xlabel('Unidades vendidas')

# --- Pregunta 2: Ventas por mes ---
ventas_mes = df.groupby('mes')['total_venta'].sum()
axes[0, 1].plot(ventas_mes.index, ventas_mes.values,
                marker='o', color='#3b82f6', linewidth=2)
axes[0, 1].fill_between(ventas_mes.index, ventas_mes.values, alpha=0.2, color='#3b82f6')
axes[0, 1].set_title('Ingresos por Mes')
axes[0, 1].set_xlabel('Mes')
axes[0, 1].set_ylabel('Total ($)')

# --- Pregunta 3: Ciudad con mas ingresos ---
ingresos_ciudad = df.groupby('ciudad')['total_venta'].sum().nlargest(6)
colores_ciudad = plt.cm.Blues(
    [0.4 + i*0.1 for i in range(len(ingresos_ciudad))]
)
axes[1, 0].bar(ingresos_ciudad.index, ingresos_ciudad.values, color=colores_ciudad)
axes[1, 0].set_title('Ingresos por Ciudad (Top 6)')
axes[1, 0].set_ylabel('Total ($)')
axes[1, 0].tick_params(axis='x', rotation=30)

# --- Pregunta 4: Precio vs Cantidad ---
axes[1, 1].scatter(df['precio'], df['cantidad'], alpha=0.2, color='#f59e0b', s=15)
correlacion = df['precio'].corr(df['cantidad'])
axes[1, 1].set_title(f'Precio vs Cantidad (r={correlacion:.3f})')
axes[1, 1].set_xlabel('Precio ($)')
axes[1, 1].set_ylabel('Cantidad')

plt.tight_layout()
plt.savefig('analisis_ventas.png', dpi=150, bbox_inches='tight')
plt.show()

print("\\n=== CONCLUSIONES ===")
print(f"Producto estrella: {top5.index[0]}")
print(f"Mes pico de ventas: {ventas_mes.idxmax()}")
print(f"Ciudad top: {ingresos_ciudad.index[0]}")
print(f"Correlacion precio-cantidad: {correlacion:.3f} (debil)")`,
        language: 'python',
      },
    ],
    exercises: [
      {
        id: 'c07-ej1',
        title: 'Extiende el analisis',
        description:
          'Agrega dos preguntas de negocio propias al analisis. Ejemplos: ¿Cual es el ticket promedio por ciudad? ¿Que categoria tiene mejor margen (mayor precio promedio)? Incluye el grafico y la conclusion de cada una.',
        hint: 'Usa groupby().agg() para calcular multiples metricas a la vez.',
        starterCode: `# Continuando el analisis del mini proyecto...
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ventas_tienda.csv")
# (aqui iria el pipeline de limpieza del Paso 2)

# Pregunta 5: Ticket promedio por ciudad
# Tu codigo aqui

# Pregunta 6: Tu pregunta propia
# Tu codigo aqui`,
      },
    ],
  },

  // ─────────────────────────────────────────────────────────
  // CLASE 08 — PRESENTACION DE HALLAZGOS
  // ─────────────────────────────────────────────────────────
  {
    id: '08-presentacion-hallazgos',
    number: 8,
    title: 'Presentacion de Hallazgos',
    description: 'Estructura de un informe de datos, storytelling, graficos para audiencias no tecnicas',
    duration: '90 min',
    level: 'Intermedio',
    colabUrl: `${BASE_COLAB}/08-presentacion-hallazgos/notebook.ipynb`,
    topics: [
      'Estructura de un informe de datos',
      'Storytelling con datos',
      'Graficos para no tecnicos',
      'Exportar a PDF/HTML',
    ],
    theory: `El analisis de datos solo tiene valor si se comunica efectivamente. Un hallazgo brillante que no se entiende no sirve de nada.\n\nEl storytelling con datos sigue esta estructura: Contexto → Conflicto → Solucion → Llamada a la accion.`,
    codeExamples: [
      {
        id: 'c08-ex1',
        title: 'Estructura de un informe',
        explanation:
          'Un informe de datos efectivo tiene secciones claras: resumen ejecutivo, hallazgos principales, analisis detallado y recomendaciones.',
        schema: 'Resumen → Hallazgos → Analisis → Recomendaciones → Apendice',
        code: `# === ESTRUCTURA DE UN INFORME DE DATOS ===
# Un informe efectivo sigue esta estructura:
#
# 1. RESUMEN EJECUTIVO (1 parrafo)
#    - ¿Que analizamos?
#    - ¿Cuales son los 3 hallazgos mas importantes?
#    - ¿Que se recomienda hacer?
#
# 2. HALLAZGOS PRINCIPALES (3-5 puntos)
#    - Cada hallazgo = 1 numero + 1 grafico + 1 conclusion
#
# 3. ANALISIS DETALLADO
#    - Metodologia
#    - Datos usados
#    - Limitaciones
#
# 4. RECOMENDACIONES
#    - Acciones concretas y medibles
#    - Prioridad alta / media / baja
#
# 5. APENDICE
#    - Tablas completas
#    - Codigo fuente

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

df = pd.read_csv("ventas_tienda.csv")
df['fecha'] = pd.to_datetime(df['fecha'])
df['total_venta'] = df['precio'] * df['cantidad']

# --- Calcular KPIs para el resumen ejecutivo ---
total_ingresos = df['total_venta'].sum()
ticket_promedio = df['total_venta'].mean()
num_transacciones = len(df)
producto_top = df.groupby('producto')['total_venta'].sum().idxmax()
ciudad_top = df.groupby('ciudad')['total_venta'].sum().idxmax()

print("=" * 60)
print("RESUMEN EJECUTIVO")
print("=" * 60)
print(f"Periodo analizado: {df['fecha'].min().date()} a {df['fecha'].max().date()}")
print(f"Total ingresos:    ${total_ingresos:,.0f}")
print(f"Transacciones:     {num_transacciones:,}")
print(f"Ticket promedio:   ${ticket_promedio:,.0f}")
print(f"\\nHALLAZGOS PRINCIPALES:")
print(f"  1. El producto '{producto_top}' lidera las ventas")
print(f"  2. '{ciudad_top}' es la ciudad con mayores ingresos")
print(f"  3. Las ventas muestran estacionalidad en Q4")
print(f"\\nRECOMENDACION: Aumentar stock de '{producto_top}' en '{ciudad_top}'")`,
        language: 'python',
      },
      {
        id: 'c08-ex2',
        title: 'Graficos para audiencias no tecnicas',
        explanation:
          'Los graficos para gerentes y clientes deben ser simples, con titulo claro que diga la conclusion, sin jerga tecnica, y con colores que guien la atencion.',
        schema: 'Titulo = conclusion  /  Un solo mensaje  /  Resalta lo importante',
        code: `# === GRAFICOS PARA NO TECNICOS ===
# Principios clave:
# 1. El TITULO del grafico debe ser la CONCLUSION, no la descripcion
#    Mal: "Ventas por mes"
#    Bien: "Las ventas de Q4 superaron en 40% al resto del año"
#
# 2. UN solo mensaje por grafico
# 3. Resalta con color lo mas importante
# 4. Elimina todo lo que no agrega informacion (menos es mas)

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("ventas_tienda.csv")
df['fecha'] = pd.to_datetime(df['fecha'])
df['total_venta'] = df['precio'] * df['cantidad']

ventas_mes = df.groupby(df['fecha'].dt.month)['total_venta'].sum()

# --- Grafico profesional para presentacion ---
fig, ax = plt.subplots(figsize=(12, 6))

# Colores: gris para contexto, verde vibrante para el mensaje principal
colores = ['#94a3b8' if m != ventas_mes.idxmax() else '#22c55e'
           for m in ventas_mes.index]

barras = ax.bar(ventas_mes.index, ventas_mes.values, color=colores, width=0.7)

# Titulo que ES la conclusion (no la descripcion)
ax.set_title(
    f"Diciembre fue el mes record con ${ventas_mes.max()/1e6:.1f}M en ventas",
    fontsize=15,
    fontweight='bold',
    pad=20
)

# Etiquetas solo en la barra mas importante
idx_max = ventas_mes.idxmax()
ax.text(
    idx_max, ventas_mes[idx_max] * 1.02,  # un poco arriba de la barra
    f"${ventas_mes[idx_max]/1e6:.1f}M",
    ha='center', fontsize=12, fontweight='bold', color='#22c55e'
)

# Eliminar elementos que no aportan (chartjunk)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.yaxis.set_visible(False)   # sin eje Y (los valores estan en las etiquetas)

nombres_mes = ['Ene','Feb','Mar','Abr','May','Jun',
               'Jul','Ago','Sep','Oct','Nov','Dic']
ax.set_xticks(range(1, 13))
ax.set_xticklabels(nombres_mes, fontsize=11)

plt.tight_layout()
plt.savefig('presentacion_ventas.png', dpi=200, bbox_inches='tight')
plt.show()`,
        language: 'python',
      },
    ],
    exercises: [
      {
        id: 'c08-ej1',
        title: 'Crea tu informe',
        description:
          'Escribe un resumen ejecutivo en markdown en un notebook, incluyendo: 3 KPIs clave, 2 graficos con titulo-conclusion, y 3 recomendaciones concretas y medibles.',
        hint: 'Usa celdas Markdown en Colab para el texto, y celdas de codigo para los graficos.',
        starterCode: `# Este ejercicio se realiza en Google Colab
# Crea las siguientes celdas en tu notebook:
#
# Celda 1 (Markdown):
# ## Resumen Ejecutivo
# **KPIs:** ...
# **Hallazgos:** ...
# **Recomendaciones:** ...
#
# Celda 2 (Codigo): Grafico 1 con titulo-conclusion
# Celda 3 (Codigo): Grafico 2 con titulo-conclusion`,
      },
    ],
  },

  // ─────────────────────────────────────────────────────────
  // CLASE 09 — MACHINE LEARNING INTRO
  // ─────────────────────────────────────────────────────────
  {
    id: '09-machine-learning-intro',
    number: 9,
    title: 'Machine Learning Intro',
    description: 'Conceptos de ML, train_test_split, regresion lineal, MAE, RMSE y R²',
    duration: '90 min',
    level: 'Avanzado',
    colabUrl: `${BASE_COLAB}/09-machine-learning-intro/notebook.ipynb`,
    topics: [
      'Conceptos: features, target, entrenamiento',
      'train_test_split',
      'LinearRegression',
      'Metricas: MAE, RMSE, R²',
    ],
    theory: `Machine Learning es enseñar a una computadora a aprender patrones de los datos en lugar de programar reglas manualmente.\n\nEn ML supervisado: tenemos datos etiquetados (X = features, y = target). El modelo aprende la relacion entre X e y durante el entrenamiento, y luego predice y para nuevos X.\n\nLa validacion correcta requiere separar los datos: nunca evalues el modelo con los mismos datos que usaste para entrenarlo.`,
    codeExamples: [
      {
        id: 'c09-ex1',
        title: 'Preparar datos para ML',
        explanation:
          'Antes de entrenar cualquier modelo, debemos preparar las features (X) y el target (y), y separar en train/test sets.',
        schema: 'X = features (columnas de entrada)  /  y = target (lo que predecimos)',
        code: `# === PREPARAR DATOS PARA MACHINE LEARNING ===
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split  # para dividir datos
from sklearn.preprocessing import StandardScaler      # para escalar features

df = pd.read_csv("ventas_tienda.csv")
df['fecha'] = pd.to_datetime(df['fecha'])
df['total_venta'] = df['precio'] * df['cantidad']

# --- Definir Features (X) y Target (y) ---
# Features = variables de ENTRADA que usa el modelo para predecir
# Target   = variable de SALIDA que queremos predecir
#
# Objetivo: predecir el total de venta a partir del precio y la cantidad

# X: matriz de features (2D: filas=observaciones, columnas=variables)
X = df[['precio', 'cantidad']].values  # .values convierte DataFrame → numpy array
print(f"Shape de X: {X.shape}")  # → (500, 2): 500 ejemplos, 2 features

# y: vector target (1D: un valor por ejemplo)
y = df['total_venta'].values
print(f"Shape de y: {y.shape}")  # → (500,): 500 valores objetivo

# --- Dividir en Train y Test ---
# REGLA DE ORO: El modelo NUNCA debe ver los datos de test durante el entrenamiento
# Train: aprende el patron
# Test: evalua si generaliza a datos nuevos

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,      # 20% para test, 80% para entrenamiento
    random_state=42     # semilla aleatoria para reproducibilidad
)
print(f"\\nTrain: {X_train.shape[0]} ejemplos")  # → 400
print(f"Test:  {X_test.shape[0]} ejemplos")     # → 100

# --- Escalar features (opcional pero recomendado) ---
# Algunos modelos son sensibles a la escala (precio: miles, cantidad: unidades)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # ajusta Y transforma train
X_test_scaled = scaler.transform(X_test)        # solo transforma test (con el ajuste de train)
# IMPORTANTE: nunca uses fit en test (filtracion de informacion)`,
        language: 'python',
      },
      {
        id: 'c09-ex2',
        title: 'Regresion Lineal',
        explanation:
          'La regresion lineal predice un valor continuo ajustando una linea (o hiperplano) a los datos. Es el modelo mas simple y un excelente punto de partida.',
        schema: 'y = w1*x1 + w2*x2 + b  →  el modelo aprende w1, w2 y b',
        code: `# === REGRESION LINEAL ===
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# --- Crear y entrenar el modelo ---
# LinearRegression ajusta la ecuacion: y = w1*precio + w2*cantidad + b
modelo = LinearRegression()

# .fit() = ENTRENAMIENTO: el modelo aprende los pesos (w1, w2, b)
# Solo pasamos datos de TRAIN
modelo.fit(X_train, y_train)

print("Modelo entrenado:")
print(f"  Coeficientes (w): {modelo.coef_}")
# Interpreta: por cada 1 unidad de precio, la venta sube en coef[0]
print(f"  Intercepto (b): {modelo.intercept_:.2f}")

# --- Hacer predicciones ---
# .predict() = aplica la formula aprendida a nuevos datos
y_pred = modelo.predict(X_test)  # predicciones para el set de test

# Ver algunas predicciones vs valores reales
print("\\nPredicciones vs Reales (primeros 5):")
for pred, real in zip(y_pred[:5], y_test[:5]):
    error = abs(pred - real)
    print(f"  Pred: ${pred:,.0f}  |  Real: ${real:,.0f}  |  Error: ${error:,.0f}")

# --- Evaluar el modelo ---
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))  # raiz cuadrada del MSE
r2 = r2_score(y_test, y_pred)

print(f"\\nMetricas en Test Set:")
print(f"  MAE  (Error Absoluto Medio):    ${mae:,.0f}")
print(f"  RMSE (Raiz Error Cuadratico):   ${rmse:,.0f}")
print(f"  R²   (Coeficiente determinacion): {r2:.4f}")
# R² = 1.0: prediccion perfecta
# R² = 0.0: el modelo no es mejor que predecir siempre la media
# R² < 0.0: el modelo es peor que la media (algo esta muy mal)`,
        language: 'python',
      },
      {
        id: 'c09-ex3',
        title: 'Visualizar resultados del modelo',
        explanation:
          'Para entender el rendimiento del modelo, comparamos graficamente los valores predichos vs los reales, y graficamos la distribucion de los errores.',
        schema: 'Grafico ideal: todos los puntos en la linea y=x (prediccion perfecta)',
        code: `# === VISUALIZAR RESULTADOS DE REGRESION ===
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# --- Grafico 1: Prediccion vs Real ---
# Si el modelo es perfecto: todos los puntos en la linea diagonal
axes[0].scatter(y_test, y_pred, alpha=0.4, color='steelblue', s=20)

# Linea ideal (y = x): prediccion perfecta
min_val = min(y_test.min(), y_pred.min())
max_val = max(y_test.max(), y_pred.max())
axes[0].plot([min_val, max_val], [min_val, max_val],
             'r--', linewidth=2, label='Prediccion perfecta')

axes[0].set_xlabel('Valor Real ($)')
axes[0].set_ylabel('Valor Predicho ($)')
axes[0].set_title(f'Predicho vs Real (R²={r2:.3f})')
axes[0].legend()

# --- Grafico 2: Distribucion de residuos ---
# Residuo = diferencia entre el valor real y el predicho
# Un buen modelo tiene residuos distribuidos normalmente alrededor de 0
residuos = y_test - y_pred

axes[1].hist(residuos, bins=30, color='#22c55e', edgecolor='white', alpha=0.8)
axes[1].axvline(x=0, color='red', linestyle='--', linewidth=2, label='Error = 0')
axes[1].set_xlabel('Residuo (Real - Predicho)')
axes[1].set_ylabel('Frecuencia')
axes[1].set_title('Distribucion de Errores')
axes[1].legend()

# Simetria: los residuos deben estar centrados en 0
print(f"Media de residuos: {residuos.mean():.2f} (debe ser ≈ 0)")
print(f"Std de residuos: ${residuos.std():,.0f}")

plt.tight_layout()
plt.show()`,
        language: 'python',
      },
    ],
    exercises: [
      {
        id: 'c09-ej1',
        title: 'Predecir precio',
        description:
          'Entrena un modelo de regresion lineal para predecir el precio de un producto usando como features: cantidad vendida, mes, y categoria (codificada numericamente). Reporta MAE, RMSE y R².',
        hint: 'Para categoria usa pd.get_dummies() o LabelEncoder de sklearn.preprocessing',
        starterCode: `import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import numpy as np

df = pd.read_csv("ventas.csv")

# 1. Preparar features (incluir categoria codificada)
# Tu codigo aqui

# 2. Dividir en train/test
# Tu codigo aqui

# 3. Entrenar modelo
# Tu codigo aqui

# 4. Evaluar
# Tu codigo aqui`,
      },
    ],
  },

  // ─────────────────────────────────────────────────────────
  // CLASE 10 — MODELOS SUPERVISADOS
  // ─────────────────────────────────────────────────────────
  {
    id: '10-modelos-supervisados',
    number: 10,
    title: 'Modelos Supervisados',
    description: 'Arbol de decision, regresion logistica, matriz de confusion y metricas de clasificacion',
    duration: '90 min',
    level: 'Avanzado',
    colabUrl: `${BASE_COLAB}/10-modelos-supervisados/notebook.ipynb`,
    topics: [
      'Clasificacion vs Regresion',
      'DecisionTreeClassifier',
      'LogisticRegression',
      'Matriz de confusion, precision, recall, F1',
    ],
    theory: `Los modelos supervisados de clasificacion predicen una categoria discreta (ej: churn si/no, spam/no-spam). A diferencia de regresion que predice un numero continuo.\n\nLas metricas de clasificacion van mas alla del simple accuracy: precision, recall y F1-score son cruciales cuando las clases estan desbalanceadas.`,
    codeExamples: [
      {
        id: 'c10-ex1',
        title: 'Arbol de Decision',
        explanation:
          'Un arbol de decision divide los datos haciendo preguntas sobre las features. Es intuitivo, facil de interpretar y no requiere escalar los datos.',
        schema: 'Raiz → Nodos de decision (preguntas) → Hojas (prediccion)',
        code: `# === ARBOL DE DECISION ===
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

df = pd.read_csv("clientes.csv")

# Objetivo: predecir si un cliente hara churn (si/no)
# Features: edad, meses_cliente, compras_ultimo_mes, monto_total
# Target: churn (0=no, 1=si)

X = df[['edad', 'meses_cliente', 'compras_ultimo_mes', 'monto_total']].values
y = df['churn'].values   # 0 o 1

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Crear el modelo ---
arbol = DecisionTreeClassifier(
    max_depth=4,           # profundidad maxima del arbol (controla overfitting)
    min_samples_split=10,  # minimo de muestras para dividir un nodo
    min_samples_leaf=5,    # minimo de muestras en una hoja
    random_state=42        # reproducibilidad
)

# --- Entrenar ---
arbol.fit(X_train, y_train)

# --- Predecir ---
y_pred = arbol.predict(X_test)            # clase predicha (0 o 1)
y_proba = arbol.predict_proba(X_test)    # probabilidades [prob_0, prob_1]

print(f"Accuracy: {arbol.score(X_test, y_test):.4f}")  # fraccion de predicciones correctas

# --- Visualizar el arbol ---
plt.figure(figsize=(14, 6))
plot_tree(
    arbol,
    feature_names=['edad', 'meses_cliente', 'compras', 'monto'],
    class_names=['No Churn', 'Churn'],
    filled=True,       # colorea los nodos segun la clase mayoritaria
    rounded=True,      # bordes redondeados
    fontsize=9
)
plt.title('Arbol de Decision - Prediccion de Churn')
plt.tight_layout()
plt.show()

# Importancia de cada feature
importancias = pd.Series(
    arbol.feature_importances_,
    index=['edad', 'meses_cliente', 'compras', 'monto']
).sort_values(ascending=False)
print("\\nImportancia de features:")
print(importancias)`,
        language: 'python',
      },
      {
        id: 'c10-ex2',
        title: 'Matriz de confusion y metricas',
        explanation:
          'La matriz de confusion muestra cuantas predicciones son correctas e incorrectas para cada clase. Es la base para calcular precision, recall y F1.',
        schema: 'TP: correcto positivo  /  FP: falso positivo  /  FN: falso negativo  /  TN: correcto negativo',
        code: `# === MATRIZ DE CONFUSION Y METRICAS DE CLASIFICACION ===
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

# Continuando con el modelo de churn...

# --- Matriz de Confusion ---
# Filas: clase REAL    (0=No Churn, 1=Churn)
# Columnas: clase PREDICHA
#
#              Pred: No  |  Pred: Si
# Real: No  |    TN    |    FP    |   (queriamos predecir No, y eso es bueno)
# Real: Si  |    FN    |    TP    |   (quisimos predecir Si correctamente)

cm = confusion_matrix(y_test, y_pred)
print("Matriz de Confusion:")
print(cm)

# Visualizar con heatmap
plt.figure(figsize=(7, 5))
sns.heatmap(
    cm,
    annot=True,           # muestra los numeros
    fmt='d',              # formato entero
    cmap='Blues',
    xticklabels=['No Churn', 'Churn'],
    yticklabels=['No Churn', 'Churn']
)
plt.ylabel('Real')
plt.xlabel('Predicho')
plt.title('Matriz de Confusion')
plt.show()

# --- Metricas individuales ---
# Accuracy: proporcion de predicciones correctas (todas las clases)
# CUIDADO: puede ser engañoso con clases desbalanceadas
acc = accuracy_score(y_test, y_pred)
print(f"\\nAccuracy:  {acc:.4f}  (% total correcto)")

# Precision: de todos los que predije como Churn, ¿cuantos SI son Churn?
# Alta precision = pocos falsos positivos
prec = precision_score(y_test, y_pred)
print(f"Precision: {prec:.4f}  (de los predichos Churn, % realmente Churn)")

# Recall (sensibilidad): de todos los Churn reales, ¿cuantos detecte?
# Alto recall = pocos falsos negativos
rec = recall_score(y_test, y_pred)
print(f"Recall:    {rec:.4f}  (de los Churn reales, % detectados)")

# F1-Score: media armonica de precision y recall (balance entre ambos)
f1 = f1_score(y_test, y_pred)
print(f"F1-Score:  {f1:.4f}  (balance precision-recall)")

# Reporte completo con todas las metricas por clase
print("\\nReporte completo:")
print(classification_report(y_test, y_pred,
                             target_names=['No Churn', 'Churn']))`,
        language: 'python',
      },
    ],
    exercises: [
      {
        id: 'c10-ej1',
        title: 'Comparar modelos',
        description:
          'Entrena un DecisionTreeClassifier y un LogisticRegression con los mismos datos de churn. Compara los F1-scores de cada modelo. ¿Cual es mejor para este problema?',
        hint: 'Usa from sklearn.linear_model import LogisticRegression',
        starterCode: `from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv("clientes.csv")

# Preparar datos
# Tu codigo aqui

# Entrenar DecisionTree
# Tu codigo aqui

# Entrenar LogisticRegression
# Tu codigo aqui

# Comparar F1-scores
# Tu codigo aqui`,
      },
    ],
  },

  // ─────────────────────────────────────────────────────────
  // CLASE 11 — EVALUACION Y PIPELINES
  // ─────────────────────────────────────────────────────────
  {
    id: '11-evaluacion-y-pipelines',
    number: 11,
    title: 'Evaluacion y Pipelines',
    description: 'Cross-validation, Pipeline de sklearn, GridSearchCV para optimizar hiperparametros',
    duration: '90 min',
    level: 'Avanzado',
    colabUrl: `${BASE_COLAB}/11-evaluacion-y-pipelines/notebook.ipynb`,
    topics: [
      'Cross-validation (K-Fold)',
      'Pipeline de sklearn',
      'GridSearchCV',
      'Curva de aprendizaje',
    ],
    theory: `Un modelo que funciona bien en los datos de entrenamiento pero mal en datos nuevos sufre de overfitting. La validacion cruzada (cross-validation) da una estimacion mas confiable del rendimiento real.\n\nEl Pipeline de sklearn encadena pasos de preprocesamiento y modelado en un objeto reutilizable, previniendo la filtracion de datos entre train y test.`,
    codeExamples: [
      {
        id: 'c11-ex1',
        title: 'Cross-Validation (K-Fold)',
        explanation:
          'En K-Fold CV dividimos los datos en K partes. Entrenamos K veces, cada vez usando una parte diferente como test. El resultado es mas confiable que un solo split.',
        schema: 'K=5: 5 divisiones → 5 entrenamientos → promedio de metricas',
        code: `# === CROSS-VALIDATION ===
import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score, KFold, StratifiedKFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("clientes.csv")
X = df[['edad', 'meses_cliente', 'compras_ultimo_mes', 'monto_total']].values
y = df['churn'].values

modelo = DecisionTreeClassifier(max_depth=4, random_state=42)

# --- Cross-Validation simple ---
# cross_val_score: divide automaticamente, entrena y evalua K veces
# cv=5: divide en 5 partes (K=5)
scores = cross_val_score(
    modelo,             # modelo a evaluar
    X,                  # features (TODOS los datos, no solo train)
    y,                  # target
    cv=5,               # K = 5 folds
    scoring='f1'        # metrica a optimizar
)

print(f"F1-Score en cada fold: {scores.round(4)}")
print(f"F1 promedio: {scores.mean():.4f}  (+/- {scores.std():.4f})")
# El "+/-" indica la estabilidad del modelo. Menor std = mas estable.

# --- StratifiedKFold: mejor para clases desbalanceadas ---
# Garantiza que cada fold tiene la misma proporcion de clases
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

scores_estratificados = cross_val_score(modelo, X, y, cv=skf, scoring='f1')
print(f"\\nStratified F1: {scores_estratificados.mean():.4f}")

# --- Multiples metricas a la vez ---
from sklearn.model_selection import cross_validate

resultados = cross_validate(
    modelo, X, y,
    cv=5,
    scoring=['accuracy', 'precision', 'recall', 'f1']
)

print("\\nResultados de CV:")
for metrica in ['accuracy', 'precision', 'recall', 'f1']:
    valores = resultados[f'test_{metrica}']
    print(f"  {metrica:10s}: {valores.mean():.4f} (+/- {valores.std():.4f})")`,
        language: 'python',
      },
      {
        id: 'c11-ex2',
        title: 'Pipeline de sklearn',
        explanation:
          'Un Pipeline encadena pasos: primero preprocesa, luego modela. Garantiza que el escalado se ajuste SOLO en train y se aplique en test, evitando data leakage.',
        schema: 'Pipeline: [("scaler", StandardScaler()), ("modelo", LogisticRegression())]',
        code: `# === PIPELINE DE SKLEARN ===
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
import pandas as pd

df = pd.read_csv("clientes.csv")

# --- Pipeline simple: scaler + modelo ---
pipeline_simple = Pipeline([
    ('scaler', StandardScaler()),      # paso 1: escala los datos
    ('modelo', LogisticRegression())   # paso 2: entrena el modelo
])
# VENTAJA: el scaler se ajusta en train y AUTOMATICAMENTE se aplica en test
# Esto evita data leakage (filtrar info del test al entrenamiento)

X = df[['edad', 'meses_cliente', 'compras_ultimo_mes', 'monto_total']].values
y = df['churn'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# .fit() en Pipeline: aplica fit en cada paso en orden
pipeline_simple.fit(X_train, y_train)

# .predict() en Pipeline: transforma con el scaler, luego predice
y_pred = pipeline_simple.predict(X_test)
print(f"F1-Score: {f1_score(y_test, y_pred):.4f}")

# --- Cross-validation con Pipeline ---
# Correcto: el pipeline previene data leakage en cada fold
scores = cross_val_score(pipeline_simple, X, y, cv=5, scoring='f1')
print(f"CV F1: {scores.mean():.4f} (+/- {scores.std():.4f})")

# --- Acceder a pasos del pipeline ---
scaler_ajustado = pipeline_simple.named_steps['scaler']  # el scaler ya entrenado
modelo_entrenado = pipeline_simple.named_steps['modelo']  # el modelo ya entrenado
print(f"Coeficientes: {modelo_entrenado.coef_}")`,
        language: 'python',
      },
      {
        id: 'c11-ex3',
        title: 'GridSearchCV: optimizar hiperparametros',
        explanation:
          'Los hiperparametros (max_depth, C, n_estimators) no se aprenden del entrenamiento: los debemos elegir nosotros. GridSearchCV prueba todas las combinaciones y elige la mejor.',
        schema: 'GridSearchCV: prueba [depth=2,3,4] x [split=5,10] → elige la mejor combinacion',
        code: `# === GRIDSEARCHCV ===
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import pandas as pd

X = df[['edad', 'meses_cliente', 'compras_ultimo_mes', 'monto_total']].values
y = df['churn'].values

# --- Definir el pipeline ---
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('modelo', DecisionTreeClassifier(random_state=42))
])

# --- Definir la grilla de hiperparametros a explorar ---
# Los nombres siguen el patron: "nombre_paso__hiperparametro"
param_grid = {
    'modelo__max_depth': [2, 3, 4, 5, 6, 8, None],
    # None = sin limite de profundidad (puede hacer overfitting)
    'modelo__min_samples_split': [2, 5, 10, 20],
    # minimo de muestras para dividir un nodo
    'modelo__min_samples_leaf': [1, 2, 5, 10],
    # minimo de muestras en una hoja
}

# --- GridSearchCV ---
grid_search = GridSearchCV(
    pipeline,
    param_grid,
    cv=5,               # 5-fold cross-validation en cada combinacion
    scoring='f1',       # optimizar F1-score
    n_jobs=-1,          # usar todos los nucleos del CPU
    verbose=1           # mostrar progreso
)

grid_search.fit(X_train, y_train)

# --- Resultados ---
print(f"Mejores hiperparametros: {grid_search.best_params_}")
print(f"Mejor F1 en CV: {grid_search.best_score_:.4f}")

# Evaluar el mejor modelo en el test set
mejor_modelo = grid_search.best_estimator_
y_pred_mejor = mejor_modelo.predict(X_test)
print(f"F1 en Test (mejor modelo): {f1_score(y_test, y_pred_mejor):.4f}")

# Ver todas las combinaciones probadas
resultados_cv = pd.DataFrame(grid_search.cv_results_)
print(resultados_cv[['param_modelo__max_depth', 'mean_test_score']].sort_values(
    'mean_test_score', ascending=False).head(5))`,
        language: 'python',
      },
    ],
    exercises: [
      {
        id: 'c11-ej1',
        title: 'Pipeline completo',
        description:
          'Construye un Pipeline con: StandardScaler + DecisionTreeClassifier. Usa GridSearchCV con al menos 3 hiperparametros y 3 valores cada uno. Reporta los mejores hiperparametros y el F1 en test.',
        hint: 'Usa n_jobs=-1 para acelerar la busqueda.',
        starterCode: `from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import f1_score
import pandas as pd

df = pd.read_csv("clientes.csv")

# Preparar datos
# Tu codigo aqui

# Crear pipeline
# Tu codigo aqui

# Definir param_grid
# Tu codigo aqui

# GridSearchCV
# Tu codigo aqui

# Reportar resultados
# Tu codigo aqui`,
      },
    ],
  },

  // ─────────────────────────────────────────────────────────
  // CLASE 12 — PROYECTO FINAL Y CIERRE
  // ─────────────────────────────────────────────────────────
  {
    id: '12-proyecto-final-cierre',
    number: 12,
    title: 'Proyecto Final y Cierre',
    description: 'Estructura profesional de un proyecto de DS, exportar modelos con joblib, y cierre del bootcamp',
    duration: '120 min',
    level: 'Avanzado',
    colabUrl: `${BASE_COLAB}/12-proyecto-final-y-cierre/notebook.ipynb`,
    topics: [
      'Estructura profesional de proyecto',
      'Exportar modelo con joblib',
      'Reporte final en Markdown',
      'Proximos pasos en Data Science',
    ],
    theory: `En este proyecto final integramos todo el bootcamp: desde la carga y limpieza de datos, pasando por el analisis exploratorio, la visualizacion, hasta el modelado y la evaluacion.\n\nUn proyecto profesional de Data Science tiene estructura clara, codigo documentado, visualizaciones limpias y conclusiones accionables.`,
    codeExamples: [
      {
        id: 'c12-ex1',
        title: 'Estructura de un proyecto profesional',
        explanation:
          'Un proyecto de Data Science profesional tiene carpetas organizadas, un README claro, requirements.txt y el codigo modularizado en funciones reutilizables.',
        schema: 'data/ → notebooks/ → src/ → models/ → reports/ → README.md',
        code: `# === ESTRUCTURA PROFESIONAL DE PROYECTO DS ===
#
# mi_proyecto_ds/
# ├── README.md                 # descripcion del proyecto
# ├── requirements.txt          # dependencias: pandas==2.0, scikit-learn==1.3...
# ├── data/
# │   ├── raw/                  # datos originales (NUNCA se modifican)
# │   │   └── ventas_raw.csv
# │   └── processed/            # datos limpios generados por el codigo
# │       └── ventas_clean.csv
# ├── notebooks/
# │   ├── 01_exploracion.ipynb  # EDA y visualizacion
# │   ├── 02_modelado.ipynb     # entrenamiento y evaluacion
# │   └── 03_resultados.ipynb   # reporte final
# ├── src/                      # codigo Python reutilizable
# │   ├── data_loader.py        # funciones para cargar datos
# │   ├── preprocessing.py      # funciones de limpieza
# │   ├── features.py           # ingenieria de features
# │   └── model.py              # entrenamiento y evaluacion
# ├── models/
# │   └── modelo_churn_v1.pkl   # modelo exportado con joblib
# └── reports/
#     └── analisis_final.pdf    # informe ejecutivo

# --- requirements.txt minimo para proyectos DS ---
print("""
pandas>=2.0.0
numpy>=1.24.0
scikit-learn>=1.3.0
matplotlib>=3.7.0
seaborn>=0.12.0
joblib>=1.3.0
jupyter>=1.0.0
""")

# --- Funcion de carga y limpieza modularizada ---
# (esto iria en src/data_loader.py)

def cargar_y_limpiar(ruta_csv):
    """
    Carga un CSV de ventas y aplica el pipeline de limpieza estandar.

    Parametros:
        ruta_csv (str): ruta al archivo CSV

    Retorna:
        pd.DataFrame: DataFrame limpio y con columnas derivadas
    """
    import pandas as pd

    # Cargar
    df = pd.read_csv(ruta_csv)

    # Tipos de datos
    df['fecha'] = pd.to_datetime(df['fecha'])
    df['precio'] = pd.to_numeric(df['precio'], errors='coerce')

    # Limpiar texto
    df['categoria'] = df['categoria'].str.strip().str.title()

    # Nulos
    df['precio'] = df['precio'].fillna(df['precio'].median())
    df = df.dropna(subset=['fecha', 'producto'])

    # Duplicados
    df = df.drop_duplicates()

    # Columnas derivadas
    df['total_venta'] = df['precio'] * df['cantidad']
    df['mes'] = df['fecha'].dt.month
    df['año'] = df['fecha'].dt.year

    print(f"Dataset cargado: {df.shape[0]} filas, {df.shape[1]} columnas")
    return df

# Uso
df = cargar_y_limpiar("data/raw/ventas_raw.csv")`,
        language: 'python',
      },
      {
        id: 'c12-ex2',
        title: 'Exportar e importar modelos con joblib',
        explanation:
          'Una vez entrenado el modelo, lo guardamos en disco con joblib. Luego podemos cargarlo para hacer predicciones sin tener que re-entrenar.',
        schema: 'joblib.dump(modelo, "archivo.pkl")  →  joblib.load("archivo.pkl") → predict()',
        code: `# === EXPORTAR E IMPORTAR MODELOS ===
import joblib
import os
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

# Entrenar el modelo final (con todos los datos de train)
df = pd.read_csv("clientes.csv")
X = df[['edad', 'meses_cliente', 'compras_ultimo_mes', 'monto_total']].values
y = df['churn'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline_final = Pipeline([
    ('scaler', StandardScaler()),
    ('modelo', DecisionTreeClassifier(max_depth=4, random_state=42))
])
pipeline_final.fit(X_train, y_train)

# --- Guardar el modelo ---
# joblib.dump() serializa el objeto Python a un archivo binario
os.makedirs('models', exist_ok=True)   # crear carpeta si no existe
ruta_modelo = 'models/modelo_churn_v1.pkl'

joblib.dump(pipeline_final, ruta_modelo)
print(f"Modelo guardado en: {ruta_modelo}")

# Guardar metadata del modelo (buena practica)
import json
from datetime import datetime
from sklearn.metrics import f1_score

metadata = {
    "version": "1.0",
    "fecha_entrenamiento": datetime.now().strftime("%Y-%m-%d %H:%M"),
    "algoritmo": "DecisionTreeClassifier",
    "max_depth": 4,
    "f1_score_test": round(f1_score(y_test, pipeline_final.predict(X_test)), 4),
    "features": ['edad', 'meses_cliente', 'compras_ultimo_mes', 'monto_total'],
    "target": "churn",
    "n_train": len(X_train),
    "n_test": len(X_test)
}
with open('models/modelo_churn_v1_metadata.json', 'w') as f:
    json.dump(metadata, f, indent=2)

# --- Cargar y usar el modelo ---
modelo_cargado = joblib.load(ruta_modelo)

# Hacer predicciones con el modelo cargado
nuevos_clientes = [[25, 12, 3, 150000],   # cliente 1
                   [45, 36, 1, 50000],    # cliente 2
                   [30, 6, 5, 300000]]    # cliente 3

predicciones = modelo_cargado.predict(nuevos_clientes)
probabilidades = modelo_cargado.predict_proba(nuevos_clientes)

for i, (pred, prob) in enumerate(zip(predicciones, probabilidades)):
    estado = "CHURN" if pred == 1 else "activo"
    print(f"Cliente {i+1}: {estado} (prob churn: {prob[1]:.1%})")`,
        language: 'python',
      },
      {
        id: 'c12-ex3',
        title: 'Pipeline completo de principio a fin',
        explanation:
          'Este es el flujo completo de un proyecto de Data Science real: desde la carga hasta el modelo exportado, pasando por todas las etapas del bootcamp.',
        schema: 'Cargar → Explorar → Limpiar → Features → Modelo → Evaluar → Exportar',
        code: `# === PIPELINE COMPLETO: DE DATOS A MODELO PRODUCTIVO ===
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, f1_score

print("=" * 60)
print("PROYECTO FINAL: PREDICCION DE CHURN DE CLIENTES")
print("=" * 60)

# === ETAPA 1: CARGAR ===
print("\\n[1/6] Cargando datos...")
df = pd.read_csv("clientes.csv")
print(f"  Datos: {df.shape}")

# === ETAPA 2: EXPLORAR ===
print("\\n[2/6] Exploracion basica...")
print(f"  Nulos: {df.isnull().sum().sum()}")
print(f"  Churn rate: {df['churn'].mean():.1%}")  # % de clientes con churn

# === ETAPA 3: LIMPIAR ===
print("\\n[3/6] Limpiando datos...")
df = df.dropna().drop_duplicates()
df['monto_total'] = pd.to_numeric(df['monto_total'], errors='coerce').fillna(0)
print(f"  Datos limpios: {df.shape}")

# === ETAPA 4: FEATURES ===
print("\\n[4/6] Ingenieria de features...")
features = ['edad', 'meses_cliente', 'compras_ultimo_mes', 'monto_total']
X = df[features].values
y = df['churn'].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y  # stratify: mantiene proporcion de clases
)

# === ETAPA 5: MODELAR ===
print("\\n[5/6] Entrenando modelo...")
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('modelo', DecisionTreeClassifier(max_depth=4, min_samples_leaf=5, random_state=42))
])
pipeline.fit(X_train, y_train)

# Cross-validation para estimacion confiable
scores_cv = cross_val_score(pipeline, X, y, cv=5, scoring='f1')
print(f"  F1 CV: {scores_cv.mean():.4f} (+/- {scores_cv.std():.4f})")

# === ETAPA 6: EVALUAR Y EXPORTAR ===
print("\\n[6/6] Evaluando y exportando...")
y_pred = pipeline.predict(X_test)
f1 = f1_score(y_test, y_pred)
print(f"  F1 Test: {f1:.4f}")
print(classification_report(y_test, y_pred, target_names=['Activo','Churn']))

joblib.dump(pipeline, 'modelo_final.pkl')
print("\\n✓ Modelo exportado: modelo_final.pkl")
print("\\n=== PROYECTO COMPLETADO ===")`,
        language: 'python',
      },
    ],
    exercises: [
      {
        id: 'c12-ej1',
        title: 'Tu proyecto final',
        description:
          'Usando cualquier dataset que elijas: completa el pipeline completo (cargar, limpiar, EDA, modelar, evaluar), exporta el modelo con joblib, y escribe un resumen ejecutivo de 1 parrafo con tus hallazgos y recomendaciones.',
        hint: 'Puedes usar datasets de Kaggle, del UCI ML Repository, o el de ventas del bootcamp.',
        starterCode: `# === MI PROYECTO FINAL ===
# Dataset elegido: _______________
# Objetivo: predecir / analizar _______________
# Preguntas de negocio:
#   1. _______________
#   2. _______________

import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

# Tu pipeline completo aqui...`,
      },
    ],
  },
];

export default CLASSES;
