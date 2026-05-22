# Clase 023 — Pandas: indexación (loc, iloc, at, iat)

> Parte: **0 — Prerrequisitos** · Fuente: VanderPlas, **cap. 3** § 3.3 *Data Indexing and Selection*.
> ⏱️ Duración estimada: **75 min**.

---

## 🎯 Objetivo

Que el alumno **domine los 4 indexers** de pandas y elija el correcto según el caso. El bug "`SettingWithCopyWarning`" y el bug del slicing por label inclusivo nacen aquí — saber qué indexer usar evita ambos.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Usar `.loc[row_label, col_label]`** para acceso por etiqueta (inclusivo en slicing).
2. **Usar `.iloc[row_pos, col_pos]`** para acceso por posición entera (exclusivo, como Python).
3. **Usar `.at` / `.iat`** para acceso a un único valor (más rápido que loc/iloc).
4. **Evitar `SettingWithCopyWarning`** usando `.loc` para asignar en una vista.
5. **Filtrar filas con boolean mask** dentro de `.loc`: `df.loc[df['edad'] > 30, 'nombre']`.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | `[]` directo: shortcut con quirks | Columnas → Series; filas → KeyError. |
| 2 | `.loc`: por label, slicing inclusivo | El indexer principal del 80% del tiempo. |
| 3 | `.iloc`: por posición, slicing exclusivo (como Python) | Cuando no te importa el label. |
| 4 | `.at` / `.iat`: single value | Optimizado para 1 celda — útil en loops. |
| 5 | Mask + loc para filtros con asignación | `df.loc[mask, 'col'] = valor`. |
| 6 | `SettingWithCopyWarning`: qué es y cómo evitarlo | Usar `.loc` para asignar. |

## 📂 Dataset / recursos

Palmer Penguins desde URL (mismo de clase 022) o el sintético si no hay internet.

## 🧪 Ejercicios

**1.** **Acceso simple.** Carga penguins. Obtén la columna `species` con los 3 métodos: `df.species`, `df['species']`, `df.loc[:, 'species']`.

**2.** **loc inclusivo vs iloc exclusivo.** Con index 0..N por default, compara `df.loc[0:5]` vs `df.iloc[0:5]`. ¿Cuántas filas devuelve cada uno?

**3.** **Filtro + columnas seleccionadas.** Pingüinos Adelie machos con bill_length > 40: `df.loc[(df.species=='Adelie') & (df.sex=='male') & (df.bill_length_mm > 40), ['species', 'island', 'bill_length_mm']]`.

**4.** **Asignación segura.** Crea una columna `is_big` que sea True si `body_mass_g > 4500`, usando `.loc`.

**5.** **Provoca y arregla SettingWithCopyWarning.** Slicea con `df[df.x > 0]` y modifica → ve warning. Hazlo con `.loc` → sin warning.

## 📝 Homework verificable

Notebook que: (a) muestra los 3 métodos de acceso a columna; (b) compara loc vs iloc en slicing con tabla; (c) filtra Adelie machos con bill_length>40 mostrando 3 columnas; (d) reproduce y arregla SettingWithCopyWarning con explicación.

**Criterio de aceptación:** Los filtros producen el subset correcto; la versión con `.loc` no emite warning.

## 🔗 Referencias

- VanderPlas, **cap. 3** § 3.3.
- [pandas Indexing user guide](https://pandas.pydata.org/docs/user_guide/indexing.html)
- [SettingWithCopyWarning explained](https://pandas.pydata.org/docs/user_guide/indexing.html#returning-a-view-versus-a-copy)

## ➡️ Siguiente clase

[Clase 024 — Pandas: operaciones y alineación](../024-pandas-operaciones-y-alineacion/README.md)
