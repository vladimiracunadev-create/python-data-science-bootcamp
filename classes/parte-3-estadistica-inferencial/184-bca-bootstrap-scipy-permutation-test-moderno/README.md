# Clase 184 — BCa bootstrap y APIs modernas de scipy

> Parte: **3 — Estadística Inferencial y Causal** · Fuente: Efron (1987) BCa + DiCiccio & Efron (1996) + [scipy.stats.bootstrap docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html). ⏱️ Duración estimada: **75 min**.

## 🎯 Objetivo

Profundizar el **BCa (Bias-Corrected and accelerated) bootstrap** —el default moderno (Efron 1987)— y las **APIs modernas de scipy** (`scipy.stats.bootstrap` ≥ 1.9, `scipy.stats.permutation_test` ≥ 1.8). Cubrir las correcciones que BCa hace sobre percentile clásico: **bias correction** (z₀) y **acceleration** (a) vía jackknife.

## 📚 Resultados de aprendizaje

Al finalizar, el estudiante podrá:

- Diferenciar bootstrap **percentile** vs **basic** vs **BCa**.
- Calcular `z₀` (bias correction) y `a` (acceleration) manualmente.
- Aplicar `scipy.stats.bootstrap((data,), statistic, method='BCa', n_resamples=10_000)`.
- Aplicar `permutation_test` para p-value de comparación de 2 grupos sin paramétrica.
- Reconocer cuándo BCa importa: estadísticos no lineales, distribuciones asimétricas.

## 🗺️ Temas

- Percentile bootstrap: cuantiles directos. Sub-cubre con asimetría.
- Basic bootstrap: reflexión `2θ̂ - q_{1-α/2}`.
- BCa: corrige bias (`z₀`) y aceleración (`a` vía jackknife).
- Studentized bootstrap: estandariza con SE bootstrap del SE.
- Scipy.stats.bootstrap API.
- Permutation test exacto.

## 📖 Definiciones y características

- **`z₀`**: `Φ⁻¹(P(θ*_b ≤ θ̂))` — fracción de bootstraps por debajo del estimador.
- **`a` (acceleration)**: estima cómo SE depende del parámetro. Calculado con jackknife.
- **BCa interval**: percentiles ajustados `α₁, α₂` función de `z₀, a, z_{α/2}`.
- **`scipy.stats.bootstrap` desde 1.9**: vectorizado, BCa default, IC + SE + bias estimate.
- **`permutation_test`**: re-mezcla labels bajo H₀, calcula stat distribution.

## 📂 Dataset / recursos

- Datos lognormales sintéticos.
- `seaborn.load_dataset('diamonds')` para mediana de price.
- Librerías: `scipy.stats`, `numpy`, `matplotlib`.

## 🧪 Ejercicios

1. **Tres ICs**: para mediana de `x = rng.lognormal(0, 1, 100)`, calcular IC con percentile, basic, BCa. Comparar.
2. **z₀ a mano**: implementar `z₀ = ppf((B_below_θ̂) / B)`. Verificar contra scipy.
3. **`a` con jackknife**: implementar leave-one-out para cada `θ̂_(i)`. Calcular `a`.
4. **Cobertura empírica**: 1000 datasets `Exp(1)`, n=25; cobertura percentile vs BCa. BCa más cerca de 95 %.
5. **Permutation_test**: comparar dos lognormales con tamaño efecto chico. P-value exacto.

## 📝 Homework verificable

IC del AUC de un clasificador binario:

1. `LogisticRegression` en breast cancer. AUC en test.
2. Bootstrap BCa de `(y_test, y_proba)`: 5000 resamples.
3. Reportar `AUC [BCa 95% CI]`.
4. Comparar con percentile bootstrap (más estrecho, sub-cubre).

**Criterio de aceptación**: BCa CI asimétrico (refleja asimetría de AUC cerca de 1.0); más amplio que percentile.

## ⚠️ Errores comunes

| Síntoma / mensaje | Causa y cómo arreglar |
|---|---|
| BCa con `n_resamples=100` | Inestable. **Fix**: ≥ 5000, idealmente 10000. |
| Estadístico no vectorizable lento | Bootstrap es O(B). **Fix**: `vectorized=False` en scipy si statistic no vectoriza. |
| Bootstrap sobre serie temporal | Asume independencia. **Fix**: block bootstrap (clase de series). |
| `permutation_test` n_resamples=999 | Resolución del p-value `1/(n+1)`. **Fix**: 10_000+. |
| Reportar percentile vs BCa indistintamente | BCa tiene cobertura nominal. **Fix**: documentar el método. |

## ❓ Preguntas frecuentes

**❓ Cuándo BCa importa?**

Con estadísticos sesgados (mediana en asimetría) o n chico. Para media + n grande, percentile basta.

**❓ Studentized bootstrap mejor que BCa?**

A veces. Requiere SE del SE → bootstrap doble → costoso. BCa es el compromiso pragmático.

**❓ Para IC de proporciones?**

Wilson o Clopper-Pearson son específicos y mejores que bootstrap genérico.

**❓ `vectorized=True` en scipy?**

Si tu statistic acepta `axis=`, sí — 100× más rápido.

**❓ Block bootstrap para series?**

`scipy` no lo tiene; `arch.bootstrap.MovingBlockBootstrap` sí.

## 🔗 Referencias

- Efron (1987), *Better Bootstrap Confidence Intervals*, JASA.
- DiCiccio & Efron (1996), *Bootstrap Confidence Intervals*, Statistical Science.
- [`scipy.stats.bootstrap`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html).
- [`scipy.stats.permutation_test`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.permutation_test.html).

## ➡️ Siguiente clase

[Clase 185 — A/B testing: tamaño de muestra, poder estadístico](../185-a-b-testing-tamano-de-muestra-poder-estadistico/README.md)
