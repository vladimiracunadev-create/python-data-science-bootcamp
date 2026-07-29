# 🪟 Guía: Build Windows — App de Escritorio (PySide6 / Qt nativo)

Genera el ejecutable Windows del Python Data Science Program como **aplicación de escritorio Qt nativa** (v3.10.0+).
No se abre ningún navegador, no se levanta Flask, no se reserva puerto local, no se usa WebView. La ventana es una app real de Windows hecha con PySide6.

---

## ❓ Qué genera este proceso

```
release_artifacts/
  PythonDSProgram_windows_portable_v3.10.0.zip   ← portable slim (~274 MB; descomprimir y ejecutar)

dist_installer/
  PythonDSProgram_Setup_v3.10.0.exe              ← instalador opcional (Inno Setup)

dist/PythonDSProgram/
  PythonDSProgram.exe                           ← ejecutable directo (Qt nativo)
  _internal/                                     ← runtime Python + PySide6 + Qt + dependencias del bundle
  app_desktop/                                   ← módulos Qt (main_window, readme_view, notebook_view, ...)
  classes/                                       ← currículo completo embebido (READMEs + notebooks)
                                                  Los PDFs/PPTX NO van empaquetados — el viewer abre la URL raw del repo.
```

---

## 📱 Arquitectura de la app de escritorio (PySide6)

```
PythonDSProgram.exe
    |
    ├── launcher.py → QApplication (PySide6 / Qt)
    └── app_desktop.MainWindow
         ├── QTreeView con las 9 partes + 232 clases
         ├── Tabs README (QTextBrowser.setMarkdown) / Notebook (QScrollArea + celdas)
         ├── Toolbar: Abrir PDF / Abrir PPTX / Abrir carpeta / navegar anterior-siguiente
         └── Theme light/dark persistente vía QSettings

         — sin servidor HTTP, sin Flask, sin WebView, sin localhost
         — sin Python ni Edge WebView2 instalados en el PC del usuario

    ↓ PyInstaller (program.spec)
    dist/PythonDSProgram/  (bundle con Python + PySide6 + Qt embebidos)

    ↓ PowerShell Compress-Archive
    release_artifacts/PythonDSProgram_windows_portable_v3.10.0.zip

    ↓ Inno Setup (installer/setup.iss)  — opcional
    dist_installer/PythonDSProgram_Setup_v3.10.0.exe
```

**Componentes clave:**

| Archivo | Rol |
|---|---|
| `launcher.py` | Punto de entrada del .exe — `QApplication` + `MainWindow` de PySide6 (sin Flask) |
| `app_desktop/` | Paquete de 8 módulos con la UI Qt (main_window, readme_view, notebook_view, curriculum, styles, ...) |
| `run_program.py` | Modo desarrollo del **laboratorio Flask + kernel Jupyter** — herramienta separada de la app nativa |
| `program.spec` | Especificación PyInstaller (bundle slim con PySide6 + shiboken6, sin pywebview/Flask/torch) |
| `installer/setup.iss` | Script Inno Setup para el instalador opcional |
| `build_windows.bat` | Automatiza todo el proceso de build |

---

## 📦 Requisitos del entorno de build

| Herramienta | Versión mínima | Instalación |
|---|---|---|
| Python | 3.10 | python.org/downloads |
| pip | último | incluido con Python |
| PySide6 | 6.6+ | `pip install "PySide6>=6.6"` |
| PyInstaller | 6.0 | `pip install pyinstaller` |
| Inno Setup | 6.0 (opcional) | jrsoftware.org/isinfo.php |
| Dependencias del repo | ver requirements.txt | `pip install -r requirements.txt` |

> El alumno/docente que usa el ZIP portable o el instalador **NO necesita Python ni ninguna dependencia**.
> El bundle incluye el runtime Python + PySide6 + Qt completos.

### 📋 Requisito en el PC del usuario final

**Ninguno.** PySide6 trae sus propias librerías Qt — no se requiere Edge WebView2 ni runtime adicional. Funciona en Windows 10 y Windows 11.

---

## 👣 Pasos para generar el instalador

### 🅰️ Opción A — Script automático (recomendado)

```bat
build_windows.bat
```

El script verifica todos los requisitos, instala PySide6 si falta, ejecuta PyInstaller,
genera el ZIP portable y compila el instalador con Inno Setup.

Opciones:

