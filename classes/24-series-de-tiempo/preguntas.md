# ❓ Preguntas — Clase 24: Series de Tiempo

> Preguntas de comprensión, discusión y evaluación.

## 🧠 Preguntas de comprensión

1. ¿Cuáles son los 3 componentes principales de una serie de tiempo? Da un ejemplo real de cada componente.
2. ¿Por qué es importante convertir una columna de fechas con `pd.to_datetime()` antes de usarla como índice? ¿Qué ventajas da tener una fecha como índice?
3. ¿Qué hace `resample('M').sum()`? ¿Qué otras frecuencias puedes usar con `resample()` (ej: semana, trimestre)?
4. ¿Qué es una media móvil y cómo `rolling(7).mean()` suaviza el ruido de una serie? ¿Qué pasa con las primeras 6 observaciones?
5. ¿Qué hace `seasonal_decompose` de statsmodels? ¿Qué muestran cada uno de los 4 gráficos que genera?
6. ¿Qué es el pronóstico ingenuo (naive forecasting) con "último valor"? ¿En qué tipo de series funciona razonablemente bien?
7. ¿Cuál es la diferencia entre media móvil como suavizador (descriptivo) y como método de pronóstico?

## 💬 Preguntas de discusión

1. Una empresa de retail quiere predecir sus ventas del próximo mes. ¿Por qué no podrías usar directamente un modelo de Machine Learning clásico (como Random Forest) sin modificaciones? ¿Qué adaptaciones serían necesarias?
2. Al descomponer una serie de ventas semanales, ves que el componente estacional tiene picos en diciembre y valles en enero. ¿Cómo usarías esa información para tomar decisiones de inventario y personal?
3. El componente residual (ruido) de una serie es muy grande comparado con la tendencia y la estacionalidad. ¿Qué significa eso para la predictibilidad de la serie? ¿Qué podrías hacer?

## 🧪 Preguntas de código

1. Carga `ventas_tienda.csv`, convierte la columna `fecha` a datetime y ponla como índice. Resamplea a frecuencia mensual (suma) y gráfica la serie temporal resultante con título y etiquetas de ejes.
2. Sobre la serie mensual de ventas, calcula una media móvil de 3 meses (`rolling(3).mean()`) y grafícala junto a la serie original en el mismo plot. ¿Qué patrón hace más visible la media móvil?
3. Aplica `seasonal_decompose` a la serie de ventas con `model='additive'` y `period=12`. gráfica la descomposición completa. ¿Qué mes tiene el pico estacional más alto?

## 🎯 Pregunta integradora

Con `ventas_tienda.csv`: (1) crea la serie temporal mensual de ventas; (2) aplica descomposición estacional con statsmodels e interpreta cada componente (¿hay tendencia creciente? ¿en qué mes hay más ventas?); (3) implementa dos pronósticos ingenuos para los próximos 3 meses: "último valor" y "media móvil de 6 meses"; (4) calcula el MAE (error absoluto medio) de cada método usando los últimos 3 meses reales como validación; (5) concluye cuál método es mejor para este dataset y justifica si alguno de los dos sería suficiente para una empresa pequeña o si recomendarías métodos más avanzados.
