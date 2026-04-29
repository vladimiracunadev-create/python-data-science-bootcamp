# 📘 Clase 18: Feature engineering — crear mejores variables

> 🎯 Ficha de clase con objetivo, materiales y foco de aprendizaje.

## 🎯 Objetivo
Aprender a transformar datos crudos en variables útiles y bien preparadas para modelos de machine learning. El estudiante creará variables derivadas, extraerá información de fechas, codificará variables categóricas, aplicará binning y escalado, y seleccionará las variables más relevantes, usando el dataset de ventas como laboratorio práctico.

## ⏱️ Duración sugerida
90 minutos

## 📦 Dataset base
- `datasets/ventas_tienda.csv`
- `datasets/estudiantes.csv`

## ✅ Resultados esperados
Al finalizar, el estudiante podrá:
- Crear variables derivadas numéricas, extraídas de fechas y combinadas (interacciones) a partir de columnas existentes.
- Aplicar codificación de variables categóricas con `pd.get_dummies` y con `map`/`replace`.
- Escalar variables numéricas con `StandardScaler` y `MinMaxScaler` y explicar cuándo usar cada uno.

## 🧭 Temas clave
- Qué es feature engineering (transformar datos crudos en señales útiles para los modelos)
- Por qué importa más que la elección del algoritmo
- Creación de variables numéricas derivadas (`total_neto`, `promedio_tecnico`)
- Extracción desde fechas (mes, día de la semana, `is_weekend`)
- Codificación de variables categóricas: `pd.get_dummies` (one-hot), `map`/`replace` (ordinal)
- Binning: `pd.cut` y `pd.qcut` (grupos de edad, rangos de puntaje)
- Escalado: `StandardScaler` (media=0, std=1), `MinMaxScaler` (0 a 1)
- Selección de variables: correlación con el target, eliminar variables redundantes
- Variables de interacción (precio × descuento, asistencia × nota)

## 🧰 Materiales del módulo
- `README.md`
- `slides.md`
- `teoria.md`
- `ejercicios.md`
- `homework.md`
- `notebook.ipynb`
- `soluciones.ipynb`

## 💻 Cómo leer el código de esta clase
- Cada bloque debe responder una pregunta concreta.
- Los comentarios deben explicar qué hace el bloque y para qué sirve.
- Antes de pasar al siguiente paso, verifica que entiendes la salida.

## 💡 Idea central
Los modelos de machine learning aprenden mejor cuando las variables son claras, relevantes y bien preparadas.

## 👩‍🏫 Nota para el docente
Usa la analogía del detective: un detective resuelve casos con pistas (features) — mejores pistas llevan a mejores deducciones. Así, el ingeniero de features es el detective que decide qué información entregar al modelo. Muestra el antes y después de preparar las variables para que el estudiante vea el impacto directo en la calidad de los datos.
