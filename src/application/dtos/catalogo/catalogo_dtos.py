from pydantic import BaseModel, Field


class CreateCatalogoRequest(BaseModel):
    nombre_catalogo: str = Field(..., min_length=2, max_length=100)
    id_tipo_catalogo: int = Field(..., gt=0)
    descripcion: str = Field(None, max_length=255)


class UpdateCatalogoRequest(BaseModel):
    nombre_catalogo: str = Field(..., min_length=2, max_length=100)
    id_tipo_catalogo: int = Field(..., gt=0)
    descripcion: str = Field(None, max_length=255)


class CatalogoResponse(BaseModel):
    id_catalogo: int
    nombre_catalogo: str
    id_tipo_catalogo: int
    descripcion: str = None


class ListCatalogoResponse(BaseModel):
    items: list[CatalogoResponse]
    total: int
    skip: int
    limit: int