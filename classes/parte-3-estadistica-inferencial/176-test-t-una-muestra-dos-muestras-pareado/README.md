# Clase 176 — Test t (una muestra, dos muestras, pareado)

> Parte: **3 — Estadística Inferencial y Causal** · Fuente: ISLP, **cap. 13** + Bruce & Bruce, **cap. 3** *Statistical Experiments and Significance Testing*. ⏱️ Duración estimada: **80 min**.

> 🎚️ **Nivel:** Intermedio-Avanzado

## 🎯 Objetivo

Que el alumno aplique correctamente las tres variantes del test t —**una muestra, dos muestras independientes (Welch por default), pareado**—, distinga **hipótesis nula y alternativa**, lea **p-value e intervalo de confianza** de la salida de `scipy.stats` y `pingouin`, y aprenda a reportar **effect size** (Cohen's d, Hedges' g) junto con el p-value para no caer en la trampa de "significativo pero irrelevante".

## 📚 Resultados de aprendizaje

Al finalizar, el estudiante podrá:

- Formular `H₀` y `H₁` (bilateral / unilateral) para un problema concreto y elegir la variante correcta del test t.
- Ejecutar `scipy.stats.ttest_1samp`, `ttest_ind(equal_var=False)` y `ttest_rel`, interpretando el `statistic`, `pvalue` y el atributo `.confidence_interval()` (scipy ≥ 1.10).
- Verificar supuestos: normalidad por grupo (Shapiro / Q-Q plot) o invocar TCL si `n ≥ 30`.
- Decidir entre test **bilateral vs unilateral** sin caer en *p-hacking* (la dirección debe estar fijada antes de mirar los datos).
- Reportar **effect size**: Cohen's `d`, Hedges' `g` corregido para muestras chicas, y su interpretación cualitativa (small/medium/large).

## 🗺️ Temas

