"""Hojas de estilo Qt (QSS) para temas claro y oscuro.

QSS es el equivalente de CSS para widgets Qt nativos — NO es CSS web.
"""

from __future__ import annotations

from PySide6.QtWidgets import QApplication

LIGHT_QSS = """
QMainWindow, QWidget {
    background-color: #f7f7f9;
    color: #1f2328;
    font-family: "Segoe UI", "Inter", Arial, sans-serif;
    font-size: 10pt;
}
QTreeView {
    background-color: #ffffff;
    border: 1px solid #d0d7de;
    border-radius: 6px;
    padding: 4px;
    selection-background-color: #0969da;
    selection-color: #ffffff;
}
QTreeView::item { padding: 4px 2px; }
QTreeView::item:hover { background-color: #eaeef2; }
QLineEdit {
    background-color: #ffffff;
    border: 1px solid #d0d7de;
    border-radius: 6px;
    padding: 6px 8px;
}
QLineEdit:focus { border-color: #0969da; }
QTabWidget::pane {
    border: 1px solid #d0d7de;
    border-radius: 6px;
    background-color: #ffffff;
}
QTabBar::tab {
    background-color: #eaeef2;
    color: #1f2328;
    padding: 8px 16px;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
    margin-right: 2px;
}
QTabBar::tab:selected {
    background-color: #ffffff;
    color: #0969da;
    font-weight: 600;
}
QTextBrowser, QTextEdit {
    background-color: #ffffff;
    border: 1px solid #d0d7de;
    border-radius: 6px;
    padding: 10px;
}
QStatusBar {
    background-color: #eaeef2;
    border-top: 1px solid #d0d7de;
}
QToolBar {
    background-color: #eaeef2;
    border-bottom: 1px solid #d0d7de;
    spacing: 6px;
    padding: 4px;
}
QToolButton {
    padding: 6px 12px;
    border-radius: 6px;
}
QToolButton:hover { background-color: #d0d7de; }
QToolButton:disabled { color: #8c959f; }
QMenuBar { background-color: #eaeef2; }
QMenuBar::item:selected { background-color: #d0d7de; }
QPushButton {
    background-color: #0969da;
    color: #ffffff;
    border: none;
    border-radius: 6px;
    padding: 6px 14px;
}
QPushButton:hover { background-color: #0860c4; }
QPushButton:disabled { background-color: #8c959f; }
QScrollArea { border: none; background-color: #f7f7f9; }
"""

DARK_QSS = """
QMainWindow, QWidget {
    background-color: #0d1117;
    color: #e6edf3;
    font-family: "Segoe UI", "Inter", Arial, sans-serif;
    font-size: 10pt;
}
QTreeView {
    background-color: #161b22;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 4px;
    selection-background-color: #1f6feb;
    selection-color: #ffffff;
}
QTreeView::item { padding: 4px 2px; }
QTreeView::item:hover { background-color: #21262d; }
QLineEdit {
    background-color: #0d1117;
    color: #e6edf3;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 6px 8px;
}
QLineEdit:focus { border-color: #1f6feb; }
QTabWidget::pane {
    border: 1px solid #30363d;
    border-radius: 6px;
    background-color: #161b22;
}
QTabBar::tab {
    background-color: #21262d;
    color: #e6edf3;
    padding: 8px 16px;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
    margin-right: 2px;
}
QTabBar::tab:selected {
    background-color: #161b22;
    color: #58a6ff;
    font-weight: 600;
}
QTextBrowser, QTextEdit {
    background-color: #161b22;
    color: #e6edf3;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 10px;
}
QStatusBar {
    background-color: #161b22;
    border-top: 1px solid #30363d;
}
QToolBar {
    background-color: #161b22;
    border-bottom: 1px solid #30363d;
    spacing: 6px;
    padding: 4px;
}
QToolButton {
    padding: 6px 12px;
    border-radius: 6px;
    color: #e6edf3;
}
QToolButton:hover { background-color: #30363d; }
QToolButton:disabled { color: #6e7681; }
QMenuBar { background-color: #161b22; color: #e6edf3; }
QMenuBar::item:selected { background-color: #30363d; }
QMenu { background-color: #161b22; color: #e6edf3; border: 1px solid #30363d; }
QMenu::item:selected { background-color: #1f6feb; }
QPushButton {
    background-color: #1f6feb;
    color: #ffffff;
    border: none;
    border-radius: 6px;
    padding: 6px 14px;
}
QPushButton:hover { background-color: #1a5dc4; }
QPushButton:disabled { background-color: #6e7681; }
QScrollArea { border: none; background-color: #0d1117; }
"""


def apply_theme(app: QApplication, mode: str) -> None:
    """Aplica el tema ``"light"`` o ``"dark"`` al QApplication."""
    if mode == "dark":
        app.setStyleSheet(DARK_QSS)
    else:
        app.setStyleSheet(LIGHT_QSS)
