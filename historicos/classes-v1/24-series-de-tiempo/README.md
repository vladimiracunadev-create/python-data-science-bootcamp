# 📘 Clase 24: Series de tiempo — datos temporales

> 🎯 Ficha de clase con objetivo, materiales y foco de aprendizaje.

## 🎯 Objetivo
Aprender a trabajar con datos que cambian con el tiempo: convertir columnas de fecha, indexar por tiempo, agregar por períodos con resample, suavizar tendencias con ventanas móviles y visualizar la evolución temporal de las ventas. Al final de la clase el alumno podrá detectar tendencias y estacionalidad en una serie de tiempo real y generar un pronóstico simple.

## ⏱️ Duración sugerida
90 minutos

## 📦 Dataset base
- `datasets/ventas_tienda.csv` (columna `fecha`)
- `datasets/retencion_clientes.csv` (columna `mes`)

## ✅ Resultados esperados
Al finalizar, el estudiante podrá:
- Convertir una columna de texto a tipo fecha con `pd.to_datetime()` y usarla como índice
- Agregar datos por mes o semana con `resample()` y calcular tendencias con `rolling()`
- Identificar visualmente tendencia y estacionalidad en una serie de tiempo

## 🧭 Temas clave
- Qué es una serie de tiempo y ejemplos reales
- `pd.to_datetime()` y `set_index()` con fechas
- `resample('M').sum()` y `resample('W').mean()` para agregar por período
- `rolling(7).mean()` — promedio móvil para suavizar ruido
- Graficar series de tiempo con matplotlib
- Identificar tendencia y estacionalidad visualmente
- Pronóstico simple: último valor, promedio móvil
- `seasonal_decompose` de statsmodels: tendencia + estacional + residuo

## 🧰 Materiales del módulo
- `README.md`, `slides.md`, `teoria.md`, `ejercicios.md`, `homework.md`, `notebook.ipynb`, `soluciones.ipynb`

## 💻 Cómo leer el código de esta clase
- Cada bloque debe responder una pregunta concreta.
- Los comentarios deben explicar qué hace el bloque y para qué sirve.

## 💡 Idea central
Las series de tiempo permiten detectar tendencias, estacionalidad y anomalías en datos que cambian con el tiempo.

## 👩‍🏫 Nota para el docente
Pregunta a la clase: "¿Qué creen que pasa con las ventas de ropa en diciembre versus julio?" Ese es el concepto de estacionalidad. Luego muéstrales que los datos de ventas mensuales graficados en el tiempo revelan exactamente ese patrón. Conectar el concepto con experiencias de compra cotidianas hace que los alumnos de cualquier edad entiendan inmediatamente por qué las series de tiempo importan.
