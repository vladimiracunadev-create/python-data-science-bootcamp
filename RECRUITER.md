# 🎯 Para reclutadores y evaluadores técnicos

> Evidencia técnica en 5 minutos. Sin lectura extensa.

---

## Qué es este repositorio

Un sistema de capacitación en Python y Data Science que integra:

- **currículo modular v2** (197 clases · 9 partes · pauta derivada de Géron 3ª ed., VanderPlas, Huyen, ISLP, Barocas/Hardt/Narayanan) — estructura scaffold con stubs; contenido pedagógico en desarrollo por bloques. El currículo v1 (31 clases con contenido completo) se conserva en `historicos/classes-v1/`;
- **laboratorio interactivo** (Flask + ejecución Python en tiempo real, matplotlib, pandas) ya migrado a v2;
- **app de escritorio nativa para Windows** (pywebview + Edge WebView2, sin navegador);
- **app Android** (Expo/React Native, contenido embebido + Google Colab) — pendiente migración a v2;
- **portal público** (GitHub Pages para alumnos + vista institucional) — pendiente migración a v2;
- **documentación de producto** organizada por audiencia.

---

## Estado real en producción

| Componente | Estado verificado | Evidencia |
|---|---|---|
| Backend Flask | operativo | 10 rutas, tests automatizados, CI en GitHub Actions |
| Ejecución de código Python | operativo | pandas, matplotlib (gráficos), scikit-learn, timeout 30s |
| 197 clases v2 (scaffold) | operativo | `/api/classes` → 197 clases, `/api/class/<path:slug>` → HTML |
| 31 clases v1 con contenido | archivado en `historicos/` | referencia y fuente de material reutilizable |
| 6 notebooks interactivos | operativo | `/api/notebooks` → 6 templates, ejecución por celda |
| App de escritorio Windows | v1.0.0 (consume v2 tras rebuild) | pywebview 6.1 + PyInstaller 6.19, ZIP portable 92MB |
| Instalador Windows | v1.0.0 | Inno Setup — sin Python requerido en el PC del usuario |
| App Android | v1.0.0 (contenido v1) | APK debug 137MB, Expo/React Native — pendiente migración a v2 |
| Portal del alumno | en vivo (contenido v1) | GitHub Pages — pendiente migración a v2 |
| CI/CD | activo | 3 workflows: tests, security scan, deploy-pages |
| Análisis de seguridad | limpio | Bandit: 0 High, 0 Medium, 0 Low |

---

## Stack técnico

| Capa | Tecnología |
|---|---|
| Backend | Python 3.10–3.12, Flask 3.x |
| Data Science | pandas 2.x, numpy 1.26+, matplotlib 3.8+, scikit-learn 1.4+ |
| Desktop Windows | pywebview 6.1 (Edge WebView2), PyInstaller 6.19 |
| Instalador | Inno Setup 6 |
| Mobile | Expo SDK 51, React Native, Android Gradle |
| Frontend | HTML/CSS/JS vanilla (SPA sin framework) |
| Tests | pytest 8.x, 4 módulos |
| Lint | ruff |
| Security | Bandit |
| CI/CD | GitHub Actions (3 workflows) |
| Deploy | GitHub Pages |
| Contenedores | Docker + Docker Compose (prod variant) |

---

## Lo que demuestra este proyecto

- capacidad de integrar backend Python con experiencia de escritorio nativa (pywebview);
- criterio de seguridad documentado y verificado con análisis estático;
- diseño pedagógico con separación clara entre contenido, laboratorio y presentación;
- estructura de producto con documentación organizada por audiencias;
- flujo de build reproducible desde fuente hasta instalador .exe y APK Android;
- operación local-first con múltiples modos de despliegue (venv, Docker, exe).

---

## Lo que este proyecto no pretende demostrar

- una plataforma multiusuario SaaS lista para internet abierta;
- personalización infinita antes de un acuerdo comercial;
- profundidad total en todas las capas desde la primera versión.

---

## Cómo evaluar en 5 minutos

1. Clona el repo y ejecuta `python run_bootcamp.py` — el navegador abre automáticamente.
2. Haz clic en cualquier clase del sidebar — carga contenido Markdown con quiz.
3. Abre una celda del notebook y ejecuta `import pandas as pd; print(pd.__version__)`.
4. Descarga el ZIP portable del Release y ejecuta `BootcampPythonDS.exe` — se abre una ventana nativa.
5. Revisa [docs/GUIA_EVALUACION.md](docs/GUIA_EVALUACION.md) para la ruta ejecutiva completa.

---

## Contacto

**Vladimir Acuña** — [github.com/vladimiracunadev-create](https://github.com/vladimiracunadev-create)
