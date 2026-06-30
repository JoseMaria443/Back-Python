from pydantic import BaseModel, Field


class RolResponsableRequestDTO(BaseModel):
    nombre_rol: str = Field(..., min_length=2, max_length=50)
    descripcion: str = Field(None, max_length=255)


class RolResponsableResponseDTO(BaseModel):
    id_rol_responsable: int
    nombre_rol: str
    descripcion: str = None