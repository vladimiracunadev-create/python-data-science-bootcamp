# Clase 030 — Pandas: operaciones vectorizadas sobre strings

> Parte: **0 — Prerrequisitos** · Fuente: VanderPlas, **cap. 3** § 3.11 *Vectorized String Operations*.
> ⏱️ Duración estimada: **60 min**.

---

## 🎯 Objetivo

Que el alumno limpie y transforme columnas de texto sin caer en `apply(lambda x: ...)`, usando el accessor `.str` de pandas — vectorizado, NaN-aware, con métodos análogos a los de Python (`lower`, `strip`, `replace`, `split`, `contains`, regex).

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Usar `.str`** para aplicar operaciones de string vectorizadamente a una Series.
2. **Manejar NaN automáticamente** (los métodos `.str` propagan NaN sin error).
3. **Aplicar regex** con `.str.contains(patron)`, `.str.extract(...)`, `.str.replace(...)`.
4. **Dividir y unir** con `.str.split(sep, expand=True)` que produce un DataFrame.
5. **Trabajar con categorical** cuando el cardinalidad es baja (memoria y speedup).

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | Accessor `.str` | Métodos vectorizados que respetan NaN. |
| 2 | Casos típicos: lower, strip, replace, contains | El 80% del trabajo. |
| 3 | Regex con `.str.extract` y grupos nombrados | Extracción estructurada. |
| 4 | `.str.split(expand=True)` → DataFrame | Desnormalizar columnas combinadas. |
| 5 | `dtype='string'` (nullable) vs object | El moderno y NA-aware. |
| 6 | `Categorical` para baja cardinalidad | Menos memoria, groupby más rápido. |

## 📂 Dataset / recursos

Sintético: emails, nombres con espacios, fechas como string.

## 🧪 Ejercicios

**1.** **Lower + strip.** Lista de emails con mayúsculas y espacios. Normaliza con `.str.lower().str.strip()`.

**2.** **Extract dominio.** De una columna de emails, extrae el dominio con regex (`@(.+)$`).

**3.** **Split nombre completo.** Columna `'Ana García'` → `nombre`, `apellido` en columnas separadas.

**4.** **Filtro por contains.** Filas donde la columna `descripcion` contiene la palabra (case-insensitive) `'urgente'`.

**5.** **Categorical.** Convierte una columna con 5 valores únicos en 100k filas a `Categorical`. Compara memoria.

## 📝 Homework verificable

Notebook con CSV sintético de contactos (nombre, email, teléfono): (a) normalizar email (lower+strip); (b) extraer dominio; (c) separar nombre/apellido; (d) flag de email corporativo (no gmail/yahoo/hotmail); (e) convertir país a Categorical y reportar memoria.

**Criterio de aceptación:** Operaciones manejan NaN sin error. Categorical reduce memoria al menos 5×.

## 🔗 Referencias

- VanderPlas, **cap. 3** § 3.11.
- [pandas Text data user guide](https://pandas.pydata.org/docs/user_guide/text.html)
- [pandas Categorical](https://pandas.pydata.org/docs/user_guide/categorical.html)

## ➡️ Siguiente clase

[Clase 031 — Pandas: series de tiempo, resampling, rolling](../031-pandas-series-de-tiempo-resampling-rolling/README.md)
