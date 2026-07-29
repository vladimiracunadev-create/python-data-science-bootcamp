# Auditoría pedagógica — 232 clases (lente: autoestudio desde cero)

> Fecha: 2026-07-27 · v3.9.0 · Metodología: 11 lotes de revisión, cada clase (README + notebook) puntuada 1-5 en 5 ejes.
> **Lente**: alumno principiante SIN instructor. Un mismo material puntúa distinto para clase guiada vs autoestudio; aquí todo se juzga para el segundo.

## Ejes evaluados (1-5)

| Eje | Qué mide |
|---|---|
| **A · Andamiaje/intuición** | ¿Construye la idea con intuición/analogía ANTES de la definición formal, o salta a lo denso? |
| **B · Demostración ejecutable** | ¿El notebook DEMUESTRA el flujo end-to-end con código que corre y explica, o solo describe/lista comandos? |
| **C · Claridad de definiciones** | ¿Autocontenidas y explicadas, o terminología terse? |
| **D · Adecuación de dificultad** | ¿El nivel calza con la posición de la clase en el curso? |
| **E · Solución de ejercicios** | ¿Hay solución trabajada, o solo enunciado ("hazlo tú"/"Ver README")? |

---

## Veredicto en una frase

**El curso es fuerte en cobertura, estructura, definiciones y andamiaje (A/C ≈ 4.5-4.6), pero tiene UN gap sistémico severo para autoestudio: los ejercicios no traen solución (E ≈ 2.4), y un gap secundario 100% transversal: los notebooks se entregan sin outputs guardados.** No le "falta contenido"; le falta *cierre didáctico para quien estudia solo*.

## Puntajes globales (n=232)

| A | B | C | D | **E** |
|:-:|:-:|:-:|:-:|:-:|
| ~4.5 | ~4.2 | ~4.6 | ~4.0 | **~2.4** |

**E es el outlier claro y uniforme en las 232 clases.**

## Scorecard por parte

| Parte | Clases | A | B | C | D | E | Lectura |
|---|:-:|:-:|:-:|:-:|:-:|:-:|---|
| 0 · Prerrequisitos (a) 001-025 | 25 | 4.2 | 3.6 | 4.0 | 4.2 | 2.0 | La más floja en B: clases de setup/tooling (venv, ccds, vscode, mypy) no se pueden demostrar en notebook |
| 0 · Prerrequisitos (b) 026-049 | 24 | 3.7 | 4.5 | 4.4 | 4.1 | 2.3 | Code sólido; algunas "solo descritas" (DuckDB, folium, CTEs) |
| 1 · ML clásico (a) 050-074 | 25 | 4.5 | 4.0 | 4.6 | 4.7 | 2.0 | Muy uniforme; 5 clases densas rompen el andamiaje |
| 1 · ML clásico (b) 075-099 | 25 | 4.2 | 4.3 | 4.6 | 4.3 | 2.6 | Reducción dim/clustering sin outputs; SHAP/t-SNE/zoo densos |
| 2 · Deep Learning (a) 100-124 | 25 | 4.8 | 4.5 | 4.8 | 4.0 | 1.9 | Altísima calidad; 117/121 desalineados README↔notebook |
| 2 · Deep Learning (b) 125-149 | 25 | 4.2 | 4.4 | 4.6 | 3.9 | 2.7 | Base CNN/RNN/atención sólida; frontera (141/146) con demos falsas |
| 2 · Deep Learning (c) 150-174 | 25 | 4.8 | 3.7 | 4.9 | 3.8 | 2.8 | NLP/LLM/RL from-scratch excelente; **cola de despliegue/cloud colapsa** |
| 3 · Estadística inferencial 175-193 | 19 | 4.4 | 3.9 | 4.2 | 3.5 | 1.8 | Base fuerte; **dificultad se dispara desde 186** (temas graduate) |
| 4 · MLOps 194-207 | 14 | 4.6 | 4.4 | 4.9 | 3.9 | 3.0 | **Muy fuerte**: simulan de verdad (DVC/MLflow/uvicorn/drift); infra externa (K8s) baja |
| 5 · Ing. de datos 208-215 | 8 | 5.0 | 4.7 | 5.0 | 4.1 | 3.1 | **Excelente**: simulan local (DuckDB/Spark-local/particiones in-memory) |
| 6 · Recomendadores 216-222 | 7 | 5.0 | 4.7 | 5.0 | 4.1 | 3.1 | **Excelente**: todo ejecutable con datos sintéticos |
| 7 · Ética/Fairness 223-228 | 6 | 5.0 | 5.0 | 5.0 | 4.0 | 3.0 | **Excepcional** y autocontenido |
| 8 · Capstones 229-232 | 4 | 5.0 | 4.6 | 5.0 | 4.0 | 4.0 | Skeletons ejecutables; 230/231 con ramas stubbeadas |

