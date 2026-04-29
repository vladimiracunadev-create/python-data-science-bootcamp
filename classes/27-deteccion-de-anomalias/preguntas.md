# ❓ Preguntas — Clase 27: Detección de Anomalías

> Preguntas de comprensión, discusión y evaluación para esta clase.

## 🧠 Preguntas de comprensión

1. ¿Qué es una anomalía en el contexto de datos? ¿Cuál es la diferencia entre una anomalía y un error de medición?
2. Explica el método IQR para detectar anomalías. ¿Cómo se calculan los límites inferior y superior?
3. ¿Qué mide el Z-score de un valor? ¿Por encima de qué valor de Z-score se considera típicamente que un punto es anómalo?
4. ¿Cómo funciona **Isolation Forest**? ¿Por qué los puntos anómalos son más fáciles de "aislar" con árboles aleatorios?
5. ¿Qué es el **Local Outlier Factor (LOF)** y en qué se diferencia de los métodos globales como Z-score?
6. ¿Por qué los diferentes métodos de detección de anomalías pueden dar resultados distintos en el mismo dataset?
7. ¿Cuándo usarías un método supervisado vs. no supervisado para detectar anomalías?

## 💬 Preguntas de discusión

1. En el dataset `ventas_tienda.csv`, ¿qué tipo de anomalías esperarías encontrar? ¿Podrían ser fraudes, errores de registro, o simplemente días excepcionales de ventas?
2. ¿Una venta extremadamente alta es siempre una anomalía negativa? Piensa en el contexto del Black Friday o Navidad.
3. ¿Cuáles son los riesgos de eliminar automáticamente todas las anomalías detectadas de un dataset? ¿Cuándo debería conservarse una anomalía?
4. Isolation Forest tiene un parámetro `contamination` que indica el porcentaje esperado de anomalías. Si no lo conoces de antemano, ¿cómo lo estimarías?
5. Discute: ¿por qué la detección de anomalías es especialmente importante en sistemas de seguridad bancaria o ciberseguridad?
6. Si IQR dice que hay 20 anomalías, Z-score dice 15 e Isolation Forest dice 30, ¿cuál de los tres confiarías más y por qué?

## 🧪 Preguntas de código

1. Dado un array `ventas = [120, 115, 130, 125, 890, 118, 122]`, escribe el código para detectar anomalías usando IQR y muestra cuáles son.
2. ¿Cómo calcularías el Z-score de cada valor en una columna de pandas sin usar scipy? ¿Y usando `scipy.stats.zscore`?
3. Escribe el código para entrenar un `IsolationForest` en el dataset de ventas y agregar una columna `es_anomalia` al DataFrame original.
4. ¿Cómo visualizarías las anomalías detectadas en un scatter plot usando matplotlib, distinguiendo puntos normales y anómalos con colores diferentes?
5. Escribe el código para comparar cuántas anomalías detecta cada método (IQR, Z-score, Isolation Forest) en el mismo dataset.
6. ¿Cómo usarías `LocalOutlierFactor` en sklearn y qué significa un score negativo muy bajo en este método?

## 🎯 Pregunta integradora

Eres analista de datos en una empresa de transporte y tienes el dataset `transporte.csv` con registros de viajes (distancia, duración, costo, velocidad promedio). Describe el proceso completo para detectar viajes anómalos: ¿qué método o combinación de métodos usarías? ¿Cómo presentarías los resultados al equipo de operaciones? ¿Cómo distinguirías entre anomalías que requieren investigación urgente (posible fraude) y anomalías benignas (un viaje inusualmente largo por condiciones de tráfico)? Propón al menos dos visualizaciones que usarías para comunicar tus hallazgos.
