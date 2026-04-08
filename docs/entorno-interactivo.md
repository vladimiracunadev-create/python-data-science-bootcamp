# Entorno interactivo local del bootcamp

## Objetivo

Este proyecto incorpora una aplicación local en Python para que el curso no dependa solo de notebooks estáticos. La idea es que el mismo repositorio sirva como:

- base de planificación pedagógica;
- espacio de práctica por clase;
- cuaderno interactivo por celdas;
- runner rápido para probar fragmentos de código;
- laboratorio local reutilizable.

## Componentes principales

- **Vista de clases**: muestra pauta, ejercicios y tarea.
- **Cuaderno tipo Colab**: permite ejecutar celdas manteniendo contexto.
- **Runner rápido**: sirve para probar ideas o resolver dudas en vivo.
- **Guardado de notebooks**: permite persistir trabajo en JSON.

## Modo de ejecución

### Nativo

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m app.app
```

### Docker opcional

```bash
docker compose up --build
```

## Nota técnica

El ejecutor está pensado para **uso local y controlado**. Si se quisiera exponer a internet o a una sala más amplia, habría que agregar sandboxing real, aislamiento por proceso, control de recursos y autenticación.
