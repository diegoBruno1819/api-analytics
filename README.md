# API Analytics - Vertex Craft

API REST diseñada para consultar y analizar información de ventas.

## Requisitos previos

- Python 3.9.25 o superior.
- Git Bash instalado.

## Instalación

1. Asegúrate de tener tu entorno virtual configurado.
2. Instala las dependencias necesarias ejecutando el siguiente comando:

```bash
./.venv/python.exe -m pip install -r requirements.txt
```

## Ejecución

Para iniciar el servidor de desarrollo, ejecuta el siguiente comando desde la raíz del proyecto en Git Bash:

```bash
./.venv/python.exe -m uvicorn app.main:app --reload
```

## Acceso a la API

Una vez que el servidor esté en marcha, puedes acceder a:

- **Endpoint principal:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Documentación interactiva (Swagger UI):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Detener el servidor

Para detener el servidor, presiona `Ctrl + C` en la terminal donde se está ejecutando.

