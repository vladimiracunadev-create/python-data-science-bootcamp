# 🔧 Tecnologías complementarias — Clase 14: NumPy — Arrays y cálculo vectorizado

> Herramientas, librerías y recursos para ampliar lo aprendido.

## 📦 Librerías relacionadas

| Librería | Para qué sirve | Nivel sugerido |
|---|---|---|
| `numpy` | Base de todo el ecosistema científico: arrays N-dimensionales y álgebra lineal | Básico |
| `pandas` | DataFrames construidos sobre NumPy; manipulación de datos tabulares | Básico |
| `scipy` | Estadística avanzada, optimización y álgebra lineal extendida sobre NumPy | Intermedio |
| `matplotlib` | Visualización de arrays y funciones matemáticas usando NumPy como base | Básico |
| `sympy` | Matemática simbólica (derivadas, integrales, álgebra) dentro de Python | Intermedio |
| `numba` | Compila código Python/NumPy a código máquina para mayor velocidad | Avanzado |
| `cupy` | NumPy en GPU (NVIDIA CUDA) para procesamiento masivo de matrices | Avanzado |
| `dask` | Arrays y DataFrames distribuidos para datos que no caben en RAM | Avanzado |
| `torch` / `tensorflow` | Tensores con diferenciación automática para deep learning | Avanzado |

## 🌐 Recursos recomendados

- **Documentación oficial**: NumPy — [numpy.org/doc/stable](https://numpy.org/doc/stable/) — incluye guías de usuario, referencia de API y tutoriales de álgebra lineal con ejemplos claros
- **Tutorial recomendado**: "100 NumPy Exercises" en GitHub (rougier/numpy-100) — colección de ejercicios progresivos desde principiante hasta avanzado, ideal para practicar
- **Concepto clave para buscar**: "operaciones vectorizadas en NumPy" / "NumPy vectorized operations" — fundamental para entender por qué NumPy es tan rápido comparado con bucles Python

## 🚀 Próximos pasos sugeridos

- Aprender álgebra lineal con NumPy: `np.dot`, `np.linalg.inv`, `np.linalg.eig` para análisis de datos multivariados y machine learning
- Explorar `np.random` para generación de datos sintéticos y simulaciones estadísticas (Monte Carlo)
- Conectar NumPy con matplotlib para visualizar funciones matemáticas, ondas y distribuciones graficando arrays directamente
- Estudiar cómo pandas usa NumPy internamente y por qué algunas operaciones de pandas son tan rápidas

## 🧰 Herramientas alternativas

| Herramienta | Descripción breve | Cuándo conviene usarla |
|---|---|---|
| R (vectores nativos) | R trata todo como vector por defecto, similar a NumPy, con funciones estadísticas integradas | Análisis estadístico académico con muchas funciones built-in |
| MATLAB | Entorno matricial propietario muy usado en ingeniería y universidades | Proyectos de ingeniería que ya tienen código MATLAB o licencia disponible |
| Julia (Arrays) | Arrays de alto rendimiento con sintaxis matemática natural y velocidad cercana a C | Simulaciones científicas que necesitan la mayor velocidad posible |
| Apache Arrow | Formato de arrays en memoria para interoperabilidad entre Python, R y otros lenguajes | Cuando los datos deben fluir entre diferentes lenguajes y herramientas sin copia |
