# 🔧 Tecnologías complementarias — Clase 24: Series de Tiempo

> Herramientas y recursos para ampliar lo aprendido.

## 📦 Librerías relacionadas

| Librería | Para qué sirve | Nivel sugerido |
|---|---|---|
| `statsmodels.tsa.holtwinters` | Suavizado exponencial (Holt-Winters): incluye tendencia y estacionalidad automáticamente | Intermedio |
| `statsmodels.tsa.arima.model.ARIMA` | Modelo clásico de series de tiempo con componentes autoregresivos y medias móviles | Avanzado |
| `prophet` (Meta) | Pronóstico automático con manejo de feriados, cambios de tendencia y datos faltantes | Intermedio |
| `sktime` | Framework de ML para series de tiempo: clasifica, agrupa y pronostica con API tipo sklearn | Avanzado |
| `pmdarima` | Selección automática de parámetros ARIMA (auto-ARIMA), equivalente al "GridSearch" de series de tiempo | Avanzado |
| `plotly` | Gráficos temporales interactivos con zoom, hover y rangos seleccionables | Intermedio |

## 🌐 Recursos recomendados

- **Documentación oficial**: https://www.statsmodels.org/stable/tsa.html
- **Tutorial recomendado**: "Time Series Analysis in Python — A Comprehensive Guide" — Machine Learning Mastery
- **Concepto clave para buscar**: "ARIMA vs Prophet forecasting" — comparativa práctica de los dos enfoques más usados en producción

## 🚀 Próximos pasos sugeridos

- Aprender el modelo SARIMA (ARIMA estacional) para series con estacionalidad marcada
- Explorar Prophet de Meta como alternativa fácil de usar para pronósticos con feriados y outliers
- Estudiar validación cruzada temporal (`TimeSeriesSplit`) para evaluar modelos sin data leakage temporal
- Practicar la detección de estacionariedad con el test ADF (Augmented Dickey-Fuller)

## 🧰 Herramientas alternativas

| Herramienta | Descripción | Cuándo usarla |
|---|---|---|
| `prophet.Prophet` | Pronóstico automático de Meta, muy robusto con datos irregulares y feriados | Cuando necesitas pronósticos rápidos con poco tuning y los datos tienen días festivos |
| `statsmodels.tsa.holtwinters.ExponentialSmoothing` | Suavizado exponencial triple (tendencia + estacionalidad) | Como alternativa simple entre naive forecasting y ARIMA |
| `Tableau / Power BI` | Visualización interactiva de series temporales para reportes de negocio | Para comunicar tendencias y estacionalidad a audiencias ejecutivas |
