# Clase 011 — pathlib, lectura y escritura de archivos

> Parte: **0 — Prerrequisitos** · Fuente: *Python Tutorial* cap. 10 · `pathlib` docs · *Effective Python* (Slatkin) ítem 38.
> ⏱️ Duración estimada: **60 min**.

---

## 🎯 Objetivo

Que el alumno deje de usar `os.path.join` + strings y adopte `pathlib.Path` — API orientada a objetos, multiplataforma (Windows/Unix), con métodos legibles para todas las operaciones de filesystem que hace todo el tiempo en DS (leer CSV, listar archivos, crear carpetas).

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Construir paths** con `Path(...) / 'subdir' / 'file.csv'` (operador `/`).
2. **Leer/escribir** archivos texto y binarios con métodos de `Path` (`read_text`, `write_bytes`).
3. **Listar y filtrar** archivos con `iterdir`, `glob`, `rglob` (recursivo).
4. **Crear/eliminar** estructuras de directorios sin pelear con `os.makedirs(exist_ok=True)`.
5. **Manejar rutas relativas vs absolutas** y entender `__file__`.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | `Path` vs strings | Objetos con métodos > concatenación manual. |
| 2 | Operador `/` para componer | Legible y multiplataforma. |
| 3 | `read_text` / `write_text` / `read_bytes` | One-liners para operaciones simples. |
| 4 | `glob` y `rglob` | Patrones tipo shell: `*.csv`, `**/*.py`. |
| 5 | `mkdir(parents=True, exist_ok=True)` | Crea árbol completo idempotente. |
| 6 | `Path(__file__).parent` y `resolve()` | Localizar recursos relativos al script. |

## 📂 Dataset / recursos

Carpeta temporal creada en el notebook con archivos sintéticos. Sin descarga.

## 🧪 Ejercicios

**1.** **Construye una ruta multiplataforma.** Dado `Path.home() / 'datos' / '2026' / 'enero.csv'`, imprime cómo se ve en Windows vs Unix.

**2.** **Lista CSVs.** En una carpeta con archivos mixtos (.csv, .txt, .py), lista solo los `.csv` ordenados por tamaño.

**3.** **Búsqueda recursiva.** En un árbol de carpetas, encuentra todos los `.py` que contengan la palabra `TODO` en su contenido.

**4.** **Escribe + lee.** Genera 3 archivos `txt` con `write_text`, léelos con `read_text`, concaténalos en uno solo.

**5.** **Ruta del script.** Escribe un script que cargue un dataset que vive *al lado* del script (no del cwd), usando `Path(__file__).parent / 'data.csv'`.

## 📝 Homework verificable

Script `inventario.py` que recibe un directorio y produce un reporte CSV con: nombre, tamaño_bytes, extensión, última_modificación para cada archivo recursivamente, usando solo `pathlib` (no `os`).

**Criterio de aceptación:** El script corre tanto en Windows como en Linux/macOS sin cambios.

## 🔗 Referencias

- [`pathlib` docs](https://docs.python.org/3/library/pathlib.html)
- [PEP 428 — Object-oriented filesystem paths](https://peps.python.org/pep-0428/)
- Slatkin, *Effective Python* 2e — ítem 38 *Use Pathlib instead of os.path*.

## ➡️ Siguiente clase

[Clase 012 — Logging](../012-logging/README.md)
