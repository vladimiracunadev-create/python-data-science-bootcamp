<div align="center">

# 🛠️ RUNBOOK

### **Operación diaria · Smoke checks · Recuperación básica**

[![Health](https://img.shields.io/badge/endpoints-%2Fhealth%20%2Fready-3fb950?style=for-the-badge)](#-smoke-checks-m%C3%ADnimos)
[![Local](https://img.shields.io/badge/host-127.0.0.1-7c5cff?style=for-the-badge)](#variables-de-entorno-disponibles-modo-desarrollo-y-docker)

</div>

---

## 🚀 Arranque estándar

### 🖥️ App de escritorio Windows (usuarios finales)

Ejecutar directamente el binario distribuido:

```bat
PythonDSProgram.exe
```

Abre una ventana Qt nativa (PySide6). No aparece consola, no se abre ningún navegador, no se levanta servidor HTTP ni se reserva puerto local.

**Requisitos en el PC del usuario:** ninguno — el bundle PyInstaller incluye PySide6 + Qt completos. No requiere Python, Edge WebView2 ni runtime adicional.

### 🐍 Modo desarrollo (desde el repositorio)

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python run_program.py
```

Levanta Flask en `http://127.0.0.1:8000` y abre el navegador automáticamente cuando el servidor responde `/health`. Ctrl+C para detener.

### 🐳 Docker Compose

```powershell
docker compose up --build
```

### 🛡️ Docker endurecido

```powershell
docker compose -f docker-compose.prod.yml up -d --build
```

---

## 🩺 Smoke checks mínimos

Los smoke checks aplican al **laboratorio de ejecución Python** (modo desarrollo en puerto 8000 o Docker). La app Windows nativa (`PythonDSProgram.exe`) **no levanta servidor HTTP**, no tiene endpoints — para verificarla, abrir el ejecutable y comprobar que el QTreeView lista las 9 partes y abre una clase.

### 💚 Health

```powershell
Invoke-WebRequest -UseBasicParsing http://127.0.0.1:8000/health
```

Respuesta esperada: `{"service": "python-data-science-program", "status": "ok"}`

### ✅ Readiness

```powershell
Invoke-WebRequest -UseBasicParsing http://127.0.0.1:8000/ready
```

Respuesta esperada: `{"classes": 232, "notebooks": 6, "status": "ready", ...}`

### 📚 Catálogo de clases

```powershell
Invoke-WebRequest -UseBasicParsing http://127.0.0.1:8000/api/classes
```

Debe devolver array de 232 objetos con `slug`, `title`, `path`.

### ⚡ Ejecución básica

```powershell
Invoke-WebRequest -UseBasicParsing -Method Post `
  -ContentType 'application/json' `
  -Body '{"notebook_id":"smoke","code":"2+2"}' `
  http://127.0.0.1:8000/api/execute
```

Respuesta esperada: `{"error": null, "images": [], "result": "4", "stdout": ""}`

### 📊 Ejecución con pandas y matplotlib

```powershell
Invoke-WebRequest -UseBasicParsing -Method Post `
  -ContentType 'application/json' `
  -Body '{"notebook_id":"smoke2","code":"import pandas as pd; print(pd.__version__)"}' `
  http://127.0.0.1:8000/api/execute
```

---

## 🧪 Validaciones del repositorio

```powershell
.\.venv\Scripts\python.exe -m pytest                        # suite completa
.\.venv\Scripts\python.exe -m ruff check .                  # lint
.\.venv\Scripts\python.exe -m bandit -r app run_program.py launcher.py -x app/saved_notebooks
```

---

## 📦 Build de distribución

```bat
build_windows.bat
```

Genera:
- 💾 `dist/PythonDSProgram/PythonDSProgram.exe` — ejecutable principal (Qt nativo)
- 🗜️ `release_artifacts/PythonDSProgram_windows_portable_v3.10.0.zip` — portable (ZIP, ~273 MB)
- 📦 `dist_installer/PythonDSProgram_Setup_v3.10.0.exe` — instalador (requiere Inno Setup 6; no se incluyó en el release v3.10.0 porque no había Inno Setup en el entorno de build)

> 📖 Ver [docs/BUILD_INSTALLER.md](docs/BUILD_INSTALLER.md) para detalle completo.

---

## 🚨 Incidentes comunes

| ⚠️ Incidente | 🔍 Qué revisar |
|---|---|
| 🖥️ App Windows nativa no abre ventana | revisar logs en consola corriendo `python launcher.py` desde el repo para ver el error de Qt/PySide6 |
| ❌ App Windows muestra una clase vacía | verificar que `classes/` se incluyó en el bundle PyInstaller (`program.spec`, sección `datas`) |
| 🐍 Modo dev: app no levanta | validar dependencias con `pip install -r requirements.txt` |
| 🔌 Modo dev: puerto 8000 ocupado | cambiar `PROGRAM_PORT=XXXX` antes de lanzar |
| ⏱️ Runner queda colgado | la celda superó el timeout de 30s; usar `POST /api/reset` desde la UI |
| 💾 No guarda notebooks | revisar permisos sobre `app/saved_notebooks/` (modo dev) o junto al .exe (modo desktop) |
| 🐳 Docker expone mal el puerto | confirmar mapeo `127.0.0.1:8000:8000` en compose |
| 🌐 GitHub Pages no se publica | confirmar que el workflow corre sobre `master` y que `site/` existe |
| 📦 Build PyInstaller falla | asegurar que PySide6 está instalado: `pip install "PySide6>=6.6"` |

---

## 🛑 Apagado

### 🖥️ App Windows nativa

Cerrar la ventana Qt normalmente. El proceso PySide6 se cierra limpio (no hay Flask ni hilos daemon que apagar).

### 🐍 Modo desarrollo

`Ctrl+C` en la terminal donde corre `python run_program.py`.

### 🐳 Docker

```powershell
docker compose down
docker compose -f docker-compose.prod.yml down
```

---

## 🩹 Recuperación básica

- 🔄 si el runner queda en estado inconsistente, usar `POST /api/reset` desde la UI o reiniciar la app;
- 🧹 si el contenido en `app/saved_notebooks/` no se necesita, eliminarlo manualmente;
- ✅ si cambia el material de clases, volver a ejecutar smoke checks de `/ready` y `/api/classes`;
- 📋 si falla un smoke check después de cambios de código, revisar `pytest` y los logs del servidor.

---

## 🔧 Variables de entorno disponibles (modo desarrollo y Docker)

| 🔤 Variable | 📌 Default | 📝 Descripción |
|---|---|---|
| `PROGRAM_HOST` | `127.0.0.1` | 🌐 dirección de escucha del servidor |
| `PROGRAM_PORT` | `8000` | 🔌 puerto del servidor |

> 🖥️ La app Windows nativa (`PythonDSProgram.exe`) no usa estas variables: no levanta servidor HTTP.
