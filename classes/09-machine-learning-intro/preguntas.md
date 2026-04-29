# ❓ Preguntas de evaluación — Clase 09: Introducción a machine learning

> Preguntas para verificar comprensión al cierre de la clase o en evaluaciones formativas.

## 🧠 Preguntas conceptuales

1. ¿Cuál es la diferencia entre una variable de entrada (X) y una variable objetivo (y) en un problema supervisado?
2. ¿Por qué dividimos los datos en conjunto de entrenamiento y conjunto de prueba antes de entrenar un modelo?
3. ¿Qué significa que un modelo "aprende" durante el entrenamiento? ¿Qué ajusta internamente una regresión lineal?
4. ¿Por qué machine learning se considera una extensión del análisis de datos y no una técnica completamente distinta?
5. Si el conjunto de prueba representa el 20 % de los datos y tienes 500 filas en total, ¿cuántas filas usará el modelo para entrenarse?

## 💻 Preguntas de código

1. ¿Qué produce este bloque y por qué el parámetro `random_state=42` es importante?

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train.shape, X_test.shape)
```

2. ¿Qué diferencia hay entre llamar `modelo.fit(X_train, y_train)` y `modelo.predict(X_test)`? ¿En cuál de los dos el modelo "aprende"?

3. El siguiente código produce un error. ¿Cuál es el problema y cómo se corrige?

```python
from sklearn.linear_model import LinearRegression
modelo = LinearRegression()
predicciones = modelo.predict(X_test)   # <-- esta línea falla
modelo.fit(X_train, y_train)
```

4. ¿Qué imprimen estas dos líneas y qué representan esos valores?

```python
print(modelo.coef_)
print(modelo.intercept_)
```

## 🔗 Preguntas integradoras

1. Un colegio quiere predecir qué estudiantes reprobarán al final del semestre usando los registros de asistencia y notas parciales. ¿Cómo definirías X e y en ese problema? ¿Qué tipo de modelo usarías, regresión o clasificación?
2. ¿Por qué no sería correcto evaluar el desempeño de un modelo usando los mismos datos con los que lo entrenaste? Da un ejemplo concreto de cómo eso podría dar una impresión falsa del rendimiento.
3. Una empresa de retail quiere estimar las ventas del mes siguiente usando datos históricos. ¿Qué columnas del dataset elegirías como X y cuál como y? ¿Qué riesgo correría el modelo si incluyes en X información que solo está disponible después de que ocurren las ventas?
