# Clase 223 — Tipos de sesgo algorítmico y orígenes

> Parte: **7 — Ética, Fairness y Privacidad** · Fuente: Suresh & Guttag, [*A Framework for Understanding Sources of Harm throughout the ML Life Cycle*](https://arxiv.org/abs/1901.10002) (EAAMO 2021) + Barocas, Hardt, Narayanan, [*Fairness and Machine Learning*](https://fairmlbook.org/) (2023), **caps. 1-2**. ⏱️ Duración estimada: **75 min**.
>
> 🎚️ **Nivel:** Intermedio-Avanzado

## 🎯 Objetivo

Aprender a **nombrar y diagnosticar** el origen del sesgo en un sistema ML antes de intentar mitigarlo. Un modelo "sesgado" no es un bug: es el resultado de decisiones tomadas en cada fase del life cycle (recolección, medición, modelado, evaluación, despliegue). Si no sabemos **dónde** entró el sesgo, no podemos elegir la mitigación correcta (Clases 225-227).

## 📚 Resultados de aprendizaje

Al finalizar, el estudiante podrá:

- Distinguir los **6 tipos** del framework Suresh-Guttag: **histórico, representación, medición, agregación, evaluación, despliegue**.
- Identificar el origen probable de un sesgo dado evidencia empírica (gap de accuracy entre subgrupos, drift, proxy-target gap).
- Reproducir el patrón de **Gender Shades** (Buolamwini & Gebru 2018): accuracy alta global, accuracy baja en subgrupo minoritario.
- Reconocer **Simpson's paradox** y por qué un modelo único puede ser peor que un modelo por subgrupo.
- Justificar por qué **fairness no es solo un problema del modelo** — empieza en la definición de la tarea.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | Sesgo histórico | El dato es "correcto" pero refleja un mundo injusto. COMPAS, Amazon Hiring 2018. |
| 2 | Sesgo de representación | Subgrupos sub-muestreados → modelo aprende mal sobre ellos (Gender Shades). |
| 3 | Sesgo de medición | El proxy ≠ el target real (re-arresto ≠ recidiva; calificación docente ≠ aprendizaje). |
| 4 | Sesgo de agregación | Un modelo único asume que todos los subgrupos comparten distribución (Simpson). |
| 5 | Sesgo de evaluación | El benchmark de test no representa la población de despliegue. |
| 6 | Sesgo de despliegue | El modelo se usa fuera del contexto en que se entrenó (population shift). |

## 📖 Definiciones y características

- **Sesgo histórico**: la realidad social que se midió ya era injusta. *El dato es preciso, pero codifica desigualdad.* Ej.: Amazon entrenó su hiring tool con 10 años de CVs (~mayoría hombres en tech) → penalizaba la palabra "women's" en CVs.
- **Sesgo de representación**: el dataset bajo-representa un subgrupo. *No es que el modelo sea injusto: nunca vio suficientes ejemplos.* Ej.: IJB-A face dataset era 79% piel clara → Gender Shades mostró error 34.7% en mujeres de piel oscura vs 0.8% en hombres de piel clara (Buolamwini & Gebru, 2018).
- **Sesgo de medición (proxy bias)**: el `y` que medimos no es el `y` que queremos. *Recidiva* (queremos predecir) ≠ *re-arresto* (lo que medimos) — el arresto depende del policing, que ya está sesgado.
- **Sesgo de agregación**: un modelo único asume una única función óptima `f(x) → y` para toda la población. Si los subgrupos tienen distintas `P(y | x)`, el modelo único es peor que **k modelos por subgrupo** (instancia del *Simpson's paradox*).
- **Sesgo de evaluación**: el test set no representa la población objetivo. Ej.: evaluar un detector de melanoma sobre un benchmark 90% piel clara y reportar "97% accuracy".
- **Sesgo de despliegue**: el modelo se aplica a una distribución distinta a la de entrenamiento (covariate shift, label shift) — o a un contexto socio-técnico donde su salida significa otra cosa. Un score que era "una sugerencia para el juez" se vuelve "la decisión".
- **Framework Suresh-Guttag (2021)**: mapea los 6 sesgos a las fases del ML life cycle (data collection → preparation → modeling → evaluation → deployment). Cada fase introduce su propio harm; mitigar en la fase equivocada no funciona.
- **Harm allocacional vs representacional** (Barocas et al., cap. 1): el sistema deniega recursos (préstamo, libertad bajo fianza) **vs** refuerza estereotipos (autocomplete de Google asocia "CEO" con foto de hombre).

## 📂 Dataset / recursos

- **Dataset**: sintético (préstamos con sesgo histórico inyectado). Auto-generado en el notebook con `numpy` seed 42.
- Librerías: `numpy`, `pandas`, `scikit-learn`. Sin descargas externas.

## 🧪 Ejercicios

1. **Sesgo histórico**: generar un dataset de préstamos donde `P(aprobado | grupo=A) = 0.70` y `P(aprobado | grupo=B) = 0.30` por razones históricas (no por capacidad de pago). Entrenar `LogisticRegression` sin la feature `grupo` y mostrar que el modelo igual reproduce el gap vía proxies (código postal, ingreso, etc.).
2. **Selection rate disparity**: calcular `P(ŷ=1 | grupo=A)` vs `P(ŷ=1 | grupo=B)` — la métrica más simple de **demographic parity** (Clase 224).
3. **Sesgo de representación (Gender Shades)**: re-muestrear el dataset al 10% del grupo B. Reportar accuracy global vs accuracy por subgrupo. Mostrar el patrón "97% global, 60% en B".
4. **Sesgo de medición**: definir `y_proxy = y_true XOR ruido_correlacionado_con_grupo`. Entrenar sobre `y_proxy`. Mostrar que el modelo aprende el patrón del **ruido**, no del target real.
5. **Sesgo de agregación (Simpson)**: comparar AUC de **un modelo único** vs **un modelo por subgrupo**. Mostrar que el modelo único es subóptimo en ambos subgrupos.

## 📝 Homework verificable

Notebook con:

1. Reproducir el patrón Gender Shades sobre un dataset tabular (sintético o UCI Adult con `sex` y `race`).
2. Calcular **gap de accuracy** entre subgrupos para 3 niveles de sub-muestreo del grupo minoritario (50%, 20%, 5%).
3. Aplicar el framework Suresh-Guttag a un caso real (COMPAS, Amazon Hiring, o un modelo del trabajo) — escribir 1 párrafo por cada uno de los 6 tipos: ¿está presente? evidencia.
4. Implementar Simpson's paradox: dataset donde la correlación global es opuesta a la correlación intra-grupo.
5. Discutir: ¿qué mitigación corresponde a cada tipo? (representación → re-sampling; medición → re-definir target; agregación → modelo por subgrupo).

**Criterio de aceptación**: el alumno identifica los 6 tipos en al menos un caso real con evidencia cuantitativa, y propone una mitigación específica por tipo (no genérica "más datos").

## ⚠️ Errores comunes

| Síntoma | Causa y cómo arreglar |
|---|---|
| "Saqué la variable sensible y el modelo sigue siendo sesgado" | **Fairness through unawareness** no funciona — hay proxies (ZIP, nombre, escuela). **Fix**: medir disparidad sobre la variable sensible aunque no la uses como input. |
| Accuracy global alta pero el cliente reporta errores en un subgrupo | Sesgo de representación o evaluación. **Fix**: stratified metrics — reportar accuracy/AUC **por subgrupo** siempre, no solo global. |
| El modelo es "objetivo, solo aprendió del dato" | El dato no es neutro — refleja decisiones históricas (sesgo histórico). **Fix**: cuestionar el dataset antes que el modelo. |
| "Agregamos más datos del grupo minoritario y empeoró" | Probablemente sesgo de medición — el `y` para ese grupo es ruidoso (ej. arrestos en zonas más patrulladas). **Fix**: auditar el proceso de labeling. |
| Modelo único performa peor que k modelos por subgrupo | Sesgo de agregación. **Fix**: modelo por subgrupo **o** features de interacción `grupo × features`. |
| Modelo cae en producción pero pasó test | Sesgo de evaluación/despliegue. **Fix**: test set representativo de **deployment**, no del train; monitoreo continuo. |

## ❓ Preguntas frecuentes

**❓ ¿Por qué no simplemente sacar la variable sensible (sex, race)?**

Eso es **fairness through unawareness** y casi nunca funciona. Las features que sí usás (ZIP, nombre, historial crediticio, escuela) son **proxies** correlacionados. Quitar la variable sensible te impide **medir** el sesgo pero no lo elimina. Lo que sí se hace: usar la variable sensible para **auditar** disparidades, no como input del modelo.

**❓ ¿Sesgo histórico vs sesgo de representación — cuál es la diferencia?**

Histórico = el dato es preciso pero el mundo medido era injusto (mujeres ganan menos → modelo de salarios predice salarios más bajos para mujeres). Representación = el dato no representa bien a un subgrupo (pocas caras oscuras en ImageNet → mala accuracy ahí). El primero requiere reescribir el target o el objetivo; el segundo, recolectar/re-muestrear.

**❓ ¿Simpson's paradox es realmente común en ML?**

Sí, especialmente en datasets con subgrupos heterogéneos (Berkeley admissions 1973 es el clásico). Si tu accuracy global mejora pero la accuracy por subgrupo empeora, es Simpson. Por eso **siempre** se reporta métrica stratificada.

**❓ ¿Esto se resuelve con un algoritmo de fairness?**

No solo. Los algoritmos (re-weighting, adversarial debiasing, Clase 226) atacan principalmente representación y agregación. El sesgo histórico y de medición requieren **decisiones humanas**: ¿qué estamos prediciendo? ¿es el target correcto? Ningún optimizador resuelve "el target estaba mal definido".

**❓ ¿Cómo encaja todo esto con Clases 224 (métricas) y 225-227 (mitigación)?**

223 = **diagnóstico** (qué tipo de sesgo y dónde nace). 224 = **medición cuantitativa** (demographic parity, equalized odds, calibration). 225-227 = **mitigación** (pre-procesamiento, in-procesamiento, post-procesamiento). El orden importa: sin diagnóstico, la mitigación es a ciegas.

## 🔗 Referencias

- Suresh, H., Guttag, J. [*A Framework for Understanding Sources of Harm throughout the ML Life Cycle*](https://arxiv.org/abs/1901.10002) (EAAMO 2021) — el framework canónico de los 6 tipos.
- Buolamwini, J., Gebru, T. [*Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification*](http://proceedings.mlr.press/v81/buolamwini18a.html) (FAT* 2018) — el paper que disparó la auditoría algorítmica.
- Barocas, S., Hardt, M., Narayanan, A. [*Fairness and Machine Learning: Limitations and Opportunities*](https://fairmlbook.org/) (MIT Press, 2023) — caps. 1-2 (libre online).
- Mehrabi, N. et al. [*A Survey on Bias and Fairness in Machine Learning*](https://arxiv.org/abs/1908.09635) (ACM Computing Surveys, 2021).
- Angwin, J. et al. [*Machine Bias*](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing) (ProPublica, 2016) — la investigación sobre COMPAS.
- Dastin, J. [*Amazon scraps secret AI recruiting tool that showed bias against women*](https://www.reuters.com/article/idUSKCN1MK0AG/) (Reuters, 2018).

## 📥 Material descargable

- 📄 [Guía explicativa (PDF)](./clase-223-tipos-de-sesgo-algoritmico-y-origenes-guia-explicativa.pdf) — versión imprimible con todo el contenido de la clase.
- 🎞️ [Presentación (PPTX)](./clase-223-tipos-de-sesgo-algoritmico-y-origenes-presentacion.pptx) — deck PowerPoint listo para proyectar en clase.
- 🧮 [Notebook ejecutable (.ipynb)](./notebook.ipynb) — abrilo desde el laboratorio del programa o desde Jupyter.

## ➡️ Siguiente clase

[Clase 224 — Métricas de fairness: demographic parity, equalized odds, calibration](../224-metricas-de-fairness-demographic-parity-equalized-odds-calibration/README.md)
