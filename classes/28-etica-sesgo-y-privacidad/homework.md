# 📝 Tarea — Clase 28: Ética, sesgo y privacidad en datos

**Entrega:** Antes de la próxima clase  
**Formato:** Jupyter Notebook o documento PDF  
**Modalidad:** Individual

---

## Parte 1: Investigación (30 minutos)

Elige UNO de los siguientes casos reales y escribe un análisis de 200-300 palabras respondiendo las preguntas indicadas.

### Opción A: COMPAS (Correctional Offender Management Profiling for Alternative Sanctions)
Sistema de predicción de reincidencia usado en el sistema judicial de Estados Unidos.

**Preguntas:**
1. ¿Qué tipo de sesgo presenta este sistema?
2. ¿Cuáles son las consecuencias reales para las personas afectadas?
3. ¿Qué datos usaría tú para construir un sistema más justo? ¿Qué datos excluirías y por qué?

### Opción B: Algoritmo de contratación de Amazon (2018)
Herramienta de IA para filtrar CVs que fue cancelada por discriminar por género.

**Preguntas:**
1. ¿Cómo pudo surgir este sesgo si nadie programó explícitamente la discriminación?
2. ¿Qué debería haber hecho Amazon diferente durante el desarrollo?
3. Si tuvieras que auditar este sistema, ¿qué pruebas harías?

### Opción C: Reconocimiento facial y sesgo racial
Sistemas comerciales de reconocimiento facial con tasas de error significativamente más altas para personas de piel oscura.

**Preguntas:**
1. ¿Por qué existe esta diferencia en tasas de error?
2. ¿En qué contextos se usa el reconocimiento facial? ¿Cuáles son los más problemáticos?
3. ¿Debería prohibirse el reconocimiento facial en espacios públicos? Argumenta tu posición.

---

## Parte 2: Análisis de datos (45 minutos)

Usando el dataset `estudiantes.csv`, realiza el siguiente análisis en Python:

### 2.1 Análisis exploratorio de equidad

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('datasets/estudiantes.csv')

# Tu código aquí
```

Responde:
1. ¿Cuántos estudiantes hay por curso? Haz un gráfico de barras.
2. ¿Cuál es la tasa de aprobación por curso? Haz un gráfico comparativo.
3. ¿Existe correlación entre la edad y la nota promedio? Haz un scatter plot.
4. ¿Hay algún grupo (curso o rango de edad) que parezca estar en desventaja?

### 2.2 Evaluación de un modelo por subgrupos

Entrena un modelo simple (puedes usar `LogisticRegression` o `RandomForestClassifier`) para predecir si un estudiante aprueba o reprueba.

Luego evalúa:
1. La precisión global del modelo
2. La precisión del modelo para cada curso por separado
3. Calcula la razón de impacto dispar entre el curso con mayor y menor tasa de predicción positiva

### 2.3 Reflexión escrita

En 100-150 palabras, responde:
- ¿Qué descubriste sobre el dataset?
- ¿El modelo parece equitativo para todos los grupos?
- ¿Usarías este modelo para tomar decisiones reales sobre estudiantes? ¿Por qué sí o por qué no?

---

## Parte 3: Propuesta de mejora (15 minutos)

Si encontraste sesgo o inequidad en el modelo, propone 2-3 acciones concretas para mejorar la equidad. No necesitas implementarlas, solo describirlas claramente.

**Ejemplo de formato:**
> "Para reducir el sesgo hacia el grupo X, yo haría Y porque Z."

---

## Criterios de evaluación

| Criterio | Puntaje |
|----------|---------|
| Análisis de caso bien argumentado | 30 pts |
| Código correcto y bien comentado | 30 pts |
| Interpretación de resultados | 25 pts |
| Reflexión crítica y propuesta de mejora | 15 pts |
| **Total** | **100 pts** |

---

## Recursos de apoyo

- [Artículo original sobre COMPAS](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing) — ProPublica
- [Gender Shades Project](http://gendershades.org/) — MIT Media Lab
- [AI Fairness 360](https://aif360.mybluemix.net/) — IBM Research
- [Fairlearn documentation](https://fairlearn.org/) — Microsoft
- Libro recomendado: *Weapons of Math Destruction* — Cathy O'Neil (disponible en biblioteca)

---

## Nota

Esta tarea no tiene una respuesta "correcta" única. Lo que se evalúa es tu capacidad para pensar críticamente sobre los datos, ser honesto sobre lo que ves y proponer soluciones concretas y bien razonadas.
