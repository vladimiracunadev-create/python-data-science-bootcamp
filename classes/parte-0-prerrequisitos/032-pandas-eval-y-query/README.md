# Clase 032 — Pandas: eval y query

> Parte: **0 — Prerrequisitos** · Fuente: VanderPlas, **cap. 3** § 3.13 *High-Performance Pandas: eval and query*.
> ⏱️ Duración estimada: **45 min**.

---

## 🎯 Objetivo

Que el alumno conozca `df.eval` y `df.query` — herramientas para expresar operaciones y filtros con sintaxis tipo SQL en strings. Útiles para legibilidad en cadenas largas y, en datasets muy grandes, también más rápidos (usan `numexpr`).

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Filtrar** con `df.query("col > 10 and other == 'X'")`.
2. **Calcular columnas nuevas** con `df.eval('z = x + y')` o `df.eval('x * 2')`.
3. **Referenciar variables locales** en query/eval con prefijo `@`: `df.query('x > @threshold')`.
4. **Decidir** cuándo usar query (legibilidad en cadenas largas) vs filtro tradicional (mejor autocompletado IDE).
5. **Saber** que el speedup real solo aparece con datasets >10k filas y expresiones complejas.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | `df.query` — sintaxis tipo SQL | Una sola string en vez de máscara compuesta. |
| 2 | `df.eval` — expresiones aritméticas | Calcula columnas sin temporales. |
| 3 | Variables locales con `@` | Pasar valores del scope. |
| 4 | `numexpr` para speedup | Solo en datasets grandes. |
| 5 | Trade-off: legibilidad vs introspección IDE | Query strings no tienen autocompletado. |

## 📂 Dataset / recursos

Sintético: DataFrame grande para benchmark. Sin descarga.

## 🧪 Ejercicios

**1.** **Filter tradicional vs query.** `df[(df.a > 10) & (df.b < 5) & (df.c == 'x')]` vs `df.query('a > 10 and b < 5 and c == "x"')`. Compara legibilidad.

**2.** **Variable local.** `threshold = 100`; filtra con `df.query('precio > @threshold')`.

**3.** **eval para nueva columna.** `df.eval('total = precio * cantidad', inplace=True)`.

**4.** **Benchmark.** Genera df 1M filas. Compara filter tradicional vs query con `%timeit`.

**5.** **eval con `inplace=False`** vs cálculo tradicional `df['total'] = df['precio'] * df['cantidad']` — verifica resultados idénticos.

## 📝 Homework verificable

Notebook con df 100k filas: (a) 3 filtros equivalentes (mask, query, query con @var); (b) eval para crear 2 columnas derivadas; (c) benchmark tradicional vs query en N=100k y N=1M; (d) reporte: cuándo conviene cada uno.

**Criterio de aceptación:** Resultados idénticos entre métodos. Speedup de query aparece en N≥100k.

## 🔗 Referencias

- VanderPlas, **cap. 3** § 3.13.
- [pandas eval/query docs](https://pandas.pydata.org/docs/user_guide/enhancingperf.html)
- [`numexpr` project](https://numexpr.readthedocs.io/)

## ➡️ Siguiente clase

[Clase 033 — Matplotlib: anatomía figura/axes](../033-matplotlib-anatomia-figura-axes/README.md)
