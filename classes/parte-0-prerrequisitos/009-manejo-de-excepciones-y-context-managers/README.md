# Clase 009 — Manejo de excepciones y context managers

> Parte: **0 — Prerrequisitos** · Fuente: *Python Tutorial* cap. 8 (Errors and Exceptions) · Ramalho, *Fluent Python* 2e — cap. 18 (Context Managers).
> ⏱️ Duración estimada: **75 min**.

---

## 🎯 Objetivo

Que el alumno maneje excepciones con criterio (sin `except: pass`), construya jerarquías de excepciones propias cuando aporta, y use context managers (`with`) — tanto los built-in como propios con `@contextmanager` — para garantizar limpieza de recursos. Sin esto, el código de carga de datos es una bomba de relojería.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Diferenciar** los 3 tipos de errores (Syntax, runtime exceptions, logical) y dónde se manejan.
2. **Capturar** excepciones específicas (`except ValueError`, no `except:`) y propagar las que no sabes manejar.
3. **Crear** una excepción propia heredando de la jerarquía estándar (`class DatasetCorruptoError(Exception)`).
4. **Usar `with`** para archivos, sesiones HTTP, transacciones DB.
5. **Escribir** un context manager propio con `@contextmanager` (timer, supress, change_dir).

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | Jerarquía de excepciones built-in | `BaseException` → `Exception` → `ValueError`/`KeyError`/... |
| 2 | `try/except/else/finally` | Cada bloque tiene un rol específico. |
| 3 | Capturar específico, no genérico | `except:` esconde bugs. |
| 4 | Excepciones propias | Comunican intención en vez de cargar mensajes string. |
| 5 | Context managers: protocolo `__enter__`/`__exit__` | Garantiza cleanup. |
| 6 | `@contextmanager` de `contextlib` | Crear cms con función + `yield`. |

## 📂 Dataset / recursos

Archivo temporal generado en el notebook. Sin descarga.

## 🧪 Ejercicios

**1.** **Captura específica.** Escribe una función `parse_int_safe(s, default=0)` que use try/except solo para `ValueError`. Demuestra que no esconde otros errores (ej. `TypeError` si pasas un dict).

**2.** **Excepción propia.** Define `class DatasetCorruptoError(Exception)` con un atributo `linea`. Lanzala desde una función `cargar_csv` cuando una línea no tenga el número correcto de columnas.

**3.** **`with` para archivo.** Lee un archivo línea por línea contando palabras. Compara con la versión sin `with` (manual `open/close`) y muestra qué pasa si hay excepción a mitad.

**4.** **Context manager propio: timer.** Con `@contextmanager`, escribe `with timer("carga"):` que imprima cuánto duró el bloque.

**5.** **Context manager: change_dir.** `with cd("/tmp"):` cambia de directorio al entrar y vuelve al salir — incluso si hay excepción.

## 📝 Homework verificable

Notebook con: (a) `parse_int_safe` con tests de los 3 casos (válido, inválido, otro tipo); (b) `DatasetCorruptoError` usada en una función `cargar_csv` que valida #columnas; (c) decorador-context manager `timer` aplicado a 2 operaciones; (d) `cd` context manager.

**Criterio de aceptación:** Excepciones se capturan solo donde sabes manejarlas. `timer` reporta segundos correctamente.

## 🔗 Referencias

- [Python Tutorial — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- Ramalho, *Fluent Python* 2e — cap. 18 *Context Managers and else Blocks*.
- [`contextlib` docs](https://docs.python.org/3/library/contextlib.html)

## ➡️ Siguiente clase

[Clase 010 — OOP básico, dataclasses, herencia](../010-oop-basico-dataclasses-herencia/README.md)
