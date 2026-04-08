# Entorno interactivo local del bootcamp

## Objetivo

Este proyecto incorpora una aplicacion local en Python para que el curso no dependa solo de notebooks estaticos. La idea es que el mismo repositorio sirva como:

- base de planificacion pedagogica;
- espacio de practica por clase;
- cuaderno interactivo por celdas;
- runner rapido para probar fragmentos de codigo;
- laboratorio local reutilizable.

## Componentes principales

- **Vista de clases**: muestra pauta, ejercicios y tarea.
- **Cuaderno tipo Colab**: permite ejecutar celdas manteniendo contexto.
- **Runner rapido**: sirve para probar ideas o resolver dudas en vivo.
- **Guardado de notebooks**: permite persistir trabajo en JSON.

## Modo de ejecucion

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

## Nota tecnica

El ejecutor esta pensado para **uso local y controlado**. Si se quisiera exponer a internet o a una sala mas amplia, habria que agregar sandboxing real, aislamiento por proceso, control de recursos y autenticacion.
