# 🏋️ Ejercicios — Clase 28: Ética, sesgo y privacidad en datos

Estos ejercicios combinan reflexión crítica con análisis de datos. Algunos tienen respuestas de código, otros son preguntas abiertas para discutir en clase.

---

## Ejercicio 1: Identificar tipos de sesgo (reflexión)

Lee los siguientes escenarios y clasifica el tipo de sesgo presente:

**Escenario A:**
Una empresa de recursos humanos entrena un modelo con 10 años de datos de contrataciones. Durante esos 10 años, el 90% de los gerentes contratados fueron hombres.

**Escenario B:**
Un hospital desarrolla un modelo para predecir enfermedades cardíacas. El dataset incluye solo pacientes que llegaron al hospital de urgencias — los pacientes con síntomas leves que nunca fueron al hospital no están representados.

**Escenario C:**
Un modelo de predicción de morosidad usa el código postal como variable. Los códigos postales de barrios históricamente marginados están asociados a mayor morosidad, aunque no por razones de comportamiento individual.

**Respuesta esperada:**
- A: Sesgo histórico
- B: Sesgo de muestreo
- C: Sesgo de medición (el código postal es un proxy de clase social/raza)

---

## Ejercicio 2: Analizar distribución del dataset

Carga el dataset `estudiantes.csv` y responde:

```python
import pandas as pd

df = pd.read_csv('datasets/estudiantes.csv')

# a) ¿Cuántos estudiantes hay por curso?
print(df['curso'].value_counts())

# b) ¿Cuál es la tasa de aprobación por curso?
print(df.groupby('curso')['aprobado'].mean().round(2))

# c) ¿Cuál es la tasa de aprobación por rango de edad?
df['rango_edad'] = pd.cut(df['edad'], bins=[0, 20, 25, 30, 100],
                           labels=['<20', '20-25', '25-30', '30+'])
print(df.groupby('rango_edad')['aprobado'].mean().round(2))
```

**Preguntas:**
1. ¿Existe una diferencia significativa en la tasa de aprobación entre cursos?
2. ¿Los grupos de edad tienen tasas similares?
3. ¿Qué conclusiones preliminares sacas sobre posible sesgo?

---

## Ejercicio 3: Calcular impacto dispar

```python
# Calcula la razón de impacto dispar entre el curso con mayor
# tasa de aprobación y el curso con menor tasa

tasas = df.groupby('curso')['aprobado'].mean()
tasa_max = tasas.max()
tasa_min = tasas.min()

razon = tasa_min / tasa_max
print(f"Razón de impacto dispar: {razon:.2f}")

if razon < 0.8:
    print("ALERTA: Posible impacto dispar (regla del 80%)")
else:
    print("No se detecta impacto dispar significativo")
```

**Pregunta:** Si hay impacto dispar, ¿significa automáticamente que el modelo es injusto? ¿O podría haber explicaciones legítimas?

---

## Ejercicio 4: Evaluar un modelo por subgrupos

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Preparar datos
features = ['nota_matematicas', 'nota_lengua', 'asistencia', 'edad']
X = df[features]
y = df['aprobado']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Necesitamos los grupos en el test set
df_test = df.iloc[X_test.index]

# Entrenar modelo
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)
predicciones = modelo.predict(X_test)

# Evaluar por curso
print("=== Rendimiento del modelo por curso ===")
for curso in df_test['curso'].unique():
    mask = df_test['curso'] == curso
    if mask.sum() > 0:
        acc = accuracy_score(y_test[mask], predicciones[mask])
        n = mask.sum()
        print(f"Curso {curso}: {acc:.2%} (n={n})")

print(f"\nPrecisión global: {accuracy_score(y_test, predicciones):.2%}")
```

**Preguntas:**
1. ¿El modelo tiene el mismo rendimiento para todos los cursos?
2. Si hay diferencias, ¿son preocupantes?
3. ¿Qué harías para mejorar la equidad del modelo?

---

## Ejercicio 5: Privacidad — identificar datos sensibles (reflexión)

Revisa esta lista de columnas de un dataset ficticio de empleados. Clasifica cada una como: **datos sensibles** (no deben compartirse sin anonimizar), **datos útiles** (pueden usarse con cuidado) o **datos seguros** (no revelan información personal).

| Columna | Tu clasificación |
|---------|-----------------|
| nombre_completo | |
| dni | |
| departamento | |
| salario | |
| fecha_nacimiento | |
| codigo_empleado | |
| años_experiencia | |
| ciudad_residencia | |
| tiene_hijos | |
| nota_rendimiento | |

**Discusión:** ¿Cambiaría tu clasificación si el dataset tiene solo 10 empleados? ¿Por qué?

---

## Ejercicio 6: Anonimizar un dataset

```python
import pandas as pd
import hashlib

# Dataset ficticio de ejemplo
datos = pd.DataFrame({
    'nombre': ['Ana García', 'Juan Pérez', 'María López'],
    'dni': ['12345678A', '87654321B', '11223344C'],
    'edad': [25, 32, 28],
    'departamento': ['Ventas', 'IT', 'Marketing'],
    'salario': [35000, 45000, 38000]
})

# Técnica 1: Eliminar identificadores directos
datos_anonimos = datos.drop(columns=['nombre', 'dni'])
print("Sin identificadores directos:")
print(datos_anonimos)

# Técnica 2: Seudonimizar con hash
def hash_id(valor):
    return hashlib.md5(str(valor).encode()).hexdigest()[:8]

datos['id_anonimo'] = datos['dni'].apply(hash_id)
datos_seudo = datos.drop(columns=['nombre', 'dni'])
print("\nSeudonimizado:")
print(datos_seudo)

# Técnica 3: Generalizar valores numéricos
datos_anonimos['rango_salario'] = pd.cut(
    datos_anonimos['salario'],
    bins=[0, 30000, 40000, 50000, float('inf')],
    labels=['<30k', '30k-40k', '40k-50k', '>50k']
)
print("\nCon salario generalizado:")
print(datos_anonimos[['edad', 'departamento', 'rango_salario']])
```

---

## Ejercicio 7: Debate final (reflexión grupal)

Discute con tus compañeros:

1. **Caso COMPAS:** Un sistema usado en EE.UU. predice la probabilidad de reincidencia de personas detenidas. Los jueces lo usan para decidir la libertad condicional. El sistema muestra tasas de error 2x más altas para personas negras. ¿Debería seguir usándose? ¿Qué cambiarías?

2. **Dilema del médico:** Un modelo de diagnóstico de cáncer tiene 95% de precisión general pero solo 80% para pacientes de zonas rurales (porque esos pacientes tenían menos representación en los datos de entrenamiento). ¿Es ético desplegarlo?

3. **Transparencia vs. seguridad:** Una empresa no quiere revelar cómo funciona su algoritmo de crédito porque dicen que si lo revelan, la gente va a "jugar el sistema". ¿Es este argumento válido? ¿Qué derechos tienen los usuarios?

---

## Checklist de ética para tu próximo proyecto

Antes de construir cualquier modelo, respóndete estas preguntas:

- [ ] ¿A quién afectan las predicciones de este modelo?
- [ ] ¿Podría el modelo perjudicar sistemáticamente a algún grupo?
- [ ] ¿Tengo representación adecuada de todos los grupos en mi dataset?
- [ ] ¿Las variables que uso podrían ser proxies de características protegidas?
- [ ] ¿Tengo consentimiento para usar estos datos?
- [ ] ¿Estoy almacenando más datos personales de los necesarios?
- [ ] ¿Puedo explicar la decisión del modelo a un afectado?
- [ ] ¿Hay un humano responsable de las decisiones finales?
