from pydantic import BaseModel, Field


class CatalogoRequestDTO(BaseModel):
    nombre_catalogo: str = Field(..., min_length=2, max_length=100)
    id_tipo_catalogo: int = Field(..., gt=0)
    descripcion: str = Field(None, max_length=255)


class CatalogoResponseDTO(BaseModel):
    id_catalogo: int
    nombre_catalogo: str
    id_tipo_catalogo: int
    descripcion: str = None