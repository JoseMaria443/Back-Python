from pydantic import BaseModel, Field


class CreateRolDestinatarioRequest(BaseModel):
    descripcion: str = Field(..., min_length=2, max_length=255)


class UpdateRolDestinatarioRequest(BaseModel):
    descripcion: str = Field(..., min_length=2, max_length=255)


class RolDestinatarioResponse(BaseModel):
    id_rol: int
    descripcion: str


class ListRolDestinatarioResponse(BaseModel):
    items: list[RolDestinatarioResponse]
    total: int
    skip: int
    limit: int