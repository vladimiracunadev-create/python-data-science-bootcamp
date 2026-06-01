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

## 📌 Complemento: Formatos columnares (Parquet, Arrow, Feather)

Los formatos columnares almacenan los datos por columna en lugar de por fila, lo que permite **compresión 5-10× mayor** que CSV, **lectura selectiva de columnas** (no cargás todo el archivo para leer 2 columnas), y **tipos preservados** (no perdés `datetime`, `int64` vs `float`, ni `category`). Son el estándar de facto en data lakes modernos, Spark, DuckDB, Polars y todo el ecosistema de data engineering.

| Aspecto | CSV | Parquet | Feather / Arrow IPC |
|---|---|---|---|
| Tamaño típico (mismo dataset) | 100% (baseline) | 10-20% | 30-50% |
| Velocidad de lectura | Lenta (parseo de texto) | Muy rápida | Máxima (memory-mapped) |
| Tipado | Se pierde (todo string) | Preservado + schema | Preservado + schema |
| Streaming / lectura parcial | Línea a línea | Por row group y columna | Por record batch |
| Herramientas que lo leen | Todas (incluso Excel) | pandas, Spark, DuckDB, Polars | pandas, R, Arrow ecosystem |

Mini-ejemplo (requiere `pip install pyarrow`):

```python
import pandas as pd
from pathlib import Path

df = pd.DataFrame({"id": [1, 2, 3], "fecha": pd.to_datetime(["2026-01-01", "2026-01-02", "2026-01-03"])})

# Parquet — almacenamiento y data lake
df.to_parquet(Path("data") / "ventas.parquet")
df2 = pd.read_parquet(Path("data") / "ventas.parquet", columns=["id"])  # solo lee 1 columna

# Feather (Arrow IPC) — cache rápido entre procesos
df.to_feather(Path("data") / "ventas.feather")
df3 = pd.read_feather(Path("data") / "ventas.feather")
```

**¿Cuándo usar cada uno?** **CSV** cuando tenés que intercambiar con humanos, Excel o sistemas legacy — es feo pero universal. **Parquet** para almacenamiento permanente, particionado por fecha en data lakes, o cualquier dataset que vas a releer varias veces. **Feather/Arrow IPC** para cache temporal entre procesos Python (o entre Python y R) donde priorizás velocidad bruta sobre compresión.

> Nota: desde pandas 2.0 podés usar Arrow como backend de tipos con `pd.read_parquet(..., dtype_backend="pyarrow")` — obtenés `string[pyarrow]` en lugar de `object`, menos memoria y operaciones más rápidas.

## 📖 Definiciones y características

