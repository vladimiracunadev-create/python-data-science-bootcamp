# bootcamp.spec — Especificacion de PyInstaller para el Bootcamp Python DS
#
# Genera un directorio dist/BootcampPythonDS/ con el ejecutable y todos los datos.
# Uso:
#   pip install pyinstaller pywebview
#   pyinstaller bootcamp.spec
#
# El resultado en dist/BootcampPythonDS/BootcampPythonDS.exe es el ejecutable
# que se entrega al instalador Inno Setup (setup.iss).

import os
from pathlib import Path

# collect_all recoge datas, binaries e hiddenimports de un paquete completo.
# Es necesario para pywebview porque incluye WebView2Loader.dll y hooks .NET.
from PyInstaller.utils.hooks import collect_all, collect_data_files  # noqa: E402

# ---------------------------------------------------------------------------
# DIRECTORIO RAIZ DEL PROYECTO
# ---------------------------------------------------------------------------
ROOT = Path(SPECPATH)  # noqa: F821 — PyInstaller inyecta SPECPATH

# ---------------------------------------------------------------------------
# RECOLECTAR PYWEBVIEW COMPLETO
# Incluye: WebView2Loader.dll, hooks de pythonnet, JS internos, etc.
# ---------------------------------------------------------------------------
wv_datas, wv_binaries, wv_hiddenimports = collect_all("webview")

# ---------------------------------------------------------------------------
# ANALISIS DE DEPENDENCIAS
# ---------------------------------------------------------------------------
a = Analysis(
    # Script de entrada: launcher que levanta Flask y abre la ventana nativa
    scripts=[str(ROOT / "launcher.py")],

    pathex=[str(ROOT)],

    binaries=wv_binaries,

    # ---------------------------------------------------------------------------
    # DATOS
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

        # Materiales derivados por clase y apoyo imprimible
        (str(ROOT / "docs" / "pdfs"),       "docs/pdfs"),
        (str(ROOT / "docs" / "presentaciones"), "docs/presentaciones"),

        # Portal publico del alumno (HTML/CSS/JS estatico)
        (str(ROOT / "site"),                "site"),

        # Datos internos de pywebview (JS, recursos WebView2)
        *wv_datas,
    ],

    # ---------------------------------------------------------------------------
    # HIDDEN IMPORTS
    # ---------------------------------------------------------------------------
    hiddenimports=[
        # Flask y werkzeug
        "flask",
        "flask.templating",
        "flask.json",
        "jinja2",
        "jinja2.ext",
        "werkzeug",
        "werkzeug.serving",
        "werkzeug.routing",

        # Markdown
        "markdown",
        "markdown.extensions.fenced_code",
        "markdown.extensions.tables",
        "markdown.extensions.codehilite",

        # Ciencia de datos
        "pandas",
        "pandas.core.arrays.masked",
        "numpy",
        "numpy.core._multiarray_umath",
        "matplotlib",
        "matplotlib.backends.backend_agg",
        "sklearn",
        "sklearn.utils._cython_blas",
        "sklearn.neighbors._partition_nodes",
        "sklearn.tree._utils",

        # Notebooks
        "nbformat",

        # pywebview — detectados por collect_all pero los declaramos explicitamente
        *wv_hiddenimports,

        # pythonnet / clr (necesario para el backend winforms de pywebview en Windows)
        "clr",
        "pythonnet",
    ],

    # Excluir lo que no se usa
    excludes=[
        "tkinter",
        "PyQt5",
        "PyQt6",
        "wx",
        "IPython",
        "jupyter_client",
        "notebook",
        "test",
    ],

    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

# ---------------------------------------------------------------------------
# ARCHIVOS OBJETO COMPILADOS
# ---------------------------------------------------------------------------
pyz = PYZ(a.pure, a.zipped_data, cipher=None)  # noqa: F821

# ---------------------------------------------------------------------------
# EJECUTABLE
# ---------------------------------------------------------------------------
exe = EXE(  # noqa: F821
    pyz,
    a.scripts,
    [],

    exclude_binaries=True,

    name="BootcampPythonDS",

    debug=False,
    bootloader_ignore_signals=False,
    strip=False,

    # Sin consola negra — la app muestra una ventana nativa
    # Cambiar a True solo para depuracion
    console=False,

    # Icono del ejecutable (si existe el .ico)
    icon=str(ROOT / "installer" / "icon.ico") if (ROOT / "installer" / "icon.ico").exists() else None,

    uac_admin=False,
)

# ---------------------------------------------------------------------------
# DIRECTORIO FINAL
# ---------------------------------------------------------------------------
coll = COLLECT(  # noqa: F821
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,

    strip=False,
    upx=False,
    upx_exclude=[],

    name="BootcampPythonDS",
)
