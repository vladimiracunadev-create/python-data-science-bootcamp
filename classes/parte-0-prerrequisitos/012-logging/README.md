# Clase 012 — Logging

> Parte: **0 — Prerrequisitos** · Fuente: *Python Tutorial* logging HOWTO · *The Pragmatic Programmer* — "Programming by Coincidence".
> ⏱️ Duración estimada: **60 min**.

---

## 🎯 Objetivo

Que el alumno **deje de usar `print` para debug** y aprenda el módulo `logging` estándar: niveles (DEBUG/INFO/WARNING/ERROR/CRITICAL), handlers (consola, archivo), formatters, y configuración por módulo. Es la diferencia entre código que se debuggea reiniciando el notebook y código que se debuggea leyendo logs.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Diferenciar** los 5 niveles de logging y cuándo usar cada uno.
2. **Configurar** un logger con `logging.basicConfig` y entender por qué `basicConfig` solo funciona una vez.
3. **Crear loggers por módulo** con `logging.getLogger(__name__)`.
4. **Agregar handlers**: uno a consola (INFO+), otro a archivo (DEBUG+).
5. **Formatear** logs con timestamp, módulo y nivel.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | `print` vs `logging` | print() es output; logging es observabilidad. |
| 2 | Niveles: DEBUG/INFO/WARNING/ERROR/CRITICAL | Filtran qué se ve sin tocar código. |
| 3 | Logger jerárquico por módulo | `getLogger(__name__)` para herencia natural. |
| 4 | Handlers: consola, archivo, rotating | Mismo log → múltiples destinos. |
| 5 | Formatters | Timestamp + nivel + módulo + mensaje. |
| 6 | `logging.basicConfig` y sus límites | Solo afecta el primero; preferir config explícita. |

## 📂 Dataset / recursos

Genera un log file de demo. Sin descarga.

## 🧪 Ejercicios

**1.** **Reemplaza prints.** Toma una función con 5 prints y conviértelos a logger con niveles apropiados.

**2.** **Logger por módulo.** Crea 2 archivos `.py` que cada uno usa `getLogger(__name__)`. Configura el root logger una vez; verifica que ambos heredan.

**3.** **Handler doble.** Configura: consola = INFO+, archivo `app.log` = DEBUG+. Genera 5 logs de niveles distintos y verifica qué aparece en cada destino.

**4.** **Formato con timestamp.** Cambia el formato a `'%(asctime)s [%(levelname)s] %(name)s: %(message)s'`. Inspecciona output.

**5.** **Logger en notebook.** Pelea con `basicConfig` no recordando estado entre reinicios — usa `dictConfig` o `force=True`.

## 📝 Homework verificable

Notebook + 2 módulos `.py` que importan y loguean. Un `logging_config.py` con `dictConfig` que define: consola (INFO+, formato corto) y `app.log` (DEBUG+, formato verbose con timestamp). El notebook ejecuta funciones que generan logs de distintos niveles desde ambos módulos. Adjunta el `app.log` resultante.

**Criterio de aceptación:** `app.log` contiene timestamp y módulo correcto en cada línea; consola filtra DEBUG.

## 🔗 Referencias

- [Logging HOWTO](https://docs.python.org/3/howto/logging.html)
- [Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html)
- [`logging.config` — dictConfig](https://docs.python.org/3/library/logging.config.html)

## ➡️ Siguiente clase

[Clase 013 — Type hints y mypy](../013-type-hints-y-mypy/README.md)
