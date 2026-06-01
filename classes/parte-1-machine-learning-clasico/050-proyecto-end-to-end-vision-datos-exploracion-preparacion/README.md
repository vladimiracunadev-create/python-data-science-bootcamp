# Clase 050 — Proyecto end-to-end: visión, datos, exploración, preparación

> Parte: **1 — Machine Learning Clásico** · Fuente: Géron, **cap. 2** (California Housing). ⏱️ Duración estimada: **90 min**.

---

## 🎯 Objetivo

Que el alumno recorra la primera mitad de un proyecto de ML real de punta a punta: framear el problema en términos de negocio, conseguir los datos, hacer un EDA honesto, separar train/test sin contaminarse, y dejar el pipeline de preparación (limpieza, encoding, scaling) listo para entrenar — todo sobre el dataset California Housing del capítulo 2 de Géron.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Framear el problema** en términos de negocio: tipo de tarea (regresión/clasificación), métrica, baseline.
2. **Hacer un EDA reproducible**: `describe`, `info`, `hist`, `corr`, scatter matrix, mapas geográficos.
3. **Separar train/test correctamente** con `train_test_split` estratificado por una variable clave (income bucket).
4. **Construir un pipeline** con `Pipeline` + `ColumnTransformer` que limpie, encode (`OneHotEncoder`) y escale (`StandardScaler`) en un solo objeto.
5. **Evitar data leakage**: todo cálculo (medias, encodings, scalers) se ajusta **solo en train** y se aplica en test.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | Framing del problema | Sin objetivo claro y métrica, cualquier modelo "anda". |
| 2 | EDA: describe, hist, corr, geo plot | Conocer los datos antes de modelar. |
| 3 | Stratified split por income bucket | Test representativo, no muestreo aleatorio ingenuo. |
| 4 | Limpieza: NaN, outliers, tipos | El 60% del trabajo real. |
| 5 | Encoding categórico (`OneHotEncoder`, `OrdinalEncoder`) | Los modelos no comen strings. |
| 6 | Scaling (`StandardScaler`, `MinMaxScaler`) | Imprescindible para modelos sensibles a escala. |
| 7 | Pipelines + `ColumnTransformer` | Reproducible, sin leakage, deployable. |

## 📌 Complemento: Feature engineering avanzado (target encoding, evitar data leakage)

En muchos problemas tabulares reales, un buen feature engineering supera al algoritmo: pasar de Random Forest a XGBoost te suele dar 1–2% de mejora, mientras que crear 3 features bien pensadas te puede dar 10%. Géron lo muestra con `rooms_per_household` y `bedrooms_per_room`, pero el catálogo va mucho más allá.

**Target encoding** — reemplaza una categoría por la media del target dentro de esa categoría. Conviene en variables de **alta cardinalidad** (códigos postales, IDs de producto, ciudades) donde `OneHotEncoder` explotaría en columnas. Problema: si se calcula sobre todo el dataset (incluido el target del test, o incluso del propio train sin cuidado), **filtra información del target** en el feature → AUC inflado en validación, modelo que se cae en producción.

**Solución con K-Fold out-of-fold**: para cada fila del train, su encoding se calcula con la media del target **excluyendo el fold al que pertenece esa fila**. En sklearn 1.3+ existe `TargetEncoder` con `cv` integrado; en `category_encoders` ya estaba hace años:

```python
from category_encoders import TargetEncoder

te = TargetEncoder(cols=['zipcode'], smoothing=10)
# fit SOLO en train
te.fit(X_train, y_train)
X_train_enc = te.transform(X_train)
X_test_enc = te.transform(X_test)  # usa medias aprendidas en train

# Alternativa sklearn 1.3+ con CV out-of-fold integrado:
from sklearn.preprocessing import TargetEncoder as SkTargetEncoder
te = SkTargetEncoder(cv=5, smooth='auto')
X_train_enc = te.fit_transform(X_train[['zipcode']], y_train)
```

**Cyclic encoding** para variables periódicas (mes, hora, día de la semana): codificar `mes=12` como 12 le dice al modelo que diciembre está lejísimos de enero, cuando en realidad están pegados. Solución: `mes_sin = sin(2π·mes/12)`, `mes_cos = cos(2π·mes/12)` — dos features que respetan la ciclicidad.

**Interaction features**: `PolynomialFeatures(degree=2, interaction_only=True)` genera productos cruzados (`a*b`, `a*c`...), o manual cuando sabés qué cruce tiene sentido de dominio (`precio_m2 = precio / metros`).

**Los 3 leakages más comunes**: (1) **target leakage** — usar una feature que en producción no existiría al momento de predecir (ej: `pago_recibido` para predecir `morosidad`); (2) **train/test contamination** — fittear scaler/encoder/imputer sobre `train+test` concatenados (clásico); (3) **temporal leakage** — usar `train_test_split` random en datos temporales en vez de cortar por fecha. Regla: **todo `.fit()` ve solo train**.

## 📌 Complemento: Imputación avanzada (KNN, MICE, MCAR/MAR/MNAR)

