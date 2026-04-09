# 🧪 Entorno interactivo del Bootcamp

> Descripción técnica del laboratorio local: modos de ejecución, componentes, sesiones y límites operativos.

---

## Objetivo

El entorno interactivo permite que el bootcamp no dependa de notebooks estáticos. El mismo repositorio sirve como:

- base de planificación pedagógica (clases, teoría, slides);
- laboratorio por celdas con persistencia de sesión (tipo Jupyter/Colab);
- runner rápido para probar fragmentos de código en vivo;
- visualizador de gráficos matplotlib inline;
- espacio de guardado de notebooks por alumno.

---

## Modos de ejecución

### Modo 1: App de escritorio Windows (distribución para alumnos)

```bat
BootcampPythonDS.exe
```

- Abre una **ventana nativa de Windows** usando pywebview + Edge WebView2
- Flask corre internamente en un **puerto libre elegido automáticamente**
- El usuario nunca ve localhost, no se abre ningún navegador
- Pantalla de carga animada mientras el entorno inicia
- Sin Python instalado requerido en el PC del usuario

**Requisito del sistema:** Edge WebView2 Runtime (preinstalado en Windows 10 v2004+ y Windows 11).

### Modo 2: Desarrollo desde el repositorio

```bash
python run_bootcamp.py
```

- Levanta Flask en `http://127.0.0.1:8000`
- Detecta si el puerto está ocupado
- Espera que `/health` responda antes de abrir el navegador
- Abre el navegador del sistema automáticamente
- Ctrl+C para detener

### Modo 3: Docker

```bash
docker compose up --build
# o endurecido:
docker compose -f docker-compose.prod.yml up -d --build
```

Acceder en `http://127.0.0.1:8000`.

---

## Componentes del laboratorio

### Vista de clases

Renderiza el contenido de las 13 clases directamente desde `classes/`:

| Sección | Archivo fuente | Descripción |
|---|---|---|
| Descripción general | `README.md` | Título, objetivos y contexto de la clase |
| Teoría | `teoria.md` | Conceptos fundamentales |
| Slides | `slides.md` | Pauta para el instructor |
| Ejercicios | `ejercicios.md` | Práctica guiada en clase |
| Tarea | `homework.md` | Trabajo fuera del aula |
| Quiz diagnóstico | `quiz.json` | Solo clase 00 — 30 preguntas, autocorregido |

El Markdown se convierte a HTML en el servidor con extensiones `fenced_code`, `tables` y `codehilite`.

### Cuaderno interactivo (tipo Jupyter)

- celdas de código Python editables, ejecutables con `Ctrl+Enter`;
- cada celda mantiene su salida (stdout, resultado, gráficos, errores);
- el estado se **comparte entre celdas** de la misma sesión (variables persisten);
- 6 notebooks precargados en `app/notebooks/`:

| Notebook | Contenido |
|---|---|
| `python_basics_lab` | variables, listas, funciones, clasificación básica |
| `pandas_bootcamp_lab` | carga de CSV, filtros, agrupaciones |
| `visualizacion_bootcamp_lab` | gráficos con matplotlib y pandas |
| `ml_intro_lab` | regresión lineal, métricas de evaluación |
| `clasificacion_lab` | árboles de decisión, regresión logística, matriz de confusión |
| `pipelines_lab` | Pipeline sklearn, GridSearchCV, cross-validation |

### Runner rápido

- área de texto libre para código Python;
- `Ctrl+Enter` para ejecutar;
- sesión separada de los notebooks (no comparte variables);
- útil para resolver dudas en vivo o probar ideas cortas.

### Guardado de notebooks

- botón de guardado en la UI → `POST /api/notebook/save`;
- auto-guardado cada 30 segundos de inactividad;
- se persiste en JSON dentro del directorio `saved_notebooks/`;
- en modo app de escritorio: junto al `.exe`; en modo dev: dentro de `app/saved_notebooks/`.

---

## Motor de ejecución — detalles técnicos

### Sesiones

| Parámetro | Valor |
|---|---|
| Sesiones concurrentes máximas | 100 |
| TTL por sesión | 1 hora sin actividad |
| Eviction | automática al crear nueva sesión cuando hay más de 100 |

Cada sesión tiene su propio namespace Python (`globals()`). Las variables definidas en una celda están disponibles en las siguientes de la misma sesión.

### Ejecución y límites

| Parámetro | Valor |
|---|---|
| Timeout por celda | 30 segundos |
| Longitud máxima de código | 20 000 caracteres |
| Tamaño máximo de payload | 1 MB |

Si una celda supera el timeout, la sesión se reinicia automáticamente y se devuelve un mensaje de error.

### Paquetes preimportados

Las siguientes librerías están disponibles sin importar explícitamente en cada celda:

```python
import math
import statistics
import pandas as pd
import matplotlib.pyplot as plt
```

El resto de las librerías disponibles (numpy, scikit-learn, etc.) deben importarse explícitamente.

### Captura de salida

| Tipo de salida | Cómo se captura |
|---|---|
| `print()` / stdout | redireccionado vía `contextlib.redirect_stdout` |
| Resultado de expresión | evaluado como `ast.Expression` separado |
| Gráficos matplotlib | convertidos a PNG base64 y devueltos en el JSON de respuesta |
| Errores / excepciones | `traceback.format_exc()` devuelto como string |

---

## API del laboratorio

| Método | Ruta | Descripción |
|---|---|---|
| `GET` | `/` | Interfaz web principal |
| `GET` | `/health` | Liveness probe: `{"status": "ok"}` |
| `GET` | `/ready` | Readiness: incluye count de clases y notebooks |
| `GET` | `/api/classes` | Lista de las 13 clases |
| `GET` | `/api/class/<slug>` | Contenido de una clase (HTML + quiz) |
| `GET` | `/api/notebooks` | Lista de templates disponibles |
| `GET` | `/api/notebook/<id>` | Contenido de un template |
| `POST` | `/api/notebook/save` | Guarda notebook del alumno |
| `POST` | `/api/execute` | Ejecuta código en una sesión |
| `POST` | `/api/reset` | Reinicia el estado de una sesión |

---

## Límites de diseño

- el runner ejecuta código Python arbitrario del alumno dentro del proceso de la app;
- el timeout de 30s reduce el riesgo de bloqueos pero no reemplaza un sandbox real de OS;
- el entorno está pensado para **uso local y controlado** (aula, máquina del docente);
- no exponer el puerto a internet sin proxy con autenticación y TLS;
- ver [SECURITY.md](../SECURITY.md) para la postura completa y los riesgos aceptados.
