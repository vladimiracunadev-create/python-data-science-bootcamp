# 🧪 Laboratorio de ejecución Python (Flask + kernel Jupyter)

> Descripción técnica del laboratorio local: modos de ejecución, componentes, sesiones y límites operativos.
>
> ⚠️ Esta página describe el **laboratorio** (`app/`, Flask + jupyter_client + ipykernel), que es **herramienta separada** de la **app Windows nativa** (`launcher.py` + `app_desktop/`, PySide6 / Qt). La app nativa no levanta servidor HTTP — para esa superficie ver [BUILD_INSTALLER.md](BUILD_INSTALLER.md).

---

## 🎯 Objetivo

El entorno interactivo permite que el programa no dependa de notebooks estáticos. El mismo repositorio sirve como:

- base de planificación pedagógica (clases, teoría, slides);
- laboratorio por celdas con persistencia de sesión (tipo Jupyter/Colab);
- runner rápido para probar fragmentos de código en vivo;
- visualizador de gráficos matplotlib inline;
- espacio de guardado de notebooks por alumno.

---

## 🚦 Modos de ejecución

### 🐍 Modo 1: Desarrollo desde el repositorio

```bash
python run_program.py
```

- Levanta Flask en `http://127.0.0.1:8000`
- Detecta si el puerto está ocupado
- Espera que `/health` responda antes de abrir el navegador
- Abre el navegador del sistema automáticamente
- Ctrl+C para detener

### 🐳 Modo 2: Docker

```bash
docker compose up --build
# o endurecido:
docker compose -f docker-compose.prod.yml up -d --build
```

Acceder en `http://127.0.0.1:8000`.

---

## 🧩 Componentes del laboratorio

### 📚 Vista de clases

El laboratorio descubre las 232 clases del currículo recorriendo `classes/parte-*/NNN-*/`. Por cada clase carga:

| Sección | Archivo fuente | Descripción |
|---|---|---|
| Ficha pedagógica | `README.md` | Objetivos, resultados, temas, Definiciones, Errores comunes, FAQ, referencias |
| Notebook ejecutable | `notebook.ipynb` | Cuaderno v3.0 (self-contained, seed 42, try/except sobre libs pesadas) |
| Material descargable | `clase-NNN-...-guia-explicativa.pdf` + `clase-NNN-...-presentacion.pptx` | Linkeados desde la ficha |

El Markdown se convierte a HTML en el servidor con extensiones `fenced_code`, `tables` y `codehilite`.

### 📓 Cuaderno interactivo (tipo Jupyter)

- celdas de código Python editables, ejecutables con `Ctrl+Enter`;
- cada celda mantiene su salida (stdout, resultado, gráficos, errores);
- el estado se **comparte entre celdas** de la misma sesión (variables persisten);
- 6 notebooks precargados en `app/notebooks/`:

| Notebook | Contenido |
|---|---|
| `python_basics_lab` | variables, listas, funciones, clasificación básica |
| `pandas_lab` | carga de CSV, filtros, agrupaciones |
| `visualizacion_lab` | gráficos con matplotlib y pandas |
| `ml_intro_lab` | regresión lineal, métricas de evaluación |
| `clasificacion_lab` | árboles de decisión, regresión logística, matriz de confusión |
| `pipelines_lab` | Pipeline sklearn, GridSearchCV, cross-validation |

### ⚡ Runner rápido

- área de texto libre para código Python;
- `Ctrl+Enter` para ejecutar;
- sesión separada de los notebooks (no comparte variables);
- útil para resolver dudas en vivo o probar ideas cortas.

### 💾 Guardado de notebooks

- botón de guardado en la UI → `POST /api/notebook/save`;
- auto-guardado cada 30 segundos de inactividad;
- se persiste en JSON dentro del directorio `saved_notebooks/`;
- en modo app de escritorio: junto al `.exe`; en modo dev: dentro de `app/saved_notebooks/`.

---

## ▶️ Motor de ejecución — detalles técnicos

### 🎬 Sesiones

| Parámetro | Valor |
|---|---|
| Sesiones concurrentes máximas | 100 |
| TTL por sesión | 1 hora sin actividad |
| Eviction | automática al crear nueva sesión cuando hay más de 100 |

Cada sesión arranca su propio **kernel Jupyter real** (`jupyter_client` + `ipykernel`). Las variables definidas en una celda están disponibles en las siguientes de la misma sesión. El kernel soporta `interrupt` (Ctrl-C lógico) y `restart` desde la UI.

### 🚧 Ejecución y límites

| Parámetro | Valor |
|---|---|
| Timeout por celda | 30 segundos |
| Longitud máxima de código | 20 000 caracteres |
| Tamaño máximo de payload | 1 MB |

Si una celda supera el timeout, la sesión se reinicia automáticamente y se devuelve un mensaje de error.

### 📦 Stack disponible en el kernel

El kernel Jupyter del lab tiene preinstalado el stack completo del currículo (vía `requirements.txt`): numpy, pandas, polars, matplotlib, seaborn, plotly, scikit-learn, xgboost, lightgbm, statsmodels, torch (CPU), transformers, sentence-transformers, faiss-cpu, fairlearn, jupyter_client, ipykernel, etc. Todo se importa explícitamente desde las celdas como en un Jupyter normal.

### 🖼️ Captura de salida

El kernel devuelve outputs estilo Jupyter por el protocolo IOPub:

| Tipo de salida | Cómo se captura |
|---|---|
| `print()` / stdout / stderr | mensajes `stream` del kernel |
| Resultado de expresión | mensajes `execute_result` con `data` (text/plain, text/html, image/png) |
| `display(...)` (HTML, DataFrames, imágenes) | mensajes `display_data` |
| Gráficos matplotlib | `image/png` base64 inline (matplotlib inline backend) |
| Errores / excepciones | mensajes `error` con `ename`, `evalue` y `traceback` |

---

## 🔌 API del laboratorio

| Método | Ruta | Descripción |
|---|---|---|
| `GET` | `/` | Interfaz web principal |
| `GET` | `/health` | Liveness probe: `{"status": "ok"}` |
| `GET` | `/ready` | Readiness: incluye count de clases y notebooks |
| `GET` | `/api/curriculum` | Árbol del currículo (🎓 232 clases · 232/232 notebooks ejecutables · `has_notebook: true` en el 100% del currículo) |
| `GET` | `/api/notebook/<slug>` | Contenido del `classes/**/notebook.ipynb` real |
| `POST` | `/api/kernel/start` | Arranca un kernel Jupyter para una sesión |
| `POST` | `/api/kernel/<id>/execute` | Ejecuta código en el kernel (outputs ricos: HTML/imágenes/errores) |
| `POST` | `/api/kernel/<id>/interrupt` | Interrumpe el kernel (Ctrl-C lógico) |
| `POST` | `/api/kernel/<id>/restart` | Reinicia el kernel preservando la sesión |
| `DELETE` | `/api/kernel/<id>` | Cierra y libera el kernel |

---

## 🚧 Límites de diseño

- el runner ejecuta código Python arbitrario del alumno dentro del proceso de la app;
- el timeout de 30s reduce el riesgo de bloqueos pero no reemplaza un sandbox real de OS;
- el entorno está pensado para **uso local y controlado** (aula, máquina del docente);
- no exponer el puerto a internet sin proxy con autenticación y TLS;
- ver [SECURITY.md](../SECURITY.md) para la postura completa y los riesgos aceptados.
