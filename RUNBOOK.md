# RUNBOOK

> Guía de operación diaria, smoke checks y recuperación básica para `python-data-science-bootcamp`.

---

## Arranque estándar

### App de escritorio Windows (usuarios finales)

Ejecutar directamente el binario distribuido:

```bat
BootcampPythonDS.exe
```

Abre una ventana nativa de Windows (Edge WebView2). No aparece consola, no se abre ningún navegador. Flask corre internamente en un puerto libre elegido automáticamente.

**Requisito en el PC del usuario:** Edge WebView2 Runtime — preinstalado en Windows 10 v2004+ y Windows 11.

### Modo desarrollo (desde el repositorio)

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python run_bootcamp.py
```

Levanta Flask en `http://127.0.0.1:8000` y abre el navegador automáticamente cuando el servidor responde `/health`. Ctrl+C para detener.

### Docker Compose

```powershell
docker compose up --build
```

### Docker endurecido

```powershell
docker compose -f docker-compose.prod.yml up -d --build
```

---

## Smoke checks mínimos

Los smoke checks aplican al modo desarrollo (puerto 8000) o Docker. En modo app de escritorio Windows, Flask corre en un puerto efímero elegido por el sistema; verificar usando las pruebas del repositorio.

### Health

```powershell
Invoke-WebRequest -UseBasicParsing http://127.0.0.1:8000/health
```

Respuesta esperada: `{"service": "python-data-science-bootcamp", "status": "ok"}`

### Readiness

```powershell
Invoke-WebRequest -UseBasicParsing http://127.0.0.1:8000/ready
```

Respuesta esperada: `{"classes": 13, "notebooks": 6, "status": "ready", ...}`

### Catálogo de clases

```powershell
Invoke-WebRequest -UseBasicParsing http://127.0.0.1:8000/api/classes
```

Debe devolver array de 13 objetos con `slug`, `title`, `path`.

### Ejecución básica

```powershell
Invoke-WebRequest -UseBasicParsing -Method Post `
  -ContentType 'application/json' `
  -Body '{"notebook_id":"smoke","code":"2+2"}' `
  http://127.0.0.1:8000/api/execute
```

Respuesta esperada: `{"error": null, "images": [], "result": "4", "stdout": ""}`

### Ejecución con pandas y matplotlib

```powershell
Invoke-WebRequest -UseBasicParsing -Method Post `
  -ContentType 'application/json' `
  -Body '{"notebook_id":"smoke2","code":"import pandas as pd; print(pd.__version__)"}' `
  http://127.0.0.1:8000/api/execute
```

---

## Validaciones del repositorio

```powershell
.\.venv\Scripts\python.exe -m pytest                        # suite completa
.\.venv\Scripts\python.exe -m ruff check .                  # lint
.\.venv\Scripts\python.exe -m bandit -r app run_bootcamp.py launcher.py -x app/saved_notebooks
```

---

## Build de distribución

```bat
build_windows.bat
```

Genera:
- `dist/BootcampPythonDS/BootcampPythonDS.exe` — ejecutable principal
- `release_artifacts/BootcampPythonDS_windows_portable_v1.0.0.zip` — portable (ZIP)
- `dist_installer/BootcampPythonDS_Setup_v1.0.0.exe` — instalador (requiere Inno Setup 6)

Ver [docs/BUILD_INSTALLER.md](docs/BUILD_INSTALLER.md) para detalle completo.

---

## Incidentes comunes

| Incidente | Qué revisar |
|---|---|
| App de escritorio no abre ventana | verificar Edge WebView2 Runtime instalado en Windows |
| App de escritorio muestra pantalla de error | Flask interno falló; ejecutar `python run_bootcamp.py` para ver el error |
| Modo dev: app no levanta | validar dependencias con `pip install -r requirements.txt` |
| Modo dev: puerto 8000 ocupado | cambiar `BOOTCAMP_PORT=XXXX` antes de lanzar |
| Runner queda colgado | la celda superó el timeout de 30s; usar `POST /api/reset` desde la UI |
| No guarda notebooks | revisar permisos sobre `app/saved_notebooks/` (modo dev) o junto al .exe (modo desktop) |
| Docker expone mal el puerto | confirmar mapeo `127.0.0.1:8000:8000` en compose |
| GitHub Pages no se publica | confirmar que el workflow corre sobre `master` y que `site/` existe |
| Build PyInstaller falla | asegurar que `pywebview` está instalado: `pip install pywebview` |

---

## Apagado

### App de escritorio Windows

Cerrar la ventana normalmente. Flask daemon se detiene con el proceso principal.

### Modo desarrollo

Ctrl+C en la terminal donde corre `python run_bootcamp.py`.

### Docker

```powershell
docker compose down
docker compose -f docker-compose.prod.yml down
```

---

## Recuperación básica

- si el runner queda en estado inconsistente, usar `POST /api/reset` desde la UI o reiniciar la app;
- si el contenido en `app/saved_notebooks/` no se necesita, eliminarlo manualmente;
- si cambia el material de clases, volver a ejecutar smoke checks de `/ready` y `/api/classes`;
- si falla un smoke check después de cambios de código, revisar `pytest` y los logs del servidor.

---

## Variables de entorno disponibles (modo desarrollo y Docker)

| Variable | Default | Descripción |
|---|---|---|
| `BOOTCAMP_HOST` | `127.0.0.1` | dirección de escucha del servidor |
| `BOOTCAMP_PORT` | `8000` | puerto del servidor |

En modo app de escritorio Windows (`BootcampPythonDS.exe`), estas variables son gestionadas internamente y no es necesario configurarlas.
