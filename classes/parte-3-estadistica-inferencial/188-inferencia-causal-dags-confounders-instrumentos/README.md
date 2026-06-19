# Clase 188 — Inferencia causal: DAGs, confounders, instrumentos

> Parte: **3 — Estadística Inferencial y Causal** · Fuente: Pearl, *The Book of Why* + Hernán & Robins, *Causal Inference: What If* (libro gratuito, 2024) + Imbens & Rubin. ⏱️ Duración estimada: **95 min**.

## 🎯 Objetivo

Distinguir **correlación de causalidad** con rigor: dibujar **DAGs** (Directed Acyclic Graphs), identificar **confounders**, **colliders** y **mediators**, aplicar el **backdoor criterion** para decidir qué variables controlar, y usar **variables instrumentales (IV)** cuando la randomización no es posible. Conocer la herramienta moderna **Double Machine Learning (DoubleML / EconML)** para estimar **ATE/CATE** con ML como nuisance estimator.

## 📚 Resultados de aprendizaje

Al finalizar, el estudiante podrá:

- Dibujar un DAG para un problema de negocio e identificar los tres tipos de estructura: chain (X → M → Y), fork (X ← Z → Y, confounder), collider (X → C ← Y).
- Aplicar el **backdoor criterion** de Pearl: encontrar el conjunto mínimo de variables a controlar para identificar el efecto causal.
- Reconocer que controlar por un **collider** o un **mediator** introduce sesgo, NO lo elimina.
- Estimar ATE (Average Treatment Effect) con regresión + controles, IPW (Inverse Probability Weighting) y matching.
- Usar **2SLS (Two-Stage Least Squares)** con `linearmodels.iv` cuando hay un instrumento válido.
- Aplicar **Double Machine Learning** con `doubleml` / `econml` para estimar ATE/CATE con ML como nuisance (sin asumir linealidad).

## 🗺️ Temas

- Correlación ≠ causalidad: el clásico ejemplo "helado y ahogamientos" — confounder: temperatura.
- DAGs: nodos = variables, flechas = relación causal.
- 3 estructuras canónicas: chain, fork, collider.
- **Backdoor criterion**: bloquear todos los caminos no causales de X a Y; **no abrir** colliders.
- ATE = `E[Y | do(T=1)] - E[Y | do(T=0)]`. El "do" indica intervención, no observación.
- Identificación: ¿se puede expresar `E[Y | do(T)]` con datos observacionales? Si sí → estimar.
- IV: variable Z que afecta T pero NO a Y excepto vía T. Permite identificar el efecto cuando hay confounders no observados.
- **Complemento moderno**: Double Machine Learning (Chernozhukov et al. 2018) — usa ML para estimar las "nuisance functions" y separa la inferencia causal de la complejidad del fit.

## 📌 Versión profundizada — 2026

El tema moderno que antes vivía como complemento dentro de esta clase ahora tiene su(s) clase(s) propia(s) con patrón completo, ejercicios y homework:

- 👉 [Clase 156a — DoubleML / EconML: Machine Learning para causalidad](../156a-doubleml-econml-ml-para-causalidad/README.md)

## 📖 Definiciones y características

- **DAG**: grafo dirigido acíclico que representa relaciones causales. Cada flecha es una hipótesis causal.
- **Confounder (fork)**: `T ← Z → Y`. Z causa tanto T como Y; controlando Z se identifica el efecto.
- **Collider**: `T → C ← Y`. Controlar C **introduce** asociación espuria (sesgo de selección). Ejemplo clásico: Berkson's bias.
- **Mediator (chain)**: `T → M → Y`. Controlar M **bloquea** el efecto causal indirecto y solo deja el directo (a veces útil, a veces no).
- **Backdoor criterion** (Pearl): un set Z de variables identifica el efecto causal de T sobre Y si: (a) bloquea todos los caminos backdoor (que empiezan con flecha entrando a T), y (b) no contiene descendientes de T.
- **ATE (Average Treatment Effect)**: `E[Y(1) - Y(0)]` — efecto promedio si todos vs nadie recibiera tratamiento.
- **CATE (Conditional ATE)**: `E[Y(1) - Y(0) | X=x]` — efecto para individuos con características X=x.
- **Instrumento (IV)**: variable Z que satisface (a) **relevancia** (afecta a T), (b) **exclusión** (no afecta Y excepto vía T), (c) **independencia** (no comparte confounders con Y).
- **2SLS**: estima IV ajustando `T = αZ + ε₁` (1ª etapa), reemplazando `T̂` en `Y = θT̂ + ε₂` (2ª etapa).
- **DML**: ML para nuisance + Neyman-orthogonal score + cross-fitting → inferencia causal robusta.

## 📂 Dataset / recursos

- Ejemplos simulados de Pearl: smoking-cancer con tar como mediator.
- `econml.tests.dgps` para datos sintéticos con efectos heterogéneos conocidos.
- Lalonde 1986 (NSW job training program) — clásico de causal inference.
- Librerías: `doubleml`, `econml`, `linearmodels`, `pgmpy` (DAG inference), `dowhy` (Microsoft, framework completo).

## 🧪 Ejercicios

