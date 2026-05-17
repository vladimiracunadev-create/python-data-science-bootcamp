# 💻 Guía de código — Clase 00: Diagnóstico inicial y orientación

> Esta clase no incluye código de análisis. La guía se enfoca en cómo organizar información del diagnóstico usando estructuras básicas de Python como orientación para las clases siguientes.

## Bloque 1: Representar resultados del diagnóstico con un diccionario

```python
# Representamos el perfil de un estudiante como un diccionario.
# Cada clave es un área evaluada; el valor es el nivel detectado.
perfil_estudiante = {
    "nombre": "Ana Torres",
    "python_basico": "intermedio",    # ya conoce variables y listas
    "lectura_tablas": "principiante", # nunca usó pandas
    "graficos": "principiante",       # nunca creó un gráfico
    "modelado": "ninguno",            # no tiene experiencia previa
    "habitos_trabajo": "bueno",       # documenta su código con comentarios
}

print(perfil_estudiante["nombre"], "->", perfil_estudiante["python_basico"])
```

**¿Qué hace este bloque?**
Crea un perfil de diagnóstico para un estudiante usando un diccionario. Cada área evaluada es una clave, y el nivel detectado es el valor. Luego imprime el nombre y el nivel en Python básico.

**¿Por qué se escribe así y no de otra forma?**
Un diccionario es más expresivo que una lista para este caso porque permite acceder a cada área por nombre (por ejemplo, `perfil["graficos"]`) sin recordar su posición. Esto hace el código más legible y fácil de mantener.

**Resultado esperado:**
```
Ana Torres -> intermedio
```

---

## Bloque 2: Agrupar varios estudiantes y filtrar por área

```python
# Lista de perfiles del grupo completo
grupo = [
    {"nombre": "Ana Torres",   "python_basico": "intermedio", "lectura_tablas": "principiante"},
    {"nombre": "Luis Vera",    "python_basico": "principiante","lectura_tablas": "principiante"},
    {"nombre": "Carla Ríos",   "python_basico": "avanzado",   "lectura_tablas": "intermedio"},
]

# Filtramos quiénes necesitan refuerzo en Python básico
necesitan_refuerzo = [
    e["nombre"]
    for e in grupo
    if e["python_basico"] == "principiante"
]

print("Estudiantes que necesitan refuerzo en Python:", necesitan_refuerzo)
```

**¿Qué hace este bloque?**
Recorre la lista de perfiles del grupo y filtra solo los estudiantes cuyo nivel en Python básico es "principiante". El resultado es una lista de nombres para que el docente identifique quiénes necesitan apoyo adicional.

**¿Por qué se escribe así y no de otra forma?**
La comprensión de listas (`[... for ... if ...]`) es una forma compacta y legible de filtrar en Python. Es equivalente a un bucle `for` con un `if` dentro, pero más concisa. El docente puede cambiar el área o el nivel que filtra sin reescribir el bucle completo.

**Resultado esperado:**
```
Estudiantes que necesitan refuerzo en Python: ['Luis Vera']
```

---

## Bloque 3: Calcular una distribución simple del grupo

```python
# Contamos cuántos estudiantes hay en cada nivel para cada área
from collections import Counter

niveles_python = [e["python_basico"] for e in grupo]
distribución = Counter(niveles_python)

print("Distribución de niveles en Python básico:")
for nivel, cantidad in distribución.items():
    print(f"  {nivel}: {cantidad} estudiante(s)")
```

**¿Qué hace este bloque?**
Extrae los niveles de Python de todos los estudiantes y los cuenta usando `Counter`. Luego imprime cuántos estudiantes hay en cada nivel, lo que permite al docente ver la distribución del grupo de un vistazo.

**¿Por qué se escribe así y no de otra forma?**
`Counter` de la librería estándar hace exactamente esto sin necesidad de escribir bucles de conteo manuales. Es más confiable y legible que incrementar contadores a mano.

**Resultado esperado:**
```
Distribución de niveles en Python básico:
  intermedio: 1 estudiante(s)
  principiante: 1 estudiante(s)
  avanzado: 1 estudiante(s)
```

---

## Bloque 4: Traducir el diagnóstico en una acción concreta

```python
# Función que convierte el nivel detectado en una recomendación de acción
def accion_de_apoyo(nivel):
    acciones = {
        "ninguno":      "Asignar recursos de nivelación antes de la clase 01.",
        "principiante": "Monitorear en los primeros ejercicios y ofrecer ayuda extra.",
        "intermedio":   "Incluir en ejercicios estándar; revisar solo si hay dudas.",
        "avanzado":     "Puede actuar como par tutor en actividades grupales.",
    }
    return acciones.get(nivel, "Nivel no reconocido — revisar diagnóstico.")

# Generamos el plan de acción para cada estudiante
for estudiante in grupo:
    nombre = estudiante["nombre"]
    nivel  = estudiante["python_basico"]
    print(f"{nombre}: {accion_de_apoyo(nivel)}")
```

**¿Qué hace este bloque?**
Define una función que mapea cada nivel a una acción pedagógica concreta. Luego la aplica a cada estudiante del grupo e imprime el plan de apoyo personalizado.

**¿Por qué se escribe así y no de otra forma?**
Usar un diccionario dentro de la función (en lugar de un `if/elif` largo) hace que agregar o modificar niveles sea trivial. El método `.get()` con valor por defecto evita errores si aparece un nivel inesperado.

**Resultado esperado:**
```
Ana Torres: Incluir en ejercicios estándar; revisar solo si hay dudas.
Luis Vera: Monitorear en los primeros ejercicios y ofrecer ayuda extra.
Carla Ríos: Puede actuar como par tutor en actividades grupales.
```

---

## ⚠️ Errores comunes y cómo resolverlos

| Error típico | Por qué ocurre | Cómo solucionarlo |
|---|---|---|
| `KeyError: 'python_basico'` | La clave no existe en el diccionario (puede estar mal escrita o ausente) | Verificar que todos los perfiles tienen exactamente las mismas claves; usar `.get("python_basico", "sin dato")` para evitar el error |
| `TypeError: list índices must be integers` | Se intenta acceder a una lista con una cadena en lugar de un índice numérico | Revisar si la variable es una lista (usa índices) o un diccionario (usa claves); preferir diccionarios para perfiles con nombres de campo |
| Resultado vacío en el filtro | La condición del `if` no coincide con ningún valor (por ejemplo, "Principiante" vs "principiante") | Normalizar los valores a minúsculas antes de comparar: `e["python_basico"].lower() == "principiante"` |
| `AttributeError: 'list' object has no attribute 'items'` | Se llama `.items()` sobre una lista en lugar de un diccionario | Verificar el tipo de la variable antes de iterar; usar `type(variable)` para diagnosticar |
