# Parte 6 — Sistemas de Recomendación

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏮️ Parte anterior](../parte-5-ingenieria-de-datos/README.md) · [⏭️ Parte siguiente](../parte-7-etica-fairness-privacidad/README.md)

**7 clases** · ~2–3 semanas · ✅ **completada (junio 2026)**

**Fuente principal:** Aggarwal *Recommender Systems: The Textbook* (Springer, 2016) + Koren/Bell/Volinsky 2009 (matrix factorization) + Hu/Koren/Volinsky 2008 (implicit feedback) + Burke 2002 (hybrids) + docs LightFM/Implicit/Surprise.

---

## 🎯 ¿De qué trata esta parte?

Una unidad especializada en una de las aplicaciones de ML con más impacto comercial directo: **recomendar el siguiente producto, video, canción o contenido**. Cubre los dos enfoques clásicos (filtrado colaborativo y content-based), su unión en sistemas **híbridos**, y la matemática detrás (factorización de matrices: SVD, ALS).

También cubre las **métricas correctas** (MAP@k, NDCG, recall@k — no accuracy) y el problema del **cold-start** (usuarios o items nuevos sin historial), que es donde mueren la mayoría de los recomendadores en su primer mes en producción. Termina con un tour por las librerías que se usan en la práctica (LightFM, Implicit, Surprise).

## 🧩 Problemas que resuelve

- Construir un recomendador user-based o item-based desde una matriz usuario-item dispersa.
- Aplicar factorización de matrices (SVD / ALS) para llegar a recomendaciones escalables.
- Combinar señales colaborativas y de contenido en un recomendador híbrido.
- Evaluar un recomendador con la métrica correcta (no con accuracy ni RMSE de rating).
- Mitigar el cold-start con estrategias basadas en contenido o popularidad.

## 🎓 Resultados de aprendizaje

Al finalizar esta parte, el estudiante podrá:

- Entrenar y evaluar un recomendador end-to-end con LightFM o Implicit sobre un dataset real (MovieLens o similar).
- Reportar la calidad del recomendador con MAP@k y NDCG, no con accuracy.
- Diseñar una estrategia explícita para usuarios y items nuevos.

## 🗺️ Estructura temática

- **Filtrado colaborativo** — clases 216–217 — user/item-based kNN, factorización de matrices (SVD truncado + ALS explicit/implicit).
- **Content-based e híbridos** — clases 218–219 — TF-IDF + sentence-transformers + FAISS, los 7 patrones de Burke + LightFM hybrid.
- **Evaluación y cold-start** — clases 220–221 — MAP@k / NDCG@k / recall@k + coverage + diversity, popularity Bayesiana + onboarding + bandits.
- **Tooling** — clase 222 — Surprise vs Implicit vs LightFM vs TF Recommenders, FAISS/Milvus para serving.

## 📚 Índice de clases (7)

- [216 — Filtrado colaborativo user-based e item-based](216-filtrado-colaborativo-user-based-e-item-based/README.md)
- [217 — Factorización de matrices: SVD, ALS](217-factorizacion-de-matrices-svd-als/README.md)
- [218 — Content-based filtering](218-content-based-filtering/README.md)
- [219 — Recomendadores híbridos](219-recomendadores-hibridos/README.md)
- [220 — Métricas: MAP@k, NDCG, recall@k](220-metricas-map-k-ndcg-recall-k/README.md)
- [221 — Cold-start problem](221-cold-start-problem/README.md)
- [222 — Librerías: LightFM, Implicit, Surprise](222-librerias-lightfm-implicit-surprise/README.md)

---

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏮️ Parte anterior](../parte-5-ingenieria-de-datos/README.md) · [⏭️ Parte siguiente](../parte-7-etica-fairness-privacidad/README.md)
