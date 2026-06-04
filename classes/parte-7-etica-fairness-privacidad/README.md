# Parte 7 — Ética, Fairness y Privacidad

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏮️ Parte anterior](../parte-6-sistemas-de-recomendacion/README.md) · [⏭️ Parte siguiente](../parte-8-capstones/README.md)

**6 clases** · ~2 semanas

**Fuente principal:** **Barocas / Hardt / Narayanan** ([*Fairness and Machine Learning*](https://fairmlbook.org/)) — el texto de referencia académico para fairness algorítmica.

---

## 🎯 ¿De qué trata esta parte?

La parte que ningún currículo serio puede omitir en 2026: cómo construir sistemas de ML que **no discriminen, no filtren datos personales y sean reproducibles**. Cubre los tipos y orígenes del sesgo algorítmico, las **métricas formales de fairness** (demographic parity, equalized odds, calibration — y por qué son matemáticamente incompatibles entre sí), técnicas modernas como **privacidad diferencial** y **federated learning**, y el marco regulatorio actual (GDPR, AI Act europeo).

Cierra con una clase sobre **reproducibilidad** (seeds, lock files, versionado de datasets) que es prerrequisito de cualquier discusión seria sobre fairness: si no se puede reproducir, no se puede auditar.

## 🧩 Problemas que resuelve

- Identificar los tipos y fuentes de sesgo en un dataset y en un modelo entrenado.
- Medir fairness con las métricas correctas y explicar por qué no se pueden cumplir todas a la vez.
- Aplicar privacidad diferencial básica para publicar estadísticas sin filtrar individuos.
- Entender cuándo federated learning es la solución correcta (y cuándo es overkill).
- Cumplir requisitos básicos de GDPR y AI Act en un proyecto de ML.
- Hacer un experimento reproducible bit-a-bit.

## 🎓 Resultados de aprendizaje

Al finalizar esta parte, el estudiante podrá:

- Auditar un modelo clasificador por demographic parity y equalized odds, y reportar trade-offs.
- Documentar un dataset y un modelo con un datasheet / model card.
- Producir un experimento que cualquiera puede reproducir desde el repo en menos de 30 minutos.

## 🗺️ Estructura temática

- **Sesgo y fairness** — clases 188–189 — tipos de sesgo, métricas de fairness.
- **Privacidad** — clases 190–191 — privacidad diferencial, federated learning.
- **Regulación y reproducibilidad** — clases 192–193 — GDPR / AI Act, reproducibilidad práctica.

## 📚 Índice de clases (6)

- [223 — Tipos de sesgo algorítmico y orígenes](223-tipos-de-sesgo-algoritmico-y-origenes/README.md)
- [224 — Métricas de fairness: demographic parity, equalized odds, calibration](224-metricas-de-fairness-demographic-parity-equalized-odds-calibration/README.md)
- [225 — Privacidad diferencial (intro)](225-privacidad-diferencial-intro/README.md)
- [226 — Federated learning (intro)](226-federated-learning-intro/README.md)
- [227 — GDPR y AI Act (EU)](227-gdpr-y-ai-act-eu/README.md)
- [228 — Reproducibilidad: seeds, lock files, versionado de datasets](228-reproducibilidad-seeds-lock-files-versionado-de-datasets/README.md)

---

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏮️ Parte anterior](../parte-6-sistemas-de-recomendacion/README.md) · [⏭️ Parte siguiente](../parte-8-capstones/README.md)
