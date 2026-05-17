# 🤝 Cómo contribuir

Gracias por tu interés en mejorar el Python Data Science Program.

---

## Tipos de contribuciones bienvenidas

| Tipo | Ejemplos |
|---|---|
| Correcciones de contenido | errores en teoría, ejercicios o soluciones |
| Mejoras pedagógicas | mejor secuencia, ejemplos más claros, nuevos ejercicios |
| Correcciones de bugs | errores en la app Flask, el motor de ejecución o el launcher |
| Mejoras de documentación | textos incorrectos, secciones faltantes, links rotos |
| Nuevos datasets | CSV sintéticos útiles para las clases |
| Mejoras de tests | mayor cobertura, casos borde, smoke tests |

---

## Qué NO aceptamos actualmente

- cambios de versión sin acuerdo previo (el versionado lo maneja el maintainer);
- dependencias nuevas no discutidas (el bundle de Windows tiene un tamaño objetivo);
- cambios en el curriculum que rompan la progresión pedagógica existente;
- código que reduzca la postura de seguridad documentada en `SECURITY.md`.

---

## Flujo de contribución

```
1. Fork del repositorio
2. Crea una rama descriptiva: git checkout -b fix/typo-clase-03
3. Haz tus cambios
4. Verifica que los tests pasan: pytest
5. Verifica lint: ruff check .
6. Verifica seguridad: python -m bandit -r app run_program.py launcher.py
7. Haz commit con mensaje descriptivo (en español)
8. Abre un Pull Request describiendo qué cambiaste y por qué
```

---

## Estándar de commits

Usa mensajes en español, en presente, descriptivos:

```
✓ Corrige error de tipeo en teoria.md de la clase 027 (pandas groupby)
✓ Agrega ejercicio de broadcasting a la clase 017 de NumPy
✓ Fix: timeout no se aplica correctamente en execution_engine
✗ fix
✗ update
✗ cambios varios
```

---

## Verificación antes de PR

```bash
# Tests
pytest

# Lint
ruff check .

# Seguridad (debe terminar con 0 issues)
python -m bandit -q -r app run_program.py launcher.py -x app/saved_notebooks

# Smoke check rápido (arrancar y verificar /health)
python run_program.py &
sleep 5
curl http://127.0.0.1:8000/health
```

---

## Estructura del currículo

El currículo vive en `classes/parte-N-slug/NNN-tema-slug/` (anidado por parte). Cada clase es un stub generado con la estructura mínima:

```
classes/parte-N-slug/NNN-tema-slug/
├── README.md          # ficha: objetivo, resultados esperados, temas
└── notebook.ipynb     # cuaderno guía (hoy stub de 8 celdas)
```

Los materiales adicionales (`teoria.md`, `slides.md`, `ejercicios.md`, `homework.md`, `soluciones.ipynb`, `quiz.json`) se incorporan cuando una clase concreta se desarrolla.

El generador idempotente de la estructura está en `scripts/generate_v2_curriculum.py`.

---

## Reportar bugs

Abre un issue con:
- versión del sistema (`python --version`, OS);
- pasos para reproducir;
- comportamiento esperado vs comportamiento real;
- si es un problema de seguridad, sigue el proceso en [SECURITY.md](SECURITY.md).

---

## Preguntas

Abre un issue con la etiqueta `pregunta`. Respondemos en español o inglés.