**Patrón macro: la calidad SUBE a lo largo del curso.** Lo "avanzado/incompleto" que percibes se concentra donde un principiante *empieza* (Parte 0 tooling) y en clusters específicos, no en el conjunto.

---

## Los 2 gaps sistémicos

### 1. E — Sin soluciones de ejercicios (el #1 para autoestudio)
En **las 232 clases**, la sección "Ejercicios" y el "Homework verificable" se plantean como enunciado + criterio de aceptación, pero **nunca con solución trabajada**. Para un alumno con instructor, esto está bien (el docente valida). Para autoestudio, es el mayor obstáculo: no hay contra qué contrastar. Ironía: las clases de Parte 1+ suelen *de facto* resolver el ejercicio en sus celdas-demo, pero no está etiquetado como solución ni separado.

### 2. B — Notebooks sin outputs guardados (100% transversal)
Ningún notebook trae celdas ejecutadas: 0 tablas, 0 gráficos, 0 resultados visibles. Quien **lee** el cuaderno / PDF / app (sin ejecutar) ve código + prosa pero ningún resultado. Es una convención del repo (los 120 notebooks "completos" tampoco los guardan). Es el arreglo de **mayor palanca / menor esfuerzo** para los notebooks ejecutables (Parte 0/1/3/4/5/6), aunque no aplica a los de DL que necesitan GPU.

---

## Clusters de prioridad Alta (19 clases)

### a) Despliegue/cloud que no se puede simular (B ≈ 1-2) — el fondo del curso
`166 tf-serving-grpc` · `168 vertex-ai-deploy` · `174 vertex-ai-escala` · `169 tf-lite-mobile` · `170 tensorflow-js` · `200 kubernetes`
→ Solo listan comandos/API detrás de guardas; nada corre. **Fix**: simulación local real (cargar el SavedModel en proceso + stub REST; mini-cluster con `kind`/kompose conceptual) — el patrón que Docker(198)/Airflow(208) SÍ usan bien.

### b) Demos falsas / mock vendidas como reales (engañan al principiante)
`117 stochastic-depth` (mock numpy/sklearn vendido como torch/timm/CIFAR) · `141 encoder-decoder` (inferencia random, modelo nunca entrenado) · `146 clip-siglip` (embeddings simulados, nunca carga imágenes) · `158 gans-dcgan` (nada numérico corre) · `192 bayes-intro` (2/3 celdas no ejecutan, sin fallback)
→ **Fix**: sustituir el placeholder por una demo pequeña que sí corra en CPU (como hace 159/160/163/164).

### c) Setup/tooling temprano (lo PRIMERO que ve un principiante, B bajo)
`001 instalacion-venv` · `004 estructura-proyecto-ccds` · `005 vscode-cursor`
→ **Fix**: walkthrough ejecutable autocontenido (crear venv en tempdir + `pip list`; generar el árbol cookiecutter y mostrarlo; para IDE, capturas embebidas ya que no se puede ejecutar).

### d) Demasiado avanzado para su posición (D bajo desde cero)
`087 shap` · `094 tsne-umap` · `097 clustering-zoo` (Parte 1) · `186 cuped` · `189 doubleml-econml` · `193 stack-bayesiano` (Parte 3, temas graduate en 80-95 min)
→ **Fix**: añadir intuición/analogía previa + un ejemplo mínimo antes del salto formal; o marcar explícitamente como "avanzado/opcional".

> Nota: `100 perceptron` y `103 functional-api` salen Alta *solo* por E=1 (son de altísima calidad); su prioridad es "merecen solución de ejercicio", no "contenido flojo".

---

## Gaps secundarios de higiene (rápidos de arreglar)

- **Cross-references internos rotos/desfasados**: `057`→052a · `067`→"clase 060" · `069`→"clase 063" (es 073) · `153` enlaces rotos · `166`→139a · `192`→158b · `215`→carpeta 216 equivocada.
- **README↔notebook desalineados** (el README promete X, el notebook hace Y): `056`/`062` (dice California/MNIST, usa diabetes/digits) · `117` · `121` (promete PyTorch, solo TF) · `230` (rama NLP sin notebook) · `231` (visión reducida a stub).
- **Typos**: `064` "ADASIN" · `060` model-cards · `031` FAQ garbled.

