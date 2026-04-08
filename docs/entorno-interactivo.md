# 💻 Entorno interactivo local del bootcamp

## Objetivo

Este proyecto incorpora una aplicaciÃ³n local en Python para que el curso no dependa solo de notebooks estÃ¡ticos. La idea es que el mismo repositorio sirva como:

- base de planificaciÃ³n pedagÃ³gica;
- espacio de prÃ¡ctica por clase;
- cuaderno interactivo por celdas;
- runner rÃ¡pido para probar fragmentos de cÃ³digo;
- laboratorio local reutilizable.

## Componentes principales

- **Vista de clases**: muestra pauta, ejercicios y tarea.
- **Cuaderno tipo Colab**: permite ejecutar celdas manteniendo contexto.
- **Runner rÃ¡pido**: sirve para probar ideas o resolver dudas en vivo.
- **Guardado de notebooks**: permite persistir trabajo en JSON.

## Modo de ejecuciÃ³n

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

## Nota tÃ©cnica

El ejecutor estÃ¡ pensado para **uso local y controlado**. Si se quisiera exponer a internet o a una sala mÃ¡s amplia, habrÃ­a que agregar sandboxing real, aislamiento por proceso, control de recursos y autenticaciÃ³n.
