# Guía: Build Windows — App de Escritorio

Genera el ejecutable Windows del Bootcamp Python DS como **aplicación de escritorio nativa**.
No se abre ningún navegador. La ventana es una app real de Windows.

---

## Qué genera este proceso

```
release_artifacts/
  BootcampPythonDS_windows_portable_v1.0.0.zip   ← portable (descomprimir y ejecutar)

dist_installer/
  BootcampPythonDS_Setup_v1.0.0.exe              ← instalador para alumno/docente

dist/BootcampPythonDS/
  BootcampPythonDS.exe                           ← ejecutable directo
  _internal/                                     ← runtime Python + dependencias
  app/templates/
  app/notebooks/
  classes/        ← curriculum completo embebido
  datasets/       ← datasets de práctica embebidos
  site/
```

---

## Arquitectura de la app de escritorio

```
BootcampPythonDS.exe
    |
    ├── Busca puerto libre automáticamente (no hay conflictos)
    ├── Arranca Flask interno en hilo daemon
    ├── Muestra ventana nativa con pantalla de carga
    ├── Espera /health hasta que Flask responde
    └── Carga la app en la ventana (Edge WebView2)
         — sin abrir ningún navegador externo
         — sin mostrar ninguna URL localhost al usuario

    ↓ PyInstaller (bootcamp.spec)
    dist/BootcampPythonDS/  (bundle con Python + pywebview embebidos)

    ↓ PowerShell Compress-Archive
    release_artifacts/BootcampPythonDS_windows_portable_v1.0.0.zip

    ↓ Inno Setup (installer/setup.iss)
    dist_installer/BootcampPythonDS_Setup_v1.0.0.exe
```

**Componentes clave:**

| Archivo | Rol |
|---|---|
| `launcher.py` | Punto de entrada del .exe — pywebview + Flask interno |
| `run_bootcamp.py` | Modo desarrollo — Flask + abre navegador (solo en repo) |
| `bootcamp.spec` | Especificación PyInstaller con `collect_all('webview')` |
| `installer/setup.iss` | Script Inno Setup para el instalador |
| `build_windows.bat` | Automatiza todo el proceso de build |

---

## Requisitos del entorno de build

| Herramienta | Versión mínima | Instalación |
|---|---|---|
| Python | 3.10 | python.org/downloads |
| pip | último | incluido con Python |
| pywebview | 4.0+ | `pip install pywebview` |
| PyInstaller | 6.0 | `pip install pyinstaller` |
| Inno Setup | 6.0 | jrsoftware.org/isinfo.php |
| Dependencias del repo | ver requirements.txt | `pip install -r requirements.txt` |

> El alumno/docente que usa el instalador **NO necesita Python ni ninguna dependencia**.
> El bundle incluye el runtime Python completo y el motor gráfico.

### Requisito en el PC del usuario final

**Edge WebView2 Runtime** — viene preinstalado en:
- Windows 10 versión 20H2 (octubre 2020) y posteriores
- Toda versión de Windows 11

Para Windows 10 anterior: descargar desde [Microsoft Edge WebView2](https://developer.microsoft.com/en-us/microsoft-edge/webview2/).

---

## Pasos para generar el instalador

### Opción A — Script automático (recomendado)

```bat
build_windows.bat
```

El script verifica todos los requisitos, instala pywebview si falta, ejecuta PyInstaller,
genera el ZIP portable y compila el instalador con Inno Setup.

Opciones:

```bat
build_windows.bat --skip-pyinstaller   # Omite PyInstaller si el bundle ya existe
build_windows.bat --skip-inno          # Genera bundle + ZIP, sin instalador
```

### Opción B — Manual paso a paso

```bat
# Paso 1: Instalar dependencias
pip install -r requirements.txt
pip install pywebview pyinstaller

# Paso 2: Generar el bundle
python -m PyInstaller bootcamp.spec --noconfirm

# Paso 3: Empaquetar portable (PowerShell)
Compress-Archive -Path "dist\BootcampPythonDS\*" `
  -DestinationPath "release_artifacts\BootcampPythonDS_windows_portable_v1.0.0.zip" -Force

# Paso 4: Compilar el instalador (requiere Inno Setup instalado)
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer\setup.iss
```

---

## Modos de ejecución

### Modo app de escritorio (producción)

```bat
BootcampPythonDS.exe
```

Abre directamente una ventana nativa de Windows.
No aparece ninguna consola, no se abre ningún navegador.
El usuario ve la app y la usa igual que cualquier programa.

### Modo desarrollo (desde el repositorio)

```bat
python run_bootcamp.py
```

Levanta Flask en `http://127.0.0.1:8000` y abre el navegador automáticamente.
Útil para desarrollar y depurar sin necesidad de re-compilar el bundle.

---

## Distribuir a alumnos

**Opción portable (sin instalador):**

Compartir `release_artifacts/BootcampPythonDS_windows_portable_v1.0.0.zip`.
El alumno descomprime y ejecuta `BootcampPythonDS.exe` directamente.

**Opción instalador:**

Compartir `dist_installer/BootcampPythonDS_Setup_v1.0.0.exe`.

El alumno lo ejecuta como cualquier instalador de Windows:
1. Doble clic en el .exe
2. Siguiente, siguiente, instalar
3. Al final puede marcar "Iniciar el Bootcamp ahora"

No se requiere internet, no se requiere Python, no se requiere ninguna configuración.

---

## Notebooks guardados por alumnos

En modo instalado, los notebooks que el alumno guarda se almacenan junto al ejecutable:

```
C:\Program Files\BootcampPythonDS\saved_notebooks\
```

Al desinstalar, esta carpeta **no se borra** por defecto para no perder el trabajo del alumno.
Ver sección `[UninstallDelete]` en `installer/setup.iss` para cambiar este comportamiento.

---

## Solucionar problemas comunes

| Síntoma | Causa probable | Solución |
|---|---|---|
| La ventana no abre | Edge WebView2 no instalado | Instalar WebView2 Runtime de Microsoft |
| Pantalla de carga no avanza | Error en Flask interno | Ejecutar `python run_bootcamp.py` para ver el error |
| Error 500 al cargar clases | Falta archivo de datos en el bundle | Revisar sección `datas` en `bootcamp.spec` |
| `ModuleNotFoundError` al buildear | Dependencia no detectada por PyInstaller | Agregar a `hiddenimports` en `bootcamp.spec` |
| Inno Setup no encontrado | Ruta incorrecta | Ajustar `INNO_SETUP` en `build_windows.bat` |
| `collect_all('webview')` falla | pywebview no instalado en el entorno de build | `pip install pywebview` |

---

## Actualizar a una nueva versión

1. Cambiar `VERSION` en `build_windows.bat`
2. Cambiar `AppVersion` en `installer/setup.iss`
3. Ejecutar `build_windows.bat`

Inno Setup detecta automáticamente si hay una versión anterior instalada y ofrece actualizarla.