---

## Plan de remediación priorizado (valor / esfuerzo)

| # | Acción | Alcance | Esfuerzo | Palanca |
|---|---|---|---|---|
| **1** | **Ejecutar y guardar outputs** de los notebooks ejecutables (P0/P1/P3/P4/P5/P6) vía paso CI `nbconvert --execute` | ~150 clases | Bajo (mecánico) | **Máxima** — hoy no se ve ningún resultado |
| **2** | **Solucionario por clase**: sección "✅ Soluciones" al final del notebook (o notebook aparte) resolviendo los ejercicios con `assert` | 232 clases | Medio-alto | **Alta** — desbloquea el autoestudio |
| **3** | **Arreglar el cluster despliegue/cloud + mock** (a y b arriba): simulación local real que corra | ~11 clases | Medio | Alta (elimina lo que "se siente incompleto") |
| **4** | **Intuición previa + tags de nivel** en clases densas (cluster d) + higiene de cross-refs/typos | ~15 clases + barrido | Bajo-medio | Media |

**Recomendación de arranque**: #1 (outputs) porque es casi gratis y sistémico, seguido de un piloto de #2+#3 en 003-git (que citaste) + una clase de despliegue (166) para fijar el formato objetivo antes de escalar.

---

## Apéndice — Tabla completa (232 clases)

Formato: `NNN | slug | tipo | A B C D E | prioridad | gap`

### Parte 0 — Prerrequisitos
```
001 instalacion-python-venv        concepto 4 2 5 5 2 Alta  notebook solo diagnostica; no ejecuta flujo venv/uv/conda
002 jupyter-jupyterlab             concepto 4 3 4 5 2 Media magics/debug descritos; sin outputs
003 git-github                     concepto 4 3 4 4 2 Media branch/merge/PR en markdown, no ejecutados
004 estructura-proyecto-ccds       concepto 4 2 4 4 2 Alta  estructura nunca se genera de verdad
005 vscode-cursor                  concepto 4 2 4 4 2 Alta  IDE no demostrable; solo describe la GUI
006 python-tipos-control           code     5 4 4 5 2 Media sin outputs; ejercicios sin solucion (1 de 5)
007 comprehensions-generadores     code     4 4 4 4 2 Media buen demo memoria; ejercicios sin resolver
008 funciones-args-closures        code     4 4 4 4 2 Media demos runnable; ejercicios solo enunciado
009 excepciones-context-managers   code     4 4 4 4 2 Media context managers bien; sin solucion ejercicios
010 oop-dataclasses-herencia       code     4 4 4 4 2 Media composicion vs herencia clara; falta resolver
011 pathlib-archivos               code     4 4 4 5 2 Media IO real con tempdir; sin outputs ni soluciones
012 logging                        code     4 4 4 4 2 Media logging ejecutable; ejercicios sin solucion
013 type-hints-mypy                concepto 4 3 4 4 2 Media mypy no se corre; solo se describe
014 numpy-tipos-creacion           code     5 4 4 5 2 Media intuicion fuerte; sin outputs; sin soluciones
015 numpy-ufuncs-vectorizacion     code     4 4 4 4 2 Media speedup medido; ejercicios sin resolver
016 numpy-agregaciones             code     4 4 4 4 2 Media bug axis bien; falta solucion ejercicios
017 numpy-broadcasting             code     5 4 4 4 2 Media reglas claras; ejercicio sin solucion
018 numpy-masks-fancy-indexing     code     4 4 4 4 2 Media vista vs copia clara; solo enunciado
019 numpy-ordenamiento-busqueda    code     4 4 4 3 2 Media partition/searchsorted algo denso
020 numpy-algebra-lineal           code     4 4 4 3 2 Media SVD/eigen avanzado para prerrequisitos
021 numpy-aleatoriedad-semillas    code     4 4 4 4 2 Media bootstrap/montecarlo buenos; sin resolver
022 pandas-series-dataframe        code     5 4 4 5 2 Media carga por URL (red); sin soluciones
023 pandas-indexacion-loc-iloc     code     4 4 4 4 2 Media loc/iloc claros; solo enunciado
024 pandas-operaciones-alineacion  code     4 4 4 4 2 Media benchmark apply vs vectorizado; sin solucion
025 pandas-datos-faltantes         code     4 4 4 4 2 Media eliminar/imputar/flag clara; sin resolver
026 multiindex                     code     3 5 4 4 2 Media homework "Ver README"; sin solucion
027 concat-merge-join              code     4 5 5 4 2 Media ejercicios solo enunciado README
028 groupby                        code     4 5 5 4 2 Media homework remite a README
029 pivot-crosstab                 code     3 5 4 4 2 Media intuicion breve; sin resolver
030 str-vectorizado                code     4 5 5 4 2 Media buen regex; homework sin solucion
031 series-tiempo                  code     3 5 4 4 2 Media "Ver README"; typo en FAQ rolling
032 eval-query                     code     4 4 5 5 2 Media benchmark prometido no hecho; sin solucion
033 polars                         code     3 5 4 3 2 Media salta a API densa sin intuicion
034 parquet-duckdb                 code     4 5 4 4 2 Media ejercicios solo enunciados
035 mpl-anatomia                   code     5 4 5 5 2 Baja  homework remite a README
036 mpl-plots-basicos              code     4 5 5 5 2 Baja  penguins sintetico; sin solucion
037 mpl-subplots-gridspec          code     4 4 4 4 2 Media tight/constrained no codificado
038 mpl-legends-anotaciones        code     3 5 4 4 2 Media homework remite a README
039 mpl-stylesheets                code     3 3 4 4 2 Media style y uso global solo descritos
040 mpl-3d                         code     3 5 4 4 2 Baja  notebook fuerte pero sin soluciones
041 seaborn-dist-facetas           code     3 5 4 4 2 Baja  ejercicios sin solucion
042 geo-plotly-folium              code     3 3 4 4 2 Media folium choropleth solo descrito
043 sql-select-join-groupby        code     4 5 4 4 3 Baja  DuckDB solo descrito no ejecutado
044 sql-avanzado-ctes-window       code     4 3 4 4 2 Media recursive CTE nunca demostrado
045 sql-desde-python               code     4 4 5 4 3 Baja  injection y CSV solo en markdown
046 nosql-mongodb-pymongo          code     4 5 5 4 3 Baja  ejercicios sin solucion trabajada
047 apis-rest-requests             code     4 3 4 4 3 Media depende de red; no simula API local
048 web-scraping-bs4               code     4 4 5 4 3 Baja  scraping real solo descrito
049 async-httpx-aiohttp            code     4 5 4 4 3 Baja  ejercicios finales solo enunciados
```

