from pydantic import BaseModel, Field


class CreateTipoCatalogoRequest(BaseModel):
    nombre_tipo_catalogo: str = Field(..., min_length=2, max_length=100)


class UpdateTipoCatalogoRequest(BaseModel):
    nombre_tipo_catalogo: str = Field(..., min_length=2, max_length=100)


class TipoCatalogoResponse(BaseModel):
    id_tipo_catalogo: int
    nombre_tipo_catalogo: str


class ListTipoCatalogoResponse(BaseModel):
    items: list[TipoCatalogoResponse]
    total: int
    skip: int
    limit: int