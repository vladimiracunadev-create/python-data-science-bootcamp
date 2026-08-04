"""Ventana principal de la app desktop.

Qué resuelve:
    Layout maestro: QTreeView del currículo (con buscador) a la izquierda,
    cabecera de clase + QTabWidget con README/Notebook a la derecha. Menubar,
    toolbar, statusbar y persistencia con QSettings.
"""

from __future__ import annotations

import logging
import re
from typing import Any

from PySide6.QtCore import QSettings, QSize, Qt
from PySide6.QtGui import QAction, QActionGroup, QIcon, QStandardItem, QStandardItemModel
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QSplitter,
    QStackedWidget,
    QTabWidget,
    QToolBar,
    QTreeView,
    QVBoxLayout,
    QWidget,
)

from app_desktop import __version__
from app_desktop.curriculum import (
    app_icon_path,
    class_dir,
    class_notebook,
    class_page_url,
    class_readme,
    class_repo_url,
    list_curriculum,
    load_notebook,
    open_pdf,
    open_pptx,
    open_url,
    open_with_system,
)
from app_desktop.notebook_view import NotebookView
from app_desktop.readme_view import ReadmeView
from app_desktop.styles import apply_theme

log = logging.getLogger(__name__)

ROLE_SLUG = Qt.ItemDataRole.UserRole + 1
ROLE_KIND = Qt.ItemDataRole.UserRole + 2  # "part" | "class"

#: "Clase 007 — Comprehensions" → "Comprehensions". El número ya va en el badge,
#: repetirlo en el árbol y en la cabecera desperdicia el ancho útil.
_CLASS_PREFIX_RE = re.compile(r"^Clase\s+\d+\s*[—\-–]\s*")

#: "Parte 0 — Prerrequisitos: Python…" → se usa tal cual; el prefijo "Parte N —"
#: ya viene en el H1 del README de la parte, así que NO se antepone otra vez.
_PART_PREFIX_RE = re.compile(r"^Parte\s+\d+\s*[—\-–]\s*")


def _clean_class_title(title: str) -> str:
    return _CLASS_PREFIX_RE.sub("", title or "").strip()


def _clean_part_title(title: str) -> str:
    """Quita el prefijo redundante y todo lo que siga a los dos puntos."""
    stripped = _PART_PREFIX_RE.sub("", title or "").strip()
    return stripped.split(":")[0].strip() or (title or "").strip()


class ClassHeader(QFrame):
    """Cabecera de la clase abierta: badge de número, título y contexto.

    Qué resuelve:
        El título completo de la clase no cabe en el árbol (se elide) y el
        README lo repite recién después de hacer scroll. Esta cabecera fija
        deja siempre visible qué clase se está leyendo y a qué parte pertenece.
    """

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("classHeader")
        layout = QHBoxLayout(self)
        layout.setContentsMargins(18, 12, 18, 12)
        layout.setSpacing(14)

        self._badge = QLabel("—")
        self._badge.setObjectName("classBadge")
        self._badge.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._badge.setFixedSize(QSize(58, 42))
        layout.addWidget(self._badge, 0)

        text_col = QVBoxLayout()
        text_col.setSpacing(2)
        self._title = QLabel("Sin clase seleccionada")
        self._title.setObjectName("classTitle")
        self._title.setWordWrap(False)
        self._context = QLabel("")
        self._context.setObjectName("classContext")
        text_col.addWidget(self._title)
        text_col.addWidget(self._context)
        layout.addLayout(text_col, 1)

    def set_class(self, number: int, title: str, part_label: str, extra: str) -> None:
        self._badge.setText(f"{number:03d}")
        self._title.setText(_clean_class_title(title))
        self._title.setToolTip(title)
        pieces = [p for p in (part_label, extra) if p]
        self._context.setText("  ·  ".join(pieces))