### Parte 1 — Machine Learning clásico
```
050 panorama-ml                    code     5 4 5 5 2 Baja  sin outputs; sin solucion trabajada
051 desafios-ml-overfitting        concepto 5 4 5 5 2 Baja  sin outputs; ejercicios sin solucion
052 testing-validacion-tuning-nfl  code     5 4 5 5 2 Baja  sin outputs; sin solucion
053 validacion-temporal            code     3 4 3 3 2 Media README terso salta a denso (purged CV)
054 proyecto-e2e                   code     5 4 5 5 2 Baja  sin outputs; sin solucion
055 feature-eng-target-mice        code     3 4 3 4 2 Media README terso; smoothing sin analogia
056 seleccion-entrenamiento        code     5 4 5 5 2 Baja  usa diabetes no California como dice README
057 grid-randomized-search         code     5 4 5 5 2 Baja  enlace roto 052a; sin outputs
058 optuna-hpo                     code     3 4 3 4 2 Media defs one-liner asumen KDE/fANOVA
059 launch-monitoreo               concepto 5 4 5 5 2 Baja  demuestra PSI/KS/shadow pero sin outputs
060 model-cards                    concepto 4 4 4 5 2 Baja  defs terse; typos; sin outputs
061 crisp-dm                       concepto 5 4 5 5 2 Baja  sin outputs; sin solucion
062 clasificacion-binaria          code     5 4 5 5 2 Baja  usa digits no MNIST; sin solucion
063 metricas-precision-recall-f1   code     5 4 5 5 2 Baja  sin outputs; sin solucion
064 class-imbalance-smote          code     3 4 3 5 2 Media typos ADASIN; defs terse
065 precision-recall-tradeoff      code     5 4 5 5 2 Baja  sin outputs; sin solucion
066 curva-roc-auc                  code     5 4 5 5 2 Media sin outputs; sin solucion
067 multiclase-multilabel          code     5 4 5 5 2 Media cross-ref stale (dice clase 060)
068 analisis-de-errores            code     5 4 5 5 2 Media sin outputs; sin solucion
069 regresion-lineal               code     5 4 5 5 2 Media cross-ref a 063 que es 073
070 gradient-descent               code     4 4 4 4 2 Media mate del gradiente densa sin analogia
071 regresion-polinomial           code     4 4 5 5 2 Baja  sin outputs; sin solucion
072 curvas-aprendizaje             concepto 4 4 5 5 2 Baja  diagnostico claro; sin solucion
073 regularizacion-ridge-lasso     code     5 4 5 5 2 Baja  intuicion L1/L2 fuerte; sin outputs
074 early-stopping                 code     5 4 5 5 2 Baja  muy claro; sin solucion
075 regresion-logistica-softmax    code     4 5 4 4 3 Media sobrecargada; ejercicios sin solucion
076 calibracion-platt-isotonic     concepto 3 5 3 4 2 Media defs telegraficas (MLE/logit)
077 svm-lineal                     code     4 5 5 5 3 Baja  ejercicios sin solucion trabajada
078 svm-no-lineal-kernel           code     4 5 5 5 3 Baja  ejercicios finales sin solucion
079 svm-para-regresion             code     4 5 5 5 3 Baja  ejercicios sin solucion
080 arboles-decision-cart          code     5 5 5 5 3 Baja  solo faltan soluciones de ejercicios
081 regularizacion-de-arboles      code     4 5 5 5 3 Baja  homework sin resolver
082 regresion-con-arboles          code     4 5 5 5 3 Baja  ejercicios sin solucion
083 voting-classifiers             code     5 5 5 5 2 Baja  ejercicios sin solucion
084 bagging-pasting                code     5 5 5 5 2 Baja  ejercicios sin solucion
085 random-forests                 code     4 5 5 5 2 Baja  falta intuicion visual decorrelacion
086 feature-importance             code     4 5 4 4 2 Media no demuestra SHAP (remite a 087)
087 shap-en-profundidad            code     4 4 3 3 2 Alta  teoria Shapley densa; sin solucion
088 boosting-adaboost-gb           code     5 5 5 4 2 Baja  GB manual excelente; sin soluciones
089 xgboost-lightgbm-catboost      code     4 4 4 4 2 Media CatBoost solo descrito, no ejecutado
090 stacking                       code     4 5 5 4 2 Baja  OOF/passthrough bien; sin solucion
091 maldicion-dimensionalidad      concepto 5 3 5 4 3 Media sin outputs; sin solucion
092 pca-variantes                  code     4 3 5 4 3 Media sin outputs; usa digits
093 lle                            code     4 3 4 4 3 Media sin outputs; tema nicho
094 mds-isomap-tsne-umap-lda       code     4 3 4 3 3 Alta  cinco metodos densos; UMAP no demostrado
095 kmeans-seleccion-k             code     5 3 5 4 3 Media sin outputs; refs cruzadas desfasadas
096 dbscan                         code     4 3 5 4 3 Media sin outputs; HDBSCAN no demostrado
097 clustering-zoo                 code     4 3 4 3 3 Alta  cinco algoritmos densos; sin outputs
098 gaussian-mixture-models        code     4 3 4 4 3 Media sin outputs; EM/Bayesian avanzado
099 deteccion-anomalias            code     4 3 5 4 3 Media sin outputs; sin solucion
```

