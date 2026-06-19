# Clase 222 — Librerías: LightFM, Implicit, Surprise

> Parte: **6 — Sistemas de Recomendación** · Fuente: docs oficiales [Surprise](https://surprise.readthedocs.io/) + [LightFM](https://making.lyst.com/lightfm/docs/home.html) + [Implicit](https://implicit.readthedocs.io/) + [TensorFlow Recommenders](https://www.tensorflow.org/recommenders). ⏱️ Duración estimada: **70 min**.

## 🎯 Objetivo

Conocer las **librerías de recomendación que vas a usar en la vida real** sin tener que reimplementar lo de Clases 216-221. Decidir cuál usar según: tipo de feedback (explicit/implicit), tamaño del dataset, features disponibles, integración con stack.

## 📚 Resultados de aprendizaje

Al finalizar, el estudiante podrá:

- Usar **Surprise** para algoritmos clásicos explicit (KNNBasic, SVD, SVD++, NMF, Co-Clustering) con API tipo sklearn.
- Usar **Implicit** para ALS implicit, BPR, Logistic MF — la opción más rápida en Python para datasets grandes.
- Usar **LightFM** cuando tenés features (Clase 219 hybrid).
- Conocer **TensorFlow Recommenders** y **Spotlight (PyTorch)** para arquitecturas deep (two-tower, sequential).
- Decidir librería según: explicit vs implicit, escala, features, deployment target.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | Surprise: explicit, didáctica | Empezar a aprender RS. |
| 2 | Implicit: ALS/BPR Cython | El caballo de batalla en producción. |
| 3 | LightFM: CF + features | Hybrid built-in. |
| 4 | TF Recommenders + Spotlight | Deep RS (two-tower, BERT4Rec). |
| 5 | Spark `pyspark.ml.recommendation.ALS` | Cuando el dataset es TB. |
| 6 | Vector DBs (FAISS, Milvus, Pinecone) | Serving de embeddings a escala. |

## 📖 Definiciones y características

- **Surprise**: librería didáctica, API tipo sklearn. Maneja explicit feedback con KNN, SVD, NMF, etc. **Bueno para aprender, lento para grandes datasets**.
- **Implicit** (Ben Frederickson): Cython + multi-thread. ALS implicit (Hu et al.), BPR (Bayesian Personalized Ranking), Logistic MF. **Default para CF en producción Python**.
- **LightFM** (Lyst): factorización con features. Loss WARP / BPR / Logistic. **El sweet spot para hybrid con metadata**.
- **TensorFlow Recommenders** (TFRS): API alto-nivel sobre TF/Keras para two-tower, ranking, retrieval. **SOTA para deep RS, requiere setup TF**.
- **Spotlight** (Maciej Kula): PyTorch library para sequential + factorización. **Para experimentos research**.
- **Spark ML ALS**: distribuido, escala a billones de interactions. **Cuando el dataset no entra en single machine**.
- **Vector DB**: para servir embeddings. FAISS (in-process), Milvus (open-source server), Pinecone/Qdrant/Weaviate (managed). Permiten `recommend(user_emb, top_k=10)` en <10 ms con M items.

## 📂 Dataset / recursos

- **Dataset**: MovieLens 100K y 1M.
- Librerías: `scikit-surprise`, `implicit>=0.7`, `lightfm>=1.17`, opcional `tensorflow-recommenders`.

## 🧪 Ejercicios

1. **Surprise SVD**: `from surprise import SVD, Dataset; data = Dataset.load_builtin('ml-100k'); algo = SVD(); cross_validate(algo, data, measures=['RMSE','MAE'], cv=5)`. Reportar RMSE.
2. **Implicit ALS**: `model = implicit.als.AlternatingLeastSquares(factors=64, regularization=0.05, iterations=20)`. `model.fit(R_sparse * 40)`. `recommend(user_id, R[user_id], N=10)`.
3. **Implicit BPR**: mismo modelo pero `implicit.bpr.BayesianPersonalizedRanking(factors=64)`. Comparar NDCG vs ALS.
4. **LightFM**: `LightFM(loss='warp', no_components=32)`. Con item features (géneros). Comparar pure CF vs hybrid.
5. **Benchmarking**: mismo dataset, mismo split, las 4 librerías. Tabla con NDCG@10, recall@10, tiempo entrenamiento, tiempo predict.

## 📝 Homework verificable

Notebook con:

1. Comparativa rigurosa sobre MovieLens 1M:
   - Surprise SVD
   - Implicit ALS
   - Implicit BPR
   - LightFM WARP (con features)
2. Mismo train/test split temporal. Mismas métricas (Clase 220).
3. Tabla: NDCG@10, recall@10, coverage, tiempo train (s), tiempo predict (ms/user), RAM peak.
4. Recomendaciones por caso de uso (decisión justificada):
   - "Quiero algo simple para aprender" → Surprise.
   - "Quiero performance en producción Python para 10M users" → Implicit.
   - "Tengo features ricos y dataset chico-medio" → LightFM.
   - "Tengo equipo ML serio y quiero SOTA" → TF Recommenders / two-tower.
5. Bonus: deploy del mejor modelo como servicio FastAPI (Clase 199) con FAISS para retrieval rápido.

**Criterio de aceptación**: 4 modelos entrenan limpio, NDCG@10 reportado correctamente, la tabla permite decidir cuál usar por caso.

## ⚠️ Errores comunes

| Síntoma / mensaje | Causa y cómo arreglar |
|---|---|
| Surprise lentísimo sobre 1M+ | Surprise está pensado para didáctico. **Fix**: migrar a Implicit o LightFM. |
| `implicit` warning OpenBLAS threads | Conflict entre BLAS threading y OpenMP threading. **Fix**: `os.environ['OPENBLAS_NUM_THREADS']='1'` antes del import. |
| LightFM WARP muy lento | WARP es O(samples) por epoch. **Fix**: `loss='bpr'` o `loss='logistic'`. Reducir epochs. |
| TFRS requiere graph mode + estructura complicada | Curva de aprendizaje fuerte. **Fix**: empezar con tutoriales oficiales `MovielensRetrievalModel`. |
| FAISS index demasiado grande para RAM | `IndexFlatIP` guarda todo en RAM. **Fix**: `IndexIVFFlat` (cuantización) o `IndexHNSWFlat` (graph-based). |
| Score implicit ALS no es probabilidad | Es un score, no proba. **Fix**: para servir como "rating" 0-1 → sigmoide o rank-normalize. |

## ❓ Preguntas frecuentes

**❓ ¿Cuál instalo primero?**

**Implicit** para CF moderno (90% de los casos). **LightFM** si tenés features. **Surprise** solo para aprender el ABC.

**❓ ¿Implicit y LightFM compiten o se complementan?**

Compiten. Implicit es CF puro (más rápido, más simple). LightFM es CF + features (más flexible). Si no tenés features útiles: Implicit gana. Si tenés metadata rica: LightFM.

**❓ ¿TF Recommenders vale la pena?**

Sí cuando: (1) Dataset >100M interactions. (2) Necesitás features complejos (text embeddings, image embeddings). (3) Tu stack ya es TF. (4) Querés sequential / session-based RS (BERT4Rec, SASRec). Para casos chicos: overkill.

**❓ ¿Cómo sirvo embeddings en producción?**

(1) Pre-computar `item_factors` offline. (2) Indexar con **FAISS** (in-process) o **Milvus/Pinecone** (managed). (3) En request: computar `user_emb` (rápido o desde cache) → `index.search(user_emb, k=10)` → top-N items. Latencia: <10 ms para millones de items con HNSW.

**❓ ¿Reentrenamiento — cada cuánto?**

Para CF: diario o semanal típicamente. Para deep RS con features estáticos: semanal-mensual. Para sequential: continuous training. Ver Clase 203.

**❓ ¿RecBole, Cornac, Spotlight?**

Frameworks de research, mucho catálogo de algoritmos. Útiles para **comparar 20 modelos en paper**. Para producción: empezás con uno (Implicit/LightFM) y lo customizás.

## 🔗 Referencias

- [Surprise docs](https://surprise.readthedocs.io/).
- [Implicit docs](https://implicit.readthedocs.io/) + [GitHub](https://github.com/benfred/implicit).
- [LightFM docs](https://making.lyst.com/lightfm/docs/home.html).
- [TensorFlow Recommenders](https://www.tensorflow.org/recommenders) — two-tower + ranking.
- [FAISS docs](https://github.com/facebookresearch/faiss) — vector similarity search.

## 📥 Material descargable

- 📄 [Guía explicativa (PDF)](./clase-222-librerias-lightfm-implicit-surprise-guia-explicativa.pdf) — versión imprimible con todo el contenido de la clase.
- 🎞️ [Presentación (PPTX)](./clase-222-librerias-lightfm-implicit-surprise-presentacion.pptx) — deck PowerPoint listo para proyectar en clase.
- 🧮 [Notebook ejecutable (.ipynb)](./notebook.ipynb) — abrilo desde el laboratorio del programa o desde Jupyter.

## ➡️ Siguiente clase

[Clase 223 — Sesgos algorítmicos: tipos y origen](../../parte-7-etica-fairness-privacidad/223-sesgos-algoritmicos-tipos-y-origen/README.md)

> 🎉 **Fin de la Parte 6 — Sistemas de Recomendación**. Tenés CF (216-217) + content (218) + híbridos (219) + métricas (220) + cold-start (221) + ecosistema de librerías (222). Parte 7 cierra el ciclo con **ética, fairness, privacidad** — qué hacer cuando tus recomendaciones afectan vidas reales.
