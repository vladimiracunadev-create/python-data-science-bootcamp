# Parte 4 — MLOps — Modelos en Producción

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏮️ Parte anterior](../parte-3-estadistica-inferencial/README.md) · [⏭️ Parte siguiente](../parte-5-ingenieria-de-datos/README.md)

**14 clases** · ~4–5 semanas

**Fuente principal:** **Huyen** ([*Designing Machine Learning Systems*](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/)) — el manual de cabecera para MLOps moderno.

---

## 🎯 ¿De qué trata esta parte?

La parte que convierte un notebook que entrena bien en un **sistema que funciona en producción 24/7**. Cubre versionado (de datos, modelos y experimentos), packaging (Docker), serving (FastAPI, Kubernetes, serverless), monitoreo (data drift, model drift) y los rituales que evitan que el modelo se degrade silenciosamente (reentrenamiento programado, shadow deployment, canary releases).

Incluye una unidad fuerte de **interpretabilidad** (SHAP, LIME, PDP, ICE) porque ningún modelo va a producción sin alguien preguntando "¿por qué dijo eso?", y otra de **testing** (datos con Great Expectations, modelos con tests de invariancia) porque en ML el bug habitual no es un crash sino un drift silencioso.

## 🧩 Problemas que resuelve

- Versionar datasets pesados con DVC y modelos/experimentos con MLflow.
- Empaquetar un modelo entrenado en un contenedor Docker reproducible.
- Servir el modelo como API (FastAPI) y escalar con Kubernetes o serverless.
- Detectar data drift y model drift antes de que el negocio reclame.
- Hacer despliegues seguros (shadow, canary) para evitar romper producción.
- Explicar predicciones individuales y globales con SHAP / LIME / PDP / ICE.
- Validar entradas con Great Expectations antes de que lleguen al modelo.

## 🎓 Resultados de aprendizaje

Al finalizar esta parte, el estudiante podrá:

- Tomar un modelo entrenado y publicarlo como API monitoreada en producción en menos de un día.
- Diseñar un pipeline CI/CD que reentrene y redesplíegue automáticamente cuando llega data nueva.
- Configurar alertas de drift que avisen *antes* de que la métrica de negocio caiga.
- Generar un reporte de interpretabilidad para stakeholders no técnicos.

## 🗺️ Estructura temática

- **Versionado** — clases 159–161 — DVC para datos, MLflow para modelos/experimentos, Feast como feature store.
- **CI/CD y packaging** — clases 162–164 — GitHub Actions para ML, Docker, FastAPI.
- **Escala y serving** — clases 165–166 — Kubernetes, serverless (AWS Lambda / GCP Functions).
- **Monitoreo y operación** — clases 167–169 — data/model drift, reentrenamiento programado, shadow/canary.
- **Interpretabilidad y testing** — clases 170–172 — SHAP/LIME/PDP/ICE, testing de datos, testing de modelos.

## 📚 Índice de clases (14)

- [159 — Versionado de datos con DVC](159-versionado-de-datos-con-dvc/README.md)
- [160 — Versionado de modelos y experimentos con MLflow](160-versionado-de-modelos-y-experimentos-con-mlflow/README.md)
- [161 — Feature stores (Feast)](161-feature-stores-feast/README.md)
- [162 — CI/CD para ML con GitHub Actions](162-ci-cd-para-ml-con-github-actions/README.md)
- [163 — Docker para empaquetar modelos](163-docker-para-empaquetar-modelos/README.md)
- [164 — APIs con FastAPI sirviendo modelos](164-apis-con-fastapi-sirviendo-modelos/README.md)
- [165 — Kubernetes para servir modelos a escala](165-kubernetes-para-servir-modelos-a-escala/README.md)
- [166 — Serverless ML: AWS Lambda, GCP Cloud Functions](166-serverless-ml-aws-lambda-gcp-cloud-functions/README.md)
- [167 — Monitoreo: data drift, model drift, alertas](167-monitoreo-data-drift-model-drift-alertas/README.md)
- [168 — Reentrenamiento programado](168-reentrenamiento-programado/README.md)
- [169 — Shadow deployment y canary releases](169-shadow-deployment-y-canary-releases/README.md)
- [170 — Interpretabilidad: SHAP, LIME, PDP, ICE](170-interpretabilidad-shap-lime-pdp-ice/README.md)
- [171 — Testing de datos: Great Expectations, Deequ](171-testing-de-datos-great-expectations-deequ/README.md)
- [172 — Testing de modelos: invariance, behavioral tests](172-testing-de-modelos-invariance-behavioral-tests/README.md)

---

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏮️ Parte anterior](../parte-3-estadistica-inferencial/README.md) · [⏭️ Parte siguiente](../parte-5-ingenieria-de-datos/README.md)
