# 🔧 Tecnologías complementarias — Clase 17: Estadística inferencial — pruebas de hipótesis

> Herramientas, librerías y recursos para ampliar lo aprendido.

## 📦 Librerías relacionadas

| Librería | Para qué sirve | Nivel sugerido |
|---|---|---|
| `scipy.stats` | Pruebas estadísticas: t-test, chi-cuadrado, ANOVA, Mann-Whitney, distribuciones | Básico |
| `numpy` | Operaciones numéricas base para cálculos estadísticos manuales | Básico |
| `pandas` | Tablas de contingencia con `pd.crosstab()` para preparar el input de chi-cuadrado | Básico |
| `seaborn` | Visualizar distribuciones para validar supuestos de normalidad antes de las pruebas | Básico |
| `statsmodels` | Modelos estadísticos completos: OLS, regresión logística, ANOVA de dos vías | Intermedio |
| `pingouin` | Pruebas estadísticas con salida enriquecida: tamaño del efecto, potencia estadística | Intermedio |
| `bootstrapped` | Intervalos de confianza por bootstrapping sin asumir distribución normal | Intermedio |
| `pymc` | Estadística bayesiana: distribuciones a posteriori e inferencia probabilística | Avanzado |
| `lifelines` | Análisis de supervivencia (tiempo hasta un evento: muerte, churn, falla) | Avanzado |

## 🌐 Recursos recomendados

- **Documentación oficial**: scipy.stats — [docs.scipy.org/doc/scipy/reference/stats.html](https://docs.scipy.org/doc/scipy/reference/stats.html) — lista completa de todas las pruebas estadísticas disponibles con parámetros y ejemplos
- **Tutorial recomendado**: Canal de YouTube "StatQuest with Josh Starmer" — explica prueba t, chi-cuadrado, ANOVA y la interpretación del p-valor con visualizaciones muy claras y sin matemáticas intimidantes
- **Concepto clave para buscar**: "tamaño del efecto Cohen's d" / "effect size statistics" — aprender por qué el p-valor solo no es suficiente para tomar decisiones y qué significa que una diferencia sea "prácticamente importante"

## 🚀 Próximos pasos sugeridos

- Aprender ANOVA (Analysis of Variance) para comparar más de dos grupos simultáneamente sin inflar el Error Tipo I
- Estudiar pruebas no paramétricas (Mann-Whitney, Kruskal-Wallis) para cuando los datos no siguen una distribución normal
- Explorar el tamaño del efecto (Cohen's d, eta-cuadrado) para saber si una diferencia estadísticamente significativa también es prácticamente importante
- Investigar la estadística bayesiana como alternativa moderna a las pruebas frecuentistas, que permite incorporar conocimiento previo

## 🧰 Herramientas alternativas

| Herramienta | Descripción breve | Cuándo conviene usarla |
|---|---|---|
| R (base stats) | Lenguaje con funciones estadísticas nativas muy completas y ampliamente aceptadas en academia | Publicaciones académicas o proyectos con fuerte componente de estadística formal |
| JASP | Software estadístico gratuito con interfaz gráfica, incluye estadística bayesiana | Para quienes no programan y necesitan hacer pruebas estadísticas con resultados publicables |
| SPSS | Software estadístico propietario muy usado en ciencias sociales y salud | Investigación en psicología, sociología y ciencias de la salud con formato de salida estándar |
| G*Power | Calcula el tamaño de muestra necesario para una potencia estadística deseada | Para diseñar experimentos antes de recolectar datos y asegurar que habrá suficiente poder |
