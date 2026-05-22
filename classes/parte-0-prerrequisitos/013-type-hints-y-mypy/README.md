# Clase 013 — Type hints y mypy

> Parte: **0 — Prerrequisitos** · Fuente: *Fluent Python* 2e cap. 8 (Type Hints in Functions) · *typing* docs · mypy docs.
> ⏱️ Duración estimada: **75 min**.

---

## 🎯 Objetivo

Que el alumno anote tipos en sus funciones y dataclasses — no por dogma, sino porque permiten que el IDE autocomplete bien, que `mypy` detecte bugs antes de runtime, y que el lector entienda la intención. Tipos como **documentación verificable**.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Anotar** funciones con tipos en parámetros y retorno (`def f(x: int) -> str`).
2. **Usar tipos compuestos**: `list[int]`, `dict[str, float]`, `tuple[int, str]`, `Optional[X]`, `X | None`.
3. **Definir tipos personalizados** con `TypeAlias` y `Protocol` (structural typing).
4. **Ejecutar mypy** sobre código y interpretar sus errores.
5. **Reconocer** cuándo type hints aportan (APIs públicas, data classes) y cuándo no (notebooks exploratorios).

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | Sintaxis básica: `x: int`, `-> bool` | Solo anotaciones — no afectan runtime. |
| 2 | Tipos compuestos modernos (3.9+): `list[int]` | Sin `from typing import List`. |
| 3 | `Optional[X]` y `X | None` (3.10+) | Cuando algo puede ser None. |
| 4 | `Literal`, `TypedDict`, `Protocol` | Tipos avanzados útiles. |
| 5 | `mypy`: instalar y correr | Static type checker. |
| 6 | `reveal_type(x)` y `# type: ignore` | Diagnóstico y escape hatch. |
| 7 | Cuándo SÍ y cuándo NO | API pública sí; notebook exploratorio quizá no. |

## 📂 Dataset / recursos

Funciones de ejemplo en el notebook. Sin descarga.

## 🧪 Ejercicios

**1.** **Anota una función.** Toma una función de los ejercicios de clase 008 (sin tipos) y anótala completa.

**2.** **Optional vs default.** Distingue `def f(x: int = 0)` (default 0) de `def f(x: int | None = None)` (puede no haber valor).

**3.** **TypedDict.** Define `class PersonaDict(TypedDict)` con `nombre: str`, `edad: int`. Úsala como tipo de un parámetro.

**4.** **Corre mypy.** Instala mypy, créate un archivo con un bug de tipo intencional (`def f(x: int) -> str: return x + 1`) y corre `mypy archivo.py`. Lee y explica el error.

**5.** **Protocol.** Define `class TienePromedio(Protocol)` con método `promedio() -> float`. Acepta cualquier clase que lo implemente (duck typing tipado).

## 📝 Homework verificable

Repo con un módulo `analytics.py` (5+ funciones completamente anotadas), `pyproject.toml` que incluye mypy en `[tool.mypy]` con `strict = true`, y screenshot/log de `mypy analytics.py` sin errores.

**Criterio de aceptación:** `mypy --strict` corre sin errores ni warnings. Tipos consistentes y precisos.

## 🔗 Referencias

- Ramalho, *Fluent Python* 2e — cap. 8.
- [`typing` docs](https://docs.python.org/3/library/typing.html)
- [mypy docs](https://mypy.readthedocs.io/)
- [PEP 484 — Type Hints](https://peps.python.org/pep-0484/)
- [PEP 604 — `X | Y` syntax](https://peps.python.org/pep-0604/)

## ➡️ Siguiente clase

[Clase 014 — NumPy: tipos, creación, atributos](../014-numpy-tipos-creacion-atributos/README.md)
