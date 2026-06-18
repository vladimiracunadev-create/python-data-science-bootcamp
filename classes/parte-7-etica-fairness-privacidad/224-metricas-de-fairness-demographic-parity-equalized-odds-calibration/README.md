# Clase 224 — Métricas de fairness: demographic parity, equalized odds, calibration

> Parte: **7 — Ética, Fairness y Privacidad** · Fuente: Barocas, Hardt, Narayanan — [*Fairness and Machine Learning*](https://fairmlbook.org/) **cap. 3** + Hardt, Price, Srebro (NeurIPS 2016) [*Equality of Opportunity in Supervised Learning*](https://arxiv.org/abs/1610.02413). ⏱️ Duración estimada: **75 min**.

## 🎯 Objetivo

Pasar de "el modelo es injusto" a **medirlo con un número**. Implementar las tres familias de métricas grupales que dominan la literatura — **demographic parity**, **equalized odds**, **calibration** — sobre un dataset binario con atributo protegido, y demostrar **numéricamente** el teorema de imposibilidad de Kleinberg-Mullainathan-Raghavan / Chouldechova (2017): salvo casos triviales, **no se pueden satisfacer las tres a la vez**.

## 📚 Resultados de aprendizaje

Al finalizar, el estudiante podrá:

- Calcular **demographic parity gap** = |P(Ŷ=1|A=0) − P(Ŷ=1|A=1)| sobre predicciones de cualquier clasificador binario.
- Calcular **equal opportunity** (TPR por grupo) y **equalized odds** (TPR y FPR por grupo) — *Hardt, Price, Srebro 2016*.
- Verificar **calibración por grupo** con reliability curves: P(Y=1|Ŝ=s, A=a) debe ser igual entre grupos para un mismo score s.
- Demostrar el **teorema de imposibilidad**: ajustar threshold por grupo para forzar demographic parity rompe calibración.
- Aplicar **mitigación post-processing** con thresholds por grupo (Hardt 2016) y reportar el trade-off accuracy vs fairness gap.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | Atributo protegido A y notación Y / Ŷ / Ŝ | Sin notación común no se discute fairness; A puede ser género, raza, edad, código postal proxy. |
| 2 | Demographic parity (statistical parity) | La métrica más antigua (regla del 80%, US EEOC); ignora el ground truth. |
| 3 | Equal opportunity y equalized odds (Hardt 2016) | Condicionan en Y — corrigen el defecto de DP cuando las base-rates difieren. |
| 4 | Calibration por grupo (Chouldechova 2017) | El score debe significar lo mismo en cada grupo; lo que reclamó ProPublica vs COMPAS. |
| 5 | Teorema de imposibilidad (KMR / Chouldechova 2017) | Si las base-rates difieren, DP + equalized odds + calibration son **mutuamente incompatibles**. |
| 6 | Post-processing: threshold por grupo | Mitigación más simple; revela explícitamente el trade-off. |

## 📖 Definiciones y características

- **Atributo protegido** `A`: variable demográfica sensible (sexo, raza, edad). En la práctica nunca está sola — hay **proxies** (zip code, nombre, historial).
- **Demographic parity (DP)**: `P(Ŷ=1 | A=0) = P(Ŷ=1 | A=1)`. Métrica: `DP_gap = |selection_rate(A=0) − selection_rate(A=1)|`. **Regla del 80%**: ratio ≥ 0.8 para que la US EEOC no lo considere discriminación.
- **Equal opportunity**: `P(Ŷ=1 | Y=1, A=0) = P(Ŷ=1 | Y=1, A=1)`. O sea, **TPR igual**. Solo a los positivos reales se les exige misma tasa de aceptación.
- **Equalized odds** (Hardt-Price-Srebro 2016): equal opportunity **+ FPR igual**. `EO_gap = max(|TPR_diff|, |FPR_diff|)`.
- **Calibration** (predictive parity, Chouldechova 2017): `P(Y=1 | Ŝ=s, A=a)` es igual entre grupos para todo score s. Un score 0.7 significa "70% chance" tanto para A=0 como para A=1.
- **Impossibility theorem** (Kleinberg-Mullainathan-Raghavan 2017 + Chouldechova 2017): si `P(Y=1|A=0) ≠ P(Y=1|A=1)` (base rates diferentes) y el clasificador no es perfecto, **no existe** clasificador que sea simultáneamente calibrado por grupo y con equalized odds. Es matemático, no técnico — no se resuelve con más datos.
- **Accuracy-fairness trade-off**: forzar cualquier paridad sobre un clasificador óptimo de Bayes **baja accuracy**. La pregunta política es cuánta accuracy estamos dispuestos a sacrificar.
- **Tooling**: [`fairlearn`](https://fairlearn.org/) (Microsoft) — `MetricFrame`, `ThresholdOptimizer`. [`aif360`](https://aif360.res.ibm.com/) (IBM) — 70+ métricas y mitigadores. Ambas open source.

## 📂 Dataset / recursos

- **Dataset notebook**: sintético binario con un atributo protegido `A∈{0,1}` y base rates diferentes (60% vs 40%) — necesario para que el teorema de imposibilidad se active.
- **Dataset real recomendado para tarea**: [Adult / Census Income](https://archive.ics.uci.edu/dataset/2/adult) (UCI) con `sex` como atributo protegido, o [COMPAS](https://github.com/propublica/compas-analysis) (ProPublica) con `race`.
- Librerías: `numpy`, `pandas`, `scikit-learn`. Opcional: `fairlearn`.

## 🧪 Ejercicios

1. **Selection rate por grupo**: entrenar `LogisticRegression` baseline. Calcular `P(Ŷ=1|A=0)` y `P(Ŷ=1|A=1)` y el `DP_gap`. ¿Cumple regla del 80%?
2. **TPR y FPR por grupo**: armar `confusion_matrix` separada por grupo. Calcular `equal_opportunity_gap = |TPR_0 − TPR_1|` y `equalized_odds_gap = max(|TPR_diff|, |FPR_diff|)`.
3. **Calibration curves por grupo**: binning de scores en 10 bins. Para cada bin y cada grupo, graficar `mean(y_true) vs mean(y_score)`. ¿Las curvas coinciden?
4. **Romper calibración**: ajustar threshold por grupo (`t_0`, `t_1`) tal que se cumpla DP exacta. Recalcular calibración — debe degradarse. (Demostración numérica del teorema.)
5. **Post-processing Hardt**: buscar `(t_0, t_1)` que **minimicen** `equalized_odds_gap` y reportar el costo en accuracy global. Tabla: baseline vs DP-fixed vs EO-fixed.

## 📝 Homework verificable

Notebook con:

1. Cargar **Adult Census** (UCI). Atributo protegido: `sex`. Target: `income > 50K`.
2. Entrenar baseline `LogisticRegression` + reportar accuracy, AUC.
3. Calcular las tres métricas: `DP_gap`, `equal_opportunity_gap`, `equalized_odds_gap` y **calibration_gap** (max |calibration(A=0) − calibration(A=1)| sobre bins).
4. Implementar post-processing con threshold por grupo que minimice `EO_gap` sujeto a `accuracy_drop ≤ 3pp`.
5. Tabla final: 3 modelos (baseline, DP-mitigated, EO-mitigated) × 5 métricas (accuracy, AUC, DP_gap, EO_gap, calibration_gap). Discutir cuál elegirías y **por qué** — no hay respuesta universal.

**Criterio de aceptación**: las 4 métricas implementadas a mano (no llamando a `fairlearn`), el `EO_gap` mitigado < 0.05, y un párrafo justificando la elección de métrica en función del **dominio de aplicación** (crédito vs admisión universitaria vs medicina).

## ⚠️ Errores comunes

| Síntoma / mensaje | Causa y cómo arreglar |
|---|---|
| `DP_gap = 0` pero el modelo es claramente injusto | DP ignora el ground truth — si las base rates difieren, forzar DP puede empeorar la utilidad para el grupo desfavorecido. **Fix**: reportar también equal opportunity. |
| Calibration "perfecta" pero TPR diferente entre grupos | Es el resultado natural cuando las base rates difieren — el teorema de imposibilidad en acción. **Fix**: documentar el trade-off explícitamente, no esconderlo. |
| Quitar el atributo protegido del input "soluciona" el problema | **Fairness through unawareness** — no funciona: zip code, nombre, historial son **proxies**. **Fix**: medir igual con A presente. |
| Threshold único 0.5 para todos los grupos | Asume que los scores significan lo mismo en cada grupo. **Fix**: medir calibración antes de asumirlo. |
| Usar accuracy global para comparar fairness | Accuracy global puede subir y empeorar al grupo minoritario simultáneamente (Simpson). **Fix**: reportar accuracy **por grupo**. |
| `MetricFrame` de fairlearn devuelve `nan` | Algún grupo tiene 0 positivos predichos o 0 reales. **Fix**: filtrar splits estratificados; revisar tamaño mínimo por grupo (>30). |

## ❓ Preguntas frecuentes

**❓ ¿Cuál de las tres métricas uso?**

Depende del **dominio**. Crédito o contratación: **equal opportunity** (no negarle empleo a quien sí calificaría). Justicia penal / riesgo de reincidencia: **calibration** + **FPR equal** (el debate ProPublica vs COMPAS giró exactamente sobre cuál priorizar). Publicidad: **DP** suele alcanzar. Pero la elección es **política, no técnica**.

**❓ ¿Demographic parity no es siempre lo que queremos?**

No. Si la base rate real difiere entre grupos (ej. distribución de ingresos), DP puede forzar al modelo a aceptar candidatos peores de un grupo y rechazar mejores de otro. **Equal opportunity** suele ser más defendible.

**❓ ¿El teorema de imposibilidad significa que fairness es imposible?**

No — significa que no se pueden satisfacer las **tres simultáneamente** cuando las base rates difieren. Hay que **elegir** cuál priorizar, y documentarlo. El paper de Chouldechova (2017) es lectura obligada.

**❓ ¿`fairlearn` o `aif360`?**

`fairlearn` para empezar (API más limpia, integrada con sklearn). `aif360` cuando se necesite catálogo amplio de mitigadores (pre/in/post-processing) y métricas exóticas. Ninguna sustituye entender las definiciones.

**❓ ¿Y la fairness individual?**

Otra familia (Dwork et al. 2012): "individuos similares deben recibir predicciones similares". Más difícil de operacionalizar (requiere métrica de similaridad justificable) y queda fuera del alcance de esta clase. Ver Clase 225-227 para privacy y Clase 228 para causal fairness.

## 🔗 Referencias

- Hardt, M., Price, E., Srebro, N. *Equality of Opportunity in Supervised Learning*, NeurIPS 2016. https://arxiv.org/abs/1610.02413
- Chouldechova, A. *Fair prediction with disparate impact: A study of bias in recidivism prediction instruments*, Big Data 2017. https://arxiv.org/abs/1610.07524
- Kleinberg, J., Mullainathan, S., Raghavan, M. *Inherent Trade-Offs in the Fair Determination of Risk Scores*, ITCS 2017. https://arxiv.org/abs/1609.05807
- Barocas, S., Hardt, M., Narayanan, A. *Fairness and Machine Learning* (fairmlbook.org), **cap. 3** — *Classification*.
- [`fairlearn` documentation](https://fairlearn.org/) — Microsoft, MIT license.
- [`AIF360` documentation](https://aif360.res.ibm.com/) — IBM, Apache 2.0.

## ➡️ Siguiente clase

[Clase 225 — Privacidad diferencial: intro](../225-privacidad-diferencial-intro/README.md)
