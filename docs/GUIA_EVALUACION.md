# 🧾 Guía de evaluación rápida

> **Audiencia:** institución, evaluador técnico, reclutador, docente externo.  
> **Tiempo estimado:** 10 minutos para el recorrido ejecutivo · 30 minutos para el técnico.

---

## ⚡ Executive summary

Este repositorio es un **curso completo de Python y Data Science** — no un repo de diapositivas ni un esqueleto vacío.

```
31 clases  ·  13 módulos  ·  30 notebooks  ·  6 datasets  ·  31 PDFs  ·  31 PPTXs
```

Incluye laboratorio interactivo local (Flask), app de escritorio nativa para Windows, app Android y una familia documental que distingue producto, operación y seguridad.

---

## 🔍 Lo que demuestra hoy

| Área | Evidencia concreta | Dónde verla |
|---|---|---|
| 📐 Diseño pedagógico completo | 31 clases con teoría, ejercicios, tarea, preguntas, notebook y soluciones | `classes/` |
| 🧪 Laboratorio operativo | Flask local con ejecución Python en tiempo real y captura de gráficos | `app/` → `python run_bootcamp.py` |
| 🖥️ Distribución de escritorio | App nativa Windows con Edge WebView2, sin navegador, sin Python instalado | `installer/` · `launcher.py` |
| 📱 Distribución móvil | App Android Expo/React Native con 31 clases embebidas + Google Colab | `mobile/` |
| 🌐 Portal público funcional | GitHub Pages con portal del alumno + vista institucional | `site/` |
| 📄 Materiales impresos | 31 PDFs guía-explicativa + 31 PPTXs presentación, uno por clase | `docs/pdfs/classes/` · `docs/presentaciones/classes/` |
| 🔒 Postura de seguridad | Validación de slugs, timeout de ejecución, CSP estricto, sin CDN externas | `SECURITY.md` · `app/app.py` |
| ⚙️ CI/CD activo | Tests + lint + build de contenedor + SAST en GitHub Actions | `.github/workflows/` |
| 📚 Documentación auditada | Arquitectura, operación, pedagogía y seguridad como documentos separados | `docs/` |

---

## 🗺️ Recorrido de 10 minutos

```
1. README.md               → qué es, estado, superficies, inicio rápido
2. RECRUITER.md            → evidencia técnica rápida sin leer código
3. docs/CATALOGO_PRODUCTO.md → qué superficies existen y qué entrega cada una hoy
4. docs/ARQUITECTURA_PRODUCTO.md → capas, diagramas de flujo, fronteras
5. SECURITY.md             → qué está protegido y qué límites se declaran
```

---

## 📦 Inventario real del producto

### Clases y materiales

| Grupo | Clases | Archivos por clase |
|---|---|---|
| Diagnóstico | 00 | README · slides · teoria · ejercicios · homework · PDF · PPTX |
| Contenido base | 01–12 | README · slides · teoria · ejercicios · homework · notebook · soluciones · PDF · PPTX |
| Contenido avanzado | 13–30 | todo lo anterior + preguntas · tecnologias · guia-codigo |

### Datasets sintéticos

| Dataset | Descripción | Clases que lo usan |
|---|---|---|
| ventas_tienda.csv | Ventas multitienda con categorías y medios de pago | 01–05 · 07 · 09 · 11 |
| retencion_clientes.csv | Serie mensual de altas, bajas e ingresos | 03 · 08 · 10 |
| soporte_tickets.csv | Tickets por categoría, prioridad y canal | 02 · 06 |
| transporte.csv | Viajes con origen, destino y retrasos | 04 · 06 |
| estudiantes.csv | Registro académico con asistencia y evaluaciones | 04 · 09 · 10 |
| comentarios_productos.csv | 100 reseñas en español con etiqueta de sentimiento | 26 (NLP) |

### Distribuciones disponibles

| Superficie | Estado |
|---|---|
| 🌐 Portal del alumno (GitHub Pages) | operativo |
| 🏛️ Vista institucional (GitHub Pages) | operativo |
| 🧪 Laboratorio Flask (local) | operativo |
| 🖥️ App Windows (Edge WebView2) | v1.0.0 · listo para build |
| 📱 App Android (Expo/React Native) | v1.0.0 · APK debug disponible |

---

## ✅ Señales de madurez

| Señal | Dónde se ve |
|---|---|
| Rutas por audiencia | [INDEX.md](INDEX.md) |
| Fuente de verdad del producto | [CATALOGO_PRODUCTO.md](CATALOGO_PRODUCTO.md) |
| Arquitectura con diagramas Mermaid | [ARQUITECTURA_PRODUCTO.md](ARQUITECTURA_PRODUCTO.md) |
| Operación reproducible y smoke checks | [../RUNBOOK.md](../RUNBOOK.md) |
| Seguridad declarada y honesta | [../SECURITY.md](../SECURITY.md) |
| CI/CD visible y rastreable | `.github/workflows/` |
| Historial de cambios | [../CHANGELOG.md](../CHANGELOG.md) |
| Capa pública no técnica | `site/` · `site/product/` |

---

## 🚧 Lo que este repositorio no vende

- una plataforma multiusuario endurecida para internet abierta;
- un LMS con autenticación, roles y seguimiento centralizado;
- la app Android en producción (APK debug, producción está en roadmap);
- personalización ilimitada antes de definir condiciones reales;
- profundidad total en cada dirección desde la primera versión.

---

## 💡 Conclusiones que una evaluación justa puede sacar

- hay una forma de trabajo sostenida, no solo una clase aislada;
- existe coherencia entre contenido, laboratorio, distribución y documentación;
- el currículo cubre el recorrido completo de un Data Scientist — desde Python hasta despliegue;
- el producto puede arrancar acotado y crecer sin rehacerse;
- el valor no depende de una tecnología puntual sino de la mediación pedagógica y el criterio de diseño.
