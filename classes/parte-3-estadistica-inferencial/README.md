# Parte 3 — Estadística Inferencial y Causal

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏮️ Parte anterior](../parte-2-deep-learning/README.md) · [⏭️ Parte siguiente](../parte-4-mlops/README.md)

**17 clases** · ~5 semanas (puede intercalarse con Parte 1) · ✅ Contenido completo (expansión 2026: effect size, CUPED+sequential, DoubleML, Synthetic Controls)

**Fuente principal:** **ISLP** ([*Statistical Learning with Python*](https://www.statlearning.com/)) — rigor matemático en tests, intervalos y diseño experimental. Complementado con **Bruce & Bruce** (*Practical Statistics for Data Scientists*, 2ª ed.), **Pearl** (*Book of Why*) para causalidad e **Imbens & Rubin** para inferencia causal moderna.

Cada clase tiene su `README.md` con objetivo, resultados de aprendizaje verificables, dataset recomendado, 5 ejercicios y homework con criterio de aceptación. Todas las 17 clases incluyen las tres secciones del patrón pedagógico v2.2.0:

- **📖 Definiciones y características** — términos técnicos con explicación y características clave.
- **⚠️ Errores comunes** — tabla de síntomas/mensajes con causa y solución concretas (las trampas que vienen de Parte 1 + las propias de inferencia).
- **❓ Preguntas frecuentes** — FAQs auténticas que aparecen al estudiar cada tema.

**📌 Cobertura moderna (audit 2026) — 2 complementos integrados + 4 clases dedicadas:**

Complementos integrados dentro de la clase original:

- Clase 153 → **BCa bootstrap** y APIs modernas de scipy (`scipy.stats.bootstrap`, `scipy.stats.permutation_test`, ≥1.9).
- Clase 158 → **PyMC v5** + **NumPyro** (JAX backend) + **ArviZ** — el stack bayesiano moderno post-Theano.

Clases dedicadas (expansión 2026 con patrón completo + ejercicios + homework propios):

- Clase **147a** → effect size dedicado (Cohen's d, Hedges' g, Cliff's δ, CLES) con `pingouin`.
- Clase **154a** → CUPED, sequential testing y always-valid p-values (Deng 2013, Howard 2021).
- Clase **156a** → DoubleML / EconML para ATE/CATE con ML como nuisance (Chernozhukov 2018).
- Clase **157a** → Synthetic Control Method dedicado (pysyncon, SparseSC, Synthetic DiD).

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

- **Tests clásicos** — clases 146–151 — distribuciones, t-test, chi-cuadrado, ANOVA, no paramétricos, comparaciones múltiples.
- **Estimación e incertidumbre** — clases 152–153 — intervalos de confianza, bootstrap, permutation tests.
- **Experimentación y causalidad** — clases 154–157 — A/B testing, diseño experimental, inferencia causal con DAGs, uplift / DiD.
- **Inferencia bayesiana** — clase 158 — priors, posterior, MCMC con PyMC.

## 📚 Índice de clases (13)

- [146 — Distribuciones: normal, binomial, Poisson, exponencial](146-distribuciones-normal-binomial-poisson-exponencial/README.md)
- [147 — Test t (una muestra, dos muestras, pareado)](147-test-t-una-muestra-dos-muestras-pareado/README.md)
- [147a — Effect size dedicado: Cohen's d, Hedges' g, Cliff's δ con pingouin](147a-effect-size-cohen-d-hedges-g-cliff-delta-pingouin/README.md) 🆕
- [148 — Test chi-cuadrado de independencia y bondad de ajuste](148-test-chi-cuadrado-de-independencia-y-bondad-de-ajuste/README.md)
- [149 — ANOVA (one-way, two-way)](149-anova-one-way-two-way/README.md)
- [150 — Tests no paramétricos: Mann-Whitney, Wilcoxon, Kruskal-Wallis](150-tests-no-parametricos-mann-whitney-wilcoxon-kruskal-wallis/README.md)
- [151 — Corrección de comparaciones múltiples (Bonferroni, FDR)](151-correccion-de-comparaciones-multiples-bonferroni-fdr/README.md)
- [152 — Intervalos de confianza](152-intervalos-de-confianza/README.md)
- [153 — Bootstrap y permutation tests](153-bootstrap-y-permutation-tests/README.md)
- [154 — A/B testing: tamaño de muestra, poder estadístico](154-a-b-testing-tamano-de-muestra-poder-estadistico/README.md)
- [154a — CUPED, sequential testing, always-valid p-values](154a-cuped-sequential-testing-always-valid-p-values/README.md) 🆕
- [155 — Diseño experimental](155-diseno-experimental/README.md)
- [156 — Inferencia causal: DAGs, confounders, instrumentos](156-inferencia-causal-dags-confounders-instrumentos/README.md)
- [156a — DoubleML / EconML: Machine Learning para causalidad](156a-doubleml-econml-ml-para-causalidad/README.md) 🆕
- [157 — Uplift modeling, DiD (difference-in-differences)](157-uplift-modeling-did-difference-in-differences/README.md)
- [157a — Synthetic Control Method dedicado (pysyncon, SparseSC)](157a-synthetic-control-method-pysyncon/README.md) 🆕
- [158 — Bayes intro: priors, posterior, MCMC con PyMC](158-bayes-intro-priors-posterior-mcmc-con-pymc/README.md)

---

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏮️ Parte anterior](../parte-2-deep-learning/README.md) · [⏭️ Parte siguiente](../parte-4-mlops/README.md)
