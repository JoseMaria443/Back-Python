from pydantic import BaseModel, Field


class RolDestinatarioRequestDTO(BaseModel):
    nombre_rol: str = Field(..., min_length=2, max_length=50)
    descripcion: str = Field(None, max_length=255)


class RolDestinatarioResponseDTO(BaseModel):
    id_rol_destinatario: int
    nombre_rol: str
    descripcion: str = None