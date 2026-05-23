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

## 📖 Definiciones y características

**Accessor `.str`**
: Espacio de nombres en Series con métodos string vectorizados. Análogos a los de Python (`.lower()`, `.split()`, `.replace()`) pero aplicados elementwise y NaN-aware (propagan NaN sin error).

**`.str.extract(pattern)`**
: Aplica regex con grupos `()` y devuelve DataFrame con una columna por grupo. Soporta grupos nombrados (`(?P<dominio>...)`).

**`.str.split(sep, expand=True)`**
: Divide cada string y opcionalmente expande a DataFrame de columnas. Útil para denormalizar 'Apellido, Nombre' → 2 cols.

**dtype `'string'` (nullable)**
: Versión moderna del dtype para texto. Diferencias con `object`: NA-aware (usa `pd.NA`), futuras optimizaciones. Recomendado en pandas 2+.

**`Categorical`**
: Dtype para columnas con cardinalidad baja (pocos valores únicos). Almacena cada valor como entero + diccionario. **Ahorra ~10× memoria** y acelera groupby/sort.

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

## ⚠️ Errores comunes

| Síntoma / mensaje | Causa y cómo arreglar |
|---|---|
| `'NoneType' has no attribute 'lower'` al hacer `s.apply(str.lower)` | Hay NaN/None en la Series. **Fix**: usa `.str.lower()` (accessor) — maneja NaN automáticamente. |
| Regex no captura nada con `.str.extract` | Falta `()` para definir grupo, o el pattern no matchea. **Fix**: testa el regex en https://regex101.com con un sample primero. |
| `.str.contains('foo')` lanza error con NaN | Por default, `na=NaN` propaga. **Fix**: `s.str.contains('foo', na=False)` trata NaN como False. |
| Convertí a `Categorical` y el sort sale alfabético | Categorical por default es no-ordenado. **Fix**: `pd.Categorical(s, categories=['bajo','medio','alto'], ordered=True)` para imponer orden. |
| `.str.split(',')` da listas, no columnas | Sin `expand=True`. **Fix**: `s.str.split(',', expand=True)` devuelve DataFrame con una columna por parte. |

## ❓ Preguntas frecuentes

**❓ ¿`.str.lower()` o `.apply(str.lower)`?**

**`.str.lower()`** siempre — vectorizado, maneja NaN, mucho más rápido en N grande. `apply` es loop Python disfrazado.

**❓ ¿Cuándo convertir a `Categorical`?**

Cuando la cardinalidad es baja (~<5% de N filas) y vas a hacer groupby/sort. Para 100k filas de 5 países: enorme ganancia. Para 100k filas de 80k strings únicos: no ayuda.

**❓ ¿`'string'` o `object` dtype?**

**`'string'`** para código nuevo (NA-aware). **`object`** sigue siendo default por compat. Conviértelo explícito: `df['col'] = df['col'].astype('string')`.

**❓ ¿Regex case-insensitive?**

`s.str.contains('foo', case=False)` o `flags=re.IGNORECASE`. También `s.str.lower().str.contains('foo')` (más explícito).

**❓ ¿Cómo elimino acentos?**

Pandas no trae nativo. Usa `unidecode` o `s.str.normalize('NFKD').str.encode('ascii', 'ignore').str.decode('ascii')`.

## 🔗 Referencias

- VanderPlas, **cap. 3** § 3.11.
- [pandas Text data user guide](https://pandas.pydata.org/docs/user_guide/text.html)
- [pandas Categorical](https://pandas.pydata.org/docs/user_guide/categorical.html)

## ➡️ Siguiente clase

[Clase 031 — Pandas: series de tiempo, resampling, rolling](../031-pandas-series-de-tiempo-resampling-rolling/README.md)