`df.fillna(df.mean())` es el default de tutorial y casi siempre es mala idea: aplasta varianza, distorsiona correlaciones, y trata todas las filas faltantes como si fueran promedio. Hay opciones mejores con pocas líneas más.

**Categorización clásica de faltantes** (Rubin, 1976):

- **MCAR** (Missing Completely At Random): la falta no depende ni de la propia variable ni de otras. Ej: un sensor falla aleatoriamente. Eliminar filas no sesga, pero pierde data.
- **MAR** (Missing At Random): la falta depende de **otras** variables observadas. Ej: los hombres reportan menos su peso. Imputar con modelos que usen las otras variables funciona.
- **MNAR** (Missing Not At Random): la falta depende del **valor faltante mismo**. Ej: la gente con sueldos altos no reporta sueldo. Caso más feo — ninguna imputación es inocua, hay que modelar la falta explícitamente.

**`sklearn.impute.KNNImputer`** — imputa el faltante con el promedio (ponderado por distancia) de los **K vecinos más parecidos** en las demás columnas. Respeta MAR. Costoso en N grande.

**`sklearn.impute.IterativeImputer`** — implementa MICE: trata cada columna con NaN como un problema de regresión donde las demás columnas son features, e itera hasta converger. Es el estado del arte clásico para MAR.

```python
from sklearn.experimental import enable_iterative_imputer  # noqa: F401
from sklearn.impute import IterativeImputer

imp = IterativeImputer(max_iter=10, random_state=42)
X_train_imp = imp.fit_transform(X_train)
X_test_imp = imp.transform(X_test)  # nunca refittear en test
```

**Indicator features (`MissingIndicator`)**: a veces el hecho de que falte un valor **es la señal** (ej: cliente que no completó campo opcional puede ser distinto del que sí). Agregá una columna binaria `col_was_missing` además de imputar — el modelo decide si la usa. `SimpleImputer(add_indicator=True)` lo hace automático.

## 📖 Definiciones y características

**`Pipeline` (sklearn)**
: Secuencia de transformaciones `(nombre, estimator)` que termina opcionalmente en un modelo. `fit` ajusta cada paso con la salida del anterior; `transform`/`predict` aplica en orden. Encadena todo en un objeto y previene leakage cuando se usa con CV.

**`ColumnTransformer`**
: Aplica transformadores distintos a subconjuntos de columnas (numéricas → scaler, categóricas → encoder) y concatena el resultado. Es el pegamento entre EDA y modelo.

**Stratified split**
: Separación train/test que preserva la distribución de una variable clave (target en clasificación, o un bucket de una numérica como `income_cat`). Evita que el test caiga sesgado por azar — crítico en N chico.

**`OneHotEncoder`**
: Convierte cada valor único de una categórica en una columna binaria. Default sklearn: sparse matrix. Parámetros clave: `handle_unknown='ignore'` (para categorías nuevas en test), `drop='first'` (para evitar multicolinealidad en modelos lineales).

**`StandardScaler`**
: Resta media y divide por desvío estándar (z-score). Necesario para modelos sensibles a escala: SVM, KNN, redes neuronales, regresión regularizada (Ridge/Lasso). Árboles no lo necesitan.

**Target leakage**
: Cualquier feature, encoding o estadístico que contenga información del target o del test al momento de entrenar. Inflará métricas en validación y colapsará en producción. Síntoma típico: AUC > 0.99 sospechoso.

**`SimpleImputer`**
: Imputación univariada (media/mediana/moda/constante). Default razonable para empezar; reemplazable por `KNNImputer` o `IterativeImputer` sin cambiar el resto del pipeline.

**Métrica vs función de costo**
: La **métrica** la elige el negocio (RMSE en dólares, recall en fraude); la **función de costo** la usa el optimizador internamente (puede ser distinta — MSE para entrenar, RMSE para reportar).

## 📂 Dataset / recursos

**California Housing** (Géron cap. 2). 20 640 filas, 10 columnas, target = `median_house_value`. Disponible vía `sklearn.datasets.fetch_california_housing()` o el CSV del repo de Géron. Contiene una categórica (`ocean_proximity`) y una columna con NaN (`total_bedrooms`) — perfecta para practicar pipeline completo.

## 🧪 Ejercicios

**1.** **EDA mínimo.** Cargá el dataset y producí: `df.info()`, `df.describe()`, `df.hist(bins=50, figsize=(12,8))`. Identificá al menos 2 anomalías (cap visual de `median_house_value`, distribución skewed de `population`).

**2.** **Stratified split por income bucket.** Creá `income_cat = pd.cut(df['median_income'], bins=[0, 1.5, 3, 4.5, 6, np.inf])` y usá `StratifiedShuffleSplit` para train/test 80/20. Verificá que la distribución de `income_cat` sea casi idéntica en train y test.

**3.** **Target encoding sin leakage.** Tomá una variable categórica (creá `zipcode_fake` a partir de buckets de lat/long si querés). Implementá target encoding con `category_encoders.TargetEncoder` ajustado **solo en train**. Compará RMSE de un `RandomForestRegressor` con (a) one-hot vs (b) target encoded.

