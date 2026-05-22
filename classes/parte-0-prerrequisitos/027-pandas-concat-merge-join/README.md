# Clase 027 — Pandas: concat, merge, join

> Parte: **0 — Prerrequisitos** · Fuente: VanderPlas, **cap. 3** §§ 3.7–3.8 *Combining Datasets: Concat/Merge*.
> ⏱️ Duración estimada: **90 min**.

---

## 🎯 Objetivo

Que el alumno **junte datasets** correctamente: `concat` (apilado simple), `merge` (SQL-style joins) y `join` (atajo por index). El error más común es usar el join equivocado y obtener duplicados o filas perdidas — saber qué tipo (inner/left/right/outer) evita semanas de bugs.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Apilar** DataFrames con `pd.concat` por filas (`axis=0`) o columnas (`axis=1`).
2. **Hacer joins SQL-style** con `pd.merge`: inner, left, right, outer, cross.
3. **Diagnosticar** duplicados generados por merge con `validate='one_to_one' | 'many_to_one' | …`.
4. **Joinear por index** con `df1.join(df2)` (atajo para merge por index).
5. **Usar `indicator=True`** para saber qué filas vienen de cada lado del merge.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | `concat` axis=0 (filas) vs axis=1 (columnas) | Apilado simple con alineación de index. |
| 2 | `merge` how='inner'/'left'/'right'/'outer' | Los 4 tipos de join SQL. |
| 3 | `on` vs `left_on`/`right_on` | Cuando los nombres de columna difieren. |
| 4 | `validate` para evitar duplicación | 1:1, 1:m, m:1, m:m. |
| 5 | `indicator=True` para auditar | Columna `_merge` con left_only/right_only/both. |
| 6 | `df.join` por index | Atajo idiomático. |

## 📂 Dataset / recursos

Sintético: tabla de clientes + tabla de órdenes (relación 1:N).

## 🧪 Ejercicios

**1.** **Concat por filas.** 3 DataFrames mensuales con mismas columnas → uno anual. `ignore_index=True`.

**2.** **Inner join.** Clientes + órdenes por `cliente_id`. Verifica que solo aparecen clientes con al menos 1 orden.

**3.** **Left join.** Clientes + órdenes, conservando clientes sin órdenes (NaN en cols de orden).

**4.** **Detectar duplicados.** Provoca un merge muchos-a-muchos no intencional. Usa `validate='one_to_many'` para que falle si hay duplicación oculta.

**5.** **`indicator=True`.** Auditar cuántas filas son left_only / right_only / both.

## 📝 Homework verificable

Notebook con clientes (10) + órdenes (25): (a) 4 tipos de join con `_merge` indicator; (b) tabla con conteo de cada tipo; (c) detección de relación con `validate`; (d) join por index con `df.join`.

**Criterio de aceptación:** Counts de cada join coherentes (inner ≤ left ≤ outer). `validate` lanza excepción si la relación esperada falla.

## 🔗 Referencias

- VanderPlas, **cap. 3** §§ 3.7-3.8.
- [pandas Merge user guide](https://pandas.pydata.org/docs/user_guide/merging.html)

## ➡️ Siguiente clase

[Clase 028 — Pandas: groupby (split-apply-combine)](../028-pandas-groupby-split-apply-combine/README.md)