### Parte 2 — Deep Learning
```
100 perceptron-mlp-backprop        code     5 5 5 4 1 Alta  excelente; ejercicios sin solucion (E=1)
101 regresion-clasif-mlp           code     5 5 5 4 1 Media mapeo salida-loss ejemplar; sin solucion
102 keras-sequential-api           code     5 5 5 5 1 Baja  refs cruzadas erroneas
103 functional-api-subclassing     code     5 5 5 4 1 Alta  Wide&Deep/ResBlock reales; sin solucion
104 callbacks-tensorboard-save     code     5 5 5 4 1 Media callbacks ejecutables; sin solucion
105 keras-tuner                    code     5 5 5 4 2 Baja  end-to-end real; sin solucion
106 ray-tune-hpo                   code     4 3 4 3 2 Media juguete+fallback Optuna, no Ray real
107 vanishing-exploding            concepto 5 5 5 4 2 Baja  diagnostico ejecutable solido
108 init-glorot-he                 code     5 5 5 4 2 Baja  varianza/histogramas idiomatico
109 activaciones                   code     5 5 5 4 2 Baja  walkthrough real + dying ReLU
110 batch-layer-norm               code     5 5 5 4 2 Baja  demo idiomatico completo
111 gradient-clipping              code     5 5 5 4 2 Baja  clipnorm/clipvalue/custom-loop
112 transfer-learning              code     5 4 5 4 2 Media fit() comentado (sin GPU)
113 optimizadores-clasicos         code     5 4 5 4 2 Media comparacion sin entrenamiento real
114 optimizadores-lion-sophia      code     5 5 5 4 2 Baja  numpy no cubre Schedule-Free del README
115 learning-rate-scheduling       code     5 4 5 4 1 Media schedules evaluados, nunca entrena
116 regularizacion-dropout-mc      code     5 4 5 4 1 Media MC-dropout real; ejercicios sin solucion
117 stochastic-depth-droppath      concepto 4 2 4 3 1 Alta  mock numpy vendido como torch/timm
118 tensorflow-tensores-variables  code     5 5 5 5 3 Baja  walkthrough completo; homework resuelto
119 losses-metricas-capas-custom   code     5 5 5 4 4 Baja  componentes custom ejecutados
120 autograph                      code     5 5 5 4 3 Baja  walkthrough real ejecutable
121 custom-training-loops          code     4 3 4 4 2 Media omite PyTorch/Lightning; link 108a roto
122 pytorch-fundamentos            code     4 4 5 4 2 Media falta nn.Module custom y DataLoader
123 lightning-trainer              code     4 5 4 4 2 Baja  Lightning end-to-end; DDP/W&B sin solucion
124 tf-data-api                    code     5 5 5 4 3 Baja  walkthrough idiomatico; sin solucion
125 tfrecord                       code     3 5 4 3 3 Media protobuf denso; poca intuicion previa
126 keras-preprocessing-layers     code     3 5 4 4 3 Media ejercicios IMDB/Hashing no resueltos
127 tfds                           code     3 4 4 4 3 Baja  no ejecutable (descargas)
128 capas-convolucionales          code     5 5 5 4 4 Baja  ejercicio filtros sin visualizacion
129 pooling                        code     4 5 5 4 4 Baja  homework comparativo sin ejecutar
130 arquitecturas-cnn              code     4 5 5 4 4 Baja  ejercicios replican codigo mostrado
131 transfer-learning-cnn          code     4 4 5 4 4 Baja  fit()/carga comentados
132 localizacion-deteccion         code     4 5 5 4 4 Baja  YOLO/DETR/SAM solo conceptuales
133 segment-anything-sam           concepto 4 4 4 4 2 Media sin celda ejercicios; fallback superpixel
134 yolov11-practica               code     4 5 4 4 3 Media sin ejercicios; fallback HOG+SVM
135 rnns-bptt                      code     5 5 5 4 2 Media predict sin entrenar; sin solucion
136 forecasting-rnn                code     4 5 5 4 2 Media homework sin soluciones
137 lstm-gru                       code     4 5 5 4 2 Baja  modelos solo con summary
138 1d-cnn-wavenet                 code     4 5 5 4 2 Baja  comparacion speed/MAE no ejecutada
139 char-rnn-texto                 code     5 5 5 4 2 Baja  pipeline completo; sin soluciones
140 analisis-sentimiento           code     4 4 4 4 1 Media corpus juguete 6 frases; sin solucion
141 encoder-decoder                code     4 3 4 3 1 Alta  inference random fake, nunca entrenado
142 mecanismos-atencion            code     5 5 5 4 3 Baja  autocontenido excelente
143 transformers-bert-gpt          code     4 4 5 4 2 Media mini-GPT sin apilar ni entrenar
144 flash-rope-gqa                 code     5 5 4 4 3 Baja  numpy verificable; ej.5 requiere H100
145 hugging-face-transformers      code     4 5 4 4 2 Baja  HF idiomatico real; sin solucion
146 clip-siglip-multimodal         code     3 2 4 3 2 Alta  embeddings simulados, nunca imagenes reales
147 whisper-asr                    code     4 3 4 4 2 Media mel-spec real; transcripcion conceptual
148 llms-fine-tuning-prompting     code     4 4 4 4 2 Media solapa con 149; sin solucion
149 lora-qlora-eficiente           code     5 5 5 4 2 Baja  LoRA from scratch excelente
150 dpo-rlhf                       code     5 5 5 3 3 Baja  DPO numpy real; tema denso
151 vllm-tgi-serving               code     5 5 5 4 3 Baja  simula batching/paging bien
152 rag-embeddings                 code     5 5 5 4 3 Baja  retrieval numpy con fallback
153 mcp                            code     5 5 5 4 3 Baja  server/cliente in-process; enlaces rotos
154 agentes-react                  code     5 5 5 4 3 Baja  ReAct+multiagente mock real
155 llm-evaluation                 code     5 5 5 4 3 Baja  MMLU/judge/ELO simulados
156 autoencoders                   code     5 3 5 4 3 Media fit() comentado; fallback no demuestra
157 vae                            code     5 3 5 3 3 Media reparam numpy ok; train no corre sin TF
158 gans-dcgan                     code     5 2 5 3 2 Media todo gated HAS_TF; nada corre
159 difusion-ddpm                  code     5 4 5 3 3 Baja  forward numpy real; denoiser placeholder
160 stable-diffusion-xl            code     5 5 4 4 3 Baja  DDPM toy real (sklearn); mejor demo
161 rl-gymnasium                   code     5 4 5 4 3 Baja  return numpy corre; gym si instalado
162 policy-gradients               code     5 4 5 3 3 Baja  returns/advantage numpy; red no corre
163 mdp                            code     5 5 5 4 4 Baja  VI+PI+MonteCarlo totalmente ejecutable
164 q-learning-dqn                 code     5 5 5 4 4 Baja  Q-learning converge; DQN conceptual
165 rl-moderno-ppo-sac             concepto 4 4 5 4 3 Media GAE/PPO numpy; SB3 guardado
166 tf-serving-grpc                concepto 4 2 5 4 2 Alta  casi todo API sin ejecutar; link 139a roto
167 onnx-runtime                   code     5 5 5 4 3 Baja  sklearn+ONNX+benchmark ejecutable
168 vertex-ai-deploy               concepto 4 1 5 4 2 Alta  cero ejecutable; pura API GCP
169 tf-lite-mobile                 code     5 2 5 4 2 Alta  conversion no corre sin TF; solo tabla
170 tensorflow-js                  code     5 3 4 4 2 Media inferencia real es JS; solo genera archivos
171 aceleracion-gpu                concepto 5 3 5 4 2 Media config GPU guardada; solo matmul numpy
172 tf-distribute                  concepto 4 3 5 4 2 Media multi-GPU no ejecutable; accum/LR numpy si
173 jax-flax                       code     5 4 5 3 3 Baja  fallback numpy corre; jit/grad reales
174 vertex-ai-escala               concepto 4 1 5 4 2 Alta  cero ejecutable; pura API GCP + Dockerfile
```

