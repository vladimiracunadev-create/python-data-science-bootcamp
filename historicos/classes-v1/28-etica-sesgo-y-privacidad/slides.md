# 📊 Slides — Clase 28: Ética, sesgo y privacidad en datos

---

## Slide 1: ¿Por qué ética en datos?

**Los modelos toman decisiones reales sobre personas reales.**

- ¿A quién se contrata?
- ¿A quién se le aprueba un préstamo?
- ¿A quién muestra el algoritmo una oferta de trabajo?

> "Un modelo no es neutro solo porque use matemáticas."

---

## Slide 2: Casos reales de algoritmos injustos

| Caso | Problema |
|------|----------|
| COMPAS (justicia penal, EE.UU.) | Predecía reincidencia con sesgo racial |
| Amazon Hiring Tool (2018) | Penalizaba CVs con la palabra "mujeres" |
| Reconocimiento facial | Tasa de error 35% mayor en mujeres de piel oscura |
| Préstamos bancarios | Minorías rechazadas con igual historial crediticio |

---

## Slide 3: ¿Qué es el sesgo en datos?

**Sesgo** = cuando los datos no representan bien la realidad, o la representan de forma injusta.

### Tipos principales:

**Sesgo histórico**
- Los datos reflejan desigualdades pasadas
- Ejemplo: datos de contratación de 20 años con pocas mujeres en liderazgo

**Sesgo de muestreo**
- Algunos grupos están subrepresentados en el dataset
- Ejemplo: un modelo de salud entrenado solo con pacientes de ciudad

**Sesgo de medición**
- La variable que medimos no captura lo que queremos medir
- Ejemplo: usar "arrestos previos" como proxy de peligrosidad

---

## Slide 4: ¿Cómo detectar sesgo?

1. **Analiza la distribución por grupos**: ¿Cuántos estudiantes de cada curso hay?
2. **Compara tasas de predicción**: ¿El modelo acierta igual para todos los grupos?
3. **Mide el impacto dispar**: ¿Un grupo recibe resultados negativos más seguido?

```python
# Distribución por grupo
df.groupby('curso')['aprobado'].mean()
```

---

## Slide 5: Métricas de equidad

### Paridad Demográfica
- El modelo predice resultados positivos con la misma tasa para todos los grupos
- `P(ŷ=1 | grupo=A) = P(ŷ=1 | grupo=B)`

### Equalized Odds (Odds Igualados)
- El modelo tiene la misma tasa de verdaderos positivos Y falsos positivos en todos los grupos
- Más exigente que paridad demográfica

> No existe una métrica perfecta — elegir la correcta depende del contexto.

---

## Slide 6: Privacidad de datos

### Principios fundamentales

1. **Minimización**: recolecta solo lo necesario
2. **Consentimiento**: la persona debe saber para qué se usan sus datos
3. **Anonimización**: eliminar o enmascarar identificadores personales
4. **Derecho al olvido**: las personas pueden pedir que se borren sus datos

### GDPR (Reglamento General de Protección de Datos)
- Ley europea que protege datos personales
- Multas de hasta el 4% de la facturación anual global
- Aplica si tus usuarios son europeos, sin importar dónde está la empresa

---

## Slide 7: Transparencia — ¿Por qué el modelo decidió eso?

**El problema de la caja negra:**
- Un modelo puede ser muy preciso pero completamente opaco
- ¿Podemos explicar por qué rechazó una solicitud de crédito?

### SHAP Values (Shapley Values)
- Cuánto contribuyó cada variable a la predicción para UN ejemplo específico
- "La nota de matemáticas aumentó la probabilidad de aprobar en 18%"
- Basado en teoría de juegos cooperativos

```python
import shap
explainer = shap.TreeExplainer(modelo)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test)
```

---

## Slide 8: Principios de IA Responsable

| Principio | Qué significa |
|-----------|---------------|
| **Equidad** | No discriminar por raza, género, edad u otras características protegidas |
| **Responsabilidad** | Alguien debe responder por las decisiones del modelo |
| **Transparencia** | Los afectados deben poder entender cómo funciona |
| **Explicabilidad** | Las predicciones deben poder justificarse |
| **Privacidad** | Proteger los datos personales de los usuarios |
| **Seguridad** | El modelo no debe ser manipulable ni causar daño |

---

## Slide 9: ¿Qué puedes hacer tú?

✅ Analiza siempre la distribución de tu dataset antes de modelar  
✅ Evalúa el rendimiento del modelo por subgrupos, no solo en promedio  
✅ Pregúntate: ¿a quién podría perjudicar este modelo?  
✅ Documenta las decisiones de diseño y sus posibles consecuencias  
✅ Nunca publiques datos personales sin anonimizar  

---

## Slide 10: Resumen

> Un modelo técnicamente correcto puede ser socialmente injusto.

La ética en datos no es un paso opcional al final del proyecto — es una lente que debe estar presente desde que defines el problema hasta que despliegas la solución.
