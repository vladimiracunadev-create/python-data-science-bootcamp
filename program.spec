# program.spec — Especificación PyInstaller del Python Data Science Program (v3.8.0)
#
# Construye dist/PythonDSProgram/PythonDSProgram.exe — app Windows NATIVA con
# PySide6 (Qt). Sin Flask, sin servidor HTTP, sin localhost, sin WebView2.
# El usuario abre el .exe y ve directamente la ventana Qt que recorre el
# currículo: árbol de partes + clases, viewer de README con `setMarkdown` nativo,
# viewer de celdas .ipynb, links a PDF/PPTX/notebook que abren con el sistema.
#
# Uso:
#   pip install pyinstaller PySide6
#   pyinstaller program.spec
#
# El bundle queda en dist/PythonDSProgram/ y el instalador Inno Setup
# (installer/setup.iss) lo empaqueta como .exe distribuible.

from pathlib import Path

# collect_all recoge datas, binaries e hiddenimports de un paquete completo.
# Es necesario para PySide6 — incluye los .dll de Qt6 (Widgets, Gui, Core).
from PyInstaller.utils.hooks import collect_all  # noqa: E402

# ---------------------------------------------------------------------------
# DIRECTORIO RAÍZ DEL PROYECTO
# ---------------------------------------------------------------------------
ROOT = Path(SPECPATH)  # noqa: F821 — PyInstaller inyecta SPECPATH

# ---------------------------------------------------------------------------
# RECOLECTAR PYSIDE6 + SHIBOKEN COMPLETOS
# Incluye DLLs Qt6 (Core, Gui, Widgets), plugins de plataforma (qwindows),
# fuentes embebidas y ICU. Sin esto la app no arranca al congelarse.
# ---------------------------------------------------------------------------
pyside_datas, pyside_binaries, pyside_hiddenimports = collect_all("PySide6")
shiboken_datas, shiboken_binaries, shiboken_hiddenimports = collect_all("shiboken6")

# ---------------------------------------------------------------------------
# DATOS DEL CURRÍCULO — bundle SLIM: solo README + notebook por clase.
# Los PDFs y PPTX NO se empaquetan en el .exe (ahorra ~70 MB del bundle
# expandido y ~50 MB del ZIP) — los botones "Abrir PDF/PPTX" abren la URL
# raw del repo en GitHub (`https://github.com/.../raw/main/classes/...`).
# ---------------------------------------------------------------------------
classes_files = []
for class_readme in (ROOT / "classes").rglob("README.md"):
    rel = class_readme.relative_to(ROOT)
    classes_files.append((str(class_readme), str(rel.parent).replace("\\", "/")))
for class_nb in (ROOT / "classes").rglob("notebook.ipynb"):
    rel = class_nb.relative_to(ROOT)
    classes_files.append((str(class_nb), str(rel.parent).replace("\\", "/")))

# ---------------------------------------------------------------------------
# ANÁLISIS DE DEPENDENCIAS
# ---------------------------------------------------------------------------
a = Analysis(  # noqa: F821 — PyInstaller inyecta Analysis
    # Script de entrada: launcher delgado que arranca la QApplication de
    # `app_desktop.main`. Sin Flask, sin pywebview.
    scripts=[str(ROOT / "launcher.py")],

    pathex=[str(ROOT)],

    binaries=[*pyside_binaries, *shiboken_binaries],

    # ---------------------------------------------------------------------------
    # DATOS (ver `classes_files` arriba — slim, sin PDFs ni PPTX).
    # ---------------------------------------------------------------------------
    datas=[
        # Currículo: solo README.md + notebook.ipynb por clase (~3 MB).
        # PDFs y PPTX quedan FUERA — el viewer los abre vía URL del repo.
        *classes_files,

        # Recursos del paquete app_desktop (icono, estilos QSS si los hubiera).
        (str(ROOT / "app_desktop"), "app_desktop"),

        # Icono del producto: además de ir incrustado en el .exe (ver `icon=`
        # más abajo), la ventana Qt lo carga en runtime con
        # `curriculum.app_icon_path()`, así que tiene que viajar como dato.
        *(
            [(str(ROOT / "installer" / "icon.ico"), "installer")]
            if (ROOT / "installer" / "icon.ico").exists()
            else []
        ),
        *(
            [(str(ROOT / "installer" / "icon.png"), "installer")]
            if (ROOT / "installer" / "icon.png").exists()
            else []
        ),

        # Datos internos de PySide6 (plugins de plataforma, fuentes, ICU).
        *pyside_datas,
        *shiboken_datas,
    ],

    # ---------------------------------------------------------------------------
    # HIDDEN IMPORTS — módulos que PyInstaller no detecta por análisis estático.
    # ---------------------------------------------------------------------------
    hiddenimports=[
        # PySide6 / shiboken6 recolectados por collect_all.
        *pyside_hiddenimports,
        *shiboken_hiddenimports,

        # Parser de notebooks .ipynb usado por app_desktop.notebook_view.
        "nbformat",
        "nbformat.v4",

        # Markdown server-side (lo usa notebook_loader.load_notebook para
        # renderizar a HTML los markdown cells; opcional pero útil).
        "markdown",
        "markdown.extensions.fenced_code",
        "markdown.extensions.tables",
        "markdown.extensions.codehilite",

        # Resaltado de sintaxis de los bloques de código. `codehilite` importa
        # Pygments por nombre en runtime, así que PyInstaller no lo detecta.
        "pygments",
        "pygments.formatters.html",
        "pygments.lexers.python",
        "pygments.styles",
        # El estilo "github-dark" vive en este módulo; se resuelve por nombre.
        "pygments.styles.gh_dark",
    ],

    # ---------------------------------------------------------------------------
    # EXCLUSIONES — librerías pesadas que NO necesita el viewer nativo.
    # El alumno que quiera ejecutar código abre el lab Flask aparte; el .exe
    # nativo es solo viewer y no carga torch/sklearn/jupyter_client/etc.
    # ---------------------------------------------------------------------------
    excludes=[
        "tkinter",
        "PyQt5",
        "PyQt6",
        "wx",
        # Sin Flask en el bundle nativo — la app no levanta HTTP.
        "flask",
        "werkzeug",
        "jinja2",
        # Sin kernel Jupyter en el bundle nativo — solo se muestran las celdas.
        "jupyter_client",
        "ipykernel",
        "notebook",
        "IPython",
        # Sin pywebview en el bundle nativo.
        "webview",
        "clr",
        "pythonnet",
        # Stack de ML pesado — no se usa para visualizar.
        "torch",
        "tensorflow",
        "transformers",
        "sklearn",
        "scipy",
        "pandas",
        "matplotlib",
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

    name="PythonDSProgram",

    debug=False,
    bootloader_ignore_signals=False,
    strip=False,

    # Sin consola negra — la app muestra una ventana Qt nativa.
    # Cambiá a True solo para depurar errores de startup.
    console=False,

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

    name="PythonDSProgram",
)
