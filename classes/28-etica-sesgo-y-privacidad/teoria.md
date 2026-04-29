# 📖 Teoría — Clase 28: Ética, sesgo y privacidad en datos

## 1. ¿Por qué importa la ética en ciencia de datos?

Durante años, se asumió que los algoritmos eran objetivos porque "solo hacen matemáticas". Esta idea es peligrosa. Los modelos aprenden de datos históricos, y esos datos están cargados de las decisiones, sesgos y desigualdades del pasado.

Cuando un banco usa un modelo para decidir quién recibe un préstamo, ese modelo puede estar perpetuando décadas de discriminación, aunque nadie se lo haya indicado explícitamente. La responsabilidad del científico de datos no termina cuando el modelo tiene buena precisión.

---

## 2. Tipos de sesgo en datos

### 2.1 Sesgo histórico

Los datos reflejan el mundo tal como fue, no como debería ser. Si durante años las empresas contrataron mayoritariamente hombres para puestos de liderazgo, un modelo entrenado con esos datos aprenderá que "hombre = buena contratación".

**Ejemplo real:** Amazon desarrolló una herramienta de selección de CVs que penalizaba automáticamente currículums que incluían la palabra "mujeres" (como en "capitana del equipo de mujeres"). El proyecto fue cancelado en 2018.

### 2.2 Sesgo de muestreo

Ocurre cuando el dataset no es representativo de la población a la que se aplicará el modelo. Si entrenas un modelo de diagnóstico médico con pacientes de hospitales privados, probablemente fallará con pacientes de bajos recursos.

**Ejemplo real:** Los sistemas de reconocimiento facial tienen tasas de error hasta 35% más altas para mujeres de piel oscura en comparación con hombres de piel clara (estudio MIT, 2018), porque los datasets de entrenamiento estaban desequilibrados.

### 2.3 Sesgo de medición

Ocurre cuando la variable que medimos no captura bien lo que realmente queremos medir.

**Ejemplo:** Si usamos "arrestos previos" como indicador de peligrosidad, estamos midiendo interacción con la policía (que varía por clase social y raza), no peligrosidad real.

### 2.4 Sesgo de confirmación

Cuando diseñamos el modelo o seleccionamos variables para confirmar lo que ya creemos, en lugar de explorar abiertamente los datos.

---

## 3. Cómo detectar sesgo en un dataset

### Paso 1: Analiza la distribución por grupos

Antes de modelar, examina cuántos registros hay por grupo (género, edad, región, etc.) y si están balanceados.

```python
# ¿Cuántos estudiantes hay por curso?
df['curso'].value_counts()

# ¿Qué porcentaje aprueba en cada curso?
df.groupby('curso')['aprobado'].mean()
```

### Paso 2: Evalúa el modelo por subgrupos

No basta con evaluar la precisión global. Un modelo puede tener 90% de precisión general pero fallar sistemáticamente en un grupo específico.

```python
for grupo in df['curso'].unique():
    subset = df[df['curso'] == grupo]
    precision = (subset['prediccion'] == subset['aprobado']).mean()
    print(f"Curso {grupo}: precisión = {precision:.2%}")
```

### Paso 3: Mide el impacto dispar

El impacto dispar ocurre cuando un grupo recibe resultados negativos con una tasa desproporcionada.

Regla del 80%: si el grupo menos favorecido recibe resultados positivos con menos del 80% de la tasa del grupo más favorecido, hay impacto dispar.

```python
tasa_grupo_a = df[df['curso'] == 'A']['aprobado'].mean()
tasa_grupo_b = df[df['curso'] == 'B']['aprobado'].mean()
razon = min(tasa_grupo_a, tasa_grupo_b) / max(tasa_grupo_a, tasa_grupo_b)
print(f"Razón de impacto: {razon:.2f}")  # Si < 0.8, hay posible sesgo
```

---

## 4. Métricas de equidad

### 4.1 Paridad Demográfica (Demographic Parity)

El modelo predice el mismo porcentaje de resultados positivos para todos los grupos, independientemente de si esas predicciones son correctas.

- **Ventaja:** fácil de medir e interpretar
- **Limitación:** puede ignorar diferencias reales entre grupos

### 4.2 Equalized Odds (Odds Igualados)

El modelo tiene la misma tasa de verdaderos positivos (TPR) Y la misma tasa de falsos positivos (FPR) en todos los grupos.