**4.** **`KNNImputer` vs `SimpleImputer`.** Sobre `total_bedrooms` (que tiene NaN reales), comparen RMSE final del pipeline usando `SimpleImputer(strategy='median')` vs `KNNImputer(n_neighbors=5)`. Reportá cuál ganó y en cuánto.

**5.** **Pipeline completo.** Armá un `ColumnTransformer` con: numéricas → `SimpleImputer(median)` + `StandardScaler`; categóricas → `OneHotEncoder(handle_unknown='ignore')`. Envolvelo en un `Pipeline` con `LinearRegression` al final. `fit` en train, RMSE en test.

## 📝 Homework verificable

Notebook con: (a) carga del dataset + EDA con al menos 4 gráficos; (b) stratified split por income bucket con verificación de proporciones; (c) pipeline `ColumnTransformer` (numéricas con `KNNImputer`+`StandardScaler`, categóricas con `OneHotEncoder`); (d) feature engineering manual con al menos 2 features derivadas (`rooms_per_household`, `bedrooms_per_room`); (e) baseline `LinearRegression` con RMSE reportado en train y test.

**Criterio de aceptación:** El pipeline se entrena con `pipeline.fit(X_train, y_train)` sin tocar `X_test` antes del scoring final. RMSE de test reportado. Sin warnings de sklearn por leakage o categorías nuevas.

## ⚠️ Errores comunes

| Síntoma / mensaje | Causa y cómo arreglar |
|---|---|
| Target encoding da AUC casi perfecto en train pero malísimo en test | Encoding calculado sobre todo el dataset → **target leakage**. **Fix**: target encoding **después** del split, con CV out-of-fold (`TargetEncoder(cv=5)` o K-Fold manual). |
| `ValueError: Found unknown categories ['X'] in column` al predecir | El test trae una categoría nueva no vista en train. **Fix**: `OneHotEncoder(handle_unknown='ignore')` o `'infrequent_if_exist'`. |
| RMSE de test ridículamente bajo, idéntico al de train | Imputaste/escalaste sobre `pd.concat([train, test])` antes de splitear. **Fix**: `train_test_split` **primero**, todo `.fit()` solo en train. |
| `fillna(df.mean())` baja drásticamente la varianza de una columna | Imputación univariada con media aplasta la distribución. **Fix**: `KNNImputer` o `IterativeImputer`, o como mínimo `strategy='median'` + `MissingIndicator`. |
| Modelo lineal con coeficientes raros (uno enorme, otros minúsculos) | Olvidaste el `StandardScaler` — features están en escalas distintas (`median_income` vs `population`). **Fix**: incluir `StandardScaler` en el pipeline para numéricas. |

## ❓ Preguntas frecuentes

**❓ ¿Cuándo target encoding > one-hot?**

Cuando la cardinalidad es alta (>~15 valores únicos) y existe relación monotónica entre categoría y target. One-hot con 1000 zipcodes te da 1000 columnas sparse y árboles que no convergen; target encoding te da 1 sola columna numérica informativa. Siempre con CV out-of-fold para no filtrar el target.

**❓ ¿Necesito escalar si uso Random Forest o XGBoost?**

**No.** Los árboles particionan por umbrales, son invariantes a transformaciones monotónicas. Sí lo necesitás para SVM, KNN, redes, regresión lineal/logística con regularización.

**❓ ¿Stratified split en regresión?**

Sí — pero estratificás por una **versión bucketizada** del target o de una feature clave (como `income_cat` en California Housing). `StratifiedShuffleSplit` no acepta target continuo directamente.

**❓ ¿`StandardScaler` o `MinMaxScaler`?**

`StandardScaler` por default (z-score, asume distribución aprox. normal). `MinMaxScaler` cuando necesitás bounds fijos `[0,1]` (redes con sigmoide, ciertos algoritmos de visión). `RobustScaler` si hay outliers fuertes.

**❓ ¿Hago feature engineering antes o después del split?**

Features que dependen **solo de la fila** (ratios, log, sin/cos): antes o después, da igual. Features que dependen de **estadísticos agregados** (target encoding, frequency encoding, z-scores globales): **siempre después del split y fit solo en train**.

## 🔗 Referencias

- Géron, **cap. 2** — *End-to-End Machine Learning Project* (California Housing).
- [sklearn — `Pipeline` y `ColumnTransformer`](https://scikit-learn.org/stable/modules/compose.html)
- [sklearn — `impute` (`SimpleImputer`, `KNNImputer`, `IterativeImputer`)](https://scikit-learn.org/stable/modules/impute.html)
- [sklearn — `TargetEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html)
- [`category_encoders` docs](https://contrib.scikit-learn.org/category_encoders/)
- Rubin, D. B. (1976). *Inference and missing data*. Biometrika.

## ➡️ Siguiente clase

[Clase 051 — Selección y entrenamiento de modelo](../051-seleccion-y-entrenamiento-de-modelo/README.md)
