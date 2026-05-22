# Clase 022 — Pandas: Series y DataFrame

> Parte: **0 — Prerrequisitos** · Fuente: VanderPlas, **cap. 3**, §§ 3.1–3.2 *Introducing Pandas Objects*.
> ⏱️ Duración estimada: **90 min**.

---

## 🎯 Objetivo

Que el alumno entienda **qué es** una `Series` (ndarray + index) y un `DataFrame` (dict de Series alineadas por index), cómo se construyen desde 5 fuentes distintas, y por qué el **index** es el rasgo que distingue pandas de NumPy.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Crear Series y DataFrames** desde dict, lista de tuplas, arrays NumPy, CSV y desde otro DataFrame.
2. **Inspeccionar** un DataFrame con `head`, `tail`, `info`, `describe`, `dtypes`, `shape`.
3. **Acceder** a columnas como atributo (`df.col`) y como key (`df['col']`) — y saber cuándo cada uno falla.
4. **Modificar el index** con `set_index`, `reset_index`, `rename`.
5. **Convertir** Series ↔ DataFrame ↔ ndarray cuando sea necesario.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | Series = ndarray + index | Index permite alineación automática. |
| 2 | DataFrame = dict de Series alineadas | Por eso `df['col']` devuelve Series. |
| 3 | Construcción desde 5 fuentes | dict, lista de dicts, arrays, CSV, Series. |
| 4 | `.loc` vs `.iloc` vs `[]` | Tres formas de acceso. |
| 5 | Index labels vs posición | El bug clásico cuando el index no es 0..N. |
| 6 | `info` y `describe` como first-look | Lo primero que mira un DS. |

## 📂 Dataset / recursos

Palmer Penguins (descargable con seaborn/palmerpenguins) — 344 filas × 7 columnas, públicas, sin issues de licencia. Reemplaza al iris dataset.

## 🧪 Ejercicios

**1.** **Series desde dict.** Crea Series con población de 5 ciudades. Accede por label y por posición.

**2.** **DataFrame desde dict de listas.** Construye DataFrame de 5 estudiantes (nombre, edad, nota). Inspecciona con `info()` y `describe()`.

**3.** **Lee Palmer Penguins.** `pd.read_csv` desde URL pública. Reporta shape, dtypes, % de NaN por columna.

**4.** **Index labeled.** Setea `species` como index. Compara `df.loc['Adelie']` vs `df.iloc[0]`.

**5.** **Alineación automática.** Crea 2 Series con index parcialmente solapado. Súmalas. Observa los NaN.

## 📝 Homework verificable

Notebook que: (a) carga Palmer Penguins y reporta `info()`, `describe()`, missing por col; (b) muestra los 3 métodos de acceso a una columna (`df.col`, `df['col']`, `df.loc[:, 'col']`); (c) cambia el index a `species`, vuelve a default con `reset_index`; (d) demuestra alineación automática sumando dos Series.

**Criterio de aceptación:** Carga sin error, los 3 accesos producen la misma Series, alineación produce NaN donde corresponde.

## 🔗 Referencias

- VanderPlas, **cap. 3** §§ 3.1, 3.2.
- [pandas user guide — DataFrame](https://pandas.pydata.org/docs/user_guide/dsintro.html)
- [Palmer Penguins](https://github.com/allisonhorst/palmerpenguins)

## ➡️ Siguiente clase

[Clase 023 — Pandas: indexación (loc, iloc, at, iat)](../023-pandas-indexacion-loc-iloc-at-iat/README.md)
