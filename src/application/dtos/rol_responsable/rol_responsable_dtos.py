from pydantic import BaseModel, Field


class CreateRolResponsableRequest(BaseModel):
    descripcion_rol: str = Field(..., min_length=2, max_length=255)


class UpdateRolResponsableRequest(BaseModel):
    descripcion_rol: str = Field(..., min_length=2, max_length=255)


class RolResponsableResponse(BaseModel):
    id_rol: int
    descripcion_rol: str


class ListRolResponsableResponse(BaseModel):
    items: list[RolResponsableResponse]
    total: int
    skip: int
    limit: int