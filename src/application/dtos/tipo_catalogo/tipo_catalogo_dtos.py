from pydantic import BaseModel, Field


class TipoCatalogoRequestDTO(BaseModel):
    nombre_tipo_catalogo: str = Field(..., min_length=2, max_length=100)


class TipoCatalogoResponseDTO(BaseModel):
    id_tipo_catalogo: int
    nombre_tipo_catalogo: str