# Parte 4 — MLOps — Modelos en Producción

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏮️ Parte anterior](../parte-3-estadistica-inferencial/README.md) · [⏭️ Parte siguiente](../parte-5-ingenieria-de-datos/README.md)

**14 clases** · ~4–5 semanas · ✅ **completada (junio 2026)**

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

- **Versionado** — clases 194–196 — DVC para datos, MLflow para modelos/experimentos, Feast como feature store.
- **CI/CD y packaging** — clases 197–199 — GitHub Actions para ML, Docker, FastAPI.
- **Escala y serving** — clases 200–201 — Kubernetes, serverless (AWS Lambda / GCP Functions).
- **Monitoreo y operación** — clases 202–204 — data/model drift, reentrenamiento programado, shadow/canary.
- **Interpretabilidad y testing** — clases 205–207 — SHAP/LIME/PDP/ICE, testing de datos, testing de modelos.

## 🛡️ Las 6 capas de protección que dejás armadas

Al terminar P4, todo modelo en producción está cubierto por:

1. **Data tests** (206) — validación de cada batch antes de entrar al pipeline.
2. **Model tests** (207) — INV/DIR/MFT/slice tests como gate de CI.
3. **Monitoring** (202) — PSI/KS/Wasserstein + CBPE sobre tráfico real.
4. **Shadow** (204) — challenger predice sin afectar usuarios.
5. **Canary** (204) — rollout 1% → 5% → 25% → 100% con sticky assignment.
6. **Rollback automático** (204) — vuelta al champion ante degradación de guardrails.

## 📚 Índice de clases (14)

- [194 — Versionado de datos con DVC](194-versionado-de-datos-con-dvc/README.md)
- [195 — Versionado de modelos y experimentos con MLflow](195-versionado-de-modelos-y-experimentos-con-mlflow/README.md)
- [196 — Feature stores (Feast)](196-feature-stores-feast/README.md)
- [197 — CI/CD para ML con GitHub Actions](197-ci-cd-para-ml-con-github-actions/README.md)
- [198 — Docker para empaquetar modelos](198-docker-para-empaquetar-modelos/README.md)
- [199 — APIs con FastAPI sirviendo modelos](199-apis-con-fastapi-sirviendo-modelos/README.md)
- [200 — Kubernetes para servir modelos a escala](200-kubernetes-para-servir-modelos-a-escala/README.md)
- [201 — Serverless ML: AWS Lambda, GCP Cloud Functions](201-serverless-ml-aws-lambda-gcp-cloud-functions/README.md)
- [202 — Monitoreo: data drift, model drift, alertas](202-monitoreo-data-drift-model-drift-alertas/README.md)
- [203 — Reentrenamiento programado](203-reentrenamiento-programado/README.md)
- [204 — Shadow deployment y canary releases](204-shadow-deployment-y-canary-releases/README.md)
- [205 — Interpretabilidad: SHAP, LIME, PDP, ICE](205-interpretabilidad-shap-lime-pdp-ice/README.md)
- [206 — Testing de datos: Great Expectations, Deequ](206-testing-de-datos-great-expectations-deequ/README.md)
- [207 — Testing de modelos: invariance, behavioral tests](207-testing-de-modelos-invariance-behavioral-tests/README.md)

---

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏮️ Parte anterior](../parte-3-estadistica-inferencial/README.md) · [⏭️ Parte siguiente](../parte-5-ingenieria-de-datos/README.md)
