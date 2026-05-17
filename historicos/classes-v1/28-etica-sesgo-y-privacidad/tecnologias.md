# 🔧 Tecnologías complementarias — Clase 28: Ética, Sesgo y Privacidad

> Herramientas, librerías y recursos para ampliar lo visto en clase.

## 📦 Librerías relacionadas

| Librería | Para qué sirve | Nivel |
|---|---|---|
| `SHAP` | Explicabilidad de modelos: muestra la contribución de cada variable a cada predicción | Básico |
| `LIME` | Explicaciones locales aproximadas de cualquier modelo (caja negra → explicable) | Intermedio |
| `Fairlearn` | Framework de Microsoft para medir y mitigar el sesgo en modelos de ML | Intermedio |
| `AI Fairness 360 (AIF360)` | Kit de herramientas de IBM con 70+ métricas de equidad y algoritmos de mitigación | Avanzado |
| `What-If Tool` | Herramienta visual de Google para explorar fairness e interpretabilidad | Básico |
| `Alibi` | Explicaciones contrafácticas y de anclaje para modelos en producción | Avanzado |
| `PyCaret` | AutoML con reportes de equidad integrados | Intermedio |
| `Evidently AI` | Monitoreo de drift y equidad en modelos en producción | Avanzado |

## 🌐 Recursos recomendados

- **SHAP documentation**: https://shap.readthedocs.io/en/latest/ — tutoriales para Tree SHAP, Kernel SHAP y gráficos de interpretabilidad.
- **Fairlearn documentation**: https://fairlearn.org/ — guía completa con ejemplos en español y casos de uso reales.
- **Google Responsible AI Practices**: https://ai.google/responsibility/responsible-ai-practices/ — principios y herramientas para IA responsable.
- **Texto del RGPD en español**: https://rgpd.es/ — versión anotada del Reglamento General de Protección de Datos.
- **Curso: Fairness in ML (Google)**: https://developers.google.com/machine-learning/crash-course/fairness/video-lecture — video gratuito de 15 minutos, muy accesible.
- **Libro: "Armas de Destrucción Matemática"** (Cathy O'Neil) — lectura recomendada sobre el impacto social de los algoritmos.

## 🚀 Próximos pasos

- Explorar **SHAP summary plots** para entender qué variables afectan más a las predicciones en el dataset de estudiantes.
- Investigar **Fairlearn** para calcular métricas de equidad (demographic parity, equalized odds) en modelos propios.
- Leer sobre **privacidad diferencial** (differential privacy): técnica matemática para agregar ruido controlado a datos y proteger la privacidad individual.
- Explorar el concepto de **federated learning**: entrenar modelos sin mover los datos de los dispositivos de los usuarios.
- Investigar la regulación de **IA en Europa (AI Act)**: la primera ley de IA del mundo, aprobada en 2024.

## 🧰 Herramientas alternativas

| Herramienta | Descripción | Cuándo usarla |
|---|---|---|
| `What-If Tool` (Google) | Interfaz visual interactiva para explorar modelos y su fairness | Presentaciones o exploración inicial sin código |
| `Fairlearn` (Microsoft) | Métricas de equidad y algoritmos de remediación bien documentados | Proyectos con requisitos de cumplimiento normativo |
| `AI Fairness 360` (IBM) | Framework más completo académicamente, 70+ métricas | Investigación o proyectos con necesidades de fairness complejas |
| `TensorFlow Privacy` | Entrenamiento con privacidad diferencial para redes neuronales | Modelos de deep learning con datos sensibles |
| `PySyft` | Framework de federated learning y encriptación homomórfica | Proyectos con datos que no pueden centralizarse |
