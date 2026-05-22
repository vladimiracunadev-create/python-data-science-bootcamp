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

## 🔗 Referencias

- [cookiecutter-data-science v2 docs](https://cookiecutter-data-science.drivendata.org/)
- Sculley et al., [*Hidden Technical Debt in ML Systems*](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) (NeurIPS 2015).
- [Palmer Penguins dataset](https://github.com/allisonhorst/palmerpenguins)

## ➡️ Siguiente clase

[Clase 005 — VS Code / Cursor para Python y Jupyter](../005-vs-code-cursor-para-python-y-jupyter/README.md)
