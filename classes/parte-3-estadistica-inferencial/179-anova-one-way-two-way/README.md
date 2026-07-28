# Clase 179 — ANOVA (one-way, two-way)

> Parte: **3 — Estadística Inferencial y Causal** · Fuente: ISLP, **cap. 13** + Bruce & Bruce, **cap. 3** *ANOVA*. ⏱️ Duración estimada: **80 min**.

> 🎚️ **Nivel:** Intermedio-Avanzado

## 🎯 Objetivo

Que el alumno aplique **ANOVA de una vía** (≥ 3 grupos, una variable categórica) y **ANOVA de dos vías** (dos factores categóricos + interacción), entienda por qué no se hacen "t-tests todos contra todos" (inflación de α) y sepa hacer **post-hoc** con Tukey HSD. Reconocer los supuestos (independencia, normalidad por grupo, homogeneidad de varianzas) y cuándo usar la alternativa robusta **Welch ANOVA** o el no paramétrico **Kruskal-Wallis** (Clase 150).

## 📚 Resultados de aprendizaje

Al finalizar, el estudiante podrá:

- Plantear `H₀: μ₁ = μ₂ = ... = μ_k` vs `H₁: al menos uno difiere` y aplicar `scipy.stats.f_oneway` o `pingouin.anova`.
- Interpretar `F = MS_between / MS_within` y su relación con la F-distribution (`F(k-1, n-k)`).
- Aplicar **Welch's ANOVA** (`pingouin.welch_anova`) cuando se viola la homogeneidad de varianzas (Levene rechaza).
- Hacer **Tukey HSD** post-hoc con `pingouin.pairwise_tukey` y leer los IC ajustados.
- Distinguir **efectos principales** de **interacción** en ANOVA two-way y graficar interaction plots con `seaborn.pointplot`.
- Reportar **η²** o **ω²** como effect size de ANOVA.

## 🗺️ Temas

- ¿Por qué no t-tests múltiples? Si hacés 10 t-tests al α=0.05, la probabilidad de al menos un falso positivo es ≈ 40 %.
- Descomposición de varianza: `SS_total = SS_between + SS_within`.
- F-statistic: razón entre varianza explicada por los grupos y varianza residual.
- Supuestos: independencia, normalidad (Shapiro por grupo o residuos), homocedasticidad (Levene/Bartlett).
- Welch ANOVA — análogo a Welch's t-test para ≥ 3 grupos.
- Post-hoc: Tukey HSD (controla family-wise error rate), Bonferroni, Holm.
- Two-way ANOVA: efectos principales A, B, e **interacción A×B**.
- Effect size: η² (eta-squared), ω² (omega-squared, menos sesgado).

## 📖 Definiciones y características

- **One-way ANOVA**: testea si la media de una variable continua difiere entre los niveles de **una** variable categórica.
- **Two-way ANOVA**: dos variables categóricas. Permite testear 3 cosas: efecto principal de A, efecto principal de B, e **interacción** (¿el efecto de A depende del nivel de B?).
- **F-statistic**: `MS_between / MS_within`. Si los grupos tienen la misma media, ambos son estimadores de σ² → F ≈ 1. Si difieren, MS_between crece.
- **SS (sum of squares) within**: variabilidad residual dentro de cada grupo. Σ (x_ij - x̄_i)².
- **SS between**: variabilidad de las medias grupales respecto a la gran media. Σ n_i · (x̄_i - x̄)².
- **Homocedasticidad**: igualdad de varianzas entre grupos. Test: **Levene** (robusto), **Bartlett** (sensible a normalidad).
- **Welch ANOVA**: no asume homocedasticidad. Es el **default razonable** moderno, igual que Welch's t-test.
- **Tukey HSD (Honestly Significant Difference)**: compara todas las parejas controlando el family-wise error rate al α global.
- **Interacción**: cuando el efecto de un factor cambia según el nivel del otro. En el plot, las líneas no son paralelas.
- **η² (eta-squared)**: `SS_between / SS_total`. Proporción de varianza explicada. Sesgado hacia arriba.
- **ω² (omega-squared)**: corrige el sesgo de η². Recomendado para reportar.

## 📂 Dataset / recursos

- `seaborn.load_dataset('tips')`: `total_bill` por `day` (one-way), o por `day × time` (two-way).
- `seaborn.load_dataset('penguins')`: `body_mass_g` por `species` (one-way claro).
- Librerías: `scipy.stats`, `pingouin`, `statsmodels.api as sm`, `statsmodels.formula.api as smf`.

## 🧪 Ejercicios

1. **One-way**: aplicá `scipy.stats.f_oneway(*[grupo for grupo in penguins.groupby('species').body_mass_g])`. Reportá F, p y `dof_between, dof_within`.
2. **Supuestos**: testá normalidad por grupo (`pingouin.normality(penguins, dv='body_mass_g', group='species')`) y homocedasticidad (`pingouin.homoscedasticity`). Si Levene rechaza, repetí con `pingouin.welch_anova`.
3. **Post-hoc Tukey**: `pingouin.pairwise_tukey(data=penguins, dv='body_mass_g', between='species')`. Identificá qué pares de especies difieren significativamente.
4. **Two-way con interacción**: `pingouin.anova(data=tips, dv='total_bill', between=['day', 'time'])`. Mirá las tres filas de la tabla (day, time, day×time).
5. **Interaction plot**: `sns.pointplot(data=tips, x='day', y='total_bill', hue='time')`. Si las líneas se cruzan o no son paralelas → hay interacción visual; cruzala con el p-value del término `day*time`.

