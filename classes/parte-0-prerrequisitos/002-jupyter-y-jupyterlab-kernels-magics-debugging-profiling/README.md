# Clase 002 — Jupyter y JupyterLab — kernels, magics, debugging, profiling

> Parte: **0 — Prerrequisitos** · Fuente: VanderPlas, *Python Data Science Handbook*, **cap. 1** — IPython: Beyond Normal Python.
> ⏱️ Duración estimada: **90 min**.

---

## 🎯 Objetivo

Que el alumno deje de usar Jupyter como un editor de texto con botón "play" y empiece a usarlo como un entorno exploratorio profesional: con magics que ahorran horas, debugger interactivo (`%debug`), y profiling real (`%timeit`, `%prun`). Al final debe poder diagnosticar por qué un notebook es lento sin adivinar.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Diferenciar** kernel, frontend (Notebook vs JupyterLab vs VS Code) y servidor — y saber qué pasa cuando uno se cuelga.
2. **Usar magics esenciales:** `%timeit`, `%%time`, `%run`, `%load`, `%matplotlib inline`, `%debug`, `%who`, `%xmode`.
3. **Conectar un kernel específico** a un notebook (`ipykernel install --user --name <env>`) sin pelearse con el venv equivocado.
4. **Debuggear** una excepción con `%debug` y `pdb` (n, s, c, q, p, l).
5. **Profilar** código lento con `%timeit` (microbenchmark) y `%prun` (line profiler) para decidir dónde optimizar.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | Kernel ↔ frontend ↔ servidor | Saber cuál murió cuando el notebook se cuelga. |
| 2 | Modo comando vs modo edición + atajos | Velocidad real: A/B/X/M/Y/Esc/Enter. |
| 3 | Magics line (`%`) vs cell (`%%`) | El 80% del valor de Jupyter está en las magics. |
| 4 | `%timeit` y `%%time` | Microbenchmark riguroso (varias corridas, descarta outliers). |
| 5 | `%debug` + pdb | Inspección post-mortem sin re-correr todo el notebook. |
| 6 | `%prun` y `%lprun` | Saber qué función pesa antes de optimizar. |
| 7 | Registro de kernels por venv | Cada proyecto, su propio kernel — evita el bug `import` falla. |

## 📂 Dataset / recursos

No requiere dataset externo. Usamos arreglos sintéticos con `numpy.random` para benchmarks. Para el ejercicio de debug, generamos un `ValueError` intencional.

## 🧪 Ejercicios

**1.** **Atajos sin mouse.** Crea 5 celdas, navega solo con teclado: convierte 2 a markdown, ejecuta todo en orden, borra una, deshaz. Cronométrate.

**2.** **Registra tu kernel.** Desde un venv recién creado: `python -m ipykernel install --user --name ds-lab-001 --display-name 'DS Lab 001'`. Abre Jupyter, selecciona ese kernel, verifica con `import sys; sys.executable`.

**3.** **Benchmark vectorización.** Con `%timeit`, compara sumar `range(10_000)` con un `for` vs `np.arange(10_000).sum()`. Anota cuántas veces más rápido es NumPy.

**4.** **Post-mortem.** Provoca un `ZeroDivisionError`, luego ejecuta `%debug` en la siguiente celda y navega el stack con `u`/`d`, inspecciona variables con `p`.

**5.** **Profila una función.** Escribe una función que ordene una lista 1000 veces con sort burbuja. Ejecuta `%prun -s cumulative tu_func()`. Identifica la línea más cara.

## 📝 Homework verificable

Entrega un notebook `homework.ipynb` con: (a) celda que muestra `sys.executable` confirmando que usas un kernel registrado por ti; (b) benchmark `%timeit` comparando `sum(range(N))` vs `np.arange(N).sum()` para N=10k, 100k, 1M; (c) tabla markdown con los resultados; (d) gráfico simple del speedup.

**Criterio de aceptación:** El notebook abre con kernel propio (no el global), las 3 mediciones corren sin errores, y la conclusión incluye un número concreto ("NumPy es ~50× más rápido para N=1M").

## 🔗 Referencias

- VanderPlas, **cap. 1** — *IPython: Beyond Normal Python*.
- [IPython magics reference](https://ipython.readthedocs.io/en/stable/interactive/magics.html)
- [JupyterLab user guide](https://jupyterlab.readthedocs.io/)

## ➡️ Siguiente clase

[Clase 003 — Git y GitHub para data scientists](../003-git-y-github-para-data-scientists/README.md)