### Parte 3 — Estadística inferencial
```
175 distribuciones                 code     5 4 5 5 2 Baja  sin outputs; sin solucion trabajada
176 test-t                         code     5 4 5 5 2 Baja  solido; sin resolver
177 effect-size                    code     4 4 4 4 2 Media README corto; defs densas
178 chi-cuadrado                   code     5 4 5 5 2 Baja  autocontenido; falta solucion
179 anova                          code     5 4 4 4 2 Baja  ejecutable con asserts; sin resolver
180 no-parametricos                code     5 4 5 4 2 Baja  bien andamiado; sin solucion
181 correccion-multiple            code     4 4 4 4 2 Media conciso; sin outputs
182 intervalos-confianza           code     5 4 5 5 2 Baja  claro autocontenido; falta resuelto
183 bootstrap                      code     5 4 5 4 2 Baja  from-scratch; sin solucion
184 bca-permutation                code     4 4 4 3 2 Media README breve; sin asserts
185 ab-testing                     code     5 4 5 4 2 Baja  solido; sin solucion mostrada
186 cuped-always-valid             code     4 4 3 2 2 Alta  avanzado/denso para cero; defs terse
187 diseno-experimental            concepto 4 4 4 4 2 Media conceptual solido; sin resolver
188 dags-iv-confounders            concepto 4 4 4 3 2 Media causal steep desde cero
189 doubleml-econml                code     4 4 3 2 1 Alta  graduate; CATE/econml no demostrado
190 uplift-did                     code     4 4 4 3 2 Media avanzado; salidas ausentes
191 synthetic-control              code     4 4 3 2 2 Media ejercicios refieren pysyncon no usada
192 bayes-intro                    concepto 4 2 4 2 1 Alta  2/3 celdas NO ejecutan; xref stale
193 stack-bayesiano                code     4 4 3 2 1 Alta  muy avanzado; refiere libs; sin solucion
```

