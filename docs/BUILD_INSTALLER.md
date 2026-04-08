# Guía: Instalador Windows

Genera un `.exe` instalable del Bootcamp Python DS para distribuir en computadores de aula sin necesitar Python, pip ni configuración manual.

---

## Qué genera este proceso

```
dist_installer/
  BootcampPythonDS_Setup_v1.0.0.exe   <- instalador para el alumno/docente

dist/BootcampPythonDS/
  BootcampPythonDS.exe                <- ejecutable directo (sin instalar)
  app/templates/
  app/notebooks/
  classes/       <- curriculum completo embebido
  datasets/      <- datasets de practica embebidos
  site/
  ...
```

El instalador copia todo lo anterior a `Program Files\BootcampPythonDS\` y crea accesos directos.

---

## Arquitectura del instalador

```
launcher.py
    |
    ├── Detecta puerto en uso (evita doble instancia)
    ├── Arranca Flask en hilo daemon
    ├── Hace polling a /health hasta que responde
    ├── Abre el navegador en http://127.0.0.1:8000
    └── Menu de consola: [Enter] reabrir | [q] apagar

    ↓ PyInstaller
    bootcamp.spec
    ↓
    dist/BootcampPythonDS/ (bundle completo con Python embebido)

    ↓ Inno Setup
    installer/setup.iss
    ↓
    dist_installer/BootcampPythonDS_Setup_v1.0.0.exe
```

---

## Requisitos del entorno de build

| Herramienta | Versión minima | Instalacion |
|---|---|---|
| Python | 3.10 | python.org/downloads |
| pip | ultimo | incluido con Python |
| PyInstaller | 6.0 | `pip install pyinstaller` |
| Inno Setup | 6.0 | jrsoftware.org/isinfo.php |
| Dependencias del repo | ver requirements.txt | `pip install -r requirements.txt` |

> El alumno/docente que usa el instalador NO necesita Python instalado.
> El bundle de PyInstaller incluye el runtime de Python completo.

---

## Pasos para generar el instalador

### Opción A — Script automatico (recomendado)

```bat
build_windows.bat
```

El script verifica todos los requisitos, ejecuta PyInstaller y luego Inno Setup.

Opciones:

```bat
build_windows.bat --skip-pyinstaller   # Omite PyInstaller si el bundle ya existe
build_windows.bat --skip-inno          # Genera solo el bundle, sin instalador
```

### Opción B — Manual paso a paso

```bat
# Paso 1: Instalar PyInstaller
pip install pyinstaller

# Paso 2: Instalar dependencias del proyecto
pip install -r requirements.txt

# Paso 3: Generar el bundle
python -m PyInstaller bootcamp.spec --noconfirm

# Paso 4: Compilar el instalador (requiere Inno Setup instalado)
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer\setup.iss
```

---

## Probar sin instalar

```bat
dist\BootcampPythonDS\BootcampPythonDS.exe
```

Se abre una consola que muestra el servidor arrancando y luego abre el navegador en `http://127.0.0.1:8000`.

Para apagar: escribir `q` en la consola o cerrar la ventana.

---

## Distribuir a alumnos

Compartir el archivo:

```
dist_installer\BootcampPythonDS_Setup_v1.0.0.exe
```

El alumno lo ejecuta como cualquier instalador de Windows:
1. Doble clic en el .exe
2. Siguiente, siguiente, instalar
3. Al final puede marcar "Iniciar el Bootcamp ahora"

No se requiere internet, no se requiere Python, no se requiere ninguna configuración adicional.

---

## Variables de entorno disponibles

| Variable | Default | Descripcion |
|---|---|---|
| `BOOTCAMP_HOST` | 127.0.0.1 | Dirección de escucha del servidor |
| `BOOTCAMP_PORT` | 8000 | Puerto del servidor |

Para cambiar el puerto: editar el acceso directo del Menu de inicio y agregar las variables antes del ejecutable, o usar un `.bat` de arranque personalizado.

---

## Notebooks guardados por alumnos

En modo instalado, los notebooks que el alumno guarda se almacenan en:

```
C:\Program Files\BootcampPythonDS\saved_notebooks\
```

Al desinstalar, esta carpeta NO se borra por defecto (para no perder el trabajo del alumno). Ver comentario en `installer\setup.iss` sección `[UninstallDelete]` para cambiar este comportamiento.

---

## Solucionar problemas comunes

| Sintoma | Causa probable | Solución |
|---|---|---|
| "Port already in use" | El servidor ya esta corriendo | Cerrar la consola anterior o cambiar BOOTCAMP_PORT |
| La consola se abre y cierra al instante | Error de dependencias en el bundle | Ejecutar desde cmd para ver el error |
| El navegador abre pero muestra error 500 | Falta un archivo de datos en el bundle | Revisar la sección `datas` en bootcamp.spec |
| "ModuleNotFoundError" en la consola | Dependencia no detectada por PyInstaller | Agregar el módulo a `hiddenimports` en bootcamp.spec |
| Inno Setup no encontrado | Ruta incorrecta | Ajustar la variable `INNO_SETUP` en build_windows.bat |

---

## Actualizar el instalador a una nueva versión

1. Cambiar `VERSION` en `build_windows.bat`
2. Cambiar `AppVersion` en `installer\setup.iss`
3. Ejecutar `build_windows.bat`

Inno Setup detecta automaticamente que hay una versión anterior instalada y ofrece actualizarla.