- `H₀` / `H₁`, errores tipo I (α) y tipo II (β).
- Test t de una muestra: `t = (x̄ - μ₀) / (s/√n)`, gl `= n - 1`.
- Test t de dos muestras independientes: **Welch** (varianzas distintas, default moderno) vs Student (varianzas iguales — supuesto fuerte, casi nunca correcto).
- Test t pareado (mismo sujeto antes/después).
- p-value: probabilidad bajo `H₀` de observar algo *al menos tan extremo*. NO es `P(H₀ | datos)`.
- Intervalo de confianza al 95 % como complemento del p-value.
- **Complemento moderno**: effect size (Cohen's d, Hedges' g, Cliff's δ) — la pregunta "¿es relevante?" que el p-value no responde.

## 📌 Versión profundizada — 2026

El tema moderno que antes vivía como complemento dentro de esta clase ahora tiene su(s) clase(s) propia(s) con patrón completo, ejercicios y homework:

- 👉 [Clase 177 — Effect size dedicado: Cohen's d, Hedges' g, Cliff's δ con pingouin](../177-effect-size-cohen-d-hedges-g-cliff-delta-pingouin/README.md)

## 📖 Definiciones y características

- **Hipótesis nula `H₀`**: la afirmación "conservadora" — no hay diferencia, o la diferencia es 0. Se busca **rechazarla**, no probarla.
- **Hipótesis alternativa `H₁`**: lo que querés demostrar. Bilateral (`≠`) o unilateral (`>`, `<`).
- **p-value**: `P(estadístico al menos tan extremo como el observado | H₀ verdadera)`. Si `p < α`, rechazo `H₀`. NO es la probabilidad de que `H₀` sea verdadera.
- **α (alpha)**: probabilidad máxima de error tipo I (rechazar `H₀` siendo verdadera). Convencional: `0.05`. Para problemas críticos: `0.01` o `0.001`.
- **β (beta)**: probabilidad de error tipo II (no rechazar `H₀` siendo falsa). Poder = `1 - β` (Clase 154).
- **Welch's t-test**: variante que no asume varianzas iguales. Es el **default razonable**. `equal_var=True` (Student clásico) es legacy.
- **Test pareado**: cuando cada observación de un grupo tiene su "par" en el otro (mismo paciente antes/después, misma página web con/sin cambio). Reduce varianza al diferenciar dentro del par.
- **Cohen's d**: magnitud estandarizada de la diferencia. `d = 0.2/0.5/0.8` → small/medium/large.
- **`alternative='greater'`**: unilateral derecho. Solo legítimo si la dirección la fijaste **antes** de ver los datos.

## 📂 Dataset / recursos

- `seaborn.load_dataset('tips')`: comparar `tip` entre `sex='Male'` vs `'Female'`, o `time='Lunch'` vs `'Dinner'`.
- Para pareado: simular un dataset *antes/después* con `numpy.random.default_rng` (presión arterial pre/post fármaco).
- Librerías: `scipy.stats`, `pingouin` (`pip install pingouin`), `seaborn`.

## 🧪 Ejercicios

1. **Una muestra**: con `tips.total_bill`, testá `H₀: μ = 20` vs `H₁: μ ≠ 20` con `scipy.stats.ttest_1samp(tips.total_bill, popmean=20)`. Reportá t, p y el IC95 % (`.confidence_interval()`).
2. **Dos muestras (Welch)**: testá si `tip` difiere entre `sex='Male'` y `sex='Female'` con `ttest_ind(equal_var=False)`. Calculá Cohen's d a mano y verificá contra `pingouin.ttest`.
3. **Pareado**: simulá presión arterial antes/después de un fármaco con `rng = np.random.default_rng(0)`: `antes = rng.normal(140, 12, 30)`, `despues = antes - rng.normal(5, 3, 30)`. Aplicá `ttest_rel(antes, despues)` y comparalo contra hacer `ttest_ind` mal (verás cómo el pareado tiene mucho más poder).
4. **Bilateral vs unilateral**: para el ejercicio 2, repetí con `alternative='greater'` y `'less'`. Observá cómo el p-value se divide ≈ 2.
5. **Significativo vs relevante**: generá `grupo_a = rng.normal(100, 15, 10_000)` y `grupo_b = rng.normal(100.5, 15, 10_000)`. El test va a dar `p < 0.001`; calculá Cohen's d y discutí en 2 líneas por qué el resultado "no importa".

## 📝 Homework verificable

Sobre `tips`:

1. Hipótesis: la propina promedio es distinta para `time='Lunch'` y `time='Dinner'`.
2. Verificar normalidad de cada grupo con `pingouin.normality` (Shapiro).
3. Ejecutar `pingouin.ttest` y reportar: T, gl, p-value, IC95 %, Cohen's d, power.
4. Una conclusión de 3 líneas que mencione **(a) si rechazás `H₀`, (b) la magnitud del efecto en palabras (small/medium/large), (c) si recomendarías ese hallazgo a un dueño de restaurante**.

**Criterio de aceptación**: el reporte debe incluir effect size y la conclusión no puede limitarse a "p < 0.05". Si Cohen's d es < 0.2, la respuesta a (c) debería ser "no" aunque el p sea bajo.

## ⚠️ Errores comunes

| Síntoma / mensaje | Causa y cómo arreglar |
|---|---|
| Aplico `ttest_ind` con `equal_var=True` por costumbre y los grupos tienen `n` muy distintos | Student clásico con varianzas desiguales y `n` desbalanceado **infla el error tipo I**. **Fix**: dejar `equal_var=False` (Welch) por default; ya es lo recomendado en la literatura desde hace décadas. |
| `p < 0.05` con `n = 10⁶` y declaro un hallazgo importante | "Significancia estadística" con muestra gigante captura efectos triviales. **Fix**: reportar Cohen's d y discutir relevancia. |
| Cambio `alternative='greater'` después de ver que `x̄_a > x̄_b` | Eso es **p-hacking**. La dirección se fija con la pregunta de negocio, no con los datos. **Fix**: bilateral por default; unilateral solo si hay un *pre-registro* o lógica de dominio fuerte. |
| Aplico `ttest_ind` a observaciones pareadas (mismo sujeto antes/después) | Pierde poder enormemente y puede dar `p > 0.05` cuando pareado da `p < 0.001`. **Fix**: `ttest_rel` cuando hay pareo natural. |
| El test asume normalidad y mis datos son muy asimétricos con `n=12` | Welch es robusto pero no mágico. **Fix**: `scipy.stats.mannwhitneyu` (Clase 150) o bootstrap (Clase 153). |

## ❓ Preguntas frecuentes

**❓ ¿Welch o Student por default?**

**Welch siempre**. No cuesta nada en poder cuando las varianzas son iguales, y protege contra el caso (muy común) de varianzas distintas. La literatura moderna (Delacre, Lakens & Leys 2017) recomienda abandonar el Student t-test.

**❓ ¿Tengo que testear normalidad antes del t-test?**

No con `n ≥ 30` por grupo (TCL). Con `n` chico y datos visiblemente asimétricos, sí — y si Shapiro rechaza, mejor pasar a bootstrap o Mann-Whitney. Cuidado: con `n` enorme, Shapiro rechaza siempre por desviaciones triviales; mirá Q-Q plot como complemento.

**❓ ¿Qué es `BF10` que reporta pingouin?**

Factor de Bayes contra `H₀`. `BF10 > 3` es evidencia moderada a favor de `H₁`; `> 10` fuerte. Es la versión bayesiana del p-value y no tiene los problemas del NHST (la testeás directamente en la Clase 158).

**❓ ¿Por qué el IC95 % de la diferencia y el p-value siempre concuerdan?**

Porque son la misma información presentada de otra forma. Si el IC95 % de `μ_a - μ_b` **no incluye 0**, entonces `p < 0.05` (bilateral). Reportar el IC es más informativo: muestra magnitud y dirección.

**❓ Cohen's d me da 0.3, ¿cómo lo explico al cliente?**

"Un efecto pequeño-mediano". Operacionalmente: si dibujás las dos distribuciones, el ≈ 55 % de los individuos del grupo tratamiento superan a la mediana del grupo control (vs 50 % bajo `H₀`). Para una conversión, traducilo a "incremento absoluto de X puntos porcentuales".

## 🔗 Referencias

- ISLP, **cap. 13** — *Multiple Testing*, intro al p-value.
- Bruce & Bruce, **cap. 3** — *Statistical Experiments and Significance Testing*.
- Delacre, Lakens & Leys (2017), *Why Psychologists Should by Default Use Welch's t-test*, IRSP.
- Cohen, J. (1988), *Statistical Power Analysis for the Behavioral Sciences* — referencia canónica de effect size.
- [pingouin docs](https://pingouin-stats.org/) — Vallat, R. (2018), *Pingouin: statistics in Python*, JOSS.
- [`scipy.stats.ttest_ind`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html) — atención a `equal_var` y `alternative`.

## 📥 Material descargable

- 📄 [Guía explicativa (PDF)](./clase-176-test-t-una-muestra-dos-muestras-pareado-guia-explicativa.pdf) — versión imprimible con todo el contenido de la clase.
- 🎞️ [Presentación (PPTX)](./clase-176-test-t-una-muestra-dos-muestras-pareado-presentacion.pptx) — deck PowerPoint listo para proyectar en clase.
- 🧮 [Notebook ejecutable (.ipynb)](./notebook.ipynb) — abrilo desde el laboratorio del programa o desde Jupyter.

## ➡️ Siguiente clase

[Clase 177 — Effect size dedicado: Cohen's d, Hedges' g, Cliff's δ con pingouin](../177-effect-size-cohen-d-hedges-g-cliff-delta-pingouin/README.md)