1. **DAG en código**: con `pgmpy` (o `networkx`), definí un DAG con T, Y, Z (confounder), C (collider). Identificá visualmente paths y aplicá `dowhy` para encontrar el adjustment set.
2. **Sesgo del collider**: simulá `T ~ N(0,1)`, `Y ~ N(T, 1)`, `C = T + Y + ε`. Estimá `Y ~ T` sin controlar C y controlando C. Mostrá que controlar el collider **destruye** la relación causal.
3. **Backdoor ajustando confounder**: simulá `Z, T = f(Z) + ε, Y = 2T + 3Z + δ`. OLS `Y ~ T` sesgado. OLS `Y ~ T + Z` recupera el 2.
4. **2SLS**: simular un IV `Z → T → Y` con confounder no observado entre T y Y. Aplicar `linearmodels.iv.IV2SLS.from_formula('Y ~ 1 + [T ~ Z]', data).fit()`. Recuperar el efecto verdadero.
5. **DML con random forest**: dataset sintético con confounders no lineales. Comparar OLS ingenuo vs OLS con polinomios vs `DoubleMLPLR(ml_g=RF, ml_m=RF)`. Verificar que DML es el menos sesgado.

## 📝 Homework verificable

Sobre un dataset simulado de "efecto de un programa de capacitación sobre salario":

1. Generar `X` (edad, educación, experiencia) como confounders. Generar `T` (participa) con `P(T|X)` no trivial. Generar `Y` con efecto causal `θ_true = 2_000`.
2. Estimar el efecto con: (a) diferencia ingenua de medias, (b) OLS con controles lineales, (c) DoubleML con RF.
3. Comparar contra `θ_true`. Reportar bias y IC95 %.
4. Dibujar el DAG (puede ser un comentario con notación o un grafo simple).
5. Discutir en 3 líneas qué pasaría si hubieras controlado por un mediator (ej.: "horas trabajadas").

**Criterio de aceptación**: DML debe recuperar `θ_true ± 200`. OLS lineal puede estar sesgado si la relación X→Y no es lineal. La diferencia ingenua debe estar fuertemente sesgada. La discusión debe mencionar que controlar mediators sesga hacia 0.

## ⚠️ Errores comunes

| Síntoma / mensaje | Causa y cómo arreglar |
|---|---|
| Controlo "todo lo que tengo" en la regresión para "estar seguro" | Si entre esos hay colliders o mediators, **introducís sesgo**. **Fix**: dibujar DAG primero, aplicar backdoor criterion. |
| Asumo que el coeficiente OLS es causal cuando hay confounders no observados | No lo es. **Fix**: IV (si tenés instrumento), DiD (con paneles), o decir explícitamente que la estimación es asociacional. |
| Uso un instrumento débil (correlación con T < 0.1) | 2SLS con IV débil tiene sesgo y SE inflado. **Fix**: F-statistic de la 1ª etapa ≥ 10 (regla de Stock & Yogo). |
| `doubleml` con `n_folds=2` y muestra chica | Cross-fitting con pocos folds no estabiliza. **Fix**: `n_folds=5` mínimo. |
| Interpreto un coeficiente OLS como ATE sin verificar identificación | OLS = ATE solo bajo unconfoundedness. **Fix**: dibujar DAG y justificar. |

## ❓ Preguntas frecuentes

**❓ ¿Cómo sé si dibujé bien el DAG?**

No hay método estadístico para validarlo completamente — el DAG codifica supuestos sustantivos (de dominio). Lo que sí podés hacer: **falsificación condicional** — el DAG implica ciertas independencias condicionales; testealas con los datos y si fallan, el DAG está mal. `dowhy.refute_estimate` automatiza muchos refutation tests.

**❓ ¿IV o DML cuando tengo ambos?**

Si tenés un IV válido y confiable, IV es **identificación más fuerte** (resiste confounders no observados). DML solo aguanta confounders observados. Lo ideal: triangular con ambos.

**❓ ¿Causal forest vs random forest clásico?**

Causal forest no minimiza error de predicción; minimiza heterogeneidad del efecto causal entre hojas. Cada hoja contiene unidades con efecto causal similar.

**❓ ¿Qué tan robusto es DML a especificación errónea?**

DML es **doubly robust**: si o el modelo de `g` o el de `m` está bien especificado, el estimador del efecto es consistente. Cero modelos correctos → sesgo. Es la mejor garantía actual sin randomización.

**❓ ¿Inferencia causal con datos observacionales puede reemplazar un RCT?**

No completamente. RCT randomiza el tratamiento → corta todas las flechas backdoor por diseño. Observacional siempre depende de supuestos no testables (unconfoundedness, IV exclusion). El estándar es: RCT cuando se puede; cuasi-experimental (DiD, IV, RDD) cuando no; y reportar sensitivity analyses.

## 🔗 Referencias

- Pearl, J. (2018), *The Book of Why* — intuición sin matemática pesada.
- Pearl, J., Glymour, M. & Jewell, N. (2016), *Causal Inference in Statistics: A Primer* — el libro técnico corto.
- Hernán, M. & Robins, J. (2024), *Causal Inference: What If*. [Libro gratuito](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/).
- Chernozhukov et al. (2018), *Double/Debiased Machine Learning for Treatment and Structural Parameters*, Econometrics Journal.
- [doubleml docs](https://docs.doubleml.org/) (Python + R).
- [EconML docs](https://econml.azurewebsites.net/) — Microsoft Research.
- [DoWhy](https://www.pywhy.org/dowhy/) — framework de identificación + estimación + refutación.

## 📥 Material descargable

- 📄 [Guía explicativa (PDF)](./clase-188-inferencia-causal-dags-confounders-instrumentos-guia-explicativa.pdf) — versión imprimible con todo el contenido de la clase.
- 🎞️ [Presentación (PPTX)](./clase-188-inferencia-causal-dags-confounders-instrumentos-presentacion.pptx) — deck PowerPoint listo para proyectar en clase.
- 🧮 [Notebook ejecutable (.ipynb)](./notebook.ipynb) — abrilo desde el laboratorio del programa o desde Jupyter.

## ➡️ Siguiente clase

[Clase 189 — DoubleML / EconML: Machine Learning para causalidad](../189-doubleml-econml-ml-para-causalidad/README.md)
