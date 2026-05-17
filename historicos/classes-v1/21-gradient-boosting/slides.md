# 🖥️ Diapositivas sugeridas — Clase 21

> 🖥️ Guion visual breve para conducir la sesión sin sobrecargar la clase.

## 🚪 Apertura

- Pregunta inicial: "Si entrenaste un modelo y sabes exactamente dónde se equivocó, ¿qué harías con esa información?"
- Conectar: eso es exactamente lo que hace el Gradient Boosting — el siguiente árbol se construye para corregir los errores del anterior.
- Comparar con Random Forest: en el bosque, los árboles se construyen en paralelo e independientemente. En Gradient Boosting, se construyen en serie, aprendiendo unos de otros.

## 🛤️ Ruta de la sesión

| Tramo | Tiempo sugerido | Enfoque | Evidencia |
|---|---|---|---|
| Inicio | 10 min | Concepto boosting vs bagging | Diferencia explicada con palabras propias |
| Desarrollo 1 | 20 min | GradientBoostingClassifier + parámetros | Modelo entrenado y accuracy impreso |
| Desarrollo 2 | 15 min | learning_rate: demasiado alto vs bajo | Gráfico de accuracy vs learning_rate |
| Desarrollo 3 | 15 min | XGBoost básico | Comparación sklearn vs xgb |
| Práctica | 20 min | Comparar 4 clasificadores | Tabla de resultados entregada |
| Cierre | 10 min | ¿Cuándo usar GBM? | Autoevaluación |

## 📌 Puntos que deben quedar claros

- Boosting = árboles en serie, cada uno corrige al anterior.
- `learning_rate` controla cuánto aprende cada árbol: alto → sobreajusta, bajo → necesita más árboles.
- GBM suele ser el mejor modelo en datos tabulares en Kaggle.
- XGBoost es una implementación optimizada y más rápida del mismo concepto.

## 🏁 Cierre esperado

Con estas tres clases (19, 20, 21) el estudiante tiene el arsenal completo de modelos supervisados para datos tabulares: regresión lineal, árboles, bosques y boosting.
