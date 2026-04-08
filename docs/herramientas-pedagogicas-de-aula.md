# 🧰 Herramientas pedagogicas de aula

Playbook de mediacion para mostrar en entrevista, usar en clase de prueba y operar el bootcamp con criterio. El objetivo de este documento es bajar la pedagogia a decisiones concretas, observables y reutilizables.

## 💡 1. Idea fuerza

Una buena clase tecnica no se mide solo por si el codigo corre. Se mide por si el estudiante:

- entiende que problema esta resolviendo;
- sabe por que uso cierta herramienta;
- puede variar una parte del ejercicio;
- interpreta el resultado con sus palabras.

## 🧱 2. Secuencia didactica base

```mermaid
flowchart LR
    A["Objetivo visible"] --> B["Activacion breve"]
    B --> C["Demostracion guiada"]
    C --> D["Practica acompanada"]
    D --> E["Chequeo de comprension"]
    E --> F["Cierre con interpretacion"]
```

Esta secuencia funciona bien en clases cortas, medias y en talleres de prueba porque:

- reduce la ansiedad del inicio;
- evita explicar demasiado antes de hacer;
- deja evidencia de comprension antes del cierre.

## 🛠 3. Caja de herramientas por momento de la clase

### Apertura

Objetivo: alinear al grupo y bajar el nivel de incertidumbre.

Herramientas:

- declarar que se aprendera hoy y para que sirve;
- mostrar una salida final simple antes del desarrollo;
- hacer una pregunta de entrada de baja exposicion;
- partir con una victoria rapida.

### Explicacion

Objetivo: construir comprension sin saturar.

Herramientas:

- una sola idea fuerte por bloque;
- ejemplo pequeno antes del caso completo;
- verbalizar el razonamiento, no solo el teclado;
- pedir prediccion antes de ejecutar.

### Practica

Objetivo: transformar observacion en accion.

Herramientas:

- ejercicio base obligatorio;
- variacion guiada para consolidar;
- desafio opcional para quien termina antes;
- checkpoints de 15 a 20 minutos.

### Cierre

Objetivo: que el aprendizaje no quede solo en ejecucion.

Herramientas:

- ticket de salida;
- conclusion escrita en lenguaje simple;
- pregunta de transferencia;
- mini recapitulacion de error comun y solucion.

## 📋 4. Matriz de intervencion docente

| Situacion | Senal observable | Intervencion recomendada | Error a evitar |
|---|---|---|---|
| miedo a equivocarse | silencio, mirada pasiva, no ejecuta | dar un paso inicial muy acotado y validar el intento | exponerlo con una pregunta demasiado amplia |
| copia sin comprension | pega codigo y no puede explicarlo | pedir que cambie una variable y prediga el resultado | corregir solo el codigo sin revisar la comprension |
| frustracion por error | se detiene en un traceback | modelar lectura del error por partes | resolverle todo sin explicar el proceso |
| ritmos muy distintos | unos esperan, otros se pierden | definir minimo comun y reto opcional | avanzar solo al ritmo del grupo mas rapido |
| baja participacion | responden siempre los mismos | usar parejas, sondeos cortos y microcierres | convertir la clase en monologo |
| dependencia de tecnologia | consulta todo antes de pensar | volver al objetivo y pedir hipotesis previa | prohibir la herramienta sin mediar su uso |

## ✨ 5. Como dar valor frente a cualquier tecnologia

El valor docente no esta en competir con asistentes, buscadores o plataformas. Esta en ordenar la experiencia de aprendizaje.

### Lo que hace la tecnologia

- entrega respuestas rapidas;
- sugiere codigo;
- muestra ejemplos;
- acelera busqueda de informacion.

### Lo que hace la mediacion docente

- selecciona dificultad adecuada;
- secuencia el aprendizaje;
- detecta confusiones del grupo;
- convierte resultado en comprension;
- regula el uso de tecnologia segun objetivo.

### Regla de aula sugerida

1. formular una hipotesis;
2. consultar la herramienta;
3. validar si sirve;
4. adaptar;
5. explicar.

## 👥 6. Herramientas para grupos con ritmos distintos

| Perfil del estudiante | Necesidad | Respuesta docente |
|---|---|---|
| muy inseguro | estructura y validacion | pasos pequenos, preguntas cerradas, refuerzo de logro |
| intermedio | practica con sentido | ejercicios base y comparacion de soluciones |
| rapido | reto y profundidad | desafio opcional, explicacion a pares, extension del caso |

La clave no es hacer tres clases distintas. La clave es sostener un minimo comun visible y capas de extension bien dosificadas.

## 📌 7. Indicaciones pedagogicas que conviene declarar

- el error es parte del trabajo, no una senal de incapacidad;
- primero se entiende la pregunta, despues la herramienta;
- se valora justificar, no solo acertar;
- la tecnologia se usa con criterio, no como reemplazo del proceso.

## 🚨 8. Problemas reales que pueden aparecer en clase

### Problema: no entienden para que sirve el contenido

Respuesta:

- conectar con una pregunta concreta;
- mostrar un resultado visible;
- volver a nombrar el objetivo en mitad de la clase.

### Problema: el curso se vuelve demasiado tecnico muy rapido

Respuesta:

- bajar la cantidad de conceptos por bloque;
- usar ejemplos mas pequenos;
- privilegiar lectura y modificacion antes que construccion desde cero.

### Problema: se apoyan demasiado en plantillas o asistentes

Respuesta:

- pedir prediccion antes de consultar;
- pedir adaptacion posterior;
- pedir explicacion oral o escrita de una parte critica.

### Problema: se quedan pegados en errores minimos

Respuesta:

- modelar una rutina de depuracion;
- separar errores de sintaxis, datos y logica;
- mostrar una correccion y luego devolver la tarea al estudiante.

## ✅ 9. Senales de una buena clase tecnica

- el grupo puede nombrar el objetivo de la sesion;
- al menos una parte del curso se resuelve con autonomia;
- los errores sirven para aprender y no solo para frenar;
- el cierre incluye interpretacion y no solo "terminamos".

## 🎤 10. Frases utiles para entrevista o clase de prueba

### Sobre enfoque

"Mi foco no es solo que ejecuten codigo. Es que entiendan la logica, puedan verificar resultados y ganen confianza para reutilizar lo aprendido."

### Sobre tecnologia

"No compito contra ninguna tecnologia. La ordeno pedagogicamente para que el estudiante no pierda criterio ni autonomia."

### Sobre manejo de aula

"Trabajo con un minimo comun claro, apoyo a quien se bloquea y retos breves para quien avanza mas rapido."

## 🔗 11. Relacion con otros documentos

- [metodologia-docente.md](metodologia-docente.md)
- [instructor-guide.md](instructor-guide.md)
- [plan-evaluacion.md](plan-evaluacion.md)
- [aula-ia-y-problemas-frecuentes.md](aula-ia-y-problemas-frecuentes.md)
