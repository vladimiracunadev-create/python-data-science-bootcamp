# Clase 010 — OOP básico, dataclasses, herencia

> Parte: **0 — Prerrequisitos** · Fuente: Ramalho, *Fluent Python* 2e — caps. 5 (Data Class Builders) y 14 (Inheritance) · *Python Tutorial* cap. 9.
> ⏱️ Duración estimada: **90 min**.

---

## 🎯 Objetivo

Que el alumno escriba clases cuando aportan (no por hábito Java), use `@dataclass` para records sin boilerplate, entienda herencia con criterio (preferir composición), y conozca los métodos dunder más usados (`__repr__`, `__eq__`, `__lt__`, `__len__`).

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Definir clases** con `__init__`, atributos de instancia y métodos.
2. **Usar `@dataclass`** para records inmutables/mutables sin escribir `__init__`/`__repr__`/`__eq__`.
3. **Heredar** y sobreescribir métodos con `super()`.
4. **Implementar dunders esenciales**: `__repr__`, `__str__`, `__eq__`, `__lt__`, `__len__`, `__iter__`.
5. **Decidir** entre clase, dataclass o NamedTuple según el caso.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | Clase mínima: `__init__` + atributos + métodos | El bloque básico. |
| 2 | `@dataclass(frozen=True)` | Records inmutables sin boilerplate. |
| 3 | Herencia + `super()` | Reutilizar implementación de la clase base. |
| 4 | Composición > herencia | "Has-a" generalmente mejor que "is-a". |
| 5 | Métodos dunder | Integran tu clase con `len()`, `==`, `repr()`, `sorted()`. |
| 6 | `dataclass` vs `NamedTuple` vs `TypedDict` | Elegir según necesidad de mutabilidad/comportamiento. |

## 📂 Dataset / recursos

Sintético: lista de objetos `Punto` y `Estudiante`. Sin descarga.

## 🧪 Ejercicios

**1.** **Clase Punto.** Define `Punto(x, y)` con `__repr__`, `__eq__`, distancia al origen y `__add__` para sumar puntos.

**2.** **Dataclass Estudiante.** `@dataclass` con `nombre`, `notas: list[float]`, método `promedio()`. Crea 3 instancias, ordena por promedio.

**3.** **Frozen Vector.** `@dataclass(frozen=True)` para un vector 2D inmutable. Intenta modificar un atributo y observa la excepción.

**4.** **Herencia.** `Animal` con `hablar()` → `'genérico'`. `Perro(Animal)` que sobreescribe a `'guau'`. `Gato(Animal)` a `'miau'`.

**5.** **Composición.** `Coche` que tiene un `Motor` (composición) en vez de heredar de `Motor`. Justifica por qué.

## 📝 Homework verificable

Notebook con: (a) `Punto` con 4 dunders y tests; (b) `@dataclass Estudiante` con sort por promedio; (c) `@dataclass(frozen=True) Vector` que demuestra inmutabilidad lanzando excepción; (d) jerarquía `Animal → Perro/Gato` con polimorfismo (lista mixta llamando `hablar()`).

**Criterio de aceptación:** Las 4 clases pasan tests; `frozen=True` lanza `FrozenInstanceError` al asignar.

## 🔗 Referencias

- Ramalho, *Fluent Python* 2e — caps. 5, 11, 14.
- [`dataclasses` docs](https://docs.python.org/3/library/dataclasses.html)
- [Python Tutorial — Classes](https://docs.python.org/3/tutorial/classes.html)

## ➡️ Siguiente clase

[Clase 011 — pathlib, lectura y escritura de archivos](../011-pathlib-lectura-y-escritura-de-archivos/README.md)
