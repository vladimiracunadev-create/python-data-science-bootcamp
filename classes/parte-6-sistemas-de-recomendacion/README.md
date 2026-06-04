# Parte 6 — Sistemas de Recomendación

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏮️ Parte anterior](../parte-5-ingenieria-de-datos/README.md) · [⏭️ Parte siguiente](../parte-7-etica-fairness-privacidad/README.md)

**7 clases** · ~2–3 semanas

**Fuente principal:** Complementaria — combinación de filtrado colaborativo clásico y enfoques modernos basados en embeddings.

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

- **Filtrado colaborativo** — clases 181–182 — user-based, item-based, factorización de matrices (SVD, ALS).
- **Content-based e híbridos** — clases 183–184 — content-based, recomendadores híbridos.
- **Evaluación y cold-start** — clases 185–186 — métricas MAP@k / NDCG / recall@k, cold-start problem.
- **Tooling** — clase 187 — LightFM, Implicit, Surprise.

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
