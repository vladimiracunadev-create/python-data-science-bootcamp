# Clase 024 — Pandas: operaciones y alineación

> Parte: **0 — Prerrequisitos** · Fuente: VanderPlas, **cap. 3** § 3.4 *Operating on Data in Pandas*.
> ⏱️ Duración estimada: **60 min**.

---

## 🎯 Objetivo

Que el alumno entienda cómo pandas **alinea automáticamente por index** en operaciones entre Series/DataFrames, cómo manejar NaN resultantes, y use `apply`/`map` para transformaciones custom (con consciencia de cuándo es lento).

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Predecir** el resultado de operar dos Series/DataFrames con indexes parcialmente distintos.
2. **Usar `fill_value`** en operaciones para no propagar NaN: `s1.add(s2, fill_value=0)`.
3. **Aplicar funciones** con `apply` (lento, flexible), `map` (Series), `applymap` / `df.map` (elementwise).
4. **Vectorizar** transformaciones cuando se puede en vez de `apply` (10–100× más rápido).
5. **Usar ufuncs NumPy** sobre Series — pandas las soporta directamente y preserva el index.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | Alineación automática por index | Producto, suma, todo — pandas alinea, no asume orden. |
| 2 | `fill_value` para operaciones | Reemplaza el NaN antes de calcular. |
| 3 | `apply` axis=0 vs axis=1 | Por columna vs por fila — costoso en filas. |
| 4 | `map` para Series con dict | `s.map({'A': 1, 'B': 2})`. |
| 5 | `df.map` (era `applymap`) — elementwise | Cell-by-cell, lento. |
| 6 | Vectorización > apply | Si puedes hacerlo con ufunc, hazlo. |

## 📂 Dataset / recursos

Sintético + Palmer Penguins. Sin descarga adicional.

## 🧪 Ejercicios

**1.** **Suma con alineación.** Dos Series con index parcialmente solapado. Súmalas (default) y con `fill_value=0`.

**2.** **`apply` por fila.** Define una función que reciba una fila de penguins y devuelva BMI = body_mass / bill_length². Aplica con `axis=1`.

**3.** **Mismo cálculo vectorizado.** Implementa BMI con operaciones vectorizadas. Mide ambos con `%timeit`.

**4.** **`map` con dict.** Mapea `species` a códigos: `{'Adelie': 0, 'Chinstrap': 1, 'Gentoo': 2}`.

**5.** **ufunc NumPy preserva index.** Aplica `np.log` a una columna; verifica que el index sigue intacto.

## 📝 Homework verificable

Notebook con penguins: (a) BMI por fila con `apply` vs vectorizado (tabla `%timeit`); (b) species → código numérico con `map`; (c) demo de alineación con `fill_value`; (d) `np.log` sobre body_mass preservando index.

**Criterio de aceptación:** Vectorizado >50× más rápido que apply. Mapping y alineación correctos.

## 🔗 Referencias

- VanderPlas, **cap. 3** § 3.4.
- [pandas — apply, map](https://pandas.pydata.org/docs/user_guide/basics.html#function-application)

## ➡️ Siguiente clase

[Clase 025 — Pandas: datos faltantes](../025-pandas-datos-faltantes/README.md)
