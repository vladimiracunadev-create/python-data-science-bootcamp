# 🛠️ Tecnologías complementarias — Clase 04: Estadística descriptiva

> Herramientas y librerías que complementan o extienden lo visto en esta clase.

## 📦 Librerías principales usadas en esta clase

| Librería | Versión recomendada | Para qué se usa en esta clase |
|---|---|---|
| pandas | 2.x | Calcular media, mediana, desviación estándar y percentiles con `.mean()`, `.median()`, `.std()` y `.describe()` |
| numpy | 1.26+ | Cálculos estadísticos de bajo nivel como `np.percentile()` y manejo de arrays numéricos |
| scipy.stats | 1.12+ | Estadísticas avanzadas como asimetría (`skew`), curtosis y pruebas de normalidad cuando se requiere ir más allá de `describe()` |
| matplotlib | 3.8+ | Histogramas y boxplots para visualizar distribución y dispersión como complemento a los números |

## 🔗 Herramientas complementarias

| Herramienta | Descripción | Cuándo usarla |
|---|---|---|
| Seaborn | Gráficos estadísticos de alto nivel: `histplot`, `boxplot`, `violinplot` con una sola línea | Cuando se necesita visualizar la distribución de una variable numérica de forma más expresiva que con matplotlib puro |
| pingouin | Librería de estadística descriptiva e inferencial con tablas bien formateadas | Cuando se necesita reportar estadísticas descriptivas por grupos con formato listo para presentar |
| statsmodels | Librería para modelos estadísticos y pruebas de hipótesis | Cuando el análisis descriptivo es el primer paso hacia un modelo de regresión o una prueba de diferencia de grupos |
| Excel / Google Sheets | Herramientas de hoja de cálculo con funciones estadísticas básicas | Para validar manualmente los resultados de pandas o compartir los números con personas no técnicas |

## 📚 Recursos para profundizar

- [Documentación de pandas — Estadísticas descriptivas](https://pandas.pydata.org/docs/user_guide/basics.html#descriptive-statistics): referencia completa de métodos como `mean`, `median`, `std`, `describe` y `quantile`
- [Khan Academy — Estadística y probabilidad](https://es.khanacademy.org/math/statistics-probability): recurso gratuito en español para reforzar los conceptos de media, mediana, varianza y distribuciones
- [Statistics for Data Science — Towards Data Science](https://towardsdatascience.com/statistics-for-data-science): colección de artículos prácticos que conectan conceptos estadísticos con código en pandas y numpy
- [scipy.stats — Documentación oficial](https://docs.scipy.org/doc/scipy/reference/stats.html): referencia para pruebas estadísticas y distribuciones cuando se necesita ir más allá de la estadística descriptiva básica

## ⚡ Comandos de instalación

```bash
pip install pandas numpy scipy matplotlib seaborn
```
