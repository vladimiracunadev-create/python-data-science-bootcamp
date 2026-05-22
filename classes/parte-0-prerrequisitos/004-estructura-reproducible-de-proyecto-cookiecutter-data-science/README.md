# Clase 004 — Estructura reproducible de proyecto (cookiecutter-data-science)

> Parte: **0 — Prerrequisitos** · Fuente: cookiecutter-data-science v2 · *Hidden Technical Debt in ML Systems* (Sculley et al., 2015).
> ⏱️ Duración estimada: **60 min**.

---

## 🎯 Objetivo

Que el alumno deje de crear proyectos como "una carpeta con notebooks" y empiece a usar una estructura estándar que separa código, datos, modelos, notebooks de exploración y documentación. Esto no es estética — es lo que permite que un compañero entienda el proyecto en 5 minutos y que el código viva más allá del notebook donde nació.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Generar** un proyecto con la plantilla `cookiecutter-data-science` (CCDS v2).
2. **Justificar** la separación `data/raw` (inmutable) ↔ `data/interim` ↔ `data/processed`.
3. **Mover código** de un notebook a `src/` cuando deja de ser exploratorio.
4. **Documentar** dependencias en `pyproject.toml` (no en `requirements.txt` suelto).
5. **Reconocer** los olores de un proyecto mal estructurado (notebooks con números 01/02/03, código duplicado, datos en git).

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | Estructura CCDS v2 | Convención > improvisación. |
| 2 | `data/raw` es sagrado | Nunca se modifica; siempre se puede regenerar todo desde ahí. |
| 3 | `notebooks/` vs `src/` | Exploración vs producción. |
| 4 | `pyproject.toml` como fuente de verdad de deps | Reemplaza `requirements.txt` suelto. |
| 5 | `Makefile` como interfaz | `make data`, `make train`, `make test` — lo lee humano y máquina. |
| 6 | Olores típicos | `Untitled27.ipynb`, datos en git, `final_FINAL_v2.py`. |

## 📖 Definiciones y características

**Cookiecutter**
: Generador de proyectos a partir de plantillas. Tomas una plantilla (URL de un repo), respondes 3-5 preguntas y obtienes un proyecto con estructura pre-armada. Característica: idempotente — la plantilla no sabe ni le importa el contenido futuro del proyecto.

**CCDS (cookiecutter-data-science)**
: Plantilla específica para proyectos de DS, v2 (2023+). Separa `data/raw`, `data/interim`, `data/processed`, `src/`, `notebooks/`, `reports/`, `docs/`. Es **convención**, no dogma.

**Editable install (`pip install -e .`)**
: Instala el paquete pero apuntando al código fuente — los cambios se reflejan sin reinstalar. Habilita `from mi_proyecto.features import x` desde notebooks dentro del repo.

**`pyproject.toml`**
: Estándar moderno (PEP 621) para metadata + dependencias + config de tools (ruff, mypy, pytest). Reemplaza `setup.py` + `setup.cfg` + `requirements.txt` suelto + configs sueltas.

**`Makefile`**
: Archivo con "recetas" nombradas (`make data`, `make train`). Escrito en tabs (no espacios), las dependencias se declaran arriba (`target: dep1 dep2`). En proyectos DS funciona como interfaz humana a comandos típicos.

## 📂 Dataset / recursos

