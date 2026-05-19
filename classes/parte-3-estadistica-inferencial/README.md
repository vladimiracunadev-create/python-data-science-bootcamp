# Parte 3 — Estadística Inferencial y Causal

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏮️ Parte anterior](../parte-2-deep-learning/README.md) · [⏭️ Parte siguiente](../parte-4-mlops/README.md)

**13 clases** · ~4 semanas (puede intercalarse con Parte 1)

**Fuente principal:** **ISLP** ([*Statistical Learning with Python*](https://www.statlearning.com/)) — rigor matemático en tests, intervalos y diseño experimental.

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
- [148 — Test chi-cuadrado de independencia y bondad de ajuste](148-test-chi-cuadrado-de-independencia-y-bondad-de-ajuste/README.md)
- [149 — ANOVA (one-way, two-way)](149-anova-one-way-two-way/README.md)
- [150 — Tests no paramétricos: Mann-Whitney, Wilcoxon, Kruskal-Wallis](150-tests-no-parametricos-mann-whitney-wilcoxon-kruskal-wallis/README.md)
- [151 — Corrección de comparaciones múltiples (Bonferroni, FDR)](151-correccion-de-comparaciones-multiples-bonferroni-fdr/README.md)
- [152 — Intervalos de confianza](152-intervalos-de-confianza/README.md)
- [153 — Bootstrap y permutation tests](153-bootstrap-y-permutation-tests/README.md)
- [154 — A/B testing: tamaño de muestra, poder estadístico](154-a-b-testing-tamano-de-muestra-poder-estadistico/README.md)
- [155 — Diseño experimental](155-diseno-experimental/README.md)
- [156 — Inferencia causal: DAGs, confounders, instrumentos](156-inferencia-causal-dags-confounders-instrumentos/README.md)
- [157 — Uplift modeling, DiD (difference-in-differences)](157-uplift-modeling-did-difference-in-differences/README.md)
- [158 — Bayes intro: priors, posterior, MCMC con PyMC](158-bayes-intro-priors-posterior-mcmc-con-pymc/README.md)

---

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏮️ Parte anterior](../parte-2-deep-learning/README.md) · [⏭️ Parte siguiente](../parte-4-mlops/README.md)
