# Clase 026 — Pandas: MultiIndex

> Parte: **0 — Prerrequisitos** · Fuente: VanderPlas, **cap. 3** § 3.6 *Hierarchical Indexing*.
> ⏱️ Duración estimada: **75 min**.

---

## 🎯 Objetivo

Que el alumno use índices jerárquicos (MultiIndex) cuando hay estructura natural en los datos (país × ciudad, año × mes, sector × empresa). Saber cuándo aporta vs cuándo complica — el 80% del tiempo en data science aplanado es mejor.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Crear MultiIndex** desde tuplas, arrays, producto cartesiano (`from_product`).
2. **Indexar** con `.loc[(nivel1, nivel2)]` y `.loc[:, ('grupo', 'col')]`.
3. **Aplanar y reconstruir** con `unstack()`, `stack()`, `reset_index()`.
4. **Decidir** cuándo MultiIndex aporta (groupby con múltiples claves devuelve uno automáticamente) y cuándo es más legible aplanar.
5. **Renombrar niveles** con `rename(level=...)` y reordenarlos con `swaplevel`.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | MultiIndex: motivación | Datos con jerarquía natural. |
| 2 | Construcción: tuples, arrays, from_product | 3 formas comunes. |
| 3 | Indexación: tuple selector | `.loc[('A', 2024)]`. |
| 4 | `stack` / `unstack` — pivot rápido | Mover niveles entre filas y columnas. |
| 5 | groupby + multiindex resultado | groupby con 2+ claves devuelve MultiIndex. |
| 6 | Cuándo aplanar | Para CSV de salida, plot, scikit-learn. |

## 📂 Dataset / recursos

Sintético: ventas por país/año.

## 🧪 Ejercicios

**1.** **Construye desde tuplas.** Crea DataFrame con index `[(España, 2023), (España, 2024), (Chile, 2023), (Chile, 2024)]` y 2 cols ventas/clientes.

**2.** **`from_product`.** Mismo con `pd.MultiIndex.from_product([paises, años])`.

**3.** **Acceso jerárquico.** `df.loc['España']`, `df.loc[('España', 2024)]`. Compara con `df.xs(2024, level=1)` para slice por nivel.

**4.** **`unstack` y `stack`.** Convierte tu MultiIndex en wide (años como columnas) y de vuelta.

**5.** **groupby produce MultiIndex.** Carga penguins, agrupa por `(species, sex)` y agrega `mean()`. Aplana con `reset_index()`.

## 📝 Homework verificable

Notebook con ventas trimestre×región sintéticas (4 trimestres × 3 regiones × 2 años): (a) construir con `from_product`; (b) acceso a un trimestre específico; (c) total por región (unstack); (d) groupby penguins por (species, sex) → MultiIndex → aplanar.

**Criterio de aceptación:** MultiIndex con shape correcto; unstack/stack reversibles.

## 🔗 Referencias

- VanderPlas, **cap. 3** § 3.6.
- [pandas MultiIndex user guide](https://pandas.pydata.org/docs/user_guide/advanced.html)

## ➡️ Siguiente clase

[Clase 027 — Pandas: concat, merge, join](../027-pandas-concat-merge-join/README.md)
