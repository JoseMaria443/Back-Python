from pydantic import BaseModel, Field


class CreateCatalogoRequest(BaseModel):
    id_tipo_catalogo: int = Field(..., gt=0)
    descripcion: str = Field(None, max_length=255)


class UpdateCatalogoRequest(BaseModel):
    id_tipo_catalogo: int = Field(..., gt=0)
    descripcion: str = Field(None, max_length=255)


class CatalogoResponse(BaseModel):
    id_catalogo: int
    id_tipo_catalogo: int
    descripcion: str = None


class ListCatalogoResponse(BaseModel):
    items: list[CatalogoResponse]
    total: int
    skip: int
    limit: int