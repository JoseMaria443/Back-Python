from pydantic import BaseModel
from datetime import datetime


class HistorialEstadoEmpleadoResponse(BaseModel):
    id_historial: int
    id_empleado: int
    accion: str
    id_empleado_ejecutor: int
    fecha: datetime


class ListHistorialEstadoEmpleadoResponse(BaseModel):
    items: list[HistorialEstadoEmpleadoResponse]
    total: int
    skip: int
    limit: int