**`Path`**
: Objeto que representa una ruta de filesystem orientada a objetos (`pathlib.Path`). Sobreescribe `/` para componer rutas, multiplataforma (Windows usa `\`, Unix `/`, transparente). Tiene métodos para casi todo: leer, escribir, listar, mover, borrar.

**Ruta absoluta vs relativa**
: **Absoluta**: empieza desde la raíz (`C:\dev\proyecto\data.csv` o `/home/user/data.csv`). **Relativa**: parte del cwd (`data.csv`). Las rutas relativas dependen de dónde se ejecuta — fuente de bugs.

**`Path.cwd()` vs `Path(__file__).parent`**
: `cwd()` es el directorio donde se ejecutó el script (cambia según el invocante). `__file__` es la ruta al archivo Python actual; `.parent` su carpeta. **Usa `__file__`** para recursos que viven junto al script.

**`glob` vs `rglob`**
: Patrones tipo shell. `glob('*.csv')` busca en el directorio actual (1 nivel). `rglob('*.csv')` busca recursivo (todo el árbol). `**` significa 'cualquier número de directorios'.

**`read_text` / `write_text`**
: One-liners para texto: `Path('x.txt').write_text(contenido, encoding='utf-8')`. Para binario: `read_bytes` / `write_bytes`. Para JSON/CSV usa librerías especializadas.

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

## ⚠️ Errores comunes

| Síntoma / mensaje | Causa y cómo arreglar |
|---|---|
| `FileNotFoundError` aunque el archivo existe | Estás usando ruta relativa y el cwd no es el que crees. **Fix**: `print(Path.cwd())` para diagnosticar; usa rutas relativas a `__file__` para archivos del proyecto. |
| `PermissionError` al escribir | Carpeta read-only, OneDrive sincronizando, antivirus bloqueando. **Fix**: chequea permisos con `p.stat()`, escribe a `tempfile.gettempdir()` para tests. |
| `mkdir()` falla si el directorio ya existe | Default es `exist_ok=False`. **Fix**: `p.mkdir(parents=True, exist_ok=True)` — crea árbol completo idempotente. |
| Mezclo `os.path` y `pathlib` | Algunos funciones esperan strings (`open()`, `pd.read_csv()`). Path soporta el protocolo `os.PathLike` y la mayoría las acepta directo; si no, `str(p)` lo convierte. |
| `glob('*.CSV')` no encuentra `archivo.csv` | Case-sensitive en Linux, insensible en Windows. **Fix**: filtra explícito con `[p for p in path.iterdir() if p.suffix.lower() == '.csv']`. |
| `ImportError: Missing optional dependency 'pyarrow'` al llamar `to_parquet`/`to_feather` | pandas delega Parquet/Arrow a `pyarrow` (o `fastparquet`), no viene de fábrica. **Fix**: `pip install pyarrow`. Bonus: confirmá que tu venv es el correcto (`which python` / `where python`). |

## ❓ Preguntas frecuentes

**❓ ¿`pathlib` o `os.path`?**

**`pathlib`** para código nuevo. `os.path` es la API funcional vieja (strings + funciones); pathlib es OO y mucho más legible. Solo usa `os.path` para compatibilidad con código viejo.

**❓ ¿Cómo evito el típico `'C:/Users/...'` vs `'/home/...'` cross-platform?**

**No hardcodees rutas absolutas.** Usa `Path.home()`, `Path(__file__).parent`, `tempfile.gettempdir()`. Y siempre `Path` + `/`, nunca strings concatenados.

**❓ ¿Cómo leo un CSV grande con pathlib?**

Pathlib es para *paths*, no parsing. Combina: `pd.read_csv(Path('data') / 'big.csv')`. El Path se convierte a string automáticamente.

**❓ ¿`Path('a') / 'b/c'` o `Path('a') / 'b' / 'c'`?**

Ambas funcionan: `Path` parsea separadores. Pero la primera es menos explícita; prefiere la segunda.

**❓ ¿`shutil` o `pathlib` para mover/copiar?**

**`shutil`** para operaciones recursivas (copytree, rmtree, move) — pathlib solo cubre operaciones simples. Combinable: `shutil.copy(src_path, dst_path)` acepta Path directo.

**❓ ¿Cuándo dejo de usar CSV?**

Regla práctica: **CSV solo para intercambio con no-técnicos** (alguien lo va a abrir en Excel o mandarlo por mail). Para cualquier dataset >100 MB, o uno que vas a releer más de una vez en tu pipeline, pasalo a **Parquet**: ahorrás disco, ganás velocidad de lectura y no perdés tipos. Si lo único que querés es cachear un DataFrame entre dos scripts de la misma máquina, usá **Feather**.

## 🔗 Referencias

- [`pathlib` docs](https://docs.python.org/3/library/pathlib.html)
- [PEP 428 — Object-oriented filesystem paths](https://peps.python.org/pep-0428/)
- Slatkin, *Effective Python* 2e — ítem 38 *Use Pathlib instead of os.path*.
- [Apache Arrow / Parquet](https://arrow.apache.org/docs/python/parquet.html)

## ➡️ Siguiente clase

[Clase 012 — Logging](../012-logging/README.md)
