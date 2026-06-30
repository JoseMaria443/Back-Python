from datetime import date
from typing import Optional
from pydantic import BaseModel


class CreateTareaRequest(BaseModel):
    id_comunicado: int
    descripcion: str
    fecha_entrega: date
    fecha_registro: date
    id_estado_tarea: Optional[int] = None


class UpdateTareaRequest(BaseModel):
    id_comunicado: int
    descripcion: str
    fecha_entrega: date
    fecha_registro: date
    id_estado_tarea: Optional[int] = None


class TareaResponse(BaseModel):
    id_tarea: int
    id_comunicado: int
    descripcion: str
    fecha_entrega: date
    fecha_registro: date
    id_estado_tarea: Optional[int] = None


class ListTareaResponse(BaseModel):
    items: list[TareaResponse]
    total: int
    skip: int
    limit: int
