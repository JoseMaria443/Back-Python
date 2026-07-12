from pydantic import BaseModel


class CreateRolEmpleadoRequest(BaseModel):
    descripcion: str


class UpdateRolEmpleadoRequest(BaseModel):
    descripcion: str


class RolEmpleadoResponse(BaseModel):
    id_rol: int
    descripcion: str


class ListRolEmpleadoResponse(BaseModel):
    items: list[RolEmpleadoResponse]
    total: int
    skip: int
    limit: int