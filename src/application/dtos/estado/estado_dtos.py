from pydantic import BaseModel, Field


class EstadoRequestDTO(BaseModel):
    nombre_estado: str = Field(..., min_length=2, max_length=50)
    descripcion: str = Field(None, max_length=255)


class EstadoResponseDTO(BaseModel):
    id_estado: int
    nombre_estado: str
    descripcion: str = None