```bat
build_windows.bat --skip-pyinstaller   # Omite PyInstaller si el bundle ya existe
build_windows.bat --skip-inno          # Genera bundle + ZIP, sin instalador
```

### 🅱️ Opción B — Manual paso a paso

```bat
# Paso 1: Instalar dependencias
pip install -r requirements.txt
pip install "PySide6>=6.6" pyinstaller

# Paso 2: Generar el bundle
python -m PyInstaller program.spec --noconfirm

# Paso 3: Empaquetar portable (PowerShell)
Compress-Archive -Path "dist\PythonDSProgram\*" `
  -DestinationPath "release_artifacts\PythonDSProgram_windows_portable_v3.10.0.zip" -Force

# Paso 4: Compilar el instalador (requiere Inno Setup instalado)
# Ruta estándar (instalación oficial de jrsoftware.org):
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer\setup.iss

# Ruta alternativa (Inno Setup vía node_modules / Antigravity / electron-builder):
"%LOCALAPPDATA%\Programs\Antigravity\resources\app\node_modules\innosetup\bin\ISCC.exe" installer\setup.iss

# Si no sabes cuál tienes instalada, busca con:
where ISCC
# o si no está en PATH:
where /R "%ProgramFiles(x86)%" ISCC.exe
where /R "%LOCALAPPDATA%" ISCC.exe
```

---

## 🚦 Modos de ejecución

### 📱 Modo app de escritorio (producción)

```bat
PythonDSProgram.exe
```

Abre directamente una ventana nativa de Windows.
No aparece ninguna consola, no se abre ningún navegador.
El usuario ve la app y la usa igual que cualquier programa.

### 🐍 Modo desarrollo (desde el repositorio)

```bat
python launcher.py   # app Qt nativa (PySide6) — sin recompilar el bundle
```

Para el **laboratorio Flask + kernel Jupyter** (herramienta separada, para ejecutar código):

```bat
python run_program.py
```

Levanta Flask en `http://127.0.0.1:8000`. Útil cuando se necesita ejecutar notebooks; la app Qt nativa solo es viewer.

---

## 🎓 Distribuir a alumnos

**Opción portable (sin instalador):**

Compartir `release_artifacts/PythonDSProgram_windows_portable_v3.10.0.zip` (~274 MB).
El alumno descomprime y ejecuta `PythonDSProgram.exe` directamente.

**Opción instalador:**

Compartir `dist_installer/PythonDSProgram_Setup_v3.10.0.exe`.

El alumno lo ejecuta como cualquier instalador de Windows:
1. Doble clic en el .exe
2. Siguiente, siguiente, instalar
3. Al final puede marcar "Iniciar el Programa ahora"

No se requiere internet, no se requiere Python, no se requiere ninguna configuración.

---

## 🎓 Notebooks guardados por alumnos

En modo instalado, los notebooks que el alumno guarda se almacenan junto al ejecutable:

```
C:\Program Files\PythonDSProgram\saved_notebooks\
```

Al desinstalar, esta carpeta **no se borra** por defecto para no perder el trabajo del alumno.
Ver sección `[UninstallDelete]` en `installer/setup.iss` para cambiar este comportamiento.

---

## 🚨 Solucionar problemas comunes

| Síntoma | Causa probable | Solución |
|---|---|---|
| La ventana no abre | Error de Qt al arrancar | Ejecutar `python launcher.py` para ver el error de PySide6 |
| Una clase aparece vacía | Falta `classes/` en el bundle | Revisar sección `datas` en `program.spec` |
| `ModuleNotFoundError` al buildear | Dependencia no detectada por PyInstaller | Agregar a `hiddenimports` en `program.spec` |
| Inno Setup no encontrado | Ruta incorrecta o instalación no estándar | Buscar con `where /R "%LOCALAPPDATA%" ISCC.exe` y ajustar `INNO_SETUP` en `build_windows.bat`. Ver rutas alternativas en la sección de instalación manual. |
| `ModuleNotFoundError: PySide6` al buildear | PySide6 no instalado en el entorno de build | `pip install "PySide6>=6.6"` |

---

## 🔄 Actualizar a una nueva versión

1. Cambiar `VERSION` en `build_windows.bat`
2. Cambiar `AppVersion` en `installer/setup.iss`
3. Ejecutar `build_windows.bat`

Inno Setup detecta automáticamente si hay una versión anterior instalada y ofrece actualizarla.