class MainWindow(QMainWindow):
    """Ventana principal con árbol del currículo y tabs README/Notebook."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(f"Python Data Science Program — v{__version__}")
        self.setMinimumSize(QSize(1000, 700))
        self.resize(1400, 900)

        icon = app_icon_path()
        if icon is not None:
            self.setWindowIcon(QIcon(icon))

        self._settings = QSettings("PythonDataScienceProgram", "Desktop")
        self._curriculum: list[dict[str, Any]] = []
        self._flat_class_slugs: list[str] = []  # para navegación anterior/siguiente
        self._class_meta: dict[str, dict[str, Any]] = {}  # slug → nº, título, parte
        self._current_slug: str | None = None
        self._theme = "light"

        self._build_ui()
        self._build_menu()
        self._build_toolbar()
        self._build_statusbar()

        self._load_curriculum_into_tree()
        self._restore_settings()

    # ------------------------------------------------------------------
    def _build_ui(self) -> None:
        splitter = QSplitter(Qt.Orientation.Horizontal, self)

        # ---- panel izquierdo: search + tree ----
        left = QWidget()
        left_layout = QVBoxLayout(left)
        left_layout.setContentsMargins(8, 8, 8, 8)
        left_layout.setSpacing(6)

        self._search = QLineEdit()
        self._search.setPlaceholderText("Buscar clase… (Ctrl+F)")
        self._search.textChanged.connect(self._on_search_changed)
        left_layout.addWidget(self._search)

        self._tree = QTreeView()
        self._tree.setHeaderHidden(True)
        self._tree.setEditTriggers(QTreeView.EditTrigger.NoEditTriggers)
        self._tree.setSelectionMode(QTreeView.SelectionMode.SingleSelection)
        self._tree.setTextElideMode(Qt.TextElideMode.ElideRight)
        self._tree.setUniformRowHeights(True)
        self._tree.setAnimated(True)
        self._tree.clicked.connect(self._on_tree_clicked)
        self._tree_model = QStandardItemModel(self)
        self._tree.setModel(self._tree_model)
        left_layout.addWidget(self._tree, 1)

        splitter.addWidget(left)

        # ---- panel derecho: empty state stacked sobre tabs ----
        right = QWidget()
        right_layout = QVBoxLayout(right)
        right_layout.setContentsMargins(0, 0, 0, 0)

        self._stack = QStackedWidget()

        # Empty state.
        self._empty_widget = QWidget()
        empty_layout = QVBoxLayout(self._empty_widget)
        empty_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        empty_title = QLabel("Python Data Science Program")
        empty_title.setObjectName("emptyTitle")
        empty_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        empty_sub = QLabel(
            "232 clases en 9 partes · README + notebook + PDF + PPTX\n"
            "Seleccioná una clase en el árbol de la izquierda para empezar."
        )
        empty_sub.setObjectName("emptySubtitle")
        empty_sub.setAlignment(Qt.AlignmentFlag.AlignCenter)
        empty_layout.addWidget(empty_title)
        empty_layout.addWidget(empty_sub)
        self._stack.addWidget(self._empty_widget)

        # Vista de clase: cabecera fija + tabs.
        class_view = QWidget()
        class_layout = QVBoxLayout(class_view)
        class_layout.setContentsMargins(0, 0, 0, 0)
        class_layout.setSpacing(0)

        self._header = ClassHeader()
        class_layout.addWidget(self._header)

        self._tabs = QTabWidget()
        self._tabs.setDocumentMode(True)
        self._readme_view = ReadmeView()
        self._notebook_view = NotebookView()
        self._tabs.addTab(self._readme_view, "📘  Clase")
        self._tabs.addTab(self._notebook_view, "🧮  Notebook")
        class_layout.addWidget(self._tabs, 1)

        self._class_view = class_view
        self._stack.addWidget(class_view)

        right_layout.addWidget(self._stack)
        splitter.addWidget(right)

        splitter.setStretchFactor(0, 0)
        splitter.setStretchFactor(1, 1)
        splitter.setSizes([340, 1060])
        splitter.setChildrenCollapsible(False)
        self.setCentralWidget(splitter)
        self._splitter = splitter

    def _build_menu(self) -> None:
        bar = self.menuBar()

        # Archivo
        menu_file = bar.addMenu("&Archivo")
        act_search = QAction("&Buscar…", self)
        act_search.setShortcut("Ctrl+F")
        act_search.triggered.connect(lambda: self._search.setFocus())
        menu_file.addAction(act_search)
        menu_file.addSeparator()
        act_quit = QAction("&Salir", self)
        act_quit.setShortcut("Ctrl+Q")
        act_quit.triggered.connect(self.close)
        menu_file.addAction(act_quit)

        # Ver — theme + zoom de texto
        menu_view = bar.addMenu("&Ver")
        self._theme_group = QActionGroup(self)
        self._theme_group.setExclusive(True)
        self._act_light = QAction("Tema &Claro", self, checkable=True)
        self._act_dark = QAction("Tema &Oscuro", self, checkable=True)
        for act, mode in ((self._act_light, "light"), (self._act_dark, "dark")):
            self._theme_group.addAction(act)
            menu_view.addAction(act)
            act.triggered.connect(lambda _checked=False, m=mode: self._set_theme(m))

        menu_view.addSeparator()
        act_zoom_in = QAction("Texto más &grande", self)
        act_zoom_in.setShortcuts(["Ctrl++", "Ctrl+="])
        act_zoom_in.triggered.connect(self._zoom_in)
        menu_view.addAction(act_zoom_in)
        act_zoom_out = QAction("Texto más &chico", self)
        act_zoom_out.setShortcut("Ctrl+-")
        act_zoom_out.triggered.connect(self._zoom_out)
        menu_view.addAction(act_zoom_out)
        act_zoom_reset = QAction("Tamaño &original", self)
        act_zoom_reset.setShortcut("Ctrl+0")
        act_zoom_reset.triggered.connect(self._zoom_reset)
        menu_view.addAction(act_zoom_reset)

        # Ayuda
        menu_help = bar.addMenu("A&yuda")
        act_about = QAction("&Acerca de…", self)
        act_about.triggered.connect(self._show_about)
        menu_help.addAction(act_about)

    def _build_toolbar(self) -> None:
        tb = QToolBar("Acciones de clase", self)
        tb.setMovable(False)
        self.addToolBar(tb)

        self._act_pdf = QAction("📄 Abrir PDF", self)
        self._act_pdf.triggered.connect(self._open_pdf)
        tb.addAction(self._act_pdf)

        self._act_pptx = QAction("🎞️ Abrir PPTX", self)
        self._act_pptx.triggered.connect(self._open_pptx)
        tb.addAction(self._act_pptx)

        self._act_folder = QAction("📂 Carpeta de la clase", self)
        self._act_folder.triggered.connect(self._open_folder)
        tb.addAction(self._act_folder)

        self._act_web = QAction("🌐 Ver en la web", self)
        self._act_web.setToolTip("Abre esta misma clase en GitHub Pages")
        self._act_web.triggered.connect(self._open_web)
        tb.addAction(self._act_web)

        tb.addSeparator()

        self._act_prev = QAction("⬅ Anterior", self)
        self._act_prev.setShortcut("Ctrl+Left")
        self._act_prev.triggered.connect(self._goto_prev)
        tb.addAction(self._act_prev)

        self._act_next = QAction("Siguiente ➡", self)
        self._act_next.setShortcut("Ctrl+Right")
        self._act_next.triggered.connect(self._goto_next)
        tb.addAction(self._act_next)

        self._update_class_actions_enabled()

    def _build_statusbar(self) -> None:
        self._status_label = QLabel("Sin clase seleccionada")
        self.statusBar().addWidget(self._status_label, 1)

    # ------------------------------------------------------------------
    def _load_curriculum_into_tree(self) -> None:
        try:
            self._curriculum = list_curriculum()
        except Exception as exc:
            log.exception("Error listando currículo: %s", exc)
            self._curriculum = []

        self._tree_model.clear()
        self._class_meta = {}
        root = self._tree_model.invisibleRootItem()
        flat: list[str] = []
        for part in self._curriculum:
            short_part = _clean_part_title(part["part_title"])
            part_label = (
                f"Parte {part['part_number']} — {short_part}  ({len(part['classes'])})"
            )
            part_item = QStandardItem(part_label)
            part_item.setData("", ROLE_SLUG)
            part_item.setData("part", ROLE_KIND)
            part_item.setToolTip(part["part_title"])
            part_item.setEditable(False)
            for cls in part["classes"]:
                # El número va aparte; repetir "Clase NNN —" dentro del título
                # solo come ancho útil del árbol.
                short_title = _clean_class_title(cls["title"])
                marker = "" if cls.get("has_notebook") else "  ·  sin .ipynb"
                cls_item = QStandardItem(f"{cls['number']:03d}   {short_title}{marker}")
                cls_item.setData(cls["slug"], ROLE_SLUG)
                cls_item.setData("class", ROLE_KIND)
                cls_item.setToolTip(cls["title"])
                cls_item.setEditable(False)
                part_item.appendRow(cls_item)
                flat.append(cls["slug"])
                self._class_meta[cls["slug"]] = {
                    "number": cls["number"],
                    "title": cls["title"],
                    "part_label": f"Parte {part['part_number']} — {short_part}",
                    "has_notebook": bool(cls.get("has_notebook")),
                }
            root.appendRow(part_item)
        self._flat_class_slugs = flat
        self._tree.expandToDepth(0)

    # ------------------------------------------------------------------
    def _on_search_changed(self, text: str) -> None:
        needle = text.strip().lower()
        root = self._tree_model.invisibleRootItem()
        for i in range(root.rowCount()):
            part_item = root.child(i)
            any_visible = False
            for j in range(part_item.rowCount()):
                cls_item = part_item.child(j)
                match = (not needle) or (needle in cls_item.text().lower())
                self._tree.setRowHidden(j, part_item.index(), not match)
                if match:
                    any_visible = True
            part_idx = self._tree_model.indexFromItem(part_item)
            self._tree.setRowHidden(i, root.index(), not any_visible and bool(needle))
            if needle and any_visible:
                self._tree.expand(part_idx)

    def _on_tree_clicked(self, index) -> None:
        item = self._tree_model.itemFromIndex(index)
        if item is None:
            return
        kind = item.data(ROLE_KIND)
        if kind != "class":
            return
        slug = item.data(ROLE_SLUG)
        if slug:
            self._open_class(slug)

    # ------------------------------------------------------------------
    def _open_class(self, slug: str) -> None:
        self._current_slug = slug
        self._stack.setCurrentWidget(self._class_view)

        # README
        readme_path = class_readme(slug)
        folder = class_dir(slug)
        if readme_path is not None:
            try:
                text = readme_path.read_text(encoding="utf-8")
                self._readme_view.load_markdown(text, base_dir=folder)
            except Exception as exc:
                log.warning("Error leyendo README de %s: %s", slug, exc)
                self._readme_view.load_empty_state(f"Error leyendo README: {exc}")
        else:
            self._readme_view.load_empty_state("README no disponible")

        # Notebook
        nb_path = class_notebook(slug)
        n_cells = 0
        if nb_path is not None:
            try:
                nb = load_notebook(slug)
                self._notebook_view.load_notebook(nb)
                n_cells = int(nb.get("metadata", {}).get("n_cells", 0)) or len(
                    nb.get("cells", []) or []
                )
            except Exception as exc:
                log.warning("Error cargando notebook %s: %s", slug, exc)
                self._notebook_view.load_empty(f"Error cargando notebook: {exc}")
        else:
            self._notebook_view.load_empty(
                "Esta clase no tiene notebook.ipynb — su material es el README, el PDF y el PPTX."
            )

        # Cabecera de clase.
        meta = self._class_meta.get(slug, {})
        extra = f"{n_cells} celdas" if n_cells else "sin notebook"
        self._header.set_class(
            int(meta.get("number", 0)),
            str(meta.get("title", slug)),
            str(meta.get("part_label", "")),
            extra,
        )
        self._tabs.setTabEnabled(1, nb_path is not None)
        if nb_path is None:
            self._tabs.setCurrentIndex(0)

        position = ""
        if slug in self._flat_class_slugs:
            position = (
                f"clase {self._flat_class_slugs.index(slug) + 1} "
                f"de {len(self._flat_class_slugs)}  ·  "
            )
        self._status_label.setText(f"{position}{slug}")
        self._update_class_actions_enabled()
        self._settings.setValue("last_slug", slug)

    def _update_class_actions_enabled(self) -> None:
        slug = self._current_slug
        has_class = slug is not None
        # PDF y PPTX siempre habilitados: si el archivo local no existe (caso
        # bundle .exe slim), la acción abre la URL raw del repo en el browser.
        self._act_pdf.setEnabled(has_class)
        self._act_pptx.setEnabled(has_class)
        self._act_web.setEnabled(has_class)
        # "Carpeta" solo cuando hay carpeta local (dev mode).
        self._act_folder.setEnabled(has_class and class_dir(slug).exists())
        self._act_prev.setEnabled(
            has_class and slug in self._flat_class_slugs
            and self._flat_class_slugs.index(slug) > 0
        )
        self._act_next.setEnabled(
            has_class and slug in self._flat_class_slugs
            and self._flat_class_slugs.index(slug) < len(self._flat_class_slugs) - 1
        )

    # ------------------------------------------------------------------
    def _open_pdf(self) -> None:
        if not self._current_slug:
            return
        # open_pdf prefiere el path local si existe; si no, abre la URL raw
        # del repo en GitHub (caso bundle .exe slim sin PDFs incluidos).
        open_pdf(self._current_slug)

    def _open_pptx(self) -> None:
        if not self._current_slug:
            return
        open_pptx(self._current_slug)

    def _open_folder(self) -> None:
        if not self._current_slug:
            return
        folder = class_dir(self._current_slug)
        if folder.exists():
            open_with_system(folder)
        else:
            # En bundle .exe la carpeta de la clase no está en disco —
            # abrimos la carpeta del repo en GitHub.
            open_url(class_repo_url(self._current_slug))

    def _open_web(self) -> None:
        if not self._current_slug:
            return
        open_url(class_page_url(self._current_slug))

    # ------------------------------------------------------------------
    def _zoom_in(self) -> None:
        self._readme_view.zoom_in()
        self._notebook_view.set_scale(self._readme_view.scale)
        self._persist_scale()

    def _zoom_out(self) -> None:
        self._readme_view.zoom_out()
        self._notebook_view.set_scale(self._readme_view.scale)
        self._persist_scale()

    def _zoom_reset(self) -> None:
        self._readme_view.zoom_reset()
        self._notebook_view.set_scale(self._readme_view.scale)
        self._persist_scale()

    def _persist_scale(self) -> None:
        self._settings.setValue("text_scale", self._readme_view.scale)
        self.statusBar().showMessage(
            f"Tamaño de texto: {int(self._readme_view.scale * 100)}%", 2000
        )

    def _goto_prev(self) -> None:
        if not self._current_slug or self._current_slug not in self._flat_class_slugs:
            return
        i = self._flat_class_slugs.index(self._current_slug)
        if i > 0:
            self._open_class(self._flat_class_slugs[i - 1])

    def _goto_next(self) -> None:
        if not self._current_slug or self._current_slug not in self._flat_class_slugs:
            return
        i = self._flat_class_slugs.index(self._current_slug)
        if i < len(self._flat_class_slugs) - 1:
            self._open_class(self._flat_class_slugs[i + 1])

    # ------------------------------------------------------------------
    def _set_theme(self, mode: str) -> None:
        mode = "dark" if mode == "dark" else "light"
        self._theme = mode
        app = QApplication.instance()
        if app is not None:
            apply_theme(app, mode)
        # Los visores renderizan HTML propio: hay que reconstruirlo con la
        # paleta del tema, no alcanza con el QSS de la ventana.
        self._readme_view.set_theme(mode)
        self._notebook_view.set_theme(mode)
        self._settings.setValue("theme", mode)
        if mode == "dark":
            self._act_dark.setChecked(True)
        else:
            self._act_light.setChecked(True)

    def _show_about(self) -> None:
        repo = "https://github.com/vladimiracunadev-create/python-data-science-program"
        release = f"{repo}/releases/tag/v{__version__}"
        QMessageBox.about(
            self,
            "Acerca de",
            f"<h2>🐍 Python Data Science Program</h2>"
            f"<p><b>App Windows nativa</b> v{__version__} · widgets Qt (PySide6) "
            f"sin WebView ni servidor local.</p>"
            f"<p><b>Currículo:</b> 🎓 232 clases en 9 partes · cobertura 100% "
            f"(README pedagógico + notebook ejecutable + PDF + PPTX por clase).</p>"
            f"<p><b>Bundle slim:</b> solo READMEs + notebooks viajan dentro del .exe. "
            f"Los PDFs y PPTX se abren desde el repo en GitHub vía la "
            f"URL raw — los botones de la toolbar funcionan tanto online (URL del repo) "
            f"como offline (si la app corre desde el repo clonado).</p>"
            f"<p><b>Laboratorio Python</b> (Flask + kernel Jupyter real) es una "
            f"herramienta separada para EJECUTAR código — esta app es solo viewer. "
            f"Ver instrucciones en el repo (<code>python -m app.app</code>).</p>"
            f"<p><b>App Android</b> companion también disponible (Expo + React Native) "
            f"en el mismo release.</p>"
            f"<hr>"
            f"<p>📥 <a href='{release}'>Release v{__version__}</a> · "
            f"📂 <a href='{repo}'>Repositorio</a> · "
            f"📜 Licencia MIT.</p>"
            f"<p style='color:#666;font-size:0.9em'>Construido con Python 3.12 + "
            f"PySide6 + nbformat. PyInstaller para el bundle Windows. "
            f"GitHub Actions para CI/Security/Pages.</p>",
        )

    # ------------------------------------------------------------------
    def _restore_settings(self) -> None:
        theme = self._settings.value("theme", "light", type=str)
        self._theme = "dark" if theme == "dark" else "light"
        # `_set_theme` corta temprano si el modo no cambia; forzamos la primera
        # aplicación invirtiendo el estado interno de los visores.
        self._readme_view.set_theme(self._theme)
        self._notebook_view.set_theme(self._theme)
        self._set_theme(self._theme)

        scale = self._settings.value("text_scale", 1.0, type=float)
        if scale and abs(scale - 1.0) > 0.001:
            self._readme_view.set_scale(scale)
            self._notebook_view.set_scale(self._readme_view.scale)

        size = self._settings.value("window/size")
        if isinstance(size, QSize) and size.isValid():
            self.resize(size)
        pos = self._settings.value("window/pos")
        if pos is not None:
            try:
                self.move(pos)
            except (TypeError, ValueError) as exc:
                log.debug("No pude restaurar posición de ventana: %s", exc)

        last_slug = self._settings.value("last_slug", "", type=str)
        if last_slug and last_slug in self._flat_class_slugs:
            self._open_class(last_slug)

    def closeEvent(self, event) -> None:  # noqa: N802 (Qt API)
        self._settings.setValue("window/size", self.size())
        self._settings.setValue("window/pos", self.pos())
        super().closeEvent(event)
