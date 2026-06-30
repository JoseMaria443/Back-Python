from pydantic import BaseModel


class CreateEstadoTareaRequest(BaseModel):
    nombre_estado: str


class UpdateEstadoTareaRequest(BaseModel):
    nombre_estado: str


class EstadoTareaResponse(BaseModel):
    id_estado_tarea: int
    nombre_estado: str


class ListEstadoTareaResponse(BaseModel):
    items: list[EstadoTareaResponse]
    total: int
    skip: int
    limit: int
