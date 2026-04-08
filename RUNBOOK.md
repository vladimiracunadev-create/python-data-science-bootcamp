# 🛠 RUNBOOK

> Guía de operación diaria, smoke checks y recuperacion básica para `python-data-science-bootcamp`.

## ▶ Arranque estandar

### 🐍 Entorno virtual

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python run_bootcamp.py
```

### 🐳 Docker Compose

```powershell
docker compose up --build
```

### 🛡 Compose endurecido

```powershell
docker compose -f docker-compose.prod.yml up -d --build
```

## ✅ Smoke checks minimos

### ❤️ Health

```powershell
Invoke-WebRequest -UseBasicParsing http://127.0.0.1:8000/health
```

### 🟢 Readiness

```powershell
Invoke-WebRequest -UseBasicParsing http://127.0.0.1:8000/ready
```

### 📚 Clase disponible

```powershell
Invoke-WebRequest -UseBasicParsing http://127.0.0.1:8000/api/classes
```

### ⚙ Ejecución básica

```powershell
Invoke-WebRequest -UseBasicParsing -Method Post -ContentType 'application/json' -Body '{"notebook_id":"smoke","code":"2+2"}' http://127.0.0.1:8000/api/execute
```

## 🔁 Validaciónes de repo

```powershell
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m pip install ruff
.\.venv\Scripts\python.exe -m ruff check .
```

## 🚨 Incidentes comunes

| Incidente | Qué revisar |
|---|---|
| La app no levanta | validar `BOOTCAMP_HOST`, `BOOTCAMP_PORT` y dependencias instaladas |
| El runner queda colgado | verificar timeout y reiniciar sesión desde la UI o `POST /api/reset` |
| No guarda notebooks | revisar permisos sobre `app/saved_notebooks` |
| Docker expone mal el puerto | confirmar mapeo `127.0.0.1:8000:8000` |
| GitHub Pages no se publica | confirmar que el workflow corre sobre `master` o `main` y que `site/` existe |

## ⏹ Apagado

### 💻 Proceso local

Detener la terminal donde corre `python run_bootcamp.py`.

### 🐳 Docker

```powershell
docker compose down
docker compose -f docker-compose.prod.yml down
```

## 🧯 Recuperacion básica

- si el runner queda en estado inconsistente, reiniciar la sesión del notebook o reiniciar la app;
- si el contenido guardado en `app/saved_notebooks` no se necesita, eliminarlo manualmente;
- si cambia el material de clases, volver a ejecutar smoke checks de `/ready` y `/api/classes`.
