# ❓ Preguntas — Clase 13: ¿Qué es la Ciencia de Datos?

> Preguntas de comprensión, discusión y evaluación para consolidar esta clase.

## 🧠 Preguntas de comprensión

1. ¿Cuáles son las 5 etapas del ciclo CRISP-DM y en qué orden ocurren normalmente? Describe brevemente qué pasa en cada una.
2. ¿Cuál es la diferencia entre una pregunta de tipo diagnóstico y una de tipo predictivo? Da un ejemplo de cada una usando datos reales.
3. ¿Qué distingue a los datos estructurados de los no estructurados? ¿A cuál categoría pertenece una imagen y a cuál un archivo CSV?
4. ¿Por qué la etapa de "entender el negocio" se considera la más importante en CRISP-DM, aunque no incluya código?
5. Nombra al menos tres herramientas del ecosistema de ciencia de datos en Python y explica brevemente para qué sirve cada una.

## 💬 Preguntas de discusión

1. ¿Por qué crees que la ciencia de datos se ha vuelto tan importante en los últimos años? ¿Qué cambios en la tecnología o en la sociedad lo explican?
2. Un hospital quiere saber si sus pacientes tienen riesgo de reingresar dentro de los 30 días siguientes al alta. ¿Qué tipo de pregunta analítica es esa? ¿Cómo le explicarías el proceso usando CRISP-DM a un médico?
3. ¿En qué situaciones podrían los datos llevarnos a conclusiones incorrectas aunque el análisis técnico esté bien hecho?

## 🧪 Preguntas de código

1. ¿Qué hace exactamente `df.info()` y qué información útil te da sobre un DataFrame? ¿En qué se diferencia de `df.describe()`?
2. Si ejecutas `pd.read_csv("ventas_tienda.csv")` y el archivo tiene una fila de encabezado en la fila 2 (no en la fila 1), ¿cómo modificarías esa línea para leerlo correctamente?
3. Dado el siguiente fragmento, ¿qué imprimiría cada línea y qué significa cada resultado?
   ```python
   df = pd.read_csv("ventas_tienda.csv")
   print(df.shape)
   print(df.columns.tolist())
   print(df.isnull().sum())
   ```

## 🎯 Pregunta integradora

Imagina que trabajas para una cadena de supermercados que quiere reducir el desperdicio de alimentos. Usando el ciclo CRISP-DM completo, describe paso a paso cómo abordarías este problema: ¿qué tipo de pregunta analítica es?, ¿qué datos necesitarías recopilar y cómo los explorarías?, ¿qué tipo de modelo podrías aplicar?, y ¿cómo comunicarías los resultados a los gerentes de tienda que no saben programar?
