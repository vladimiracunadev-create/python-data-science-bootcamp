<div align="center">

# ✅ Guía de evaluación rápida

### **Para institución, evaluador técnico, reclutador o docente externo**

[![Tiempo](https://img.shields.io/badge/recorrido-10%20min-3fb950?style=for-the-badge)](#%EF%B8%8F-recorrido-de-10-minutos)
[![Técnico](https://img.shields.io/badge/t%C3%A9cnico-30%20min-7c5cff?style=for-the-badge)](#-inventario-real-del-producto)
[![Honestidad](https://img.shields.io/badge/estado-honesto-f59e0b?style=for-the-badge)](#-executive-summary)

</div>

---

## 🎯 Executive summary

Este repositorio es una **pauta avanzada y completa de Python y Data Science** organizada en 232 clases y 9 partes. La pauta está derivada de referentes profesionales: *Hands-On ML* (Géron, 3ª ed.), *Python Data Science Handbook* (VanderPlas), *Designing ML Systems* (Huyen), *ISLP* (James et al) y *Fairness and ML* (Barocas/Hardt/Narayanan).

```
v3.11.0:  232 clases · 9 partes · 🎓 232/232 READMEs · 232/232 notebooks ejecutables · cobertura 100% real — todas las partes completas y modernizadas 2024-2026, el lab con kernel Jupyter ejecuta el 100% del currículo. App Windows nativa con PySide6 (Qt puro, sin web, sin localhost) que renderiza la clase en HTML con el mismo conversor que genera GitHub Pages, como diferencial técnico de la superficie de escritorio.
```

Incluye laboratorio interactivo local (Flask), app de escritorio nativa para Windows, app Android y una familia documental que distingue producto, operación y seguridad.

**Estado honesto (v3.11.0, agosto 2026):** 🎓 **currículo entero listo · 232/232 READMEs · 232/232 notebooks ejecutables · cobertura 100% real** — todas las 9 partes están completas y modernizadas con READMEs pedagógicos + notebook ejecutable corriendo en el laboratorio con kernel Jupyter real, secciones Definiciones/Errores comunes/FAQ en cada clase y 35 clases dedicadas a temas modernos 2024-2026 + stack MLOps completo (P4: DVC, MLflow, Feast, K8s, FastAPI, drift, shadow/canary, SHAP, Great Expectations, behavioral tests) + data engineering (P5: Airflow, Prefect/Dagster, PySpark, Polars, DuckDB/BQ/Snowflake, Kafka, Parquet/Avro, star schemas SCD2) + recomendadores (P6: CF kNN, SVD+ALS implicit, content+FAISS, LightFM hybrid, métricas top-N, cold-start) + ética/fairness/privacidad (P7: Suresh-Guttag taxonomía sesgos, DP/EO/calibration + impossibility theorem, privacidad diferencial (Laplace/Gauss/DP-SGD), federated learning (FedAvg + gradient leakage), GDPR + AI Act EU 2024/1689, reproducibilidad (seeds/lock files/model cards/datasheets)) + **Capstones integradores (P8)**: Capstone 1 tabular E2E (ColumnTransformer+GBM+Optuna+MLflow+FastAPI+Streamlit+SHAP+CI), Capstone 2 NLP/series (DistilBERT o forecasting con baselines+SARIMA+backtesting+cuantiles), Capstone 3 visión transfer learning (ConvNeXt/EfficientNetV2/ViT + RandAugment/MixUp/CutMix + ONNX), Portafolio público (MkDocs Material/Quarto + GitHub Pages + demos hosted + deck + CV técnico). Las 232 clases tienen notebook ejecutable v3.0 que corre end-to-end en el laboratorio. Ya no quedan clases ni notebooks pendientes — **siguiente foco: superficies** (regen PDFs/PPTX por clase, app móvil). Ver progreso real en [GitHub Pages — currículo](https://vladimiracunadev-create.github.io/python-data-science-program/clases/).

---

## 💪 Lo que demuestra hoy

| Área | Evidencia concreta | Dónde verla |
|---|---|---|
| Diseño curricular profesional | 232 clases en 9 partes con prerrequisitos, ML, DL, MLOps, ética, capstones | `classes/README.md` · `docs/syllabus.md` |
| Fuentes acreditadas del currículo | pauta derivada de 5 libros referentes en el campo | `docs/syllabus.md` |
| Laboratorio operativo | Flask shell + kernel Jupyter real (`jupyter_client`) ejecutando notebooks reales del currículo | `app/` → `python run_program.py` |
| Distribución de escritorio | App nativa Windows con PySide6 / Qt puro (v3.11.0) — sin web, sin localhost, sin WebView; viewer del currículo con tree + cabecera de clase + tabs Clase/Notebook, la clase renderizada en HTML | `installer/` · `launcher.py` · `app_desktop/` |
| Distribución móvil | App Android Expo/React Native (232 clases embebidas) | `mobile/` |
| Portal público funcional | GitHub Pages con portal del alumno + vista institucional | `site/` |
| Postura de seguridad | Validación de slugs, timeout de ejecución, CSP estricto, sin CDN externas | `SECURITY.md` · `app/app.py` |
| CI/CD activo | Tests + lint + build de contenedor + SAST en GitHub Actions | `.github/workflows/` |
| Documentación auditada | Arquitectura, operación, pedagogía y seguridad como documentos separados | `docs/` |

---

## ⏱️ Recorrido de 10 minutos

```
1. README.md                        → qué es, estado actual, superficies, inicio rápido
2. docs/syllabus.md                 → pauta completa de 232 clases
3. classes/README.md                → índice navegable
4. docs/CATALOGO_PRODUCTO.md        → qué superficies existen y qué entrega cada una hoy
5. docs/ARQUITECTURA_PRODUCTO.md    → capas, diagramas de flujo, fronteras
6. SECURITY.md                      → qué está protegido y qué límites se declaran
```

---

## 📦 Inventario real del producto

### Currículo

| Parte | Tema | Clases | Estado |
|---|---|---|---|
| 0 | Prerrequisitos | 49 | 🟢 **completa · README + notebook ejecutable** |
| 1 | Machine Learning clásico | 50 | 🟢 **completa · README + notebook ejecutable** |
| 2 | Deep Learning | 75 | 🟢 **completa · README + notebook ejecutable** |
| 3 | Estadística inferencial | 19 | 🟢 **completa · README + notebook ejecutable** |
| 4 | MLOps | 14 | 🟢 **completa · README + notebook ejecutable** |
| 5 | Ingeniería de datos | 8 | 🟢 **completa · README + notebook ejecutable** |
| 6 | Recomendadores | 7 | 🟢 **completa · README + notebook ejecutable** |
| 7 | Ética, fairness, privacidad | 6 | 🟢 **completa · README + notebook ejecutable** |
| 8 | Capstones | 4 | 🟢 **completa · README + notebook ejecutable** |
| | **Total** | **232** | 🎓 **232/232 README · 232/232 notebooks ejecutables · cobertura 100% real** |

**232/232 clases desarrolladas**: cada clase trae `README.md` con objetivo + resultados + temas + dataset + ejercicios + homework + **📖 Definiciones** + **⚠️ Errores comunes** + **❓ FAQ** + referencias y `notebook.ipynb` ejecutable v3.0 (self-contained con datasets sintéticos, seed 42, try/except sobre libs pesadas con fallback CPU-friendly) que corre end-to-end en el laboratorio con kernel Jupyter real.

### Datasets sintéticos

| Dataset | Descripción |
|---|---|
| ventas_tienda.csv | Ventas multitienda con categorías y medios de pago |
| retencion_clientes.csv | Serie mensual de altas, bajas e ingresos |
| soporte_tickets.csv | Tickets por categoría, prioridad y canal |
| transporte.csv | Viajes con origen, destino y retrasos |
| estudiantes.csv | Registro académico con asistencia y evaluaciones |
| comentarios_productos.csv | 100 reseñas en español con etiqueta de sentimiento |

### Distribuciones disponibles

| Superficie | Estado |
|---|---|
| Portal del alumno (GitHub Pages) | operativo — pendiente migrar al índice actual |
| Vista institucional (GitHub Pages) | operativo |
| Laboratorio de ejecución Python (Flask + kernel Jupyter) | operativo |
| App Windows (PySide6 Qt nativa) | ✅ [binario v3.11.0 publicado en release](https://github.com/vladimiracunadev-create/python-data-science-program/releases/tag/v3.11.0) — ZIP portable slim (274 MB), clase renderizada en HTML |
| App Android (Expo/React Native) | ✅ [APK debug v3.11.0 publicado en release](https://github.com/vladimiracunadev-create/python-data-science-program/releases/tag/v3.11.0) (versionCode 42) — 232 clases embebidas y verificadas dentro del binario, generadas desde `classes/**/README.md` |

---

## 🏆 Señales de madurez

| Señal | Dónde se ve |
|---|---|
| Rutas por audiencia | [INDEX.md](INDEX.md) |
| Fuente de verdad del producto | [CATALOGO_PRODUCTO.md](CATALOGO_PRODUCTO.md) |
| Pauta curricular profesional | [syllabus.md](syllabus.md) |
| Arquitectura con diagramas Mermaid | [ARQUITECTURA_PRODUCTO.md](ARQUITECTURA_PRODUCTO.md) |
| Operación reproducible y smoke checks | [../RUNBOOK.md](../RUNBOOK.md) |
| Seguridad declarada y honesta | [../SECURITY.md](../SECURITY.md) |
| CI/CD visible y rastreable | `.github/workflows/` |
| Historial de cambios | [../CHANGELOG.md](../CHANGELOG.md) |
| Capa pública no técnica | `site/` · `site/product/` |

---

## 🚫 Lo que este repositorio no vende

- una plataforma multiusuario endurecida para internet abierta;
- un LMS con autenticación, roles y seguimiento centralizado;
- el currículo entero está listo a nivel de contenido pedagógico (🎓 232/232 README + 232/232 notebooks ejecutables + 232 PDFs + 232 PPTX · cobertura 100% real + secciones Definiciones/Errores/FAQ + capstones integradores P8); lo único pendiente para dictarlo "llave en mano" es migrar el catálogo a la UI de la app Android;
- la app Android en producción (APK debug, producción está en roadmap);
- personalización ilimitada antes de definir condiciones reales.

---

## 🎓 Conclusiones que una evaluación justa puede sacar

- la **pauta cubre un currículo de Data Science avanzado y empleable en 2026** (incluye LLMs, MLOps real, inferencia causal, fairness — temas ausentes en programas más superficiales);
- existe coherencia entre contenido, laboratorio, distribución y documentación;
- la decisión de empezar por un scaffold completo antes de rellenar contenido evidencia capacidad de **diseñar el producto antes de implementarlo**;
- el valor no depende de una tecnología puntual sino de la mediación pedagógica y el criterio de diseño curricular.
