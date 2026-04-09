# 📝 Changelog

Todos los cambios notables de este proyecto se documentan aquí.

El formato sigue [Keep a Changelog](https://keepachangelog.com/es/1.0.0/).
El versionado sigue [Semantic Versioning](https://semver.org/lang/es/).

---

## [v1.0.0] — 2026-04-09

Primera versión operativa y publicada como release oficial.

### Añadido

**App de escritorio Windows:**
- `launcher.py` reescrito con pywebview 6.1 — abre una ventana nativa de Windows (Edge WebView2) sin abrir el navegador del sistema
- puerto libre elegido automáticamente (no hardcodeado), elimina conflictos de red
- pantalla de carga animada mientras Flask interno inicia
- página de error en ventana si el servidor no responde en 45 segundos
- `run_bootcamp.py` mejorado — detecta puerto ocupado, espera health, abre navegador automáticamente, maneja Ctrl+C

**Build:**
- `bootcamp.spec` actualizado con `collect_all('webview')` para bundlear pywebview correctamente
- `console=False` en el spec — elimina la ventana negra de consola al lanzar el .exe
- `build_windows.bat` instala pywebview automáticamente, genera ZIP portable con PowerShell
- favicon SVG inline en `index.html` — elimina 404 en cada carga

**Seguridad:**
- CSP endurecida: eliminada dependencia de Google Fonts CDN externo
- `# nosec B310` y `# nosec B110` justificados en los polling loops de health check
- Bandit: 0 High, 0 Medium, 0 Low en el escaneo completo

**Documentación:**
- `README.md` actualizado — refleja app de escritorio, rutas por perfil, mapa documental completo
- `RUNBOOK.md` actualizado — incluye arranque en modo desktop, smoke checks, variables de entorno
- `SECURITY.md` reescrito — superficies por modo, tabla de protecciones detallada, versiones soportadas
- `docs/BUILD_INSTALLER.md` reescrito — arquitectura actualizada, WebView2 requirement, troubleshooting
- `docs/CATALOGO_PRODUCTO.md` actualizado — corrección de descripción del instalador Windows
- `docs/entorno-interactivo.md` reescrito — describe ambos modos (desktop + dev)
- `docs/ARQUITECTURA_PRODUCTO.md` actualizado — app de escritorio en diagramas
- `docs/INDEX.md` actualizado — incluye nuevos archivos estándar
- `LICENSE` completado con texto MIT completo + clarificaciones sobre componentes
- Creados: `RECRUITER.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `ROADMAP.md`

**Correcciones:**
- `app/app.py`: `_get_base_dir()` con soporte `sys._MEIPASS` para PyInstaller frozen mode
- `app/templates/index.html`: eliminado Google Fonts (requería conexión a internet)
- `app/static/styles.css`: fuentes del sistema (`Segoe UI, system-ui`) en lugar de Google Fonts

### Artefactos de release

| Artefacto | Tamaño | SHA256 |
|---|---|---|
| `BootcampPythonDS_windows_portable_v1.0.0.zip` | 92 MB | `239d2261...` |
| `BootcampPythonDS_android_v1.0.0_debug.apk` | 137 MB | `cb69408b...` |

Build: Python 3.12 · PyInstaller 6.19 · pywebview 6.1 · commit `487b229`

---

## [pre-v1.0.0] — 2026-04-08 (scaffolding inicial)

> Versiones de construcción — no publicadas como release. Documentadas aquí por completitud.

### Incluido en la construcción inicial

- Curriculum completo: clase 0 diagnóstica + clases 01–12 con teoría, slides, ejercicios, tarea, notebook y soluciones
- Laboratorio Flask con 10 rutas (clases, notebooks, ejecución, guardado, reset, health, ready)
- Motor de ejecución con sesiones persistentes, timeout, eviction y captura de matplotlib
- 6 notebooks interactivos en JSON para el laboratorio web
- 5 datasets sintéticos (CSV)
- Portal del alumno en `site/` + vista institucional en `site/product/`
- App Android (Expo/React Native) en `mobile/` con scaffold Android nativo
- 3 workflows de CI/CD (tests, security, deploy-pages)
- 4 módulos de tests (pytest)
- Documentación inicial: 19 documentos en `docs/`
- Dockerfile + docker-compose (dev y prod)
- Scripts de build y generación de PDFs

---

[v1.0.0]: https://github.com/vladimiracunadev-create/python-data-science-bootcamp/releases/tag/v1.0.0
