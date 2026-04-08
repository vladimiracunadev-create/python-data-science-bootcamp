# Guía del estudiante

## Qué necesitas

- Python 3.11 o superior
- conexión básica para instalar dependencias
- editor o navegador para trabajar con Jupyter Notebook

## Preparación del entorno

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

### Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter notebook
```

## Cómo trabajar el material

1. leer el `README.md` de la clase;
2. abrir el notebook correspondiente;
3. ejecutar celda por celda;
4. intentar los ejercicios antes de ver soluciones;
5. registrar dudas y hallazgos.

## Buenas prácticas

- ejecutar con calma;
- cambiar valores y observar resultados;
- escribir comentarios breves en el notebook;
- guardar una copia propia si quieres experimentar más.

## Si algo falla

- revisar si el entorno está activado;
- verificar instalación de dependencias;
- usar `python examples/validate_bootcamp.py`;
- pedir apoyo al docente mostrando el error exacto.
