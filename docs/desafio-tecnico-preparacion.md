# Preparacion para desafio tecnico

## Objetivo de este documento

Tener una guia general de todo lo que deberias manejar si el desafio tecnico evalua no solo codigo, sino tambien criterio docente, estructura de solucion, despliegue local y seguridad basica.

## Regla principal

No intentes impresionar por complejidad. En un desafio tecnico de este perfil vale mas:

- claridad;
- criterio;
- capacidad de explicacion;
- una solucion correcta y verificable;
- buenas decisiones de alcance.

## 1. Contenido tecnico general que debes manejar

## Python base

- variables, tipos, listas, diccionarios y tuplas;
- condicionales, bucles y funciones;
- comprensiones;
- manejo de errores con `try/except`;
- modulos e imports;
- lectura y escritura basica de archivos;
- legibilidad, nombres y descomposicion en funciones simples.

## Analisis de datos

- `pandas.read_csv`;
- `head`, `info`, `describe`;
- seleccion de columnas;
- filtros booleanos;
- nulos y limpieza basica;
- `groupby`, agregaciones y ordenamiento;
- creacion de columnas derivadas;
- interpretacion de resultados.

## Visualizacion

- graficos de barras, lineas y dispersión;
- eleccion de grafico segun pregunta;
- titulos, ejes y legibilidad;
- lectura de patrones;
- errores comunes de interpretacion.

## Estadistica y lectura de resultados

- media, mediana, conteo, porcentaje;
- outliers y distribuciones simples;
- diferencia entre correlacion e interpretacion causal;
- comunicar un hallazgo en lenguaje simple.

## Machine Learning basico

Aunque la V1 no dependa de esto, conviene manejar:

- diferencia entre regresion y clasificacion;
- train/test split;
- feature vs target;
- overfitting basico;
- metricas simples como accuracy, MAE o RMSE;
- por que no todo problema necesita ML.

## Desarrollo de aplicaciones y APIs

- estructura minima de una app Flask;
- rutas GET y POST;
- `request`, `jsonify`, validaciones basicas;
- carga de contenido desde archivos;
- manejo de errores y codigos HTTP;
- separar logica de interfaz, contenido y ejecucion.

## Calidad y validacion

- probar rapido desde `pytest`;
- revisar edge cases;
- confirmar que una ruta responde;
- validar inputs;
- explicar que se verifico y que no.

## Seguridad y despliegue

- no exponer la app a internet por defecto;
- bind local a `127.0.0.1` cuando corresponde;
- usar variables de entorno para host y puerto;
- limitar payloads y longitud de entradas;
- bloquear path traversal y nombres invalidos;
- usar timeouts en ejecucion de codigo;
- agregar headers de seguridad basicos;
- si se expone, poner proxy con TLS y autenticacion adicional;
- no commitear secretos.

## 2. Lo que podrian pedirte en el desafio

## Caso A: corregir o mejorar codigo

Podrian pedir:

- arreglar un bug;
- simplificar una funcion;
- mejorar validaciones;
- agregar una ruta o una clase;
- mejorar legibilidad.

Lo importante:

- aislar el cambio;
- explicar el problema;
- validar con una prueba o reproduccion minima.

## Caso B: resolver un ejercicio de datos

Podrian pedir:

- cargar un CSV;
- limpiar datos;
- responder preguntas de negocio;
- graficar resultados;
- escribir conclusiones.

Lo importante:

- explicar la pregunta antes del codigo;
- mostrar pasos intermedios;
- evitar saltar directo a una respuesta final.

## Caso C: adaptar algo a contexto educativo

Podrian pedir:

- convertir una solucion tecnica en una actividad de clase;
- proponer una clase de prueba;
- explicar como ensenarlo a principiantes;
- anticipar errores del grupo.

Lo importante:

- traducir, no simplificar en exceso;
- mantener objetivo, practica y cierre;
- mostrar criterio de ritmo y apoyo.

## Caso D: revisar despliegue o seguridad

Podrian pedir:

- revisar Docker o compose;
- detectar riesgos de exposicion;
- proponer una postura local segura;
- explicar por que una demo no es produccion.

Lo importante:

- separar quickstart de hardening;
- priorizar mejoras de bajo riesgo;
- hablar de TLS, proxy, auth, rate limit y secretos si hay exposicion externa.

## 3. Respuestas marco que debes poder dar

## "Por que tomaste esta decision?"

"Priorizo una solucion clara, verificable y facil de mantener. Si despues el contexto pide mas complejidad, la escalo sobre esta base."

## "Por que no usaste algo mas avanzado?"

"Porque primero quise resolver bien el problema real. La complejidad extra solo tiene sentido si agrega valor claro y no dificulta la comprension o el mantenimiento."

## "Como lo ensenarias?"

"Lo dividiria en una explicacion breve, una demostracion guiada, una practica corta y un cierre donde el estudiante tenga que interpretar el resultado."

## "Que riesgo ves aqui?"

"El principal riesgo es mezclar una demo local con una postura de despliegue abierta. Si esto saliera de entorno controlado, pisaria TLS, autenticacion, proxy y limites de exposicion."

## 4. Checklist rapido antes de responder cualquier desafio

1. Entender el objetivo exacto.
2. Confirmar supuestos si algo esta ambiguo.
3. Identificar el minimo correcto que resuelve.
4. Implementar de forma clara.
5. Validar el resultado.
6. Explicar decisiones, tradeoffs y limites.

## 5. Bateria de preguntas que debes estar listo para responder

- Que debe aprender un principiante primero y por que.
- Como traduces una herramienta tecnica a una actividad de aula.
- Como manejas estudiantes con ritmos distintos.
- Como usarias o regularias herramientas de IA en clase.
- Como protegerias una app local de practica.
- Que diferencia hay entre una demo, un piloto y una implementacion real.
- Que validarias antes de exponer una app o runner de codigo.
- Como pruebas rapido que tu cambio no rompio lo existente.

## 6. Que conviene practicar hoy mismo

- explicar `pandas` en voz alta como si fuera una clase;
- resolver un CSV simple de principio a fin;
- revisar los endpoints de esta app;
- practicar el argumento de valor docente frente a cualquier tecnologia;
- repasar por que este repo no debe exponerse a internet sin capas extra;
- tener a mano un ejemplo de bug, validacion y prueba.

## 7. Criterio final

Si el desafio es muy abierto, tu mejor respuesta no es "puedo hacer cualquier cosa". Tu mejor respuesta es mostrar que sabes acotar, priorizar, ejecutar y justificar.
