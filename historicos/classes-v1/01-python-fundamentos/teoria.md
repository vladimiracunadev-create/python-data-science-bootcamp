# 🧠 Documento teórico — Clase 01: Fundamentos de Python aplicados a datos

> 🧠 Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## 💡 Idea central

Python se presenta como herramienta para ordenar y transformar información, no como teoría abstracta.

## ❓ Por qué importa este módulo

Es la base para que el estudiante pueda leer, modificar y comentar código con confianza.

## 💻 Bloque de código documentado

### Función para calcular ingreso bruto

Encapsular una operación en una función evita repetir lógica y facilita explicar cada paso.

**Qué hace:** entrada → calcular → devolver → reutilizar

**Para qué sirve:** Sirve para introducir reutilización, parámetros y retorno usando un ejemplo cercano al análisis de ventas.

```python
# Qué hace: entrada → calcular → devolver → reutilizar.
# Para qué sirve: Sirve para introducir reutilización, parámetros y retorno usando un ejemplo cercano al análisis de ventas.
def calcular_total_bruto(unidades, precio_unitario):
    # Multiplicamos cantidad por precio para estimar el ingreso bruto.
    return unidades * precio_unitario


ventas = [
    {"producto": "Mouse", "unidades": 3, "precio_unitario": 8990},
    {"producto": "Teclado", "unidades": 2, "precio_unitario": 15990},
]

totales = [calcular_total_bruto(v["unidades"], v["precio_unitario"]) for v in ventas]
print(totales)
```

## ⚠️ Errores frecuentes a vigilar

- Saltar al código sin aclarar la pregunta.
- Ejecutar bloques sin leer la salida.
- Dejar bloques importantes sin comentarios o sin explicación oral.

## 🔗 Conexión con el siguiente módulo

La clase 02 traslada estas bases a tablas con pandas.
