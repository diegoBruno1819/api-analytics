from fastapi import FastAPI
from app.api.v1.sales import router as sales_router

# Instancia de la aplicación FastAPI con metadatos
app = FastAPI(
    title="API Analytics",
    description="API REST para consultar y analizar información de ventas.",
    version="0.1.0"
)

# Incluir routers
app.include_router(sales_router, prefix="/api/v1")

# Endpoint raíz
@app.get("/")
def read_root():
    return {
        "project": "API Analytics",
        "status": "running",
        "message": "Bienvenido a la API de análisis de ventas de Vertex Craft"
    }


