# Clase 147a — Effect size dedicado: Cohen's d, Hedges' g, Cliff's δ con pingouin

> Parte: **3 — Estadística Inferencial y Causal** · Fuente: Cohen (1988) + Lakens (2013) + Vallat (2018) pingouin. ⏱️ Duración estimada: **75 min**.

## 🎯 Objetivo

Dominar **effect size** —la métrica que el p-value no responde: "cuán grande es la diferencia"—. Cubrir 6 medidas: **Cohen's d** (means, varianzas similares), **Hedges' g** (bias-corrected para n chico), **Glass's Δ** (varianza del control como denominador), **Cliff's δ** (no paramétrico), **r de correlación**, **odds ratio**. Aplicar con `pingouin` en una sola llamada. Reportar correctamente: APA 7 lo exige.

## 📚 Resultados de aprendizaje

Al finalizar, el estudiante podrá:

- Calcular Cohen's d a mano y con `pingouin.compute_effsize`.
- Aplicar la corrección de Hedges (recomendada cuando n < 50/grupo).
- Interpretar magnitudes (Cohen 1988): 0.2 / 0.5 / 0.8 = small / medium / large.
- Calcular Cliff's δ para datos ordinales / muy asimétricos.
- Reportar effect size con IC95 % bootstrap.
- Diseñar tabla APA-7 con `mean ± SD`, `Cohen's d [95% CI]`, `t`, `p`.

## 🗺️ Temas

- Cohen's d: `(x̄₁ - x̄₂) / s_pooled`.
- Hedges' g: `d · (1 - 3/(4·gl - 1))`.
- Glass's Δ: usar `s_control` como denominator. Útil cuando control y treatment tienen varianza distinta.
- Cliff's δ: probabilistic dominance.
- Effect size para correlación: r (= Pearson) o R².
- Effect size para chi-cuadrado: Cramér's V, phi.
- IC95 % de effect size: bootstrap o fórmulas paramétricas.

## 📖 Definiciones y características

- **Cohen's d**: estándar para 2 grupos independientes.
- **`s_pooled`**: `sqrt(((n1-1)·s1² + (n2-1)·s2²) / (n1+n2-2))`.
- **Hedges' g**: corrección para muestras chicas; siempre menor que d.
- **Cliff's δ**: en `[-1, 1]`. Interpretación Romano (2006): < 0.147 negligible, < 0.33 small, < 0.474 medium, ≥ 0.474 large.
- **CLES (Common Language Effect Size)**: P(rand X > rand Y). Más interpretable para no-técnicos.

## 📂 Dataset / recursos

- `seaborn.load_dataset('tips')`.
- Librerías: `pingouin`, `scipy.stats`, `numpy`.

## 🧪 Ejercicios

1. **Cohen's d a mano**: para `tip` por `sex`, calcular manualmente con `s_pooled`.
2. **`pingouin.compute_effsize`**: verificar contra cálculo manual. Probar `eftype='cohen' | 'hedges' | 'glass' | 'CLES'`.
3. **Hedges' g**: con n=10 por grupo, ver diferencia entre d y g (Hedges < d).
4. **Cliff's δ**: para datos Likert ordinales o muy asimétricos, calcular y interpretar.
5. **Effect size + IC**: bootstrap del Cohen's d → IC95 %.

## 📝 Homework verificable

Análisis estadístico riguroso de `tips`:

1. Comparar `tip` por `time` (Lunch/Dinner) y por `day`.
2. Reportar Cohen's d (o Hedges' g si n < 30) con IC95 % bootstrap.
3. Para `day` (4 niveles), reportar partial η² del ANOVA.
4. Conclusión APA-7 estilo: "M ± SD, t(df) = X, p = Y, d [95% CI]".

**Criterio de aceptación**: tabla bien formada con todas las columnas; conclusión no usa solo p-value.

## ⚠️ Errores comunes

| Síntoma / mensaje | Causa y cómo arreglar |
|---|---|
| Reportar solo `p < 0.05` | Mala práctica desde 1999. **Fix**: agregar effect size con IC. |
| Cohen's d sobre datos muy asimétricos | Sesgado. **Fix**: Cliff's δ. |
| Mismo Cohen's d en 2 estudios sin contexto | Magnitudes 0.2/0.5/0.8 son orientativas — depende del dominio. **Fix**: comparar contra meta-analyses del campo. |
| Effect size sin IC | Incompleto. **Fix**: bootstrap CI. |
| Confundir d con η² | Distintos rangos y significados. **Fix**: d para 2 grupos, η² para ANOVA. |

## ❓ Preguntas frecuentes

**❓ Cohen's d o Hedges' g?**

Hedges siempre si n < 50/grupo. Para n grande son indistinguibles.

**❓ Magnitudes 0.2/0.5/0.8 son universales?**

No. Son orientación. En medicina pueden ser muy distintas. Reporte tu d, dejá que el lector compare con su literatura.

**❓ CLES interpretable?**

Sí — "65 % chance que una persona random del grupo A tenga mayor valor que una random del B". Comunicable a no-técnicos.

**❓ Effect size para A/B testing?**

Sí — Cohen's h para proporciones, Cohen's d para continuous. Ver clase 154.

**❓ Effect size negativo?**

Solo indica dirección. La magnitud `|d|` es lo que se interpreta.

## 🔗 Referencias

- Cohen (1988), *Statistical Power Analysis for the Behavioral Sciences*.
- Lakens (2013), *Calculating and reporting effect sizes to facilitate cumulative science*, Frontiers in Psychology.
- Romano et al. (2006), *Cliff's δ interpretation*.
- [pingouin docs](https://pingouin-stats.org/).
- APA Publication Manual 7th ed.

## ➡️ Siguiente clase

[Clase 148 — Test chi-cuadrado de independencia y bondad de ajuste](../148-test-chi-cuadrado-de-independencia-y-bondad-de-ajuste/README.md)
