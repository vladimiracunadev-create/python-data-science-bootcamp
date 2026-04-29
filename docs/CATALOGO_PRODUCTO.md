# 🧱 Catálogo del producto

> Fuente de verdad de superficies, artefactos y reglas de comunicación.  
> Si algún README, landing o presentación contradice este documento, **este tiene prioridad.**

---

## 🧭 Definiciones

| Término | Significado |
|---|---|
| **Superficie** | Forma concreta en que una audiencia interactúa con el producto |
| **Artefacto** | Archivo o salida reutilizable que apoya la evaluación, presentación u operación |
| **Ruta documental** | Documento canónico que ordena, explica o limita el producto |
| **Evolución** | Capacidad proyectada, pero no operativa hoy como pieza principal |

---

## 🧱 Matriz canónica de superficies

| Superficie | Tipo | Estado | Audiencia | Qué entrega hoy |
|---|---|---|---|---|
| 🧪 Laboratorio interactivo (`app/`) | núcleo operativo | operativo | docente / estudiante guiado | acceso a las 31 clases, notebooks editables, ejecución Python en tiempo real, captura de gráficos, guardado local |
| 🖥️ App de escritorio Windows (`launcher.py` + `installer/`) | distribución de escritorio | listo para build | alumno / docente en aula | ventana nativa Edge WebView2 sin navegador, sin Python instalado en el equipo del usuario, Flask interno transparente |
| 📱 App Android (`mobile/`) | distribución móvil | listo para build | alumno en movimiento | 31 clases embebidas, código documentado, apertura en Google Colab, seguimiento de progreso local |
| 🌐 Portal del alumno (`site/`) | superficie pública | operativo | alumno | enlace oficial, ruta de inicio, recursos y reglas de uso |
| 🏛️ Vista institucional (`site/product/`) | superficie pública | operativo | institución / evaluador | narrativa del producto, alcance, arquitectura visual y crecimiento posible |
| 📂 Curriculum modular (`classes/`) | base pedagógica | operativo | docente / alumno | clase 00 diagnóstica + 30 clases en 13 módulos: Python, NumPy, SQL, visualización (matplotlib + seaborn), estadística descriptiva e inferencial, feature engineering, regresión, árboles/RF, Gradient Boosting, clustering, PCA, series de tiempo, ajuste de hiperparámetros, NLP, detección de anomalías, ética, redes neuronales, despliegue con Flask |
| 📚 Kit documental (`docs/`) | capa editorial | operativo | docente / stakeholder | metodología, operación, evaluación, seguridad y arquitectura |
| 📄 PDFs (`docs/pdfs/`) | artefacto de apoyo | operativo | docente / alumno / evaluador | 31 guías explicativas por clase + 2 guías de estudio adicionales |
| 📊 Presentaciones (`docs/presentaciones/`) | artefacto de apoyo | operativo | docente | 31 decks `.pptx` listos para exposición, uno por clase |

---

## ⚙️ Funcionalidad real por superficie

| Capacidad | Lab Flask | App Windows | App Android | Portal alumno | Vista institucional |
|---|---|---|---|---|---|
| Ver contenido de las 31 clases | ✅ | ✅ (embebido) | ✅ (embebido) | ❌ | ❌ |
| Ejecutar código Python | ✅ (runner local) | ✅ (runner local) | ↗️ Google Colab | ❌ | ❌ |
| Leer código comentado | ✅ | ✅ | ✅ | ❌ | ❌ |
| Abrir en Colab | ❌ | ❌ | ✅ | ❌ | ❌ |
| Guardar notebooks | ✅ | ✅ | ❌ | ❌ | ❌ |
| Seguimiento de progreso | ❌ | ❌ | ✅ (local) | ❌ | ❌ |
| Mostrar producto a terceros | parcial | ❌ | ❌ | parcial | ✅ |
| Operar sin internet | ✅ | ✅ | ✅ (contenido) | ❌ | ❌ |
| Sin Python instalado | ❌ | ✅ | ✅ | ✅ | ✅ |

---

## 📦 Artefactos oficiales de apoyo

| Artefacto | Rol | Estado |
|---|---|---|
| `docs/pdfs/classes/clase-NN-*-guia-explicativa.pdf` (×31) | guía imprimible por clase con teoría, ejercicios y preguntas | vigente |
| `docs/presentaciones/classes/clase-NN-*-presentacion.pptx` (×31) | deck de presentación por clase con esquema teal corporativo | vigente |
| `docs/pdfs/guia-estudio-repositorio.pdf` | ruta de lectura rápida del repo para evaluador técnico | vigente |
| `docs/pdfs/guia-total-python-data-science.pdf` | guía ampliada de Python con Data Science investigada con fuentes oficiales | vigente |
| `scripts/generate_class_docs.py` | generación reproducible de PDFs y PPTXs para clases 13–30 | vigente |
| `scripts/generate_class_assets.py` | generación de assets por clase | vigente |
| `scripts/generate_extended_study_pdf.py` | regeneración de la guía ampliada | vigente |

---

## 🗣️ Reglas de comunicación

### ✅ Lo que sí se puede afirmar

- el repo contiene un curso completo de Python y Data Science, no solo una landing;
- el laboratorio interactivo es operativo como herramienta local de aula;
- existen superficies públicas funcionales para alumno e institución;
- hay 31 PDFs guía y 31 PPTXs presentación, uno por clase;
- la propuesta puede arrancar acotada y crecer sin rehacer la base.

### ❌ Lo que no se debe mezclar

- el portal del alumno **no es** todo el producto;
- la vista institucional **no reemplaza** el laboratorio;
- los PDFs **no son** el producto — son artefactos derivados;
- la app Android **no ejecuta Python nativo** — usa Google Colab para ejecución;
- el instalador Windows es una app de escritorio real con ventana nativa — **no abre el navegador del sistema**;
- el runner local **no debe presentarse** como SaaS expuesto a internet.

---

## 🏫 Versión inicial sugerida para primeros pasos

La primera implementación no necesita usar todo el catálogo. Una versión acotada funcional:

1. fundamentos de Python (`classes/01`);
2. lectura de CSV con pandas (`classes/02`);
3. filtros y tablas resumen (`classes/02`–`03`);
4. visualización básica (`classes/03`–`05`);
5. mini proyecto guiado (`classes/07`);
6. presentación de hallazgos (`classes/08`).

Desde ahí, se puede extender módulo a módulo según el ritmo del grupo.

---

## 📌 Regla de prioridad

Si alguna presentación, README o landing contradice esta matriz, **este documento tiene prioridad.**
