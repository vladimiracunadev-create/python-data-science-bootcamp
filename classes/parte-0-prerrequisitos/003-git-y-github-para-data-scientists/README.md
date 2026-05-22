# Clase 003 — Git y GitHub para data scientists

> Parte: **0 — Prerrequisitos** · Fuente: Pro Git (Chacon & Straub) — caps. 2 y 3 · GitHub docs.
> ⏱️ Duración estimada: **120 min**.

---

## 🎯 Objetivo

Que el alumno use git no como "botón save" sino como un sistema serio de versionado: commits atómicos con mensajes útiles, branches por feature, PRs con review, y resolución de conflictos sin pánico. Adicionalmente: ignorar correctamente los archivos típicos de DS (datos pesados, notebooks con output, secrets).

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Inicializar** un repo, hacer commits atómicos con mensajes en formato convencional.
2. **Trabajar con branches**: crear, cambiar, mergear y resolver un conflicto sin perder código.
3. **Configurar `.gitignore`** para un proyecto de DS (datos, `.venv`, secrets, outputs de notebooks).
4. **Abrir y revisar un PR en GitHub** desde la línea de comandos con `gh`.
5. **Recuperar** trabajo perdido con `git reflog` (la red de seguridad invisible).

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | Modelo de git: working tree → staging → repo → remote | Sin este modelo mental, todo parece magia. |
| 2 | Commits atómicos + mensajes convencionales | Un commit = un cambio lógico revertible. |
| 3 | Branches y merge vs rebase | Cuándo usar cada uno; por qué no rebasear ramas públicas. |
| 4 | `.gitignore` para data science | Datos, modelos, notebooks con output, `.env` no van al repo. |
| 5 | Conflictos: anatomía y resolución | `<<<<<<<`, `=======`, `>>>>>>>` y cómo no entrar en pánico. |
| 6 | Pull Requests + review en GitHub | El review es donde se transfiere conocimiento. |
| 7 | `git reflog` — la red de seguridad | Aunque borres una rama, los commits viven 90 días. |

## 📂 Dataset / recursos

No requiere dataset. El "dataset" son los propios cambios que el alumno hace en archivos de prueba. Para el ejercicio del `.gitignore`, simulamos archivos típicos de DS (csv pesado, `.env`, `.ipynb_checkpoints/`).

## 🧪 Ejercicios

**1.** **Repo desde cero.** `git init`, crea 3 archivos (`README.md`, `data.csv`, `notebook.ipynb`), haz 3 commits con mensajes en formato `tipo: descripción` (feat/fix/docs/chore).

**2.** **Branch + conflicto.** Crea rama `feature/x`, modifica una línea en `README.md`. Vuelve a `main`, modifica la **misma línea** distinto. Mergea, resuelve el conflicto a mano.

**3.** **`.gitignore` profesional.** Genera uno que ignore: `.venv/`, `__pycache__/`, `.ipynb_checkpoints/`, `*.csv` en `data/raw/`, `.env`, `models/*.pkl`. Verifica con `git status` que no aparecen.

**4.** **PR desde la CLI.** Crea repo en GitHub (con `gh repo create`), push, crea PR con `gh pr create` y descripción no trivial.

**5.** **Recuperación.** Borra una rama con commits. Recupera el HEAD con `git reflog` + `git checkout <sha>` + `git switch -c rescate`.

## 📝 Homework verificable

Repo público en GitHub con: 5+ commits en formato convencional, al menos 1 branch mergeada, un `.gitignore` de DS completo, README con badges (build status si aplica) y un PR cerrado.

**Criterio de aceptación:** El historial (`git log --oneline`) se lee como cambios atómicos coherentes. `git status` limpio después de un experimento. PR mergeado con descripción legible.

## 🔗 Referencias

- [Pro Git book](https://git-scm.com/book) — cap. 2 *Git Basics*, cap. 3 *Branching*.
- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub CLI manual](https://cli.github.com/manual/)

## ➡️ Siguiente clase

[Clase 004 — Estructura reproducible de proyecto](../004-estructura-reproducible-de-proyecto-cookiecutter-data-science/README.md)