## 📝 Homework verificable

Sobre `penguins` (filtrando filas con NA):

1. ANOVA one-way de `flipper_length_mm` por `species`.
2. Chequear Levene y Shapiro; decidir entre ANOVA clásico y Welch ANOVA, justificando.
3. Tukey HSD post-hoc.
4. Reportar ω² (`pingouin.anova(... effsize='n2'`, y calcular ω² manualmente).
5. Conclusión en 3 líneas: qué pares difieren, magnitud del efecto general (η²/ω²), si hay alguna comparación dudosa.

**Criterio de aceptación**: el ANOVA debe rechazar `H₀` (p < 0.001), Tukey debe mostrar las tres parejas significativas, y η² debe ser > 0.5 (efecto grande — las tres especies tienen aletas claramente distintas).

## ⚠️ Errores comunes

| Síntoma / mensaje | Causa y cómo arreglar |
|---|---|
| Hago `ttest_ind` entre cada par de 4 grupos y reporto los p-values | Con 4 grupos son 6 comparaciones; α efectivo ≈ 0.26. **Fix**: ANOVA + Tukey post-hoc, o ajustar con Bonferroni (Clase 151). |
| ANOVA da p < 0.05 pero ningún Tukey lo da | Puede pasar con varianzas muy distintas. **Fix**: Welch ANOVA + Games-Howell post-hoc (`pingouin.pairwise_gameshowell`). |
| Aplico ANOVA con varianzas muy distintas (Levene p < 0.01) | El F-test clásico es sensible a esto, especialmente con grupos desbalanceados. **Fix**: Welch ANOVA. |
| Los residuos no son normales y reporto ANOVA igual | Si los grupos son grandes (n ≥ 30 c/u), TCL salva. Si son chicos y muy asimétricos, **Fix**: Kruskal-Wallis (Clase 150) o ANOVA con bootstrap. |
| Interpreto "efecto de A" sin mirar la interacción A×B significativa | Si hay interacción, el efecto principal de A **no es interpretable solo** — depende del nivel de B. **Fix**: interpretar interacción primero; los main effects solo si la interacción es no significativa. |

## ❓ Preguntas frecuentes

**❓ ¿ANOVA o regresión lineal con dummies?**

Son matemáticamente equivalentes. ANOVA es la presentación tradicional; OLS con dummies (`statsmodels.formula.api.ols('y ~ C(species)', data).fit()`) da los mismos F y p. La regresión también te da los coeficientes de cada nivel respecto a la categoría de referencia, lo cual es más informativo.

**❓ ¿Tukey o Bonferroni post-hoc?**

Tukey es **mejor** para todas-las-parejas porque controla el family-wise error rate de manera específica para ANOVA (es uniformemente más poderoso que Bonferroni en ese caso). Bonferroni es más conservador (peor poder). Ver Clase 151 para alternativas modernas (Holm, BH).

**❓ ¿Qué pasa si los grupos están desbalanceados (n distinto)?**

ANOVA aguanta moderadamente, pero con varianzas distintas el F-test se rompe. **Welch ANOVA** lo maneja bien.

**❓ ¿Two-way ANOVA cuando alguna celda tiene n=0?**

Modelo no balanceado: usar **Type III SS** (`statsmodels` lo soporta vía `sm.stats.anova_lm(model, typ=3)`). Type I (default) depende del orden de los factores en la fórmula.

**❓ ¿Y si tengo medidas repetidas (mismo sujeto en cada nivel)?**

`pingouin.rm_anova` (repeated measures ANOVA). Modela la correlación intra-sujeto, lo cual ANOVA clásico ignora.

## 🔗 Referencias

- ISLP, **cap. 13** — sección sobre ANOVA y multiple testing.
- Bruce & Bruce, **cap. 3** — sección *ANOVA*.
- Welch, B.L. (1951), *On the comparison of several mean values: an alternative approach*, Biometrika.
- [`scipy.stats.f_oneway`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f_oneway.html), [`pingouin.welch_anova`](https://pingouin-stats.org/generated/pingouin.welch_anova.html), [`pingouin.pairwise_tukey`](https://pingouin-stats.org/generated/pingouin.pairwise_tukey.html).
- [statsmodels — ANOVA](https://www.statsmodels.org/stable/anova.html) (para Type II/III SS y modelos mixtos).

## 📥 Material descargable

- 📄 [Guía explicativa (PDF)](./clase-179-anova-one-way-two-way-guia-explicativa.pdf) — versión imprimible con todo el contenido de la clase.
- 🎞️ [Presentación (PPTX)](./clase-179-anova-one-way-two-way-presentacion.pptx) — deck PowerPoint listo para proyectar en clase.
- 🧮 [Notebook ejecutable (.ipynb)](./notebook.ipynb) — abrilo desde el laboratorio del programa o desde Jupyter.

## ➡️ Siguiente clase

[Clase 180 — Tests no paramétricos: Mann-Whitney, Wilcoxon, Kruskal-Wallis](../180-tests-no-parametricos-mann-whitney-wilcoxon-kruskal-wallis/README.md)