Para el ejercicio principal, descarga el dataset de Palmer Penguins (https://github.com/allisonhorst/palmerpenguins) — pequeño (~13 KB), público, ideal para que `data/raw/penguins.csv` ocupe poco y se pueda commitear sin mala práctica.

## 🧪 Ejercicios

**1.** **Genera un proyecto CCDS.** `pipx run cookiecutter https://github.com/drivendataorg/cookiecutter-data-science` con nombre `ds-lab-004`. Explora la estructura.

**2.** **Mueve código a `src/`.** Toma una función de un notebook tuyo previo y muévela a `src/<proyecto>/features.py`. Importa desde el notebook con `from <proyecto>.features import …`.

**3.** **Convierte `requirements.txt` a `pyproject.toml`** (sección `[project.dependencies]`).

**4.** **Refactoriza un notebook caótico.** Toma uno con bloques copy-paste y extrae 2 funciones a `src/`.

**5.** **Lista 5 olores** en un repo público que conozcas y propón cómo arreglarlos.

## 📝 Homework verificable

Un repo público con estructura CCDS, `data/raw/` con un dataset pequeño, al menos 1 notebook que importa funciones desde `src/`, `pyproject.toml` con deps, Makefile con `make setup` y `make data`.

**Criterio de aceptación:** Un compañero clona, corre `make setup && make data` y obtiene la misma estructura de datos procesados que tú reportaste. README explica el flujo.

## ⚠️ Errores comunes

| Síntoma / mensaje | Causa y cómo arreglar |
|---|---|
| `ModuleNotFoundError: No module named 'mi_proyecto'` al importar desde notebook | El paquete no está instalado en el venv del kernel. **Fix**: con el venv activo, `pip install -e .` desde la raíz del proyecto (necesita `pyproject.toml` con `[project] name='mi_proyecto'`). |
| CSV en `data/raw/` apareció en `git status` y pesa 200 MB | El `.gitignore` no cubre `data/raw/*` o no se aplicó a tiempo. **Fix**: añade `data/raw/*` al `.gitignore` + `!data/raw/.gitkeep` (mantén placeholder); si ya commiteaste, `git rm --cached data/raw/customers.csv`. |
| Tengo 3 notebooks con la misma función `limpiar_fechas` | Copy-paste. **Fix**: extrae a `src/mi_proyecto/features/cleaning.py` y haz `from mi_proyecto.features.cleaning import limpiar_fechas` en cada notebook. Si modificas la función, todos los notebooks la heredan. |
| El compañero clonó el repo y `make data` falla con "command not found" | Make no está instalado en Windows por default. **Fix**: instalar make (Git Bash trae uno) o documentar el comando equivalente en README; alternativamente, usa scripts Python directos. |
| Edité `pyproject.toml` y los imports siguen viejos | Tras cambios en metadata o entry-points debes reinstalar. **Fix**: `pip install -e . --force-reinstall --no-deps` (sin deps si no las cambiaste). |

## ❓ Preguntas frecuentes

**❓ ¿Realmente necesito una plantilla? ¿No puedo improvisar?**

Puedes, pero perderás el 80% de la ganancia: el compañero que ya conoce CCDS sabe dónde buscar; sin plantilla, cada proyecto es una caja de sorpresas.

**❓ ¿`data/raw/` o `data/01_raw/`?**

CCDS v2 usa `data/raw/`, `data/interim/`, `data/processed/`, `data/external/`. La numeración `01_/02_/03_` la verás en Kedro y en algunas variantes — ambas son válidas, sigue una sola convención por proyecto.

**❓ ¿`requirements.txt` o `pyproject.toml`?**

**`pyproject.toml`** para declarar las deps de tu paquete. **`requirements.txt`** (generado con `pip freeze` o `uv pip compile`) es el **lockfile** con versiones exactas para reproducir. No están en conflicto; conviven.

**❓ ¿Y si el proyecto es solo un notebook exploratorio?**

No fuerces CCDS. Carpeta con `notebook.ipynb`, `data.csv` y `README.md` está bien. La estructura completa aporta cuando el proyecto vive >3 meses o tiene >1 persona.

**❓ ¿Por qué los notebooks tienen prefijo numérico como `0.01-jvp-eda.ipynb`?**

Convención CCDS: `<fase>.<orden>-<iniciales>-<tema>`. Fase 0=exploración, 1=features, 2=modelos, 3=reportes. Iniciales del autor evitan conflictos cuando varias personas crean notebooks.

## 🔗 Referencias

- [cookiecutter-data-science v2 docs](https://cookiecutter-data-science.drivendata.org/)
- Sculley et al., [*Hidden Technical Debt in ML Systems*](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) (NeurIPS 2015).
- [Palmer Penguins dataset](https://github.com/allisonhorst/palmerpenguins)

## ➡️ Siguiente clase

[Clase 005 — VS Code / Cursor para Python y Jupyter](../005-vs-code-cursor-para-python-y-jupyter/README.md)
