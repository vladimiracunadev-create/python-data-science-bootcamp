# Clase 005 — VS Code / Cursor para Python y Jupyter

> Parte: **0 — Prerrequisitos** · Fuente: VS Code Python docs · Cursor docs · *The Pragmatic Programmer* cap. "Power Editing".
> ⏱️ Duración estimada: **60 min**.

---

## 🎯 Objetivo

Que el alumno deje de usar VS Code como Notepad y lo configure como un IDE serio para Python + Jupyter: selector de intérprete, debugger gráfico, linter (ruff), formatter (ruff format), tests integrados y notebooks editables. Bonus: cuándo conviene Cursor (VS Code + IA integrada).

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Configurar VS Code** con la extensión Python + Jupyter, seleccionando el intérprete del venv del proyecto.
2. **Debuggear** un script Python paso a paso desde el panel gráfico (breakpoints, watch, call stack).
3. **Editar y ejecutar notebooks** sin Jupyter web — con autocompletado, type hints y debug de celda.
4. **Configurar ruff** como linter + formatter (reemplaza black + isort + flake8 en un solo tool).
5. **Decidir cuándo usar Cursor** (idéntico a VS Code + IA integrada con autorización por chat).

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | Selección de intérprete por workspace | El bug "funciona en terminal pero no en VS Code" se evita aquí. |
| 2 | Debugger gráfico vs `print` | Breakpoints, watch, evaluación expresiones — mucho más rápido. |
| 3 | Notebooks nativos en VS Code | Mejor UX que Jupyter web para edición; mismo backend. |
| 4 | ruff = linter + formatter en uno | Reemplaza black/isort/flake8/pylint. Más rápido (Rust). |
| 5 | Tests integrados (`pytest`) | Run/debug tests con un click; coverage inline. |
| 6 | Extensiones esenciales | Python, Jupyter, GitLens, ruff, Even Better TOML. |
| 7 | Cursor: cuándo sí | Cuando quieres pair-programming con IA sin salir del editor. |

## 📂 Dataset / recursos

Sin dataset externo. Usamos un script Python con un bug intencional para practicar debug gráfico, y un notebook trivial para verificar autocompletado/type hints.

## 🧪 Ejercicios

**1.** **Selecciona intérprete.** En VS Code: `Ctrl+Shift+P` → "Python: Select Interpreter" → elige el del `.venv` del proyecto. Verifica con `print(sys.executable)` en una celda.

**2.** **Debug paso a paso.** Toma un script con un bug, pon breakpoint (F9), ejecuta con F5, navega con F10 (next), F11 (step in), Shift+F11 (step out). Inspecciona variables en panel.

**3.** **Configura ruff.** En `pyproject.toml`: `[tool.ruff]` con `line-length = 100`, `[tool.ruff.lint]` con `select = ["E", "F", "I", "UP"]`. Habilita format on save.

**4.** **Edita un notebook.** Abre `notebook.ipynb` en VS Code, ejecuta una celda, comprueba que el autocompletado funciona con type hints de pandas.

**5.** **Tests con un click.** Instala `pytest`, crea `tests/test_simple.py` con 2 tests (uno OK, uno FAIL). Usa el panel "Testing" para correr/debuggear.

## 📝 Homework verificable

Repo con `pyproject.toml` que incluye `[tool.ruff]`, `.vscode/settings.json` con `python.defaultInterpreterPath` y format-on-save habilitado, screenshot del debugger gráfico mostrando un breakpoint activo y variables inspeccionadas.

**Criterio de aceptación:** Otro alumno clona el repo, abre en VS Code, y al guardar un .py se aplica ruff format automáticamente. El screenshot muestra al menos 1 breakpoint y la variable inspeccionada.

## 🔗 Referencias

- [VS Code Python docs](https://code.visualstudio.com/docs/python/python-tutorial)
- [VS Code Jupyter docs](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
- [ruff docs](https://docs.astral.sh/ruff/)
- [Cursor docs](https://docs.cursor.com/)

## ➡️ Siguiente clase

[Clase 006 — Python: tipos, estructuras, control de flujo](../006-python-tipos-estructuras-control-de-flujo/README.md)
