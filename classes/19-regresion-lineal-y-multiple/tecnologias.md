# 🔧 Tecnologías complementarias — Clase 19: Regresión Lineal y Múltiple

> Herramientas y recursos para ampliar lo aprendido.

## 📦 Librerías relacionadas

| Librería | Para qué sirve | Nivel sugerido |
|---|---|---|
| `statsmodels` | Regresión con estadísticas detalladas: p-values, intervalos de confianza, test F | Intermedio |
| `scipy.stats` | Correlaciones, tests estadísticos para validar supuestos de regresión | Intermedio |
| `yellowbrick` | Visualizaciones específicas para ML: residuales, ResidualsPlot, PredictionError | Intermedio |
| `sklearn.preprocessing.PolynomialFeatures` | Extiende regresión lineal a relaciones curvilíneas (regresión polinomial) | Intermedio |
| `sklearn.linear_model.Ridge / Lasso` | Regresión regularizada para evitar sobreajuste con muchas variables | Avanzado |
| `pingouin` | Estadística descriptiva e inferencial amigable, correlaciones parciales | Básico |

## 🌐 Recursos recomendados

- **Documentación oficial**: https://scikit-learn.org/stable/modules/linear_model.html
- **Tutorial recomendado**: "Linear Regression in Python" — Real Python (realpython.com/linear-regression-in-python/)
- **Concepto clave para buscar**: "ordinary least squares regression assumptions" — para entender cuándo la regresión lineal es válida

## 🚀 Próximos pasos sugeridos

- Explorar regresión polinomial con `PolynomialFeatures` para capturar relaciones no lineales
- Aprender Ridge y Lasso para controlar el sobreajuste cuando hay muchas variables
- Estudiar los supuestos de la regresión lineal (normalidad de residuales, homocedasticidad) con `statsmodels`
- Practicar la interpretación de coeficientes estandarizados para comparar el peso real de cada variable

## 🧰 Herramientas alternativas

| Herramienta | Descripción | Cuándo usarla |
|---|---|---|
| `statsmodels.OLS` | Regresión con output estadístico completo tipo R | Cuando necesitas p-values y validación estadística formal |
| `sklearn.linear_model.ElasticNet` | Combinación de Ridge y Lasso | Cuando no sabes qué tipo de regularización usar |
| `Excel / Power BI` | Regresión básica con visualización de negocio | Para presentar resultados a audiencias no técnicas |
