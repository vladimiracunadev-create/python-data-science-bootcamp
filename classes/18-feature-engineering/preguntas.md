# ❓ Preguntas — Clase 18: Feature Engineering — crear mejores variables

> Preguntas de comprensión, discusión y evaluación para consolidar esta clase.

## 🧠 Preguntas de comprensión

1. ¿Qué es el feature engineering y por qué se considera una de las habilidades más importantes en ciencia de datos? ¿Qué problema resuelve?
2. ¿Cuál es la diferencia entre `pd.get_dummies()` para encoding nominal y el encoding ordinal con `.map()`? ¿Cuándo se usa cada uno y qué pasa si usas el incorrecto?
3. ¿Qué hace `pd.cut()` y en qué se diferencia de `pd.qcut()`? ¿Qué garantiza cada uno?
4. ¿Por qué es necesario escalar las variables numéricas antes de algunos modelos de machine learning? ¿Qué pasa si no lo haces en un modelo de regresión lineal o una red neuronal?
5. ¿Cuál es la diferencia entre `StandardScaler` y `MinMaxScaler`? ¿Qué hace cada uno con los outliers?

## 💬 Preguntas de discusión

1. Muchos científicos de datos dicen que "los datos crudos nunca están listos para los modelos". ¿Cuáles son los problemas más típicos que tienen los datos sin preparar?
2. ¿Por qué podría ser un problema aplicar one-hot encoding a una columna con 500 categorías únicas (como el nombre del producto)? ¿Qué alternativas existen?
3. Imagina que estás prediciendo si un cliente abandonará tu servicio (churn). ¿Qué features derivadas crearías a partir de las columnas `fecha_registro`, `ultimo_acceso` y `num_compras_historico`? Explica el razonamiento de cada una.

## 🧪 Preguntas de código

1. Dado un DataFrame `df` con una columna `fecha_venta` de tipo string, escribe el código completo para convertirla a datetime y extraer el año, mes, día de la semana (número), nombre del día, si es fin de semana (0 o 1) y el trimestre.
2. Escribe el código para aplicar one-hot encoding a la columna `categoria` de `df`, descartando la primera categoría para evitar multicolinealidad, y usando enteros (0/1) en lugar de booleanos.
3. Escribe el código completo para aplicar `StandardScaler` a las columnas numéricas de un DataFrame, recuperando el resultado como DataFrame con nombres de columna originales más el sufijo `_scaled`.

## 🎯 Pregunta integradora

Tienes un dataset de ventas con las columnas: `fecha_venta` (datetime), `producto` (8 valores únicos), `precio` (numérico), `cantidad` (entero), `cliente_tipo` (Nuevo/Regular/VIP), `descuento_pct` (0 a 50), `ciudad` (15 ciudades). El objetivo es predecir si una venta generará una reseña positiva. Diseña el plan completo de feature engineering: (1) qué transformarías de cada columna y por qué, (2) qué features derivadas crearías y su razonamiento, (3) qué técnica de encoding usarías para cada columna categórica y por qué, (4) qué tipo de escalado aplicarías y a qué columnas, y (5) escribe el código Python completo para al menos 3 de las transformaciones que propones.
