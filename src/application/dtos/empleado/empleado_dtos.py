from pydantic import BaseModel


class EmpleadoResponse(BaseModel):
    id_empleado: int
    nombre: str
    email: str
    id_area: int
    id_cargo: int
    activo: bool


class ListEmpleadoResponse(BaseModel):
    items: list[EmpleadoResponse]
    total: int
    skip: int
    limit: int