### Parte 4 — MLOps
```
194 dvc                            code     5 5 5 4 3 Baja  pipeline DVC real; sin solucion explicita
195 mlflow                         code     5 5 5 4 3 Baja  runs+registry reales; sin resolver
196 feast                          code     4 5 5 3 3 Media apply/materialize real; install fragil
197 ci-cd-gh-actions               code     4 3 4 4 3 Media YAML declarativo; workflow no verificable
198 docker                         code     4 3 5 4 3 Media Dockerfile real; build/run comentados
199 fastapi                        code     5 5 5 4 3 Baja  servidor subprocess real+benchmark
200 kubernetes                     code     4 2 5 3 3 Media solo genera manifests; nada ejecuta
201 serverless                     code     4 3 4 4 3 Media deploy declarativo; solo cost-calc corre
202 monitoreo-drift                code     5 5 5 4 3 Baja  PSI/KS/Wasserstein+Evidently reales
203 reentrenamiento                code     5 5 5 4 3 Baja  flow Prefect corre 5 dias
204 shadow-canary                  code     5 5 5 4 3 Baja  shadow/canary/AB con statsmodels
205 interpretabilidad              code     5 5 5 4 3 Baja  SHAP/LIME/PDP/ICE ejecutan
206 testing-datos                  code     5 5 5 4 3 Baja  GE+Pandera detectan bug inyectado
207 testing-modelos                code     5 5 5 4 3 Baja  MFT/INV/DIR/slice con asserts
```