- **Ventaja:** considera tanto los errores como los aciertos
- **Limitación:** a veces es matemáticamente imposible satisfacer todas las métricas de equidad simultáneamente

### 4.3 ¿Cuál usar?

No existe una respuesta única. Depende del contexto:

| Contexto | Métrica sugerida |
|----------|-----------------|
| Contratación | Paridad demográfica + equalized odds |
| Diagnóstico médico | Equalized odds (los errores tienen consecuencias asimétricas) |
| Recomendaciones de contenido | Paridad demográfica |

---

## 5. Privacidad de datos

### 5.1 Principios fundamentales

**Minimización de datos:** Recolecta solo la información que realmente necesitas. Si no necesitas la fecha de nacimiento exacta, no la pidas.

**Consentimiento informado:** Las personas deben saber exactamente para qué se usarán sus datos antes de proporcionarlos.

**Anonimización:** Eliminar o enmascarar información que permita identificar a una persona (nombre, DNI, dirección, teléfono, etc.).

**Seudonimización:** Reemplazar identificadores por códigos, manteniendo la posibilidad de re-identificar si es necesario (con controles de seguridad).

### 5.2 GDPR básico

El Reglamento General de Protección de Datos (GDPR) es una ley europea que establece cómo deben tratarse los datos personales. Aplica a cualquier empresa que maneje datos de ciudadanos europeos.

**Principios clave:**
- Las personas tienen derecho a saber qué datos se tienen de ellas
- Pueden pedir que se corrijan o eliminen
- Los datos no pueden usarse para propósitos distintos al declarado
- Deben protegerse con medidas de seguridad adecuadas

**Multas:** hasta €20 millones o el 4% de la facturación global anual.

### 5.3 Buenas prácticas en el bootcamp

- Nunca uses datos personales reales en ejercicios de práctica
- Usa datasets sintéticos o anonimizados
- No compartas datos de clientes aunque sean "solo para probar algo"

---

## 6. Transparencia y explicabilidad del modelo

### 6.1 El problema de la caja negra

Algunos modelos (redes neuronales profundas, Random Forest con miles de árboles) son muy precisos pero difíciles de interpretar. Esto crea problemas:

- No podemos saber si el modelo usa variables inapropiadas
- No podemos explicarle a una persona por qué fue rechazada
- No podemos corregir errores si no entendemos qué hace el modelo

### 6.2 SHAP Values (Shapley Values)

SHAP es una técnica que asigna a cada variable una contribución numérica a la predicción para un ejemplo específico. Está basado en la teoría de juegos cooperativos de Shapley (Premio Nobel de Economía, 2012).

**Interpretación:**
- Un SHAP positivo = esta variable aumentó la predicción
- Un SHAP negativo = esta variable disminuyó la predicción
- La magnitud indica cuánto influyó

```python
# Ejemplo conceptual
# Para un estudiante específico:
# nota_matematicas: +0.23 (aumentó probabilidad de aprobar)
# asistencia: +0.15
# edad: -0.05
# curso: +0.08
```

---

## 7. Principios de IA Responsable

Varias organizaciones (Google, Microsoft, UE) han publicado principios para el desarrollo responsable de IA:

1. **Equidad:** Los sistemas de IA deben tratar a todas las personas de manera justa
2. **Confiabilidad y seguridad:** Deben funcionar correctamente sin causar daño
3. **Privacidad y seguridad de datos:** Proteger la información personal
4. **Inclusividad:** Deben servir a todas las personas, no solo a algunos grupos
5. **Transparencia:** Las personas deben entender cómo funcionan
6. **Responsabilidad:** Siempre debe haber un humano que responda por las decisiones

---

## 8. ¿Qué hacer en la práctica?

1. **Antes de modelar:** Analiza quién está en tu dataset y quién falta
2. **Durante el diseño:** Pregúntate qué variables podrían ser proxies de características protegidas
3. **Al evaluar:** Mide el rendimiento por subgrupos, no solo en promedio
4. **Al desplegar:** Establece un proceso para monitorear si el modelo produce resultados inequitativos en producción
5. **Siempre:** Documenta tus decisiones y sus posibles consecuencias

---

## Resumen

La ética en datos no es un tema filosófico abstracto — tiene consecuencias concretas para personas reales. Como científicos de datos, tenemos la responsabilidad de entender estos conceptos y aplicarlos activamente en cada proyecto.
