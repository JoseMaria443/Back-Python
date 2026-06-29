"""Aplicación FastAPI principal."""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.infrastructure.adapters.entry.web.empleado import router as empleado_router
from src.infrastructure.adapters.entry.web.comunicado import router as comunicado_router
from src.infrastructure.adapters.entry.web.tarea import router as tarea_router
from src.infrastructure.adapters.entry.web.archivo import router as archivo_router
from src.infrastructure.adapters.entry.web.tipo_catalogo import router as tipo_catalogo_router
from src.infrastructure.adapters.entry.web.catalogo import router as catalogo_router
from src.infrastructure.adapters.entry.web.rol_destinatario import router as rol_destinatario_router
from src.infrastructure.adapters.entry.web.rol_responsable import router as rol_responsable_router
from src.infrastructure.adapters.entry.web.estado_tarea import router as estado_tarea_router
from src.infrastructure.adapters.entry.web.emp_cargo import router as emp_cargo_router

app = FastAPI(
    title="Sistema de Gestión de Comunicados",
    description="API Backend con Arquitectura Hexagonal",
    version="0.1.0",
)

app.include_router(empleado_router)
app.include_router(comunicado_router)
app.include_router(tarea_router)
app.include_router(archivo_router)
app.include_router(tipo_catalogo_router)
app.include_router(catalogo_router)
app.include_router(rol_destinatario_router)
app.include_router(rol_responsable_router)
app.include_router(estado_tarea_router)
app.include_router(emp_cargo_router)


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
