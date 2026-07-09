from pydantic import BaseModel, Field


class EstadoRequestDTO(BaseModel):
    nombre_estado: str = Field(..., min_length=2, max_length=50)


class EstadoResponseDTO(BaseModel):
    id_estado: int
    nombre_estado: str


class ListEstadoResponse(BaseModel):
    items: list[EstadoResponseDTO]
    total: int
    skip: int
    limit: int