"""Aplicación FastAPI principal."""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.infrastructure.adapters.entry.web.empleado import router as empleado_router

# Crear aplicación FastAPI
app = FastAPI(
    title="Sistema de Gestión de Comunicados",
    description="API Backend con Arquitectura Hexagonal",
    version="0.1.0",
)

# Incluir routers
app.include_router(empleado_router)


@app.get("/", tags=["root"])
def read_root():
    """Endpoint raíz para verificar que la API está activa."""
    return {
        "message": "Sistema de Gestión de Comunicados - API Backend",
        "version": "0.1.0",
        "status": "operational",
    }


@app.get("/health", tags=["health"])
def health_check():
    """Endpoint de health check."""
    return {
        "status": "ok",
    }


# Manejo de excepciones global
@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """Manejador global de excepciones."""
    return JSONResponse(
        status_code=500,
        content={"detail": "Error interno del servidor"},
    )
