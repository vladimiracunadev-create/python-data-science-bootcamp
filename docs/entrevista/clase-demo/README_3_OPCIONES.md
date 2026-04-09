# 🎥 3 Opciones de Clase — 45 Minutos Online

## Formato: Presentación Online con Evaluador

---

## 📊 Comparativa Rápida

| Aspecto | Opción 1: Visualización | Opción 2: ML Intro | Opción 3: Pipelines |
|---------|---|---|---|
| **Clase** | 6 (Matplotlib) | 9 (Machine Learning) | 11 (Evaluación y Pipelines) |
| **Dificultad** | Media | Media-Alta | Alta |
| **Diapositivas** | 8 | 8 | 8 |
| **Código en vivo** | Gráficos (bonito) | Simple (rentable) | GridSearchCV (complejo) |
| **Engagement** | Alto (visual) | Alto (conceptual) | Medio-Alto (técnico) |
| **Riesgo** | Bajo | Medio | Medio-Alto |
| **Mejor para mostrar** | Creatividad + claridad | Fundamentos sólidos | Profundidad técnica |

---

## 🎯 Opción 1: Visualización (Clase 6)

### **Lo que enseñas:**
- Por qué visualizar datos (Anscombe's Quartet)
- Tipos de gráficos (scatter, line, bar, histogram, box)
- Matplotlib basics (plot, xlabel, title, estilo)
- Subplots (múltiples gráficos)
- Ejercicio: Gráficos de Iris dataset

### **Ventajas:**
✅ Visual impactante  
✅ Fácil de entender  
✅ Código corto y simple  
✅ Buen ejercicio (alumnos ven resultados)  

### **Desventajas:**
❌ Menos "hardcore"  
❌ Riesgo de parecer superficial  

### **Timing exacto:**
```
0-1 min: Apertura
1-5 min: ¿Por qué visualizar? + Anscombe
5-15 min: Tipos de gráficos
15-25 min: Código matplotlib
25-35 min: Subplots
35-40 min: Ejercicio Iris (scatter + histogram)
40-45 min: Resumen + preguntas
```

### **Demo principal:**
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title('Onda Seno')
plt.show()
```

### **Si quieres escolher esta:**
- Ejecuta mínimo 3 demos
- Dibuja Anscombe's Quartet si puedes
- Haz el ejercicio final interactivo (pide que piensen qué gráfico usar)

---

## 🤖 Opción 2: ML Intro (Clase 9)

### **Lo que enseñas:**
- ¿Qué es Machine Learning? (Supervised vs Unsupervised)
- Flujo típico (datos → limpiar → entrenar → evaluar)
- Primer modelo: Regresión Lineal
- Overfitting vs Underfitting
- Algoritmos comunes (por nombre)
- Evaluación: Accuracy

### **Ventajas:**
✅ Demuestra conceptos fundamentales  
✅ Nivel intermedio (ni trivial, ni demasiado hard)  
✅ Prepara para Clase 10  
✅ Evaluador ve breadth

### **Desventajas:**
❌ Riesgo de parecer genérico  
❌ Muchos conceptos (es rápido)  

### **Timing exacto:**
```
0-1 min: Apertura + pregunta hook ("Netflix sabe qué viste")
1-5 min: ¿Qué es ML? 3 tipos
5-10 min: Flujo (obtener → explorar → limpiar → entrenar → evaluar)
10-20 min: Código: LinearRegression + train_test_split
20-28 min: Overfitting vs Underfitting (dibuja curvas)
28-35 min: Algoritmos comunes (nombres)
35-40 min: Evaluación: accuracy
40-45 min: Resumen + preguntas
```

### **Demo principal:**
```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

modelo = LinearRegression()
modelo.fit(X_train, y_train)
score = modelo.score(X_test, y_test)
print(f'Score: {score:.3f}')
```

### **Si quieres escolher esta:**
- Menciona ejemplos del mundo real (Netflix, Spotify, Uber)
- Dibuja CURVAS de learning (train vs test) en pizarra
- Explica por qué overfitting es peligroso

---

## ⚙️ Opción 3: Pipelines (Clase 11)

### **Lo que enseñas:**
- Overfitting (problema existente)
- Cross-Validation (k-fold, solución)
- Métricas: Precision, Recall, F1 (contexto importa)
- GridSearchCV (búsqueda automática de hiperparámetros)
- Pipelines (encadenamiento automático)
- Todo junto: Pipeline + GridSearchCV

### **Ventajas:**
✅ Demuestra profundidad técnica  
✅ Muy práctico (se usa en producción)  
✅ Evaluador ve que dominas ML avanzado  
✅ Código interesante

### **Desventajas:**
❌ Difícil de explicar en 45 min  
❌ Riesgo de confundir  
❌ Muchas líneas de código  

### **Timing exacto:**
```
0-1 min: Apertura + problema (95% train, 62% test)
1-6 min: Cross-Validation (qué es, por qué)
6-13 min: Código: cross_val_score
13-20 min: Métricas: Precision, Recall, F1 (ejemplo médico)
20-27 min: GridSearchCV (qué hace, por qué)
27-35 min: Código: GridSearchCV
35-40 min: Pipelines + GridSearchCV (lo mejor de todo)
40-45 min: Resumen + preguntas
```

### **Demo principal:**
```python
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier

param_grid = {'max_depth': [3, 5, 7, 10]}

grid = GridSearchCV(DecisionTreeClassifier(), param_grid, cv=5)
grid.fit(X_train, y_train)

print(f'Mejores parámetros: {grid.best_params_}')
print(f'Mejor score: {grid.best_score_:.3f}')
```

### **Si quieres escolher esta:**
- Ejecuta GridSearchCV (tarda ~10 seg, vale la pena)
- Dibuja confusion matrix en pizarra (visual fuerte)
- Explica por qué Precision vs Recall depende del contexto

---

## 🎓 ¿Cuál Elegir?

### **Elige OPCIÓN 1 si:**
- Quieres destacar por CLARIDAD y COMUNICACIÓN
- Prefieres minimizar riesgo técnico
- Quieres que sea visual y atractivo
- El evaluador valora pedagogía > profundidad

### **Elige OPCIÓN 2 si:**
- Quieres balance entre profundidad y claridad
- Prefieres conceptos fundamentales bien explicados
- Quieres mostrar amplitud (no solo 1 tema)
- Tienes confianza media-alta

### **Elige OPCIÓN 3 si:**
- Quieres impresionar con profundidad técnica
- Dominas BIEN los temas (has practicado mucho)
- El evaluador valora técnica > pedagogía
- Te sientes cómodo con errores menores en explicación (si captas lo esencial, está bien)

---

## 📂 Estructura de Carpetas

```
interview-prep/
├── opcion-1-visualizacion/
│   ├── doc/
│   │   └── Clase_06_Visualizacion_45min.pptx
│   ├── README.md
│   └── guia-rapida.txt
│
├── opcion-2-ml-intro/
│   ├── doc/
│   │   └── Clase_09_ML_Intro_45min.pptx
│   ├── README.md
│   └── guia-rapida.txt
│
├── opcion-3-pipelines/
│   ├── doc/
│   │   └── Clase_11_Evaluacion_Pipelines_45min.pptx
│   ├── README.md
│   └── guia-rapida.txt
│
├── PRESENTACION_ONLINE_CON_EVALUADOR.md [LEER ESTO PRIMERO]
└── README_3_OPCIONES.md [ESTÁS AQUÍ]
```

---

## ✅ Checklist Decisión

- [ ] Leí las 3 opciones
- [ ] Ejecuté (o imaginé) las demos principales
- [ ] Elegí una que me deja confiado/a
- [ ] Abierto el PPTX de mi opción
- [ ] Leí PRESENTACION_ONLINE_CON_EVALUADOR.md
- [ ] Preparé reloj para timing
- [ ] Hice una "carrera" de 45 min (ensayo completo)

---

## 🚀 Próximas Etapas

1. **Ahora:** Elige tu opción
2. **Hoy:** Lee la guía ONLINE + 1 carrera completa
3. **Mañana:** 2 carreras más, enfocándote en timing
4. **Pasado:** 1 carrera final, "en serio" (como si fuera la real)
5. **Día de la entrevista:** Confía, respira, ¡hazlo!

---

**¿Listo?** Abre la carpeta de tu opción elegida.

*Tiempo de preparación restante: 4-6 horas*
