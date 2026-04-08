# bootcamp.spec — Especificacion de PyInstaller para el Bootcamp Python DS
#
# Genera un directorio dist/BootcampPythonDS/ con el ejecutable y todos los datos.
# Uso:
#   pip install pyinstaller
#   pyinstaller bootcamp.spec
#
# El resultado en dist/BootcampPythonDS/BootcampPythonDS.exe es el ejecutable
# que se entrega al instalador Inno Setup (setup.iss).

import os
from pathlib import Path

# ---------------------------------------------------------------------------
# DIRECTORIO RAIZ DEL PROYECTO
# ---------------------------------------------------------------------------
# Definido en tiempo de spec para que los paths sean absolutos y portables.
ROOT = Path(SPECPATH)  # noqa: F821 — PyInstaller inyecta SPECPATH

# ---------------------------------------------------------------------------
# ANALISIS DE DEPENDENCIAS
# ---------------------------------------------------------------------------
a = Analysis(
    # Script de entrada: el launcher que arranca Flask y abre el navegador
    scripts=[str(ROOT / "launcher.py")],

    # Directorios donde PyInstaller busca modulos importados
    pathex=[str(ROOT)],

    # DLLs y extensiones binarias adicionales que PyInstaller no detecta solo
    # numpy, pandas y scikit-learn incluyen extensiones C compiladas (.pyd/.so)
    binaries=[],

    # ---------------------------------------------------------------------------
    # DATOS (archivos no-Python que el ejecutable necesita en runtime)
    # ---------------------------------------------------------------------------
    datas=[
        # Plantillas HTML y CSS/JS del laboratorio Flask
        (str(ROOT / "app" / "templates"),   "app/templates"),
        (str(ROOT / "app" / "static"),      "app/static"),

        # Notebooks de laboratorio (JSON)
        (str(ROOT / "app" / "notebooks"),   "app/notebooks"),

        # Curriculum: 12 clases con teoria, ejercicios y notebooks
        (str(ROOT / "classes"),             "classes"),

        # Datasets sinteticos para las practicas
        (str(ROOT / "datasets"),            "datasets"),

        # Portal publico del alumno (HTML/CSS/JS estatico)
        (str(ROOT / "site"),                "site"),
    ],

    # Imports que PyInstaller no detecta por ser dinamicos o condicionales
    hiddenimports=[
        # Flask y sus extensiones internas
        "flask",
        "flask.templating",
        "flask.json",
        "jinja2",
        "jinja2.ext",
        "werkzeug",
        "werkzeug.serving",
        "werkzeug.routing",

        # Procesamiento de Markdown (usado en app.py)
        "markdown",
        "markdown.extensions.fenced_code",
        "markdown.extensions.tables",
        "markdown.extensions.codehilite",

        # Ciencia de datos
        "pandas",
        "pandas.core.arrays.masked",   # extension interna necesaria en algunos builds
        "numpy",
        "numpy.core._multiarray_umath",
        "matplotlib",
        "matplotlib.backends.backend_agg",  # backend no-interactivo usado por el runner
        "sklearn",
        "sklearn.utils._cython_blas",
        "sklearn.neighbors._partition_nodes",
        "sklearn.tree._utils",

        # Formato de notebooks
        "nbformat",
    ],

    # Modulos a excluir para reducir el tamano del bundle
    excludes=[
        "tkinter",       # GUI toolkit de Python — no se usa
        "PyQt5",         # Otro toolkit GUI
        "wx",            # wxPython GUI
        "IPython",       # Solo necesario para Jupyter interactivo, no para el runner
        "jupyter_client",
        "notebook",      # El servidor Jupyter completo no es necesario
        "test",          # Tests de la stdlib de Python
    ],

    # No empaquetar en un solo archivo (modo onedir es mas rapido de arrancar)
    # onefile=True ralentiza el inicio porque descomprime todo en un temp dir
    win_no_prefer_redirects=False,
    win_private_assemblies=False,

    # Cache del analisis (acelera recompilaciones)
    cipher=None,
    noarchive=False,
)

# ---------------------------------------------------------------------------
# ARCHIVOS OBJETO COMPILADOS (PYC)
# ---------------------------------------------------------------------------
pyz = PYZ(a.pure, a.zipped_data, cipher=None)  # noqa: F821

# ---------------------------------------------------------------------------
# EJECUTABLE
# ---------------------------------------------------------------------------
exe = EXE(  # noqa: F821
    pyz,
    a.scripts,
    [],

    # NO incluir todo en un solo .exe — modo onedir es obligatorio
    # para que los datas (templates, clases, datasets) sean accesibles
    exclude_binaries=True,

    # Nombre del ejecutable final (sin extension .exe)
    name="BootcampPythonDS",

    # Informacion del ejecutable
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,

    # No mostrar la consola negra al ejecutar en Windows
    # Cambiar a console=True para debug — la consola muestra los logs de Flask
    console=True,  # True para que el usuario vea el menu y los logs

    # Icono del ejecutable (debe existir como .ico)
    # icon=str(ROOT / "installer" / "icon.ico"),

    # Manifesto de Windows para solicitar permisos de usuario normal (no admin)
    uac_admin=False,
)

# ---------------------------------------------------------------------------
# DIRECTORIO FINAL DE DISTRIBUCION
# ---------------------------------------------------------------------------
coll = COLLECT(  # noqa: F821
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,

    # No comprimir — inicio mas rapido a costa de mas espacio en disco
    strip=False,
    upx=False,               # UPX comprime pero puede ser detectado como virus
    upx_exclude=[],

    # Nombre del directorio en dist/
    name="BootcampPythonDS",
)
