# Guía de evaluación rápida

> **Audiencia:** institución, evaluador técnico, reclutador, docente externo.
> **Tiempo estimado:** 10 minutos para el recorrido ejecutivo · 30 minutos para el técnico.

---

## Executive summary

Este repositorio es una **pauta avanzada y completa de Python y Data Science** organizada en 197 clases y 9 partes. La pauta está derivada de referentes profesionales: *Hands-On ML* (Géron, 3ª ed.), *Python Data Science Handbook* (VanderPlas), *Designing ML Systems* (Huyen), *ISLP* (James et al) y *Fairness and ML* (Barocas/Hardt/Narayanan).

```
v2.0.0-scaffold:  197 clases  ·  9 partes  ·  scaffold + READMEs + notebooks stub
```

Incluye laboratorio interactivo local (Flask), app de escritorio nativa para Windows, app Android y una familia documental que distingue producto, operación y seguridad.

**Estado honesto:** el currículo está en fase **scaffold** — la estructura y la pauta están definidas, pero el contenido pedagógico de cada clase debe desarrollarse por bloques.

---

## Lo que demuestra hoy

| Área | Evidencia concreta | Dónde verla |
|---|---|---|
| Diseño curricular profesional | 197 clases en 9 partes con prerrequisitos, ML, DL, MLOps, ética, capstones | `classes/README.md` · `docs/syllabus.md` |
| Fuentes acreditadas del currículo | pauta derivada de 5 libros referentes en el campo | `docs/syllabus.md` |
| Laboratorio operativo | Flask local con ejecución Python en tiempo real | `app/` → `python run_program.py` |
| Distribución de escritorio | App nativa Windows con Edge WebView2, sin navegador, sin Python instalado | `installer/` · `launcher.py` |
| Distribución móvil | App Android Expo/React Native (pendiente migrar contenido al índice actual) | `mobile/` |
| Portal público funcional | GitHub Pages con portal del alumno + vista institucional | `site/` |
| Postura de seguridad | Validación de slugs, timeout de ejecución, CSP estricto, sin CDN externas | `SECURITY.md` · `app/app.py` |
| CI/CD activo | Tests + lint + build de contenedor + SAST en GitHub Actions | `.github/workflows/` |
| Documentación auditada | Arquitectura, operación, pedagogía y seguridad como documentos separados | `docs/` |

---

## Recorrido de 10 minutos

```
1. README.md                        → qué es, estado actual, superficies, inicio rápido
2. docs/syllabus.md                 → pauta completa de 197 clases
3. classes/README.md                → índice navegable
4. docs/CATALOGO_PRODUCTO.md        → qué superficies existen y qué entrega cada una hoy
5. docs/ARQUITECTURA_PRODUCTO.md    → capas, diagramas de flujo, fronteras
6. SECURITY.md                      → qué está protegido y qué límites se declaran
```

---

## Inventario real del producto

### Currículo (scaffold)

| Parte | Tema | Clases |
|---|---|---|
| 0 | Prerrequisitos | 46 |
| 1 | Machine Learning clásico | 43 |
| 2 | Deep Learning | 56 |
| 3 | Estadística inferencial | 13 |
| 4 | MLOps | 14 |
| 5 | Ingeniería de datos | 8 |
| 6 | Recomendadores | 7 |
| 7 | Ética, fairness, privacidad | 6 |
| 8 | Capstones | 4 |
| | **Total** | **197** |

Cada clase: `README.md` (ficha: objetivo, resultados, temas, prerrequisitos) + `notebook.ipynb` (stub con 8 celdas guía).

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
| Laboratorio Flask (local) | operativo |
| App Windows (Edge WebView2) | código operativo · binario pendiente de rebuild |
| App Android (Expo/React Native) | APK debug · pendiente migrar contenido embebido al índice actual |

---

## Señales de madurez

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

## Lo que este repositorio no vende

- una plataforma multiusuario endurecida para internet abierta;
- un LMS con autenticación, roles y seguimiento centralizado;
- **el currículo listo para dictar** — está en scaffold; el contenido por clase se desarrolla por bloques;
- la app Android en producción (APK debug, producción está en roadmap);
- personalización ilimitada antes de definir condiciones reales.

---

## Conclusiones que una evaluación justa puede sacar

- la **pauta cubre un currículo de Data Science avanzado y empleable en 2026** (incluye LLMs, MLOps real, inferencia causal, fairness — temas ausentes en programas más superficiales);
- existe coherencia entre contenido, laboratorio, distribución y documentación;
- la decisión de empezar por un scaffold completo antes de rellenar contenido evidencia capacidad de **diseñar el producto antes de implementarlo**;
- el valor no depende de una tecnología puntual sino de la mediación pedagógica y el criterio de diseño curricular.
