from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.infrastructure.config.database import init_db

from src.infrastructure.adapters.entry.routes.empleado_routes import router as empleado_router
from src.infrastructure.adapters.entry.routes.tipo_catalogo_routes import router as tipo_catalogo_router
from src.infrastructure.adapters.entry.routes.catalogo_routes import router as catalogo_router
from src.infrastructure.adapters.entry.routes.estado_routes import router as estado_router
from src.infrastructure.adapters.entry.routes.emp_cargo_routes import router as emp_cargo_router
from src.infrastructure.adapters.entry.routes.rol_destinatario_routes import router as rol_destinatario_router
from src.infrastructure.adapters.entry.routes.rol_responsable_routes import router as rol_responsable_router

app = FastAPI(
    title="API Backend Python",
    description="API REST con arquitectura hexagonal",
    version="1.0.0",
)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(empleado_router)
app.include_router(tipo_catalogo_router)
app.include_router(catalogo_router)
app.include_router(estado_router)
app.include_router(emp_cargo_router)
app.include_router(rol_destinatario_router)
app.include_router(rol_responsable_router)


@app.get("/")
def root():
    return {"message": "API Backend Python - Funcionando correctamente"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}