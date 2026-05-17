# 📘 Clase 27: Detección de Anomalías

> 🎯 Ficha de clase con objetivo, materiales y foco de aprendizaje.

## 🎯 Objetivo
Aprender a identificar valores anómalos en datos usando métodos estadísticos (IQR, Z-score) y algoritmos de Machine Learning (Isolation Forest, Local Outlier Factor), con aplicaciones prácticas en ventas y transporte.

## ⏱️ Duración sugerida
90 minutos

## 📦 Dataset base
- `datasets/ventas_tienda.csv`
- `datasets/transporte.csv`

## ✅ Resultados esperados
Al finalizar, el estudiante podrá:
- Distinguir anomalías de outliers estadísticos, aplicar métodos IQR y Z-score, usar Isolation Forest y LOF de sklearn para detectar puntos inusuales.

## 🧭 Temas clave
- Anomalías vs outliers
- Regla del IQR
- Z-score
- Isolation Forest
- Local Outlier Factor (LOF)
- Visualización de anomalías (boxplot, scatter)
- Cuándo usar cada método

## 🧰 Materiales del módulo
- `README.md`, `slides.md`, `teoria.md`, `ejercicios.md`, `homework.md`, `notebook.ipynb`, `soluciones.ipynb`

## 💻 Cómo leer el código de esta clase
- Cada bloque debe responder una pregunta concreta.

## 💡 Idea central
La detección de anomalías encuentra los puntos que no siguen el patrón esperado — clave para detectar fraudes, fallos o eventos raros.

## 👩‍🏫 Nota para el docente
Usa ejemplos del mundo real desde el inicio: una transacción bancaria a las 3am en otro país, una máquina que de repente consume el doble de energía. Estos ejemplos generan curiosidad antes de ver el código. Compara siempre los resultados de los distintos métodos sobre el mismo dataset.