### Parte 5 — Ingeniería de datos · Parte 6 — Recomendadores
```
208 airflow-etl                    code     5 4 5 4 3 Baja  sim local DuckDB corre; sin solucion
209 prefect-dagster                code     5 4 5 4 3 Baja  Prefect in-process; Dagster snippet
210 pyspark                        code     5 5 5 4 3 Baja  Spark local ejecutable end-to-end
211 polars                         code     5 5 5 4 3 Baja  benchmark lazy/streaming/DuckDB real
212 warehouses-bq-sf-duckdb        code     5 5 5 4 3 Baja  DuckDB local; BQ/SF snippets
213 streaming-kafka                code     5 4 5 4 3 Baja  sim in-memory particiones
214 parquet-avro                   code     5 5 5 4 3 Baja  benchmarks + schema evolution
215 modelado-dimensional           code     5 5 5 5 3 Baja  star schema + SCD2 en DuckDB; next roto
216 filtrado-colaborativo          code     5 5 5 4 3 Baja  user/item-based sparse ejecutable
217 factorizacion-svd-als          code     5 5 5 4 3 Baja  ALS a mano recupera estructura latente
218 content-based                  code     5 5 5 4 3 Baja  TF-IDF+ST+FAISS con fallbacks
219 recomendadores-hibridos        code     5 5 5 4 3 Baja  weighted/switching/LightFM + eval segmento
220 metricas-map-ndcg              code     5 5 5 4 4 Baja  metricas from-scratch validadas vs sklearn
221 cold-start                     code     5 5 5 4 3 Baja  bayesian shrinkage+onboarding+bandit
222 librerias-lightfm-implicit     code     5 4 5 4 3 Baja  benchmark 3 libs; requiere instalar
```

### Parte 7 — Ética/Fairness/Privacidad · Parte 8 — Capstones
```
223 tipos-de-sesgo                 code     5 5 5 4 3 Baja  ejercicios/homework sin solucion
224 metricas-fairness              code     5 5 5 4 3 Baja  impossibility demostrado; Adult/COMPAS sin resolver
225 privacidad-diferencial         code     5 5 5 4 3 Baja  DP-SGD manual denso; sin solucion
226 federated-learning             code     5 5 5 4 3 Baja  FedProx/DP-FedAvg como ejercicio sin codigo
227 gdpr-ai-act                    concepto 5 5 5 4 3 Baja  toolkit ejecutable; compliance sin solucion
228 reproducibilidad               code     5 5 5 4 3 Baja  cierre con asserts; DVC/uv sin resolver
229 capstone-tabular               code     5 5 5 4 4 Baja  skeleton corre entero; repo/CI al alumno
230 capstone-nlp-series            code     5 5 5 4 4 Media rama NLP solo README; notebook solo series
231 capstone-vision                code     5 4 5 4 4 Media transfer learning real solo stub; proxy HOG
232 portafolio-github              concepto 5 5 5 4 4 Baja  generador ejecutable; entregables al alumno
```

---

*Auditoría generada sin modificar ningún archivo del curso. Los puntajes son juicio pedagógico bajo el lente autoestudio-desde-cero; una clase guiada por instructor puntuaría más alto en E (el docente valida los ejercicios).*
