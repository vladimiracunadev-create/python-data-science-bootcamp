# Parte 3 — Estadística Inferencial y Causal

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏮️ Parte anterior](../parte-2-deep-learning/README.md) · [⏭️ Parte siguiente](../parte-4-mlops/README.md)

**19 clases** · ~6 semanas (puede intercalarse con Parte 1) · ✅ Contenido completo (expansión 2026: effect size, BCa bootstrap, CUPED+sequential, DoubleML, Synthetic Controls, PyMC v5/NumPyro/ArviZ)

**Fuente principal:** **ISLP** ([*Statistical Learning with Python*](https://www.statlearning.com/)) — rigor matemático en tests, intervalos y diseño experimental. Complementado con **Bruce & Bruce** (*Practical Statistics for Data Scientists*, 2ª ed.), **Pearl** (*Book of Why*) para causalidad e **Imbens & Rubin** para inferencia causal moderna.

Cada clase tiene su `README.md` con objetivo, resultados de aprendizaje verificables, dataset recomendado, 5 ejercicios y homework con criterio de aceptación. Todas las 19 clases incluyen las tres secciones del patrón pedagógico v2.2.0:

- **📖 Definiciones y características** — términos técnicos con explicación y características clave.
- **⚠️ Errores comunes** — tabla de síntomas/mensajes con causa y solución concretas (las trampas que vienen de Parte 1 + las propias de inferencia).
- **❓ Preguntas frecuentes** — FAQs auténticas que aparecen al estudiar cada tema.

**📌 Cobertura moderna (audit 2026) — 6 clases dedicadas:**

Todos los temas modernos ahora son clases independientes con patrón completo + ejercicios + homework:

- Clase **177** → Effect size dedicado (Cohen's d, Hedges' g, Cliff's δ, CLES) con pingouin.
- Clase **184** → BCa bootstrap y APIs modernas de scipy (`scipy.stats.bootstrap`, `permutation_test`).
- Clase **186** → CUPED, sequential testing y always-valid p-values (Deng 2013, Howard 2021).
- Clase **189** → DoubleML / EconML para ATE/CATE con ML como nuisance (Chernozhukov 2018).
- Clase **191** → Synthetic Control Method dedicado (pysyncon, SparseSC, Synthetic DiD).
- Clase **193** → Stack bayesiano moderno: PyMC v5, NumPyro, ArviZ.

---

## 🎯 ¿De qué trata esta parte?

La parte que separa al data scientist del "sklearn user". Cubre **inferencia estadística** (tests, intervalos, bootstrap), **diseño de experimentos** (A/B testing real, no solo `p < 0.05`) e **inferencia causal** (DAGs, confounders, instrumentos, DiD, uplift) — herramientas que se usan a diario para responder preguntas tipo "¿esto que cambiamos en el producto realmente movió la métrica?" o "¿este coeficiente significa lo que creo que significa?".

Se intercala bien con la Parte 1 porque la mayoría de los problemas de evaluación de modelos (comparar dos clasificadores, decidir si una mejora es real) son problemas estadísticos disfrazados. Incluye una introducción a estadística bayesiana con PyMC para abrir la puerta a inferencia con incertidumbre explícita.

## 🧩 Problemas que resuelve

- Decidir si una diferencia observada es estadísticamente significativa o ruido.
- Diseñar un A/B test con tamaño de muestra y poder estadístico correctos, no a ojo.
- Aplicar el test correcto según los supuestos del dato (paramétrico vs no paramétrico, pareado vs independiente).
- Corregir comparaciones múltiples (Bonferroni, FDR) para no inflar el falso positivo.
- Estimar incertidumbre con bootstrap cuando los supuestos clásicos no aplican.
- Identificar confounders en un DAG y elegir la estrategia causal correcta (control, IV, DiD, uplift).
- Hacer una inferencia bayesiana básica con MCMC en PyMC.

## 🎓 Resultados de aprendizaje

Al finalizar esta parte, el estudiante podrá:

- Diseñar y analizar un A/B test end-to-end, incluyendo poder estadístico y corrección por múltiples métricas.
- Aplicar bootstrap para construir intervalos de confianza no paramétricos sobre cualquier estimador.
- Dibujar el DAG de un problema de negocio y justificar qué variables controlar.
- Implementar un modelo bayesiano simple en PyMC e interpretar el posterior.

## 🗺️ Estructura temática

- **Tests clásicos** — clases 175–181 — distribuciones, t-test, chi-cuadrado, ANOVA, no paramétricos, comparaciones múltiples.
- **Estimación e incertidumbre** — clases 182–184 — intervalos de confianza, bootstrap, permutation tests.
- **Experimentación y causalidad** — clases 185–191 — A/B testing, diseño experimental, inferencia causal con DAGs, uplift / DiD.
- **Inferencia bayesiana** — clases 192–193 — priors, posterior, MCMC con PyMC.

## 📚 Índice de clases (19)

- [175 — Distribuciones: normal, binomial, Poisson, exponencial](175-distribuciones-normal-binomial-poisson-exponencial/README.md)
- [176 — Test t (una muestra, dos muestras, pareado)](176-test-t-una-muestra-dos-muestras-pareado/README.md)
- [177 — Effect size dedicado: Cohen's d, Hedges' g, Cliff's δ con pingouin](177-effect-size-cohen-d-hedges-g-cliff-delta-pingouin/README.md)
- [178 — Test chi-cuadrado de independencia y bondad de ajuste](178-test-chi-cuadrado-de-independencia-y-bondad-de-ajuste/README.md)
- [179 — ANOVA (one-way, two-way)](179-anova-one-way-two-way/README.md)
- [180 — Tests no paramétricos: Mann-Whitney, Wilcoxon, Kruskal-Wallis](180-tests-no-parametricos-mann-whitney-wilcoxon-kruskal-wallis/README.md)
- [181 — Corrección de comparaciones múltiples (Bonferroni, FDR)](181-correccion-de-comparaciones-multiples-bonferroni-fdr/README.md)
- [182 — Intervalos de confianza](182-intervalos-de-confianza/README.md)
- [183 — Bootstrap y permutation tests](183-bootstrap-y-permutation-tests/README.md)
- [184 — BCa bootstrap y APIs modernas de scipy](184-bca-bootstrap-scipy-permutation-test-moderno/README.md)
- [185 — A/B testing: tamaño de muestra, poder estadístico](185-a-b-testing-tamano-de-muestra-poder-estadistico/README.md)
- [186 — CUPED, sequential testing, always-valid p-values](186-cuped-sequential-testing-always-valid-p-values/README.md)
- [187 — Diseño experimental](187-diseno-experimental/README.md)
- [188 — Inferencia causal: DAGs, confounders, instrumentos](188-inferencia-causal-dags-confounders-instrumentos/README.md)
- [189 — DoubleML / EconML: Machine Learning para causalidad](189-doubleml-econml-ml-para-causalidad/README.md)
- [190 — Uplift modeling, DiD (difference-in-differences)](190-uplift-modeling-did-difference-in-differences/README.md)
- [191 — Synthetic Control Method dedicado (pysyncon, SparseSC)](191-synthetic-control-method-pysyncon/README.md)
- [192 — Bayes intro: priors, posterior, MCMC con PyMC](192-bayes-intro-priors-posterior-mcmc-con-pymc/README.md)
- [193 — Stack bayesiano moderno: PyMC v5, NumPyro, ArviZ](193-pymc-v5-numpyro-arviz-stack-bayesiano/README.md)

## 📥 Material descargable — parte completa

Materiales consolidados con TODAS las clases de esta parte (útiles para revisar offline o imprimir el bloque entero):

- 📄 [Guía PDF — parte completa](../../docs/pdfs/parts/parte-3-estadistica-inferencial-completa.pdf) — todas las clases concatenadas con headings demoteados.
- 🎞️ [Presentación PPTX — parte completa](../../docs/presentaciones/parts/parte-3-estadistica-inferencial-completa.pptx) — portada + TOC + slides de cada clase.

---

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏮️ Parte anterior](../parte-2-deep-learning/README.md) · [⏭️ Parte siguiente](../parte-4-mlops/README.md)
