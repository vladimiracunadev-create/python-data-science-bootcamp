# 🧠 Documento teórico — Clase 13: ¿Qué es la Ciencia de Datos?

> 🧠 Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## 💡 Idea central

La ciencia de datos convierte datos en decisiones, combinando programación, estadística y comprensión del problema.

## ❓ Por qué importa este módulo

Antes de escribir una sola línea de código, necesitamos entender qué problema estamos resolviendo y por qué los datos pueden ayudarnos. La ciencia de datos no comienza con un dataset: comienza con una pregunta. Este módulo te da el mapa conceptual para que cada técnica que aprendas en el bootcamp tenga sentido dentro de un proceso más grande.

## 📖 ¿Qué es la ciencia de datos?

La ciencia de datos es la disciplina que extrae conocimiento útil de los datos para apoyar decisiones. Combina tres áreas:

1. **Programación**: para procesar, limpiar y transformar datos a escala
2. **Estadística y matemáticas**: para encontrar patrones y medir la confianza en los resultados
3. **Dominio del problema**: para saber qué preguntas tienen sentido y cómo interpretar las respuestas

Sin programación, no podemos manejar millones de filas. Sin estadística, confundimos ruido con señal. Sin conocimiento del dominio, respondemos la pregunta equivocada.

## 🔄 El ciclo de vida de un proyecto de datos (CRISP-DM)

CRISP-DM (Cross Industry Standard Process for Data Mining) describe los pasos que sigue cualquier proyecto de datos real:

1. **Entender el problema** — ¿Qué decisión quiero tomar? ¿Qué necesito saber?
2. **Recolectar y entender los datos** — ¿Qué datos tengo? ¿Son suficientes? ¿Son confiables?
3. **Preparar los datos** — Limpiar, transformar, unir tablas, manejar valores faltantes
4. **Modelar** — Aplicar técnicas estadísticas o de machine learning
5. **Evaluar** — ¿El resultado responde la pregunta original? ¿Es confiable?
6. **Comunicar e implementar** — Presentar hallazgos, tomar decisiones, desplegar el modelo

El ciclo es iterativo: después de modelar puedes volver a preparar datos, o después de evaluar volver a redefinir el problema.

## 📊 Tipos de datos

| Tipo | Descripción | Ejemplos |
|---|---|---|
| Numéricos | Cantidades medibles | Precio, temperatura, edad, ventas |
| Texto | Lenguaje natural | Comentarios, correos, artículos |
| Imágenes | Píxeles organizados | Fotos médicas, fotos de productos |
| Series de tiempo | Valores ordenados en el tiempo | Precio de acciones, temperatura diaria |
| Categóricos | Etiquetas o grupos | País, género, categoría de producto |

## ❓ Tipos de preguntas que responde la ciencia de datos

| Tipo | Pregunta | Ejemplo |
|---|---|---|
| **Descriptiva** | ¿Qué pasó? | ¿Cuánto vendimos el mes pasado? |
| **Diagnóstica** | ¿Por qué pasó? | ¿Por qué bajaron las ventas en diciembre? |
| **Predictiva** | ¿Qué pasará? | ¿Cuánto venderemos el próximo trimestre? |
| **Prescriptiva** | ¿Qué debemos hacer? | ¿A qué clientes debemos ofrecer descuentos? |

Las preguntas descriptivas y diagnósticas son más simples y se responden con análisis exploratorio. Las predictivas y prescriptivas requieren modelos más complejos.

## 🌍 Ciencia de datos en la vida diaria

- **Netflix / YouTube / TikTok**: el algoritmo de recomendación predice qué video verás con más gusto, basado en tu historial
- **Pronóstico del tiempo**: modelos que procesan millones de datos de sensores atmosféricos para predecir el clima
- **Google Maps**: estima el tiempo de llegada usando datos de velocidad de miles de vehículos en tiempo real
- **Detección de fraude**: los bancos analizan patrones en tus compras para detectar transacciones inusuales
- **Calificaciones adaptativas**: algunas plataformas educativas ajustan la dificultad según tu desempeño previo

## 🛠️ Herramientas del bootcamp

| Herramienta | Para qué sirve |
|---|---|
| **Python** | Lenguaje base: leer, transformar, calcular, visualizar |
| **pandas** | Manipular tablas de datos (cargar CSVs, filtrar, agrupar) |
| **NumPy** | Cálculo numérico rápido sobre arrays |
| **matplotlib / seaborn** | Crear gráficas y visualizaciones |
| **scikit-learn** | Entrenar y evaluar modelos de machine learning |
| **SQLite / SQL** | Consultar bases de datos relacionales |

## 💻 Bloque de código documentado

### Leer un dataset y explorar sus primeros datos

Este bloque muestra cómo en tres líneas de código podemos ver el contenido de un archivo de datos real.

**Qué hace:** carga un archivo CSV en memoria, muestra las primeras filas y describe los tipos de datos de cada columna.

**Para qué sirve:** es el primer paso de cualquier proyecto de datos — verificar que los datos cargaron correctamente y entender su estructura antes de analizarlos.

```python
# Importamos pandas, la herramienta principal para trabajar con tablas
import pandas as pd

# Cargamos el dataset de ventas desde un archivo CSV
# pd.read_csv() convierte el archivo en una tabla (DataFrame)
df = pd.read_csv("datasets/ventas_tienda.csv")

# Mostramos las primeras 5 filas para ver cómo se ven los datos
print(df.head())

# Mostramos información sobre columnas, tipos y valores faltantes
print(df.info())
```

## ⚠️ Errores frecuentes a vigilar

- **Confundir datos con información**: los datos son registros crudos; la información es el significado que extraemos al analizarlos con una pregunta en mente
- **Saltarse la definición del problema**: empezar a escribir código sin entender qué decisión se quiere tomar lleva a análisis que no se usan
- **Creer que más datos siempre es mejor**: datos de baja calidad o irrelevantes agregan ruido, no señal

## 🔗 Conexión con el siguiente módulo

Esta clase es el mapa; las clases 01 a 12 son el recorrido técnico. Al volver a este mapa después de completar el bootcamp, cada herramienta que aprendiste encajará en uno de los pasos del ciclo CRISP-DM. La clase 14 introduce NumPy, la base numérica sobre la que se construyen pandas y scikit-learn.
