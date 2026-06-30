from pydantic import BaseModel, EmailStr, Field


class CreateEmpleadoRequestDTO(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=50)
    id_area: int = Field(..., gt=0)
    id_cargo: int = Field(..., gt=0)


class CreateEmpleadoResponseDTO(BaseModel):
    id_empleado: int
    nombre: str
    email: EmailStr
    id_area: int
    id_cargo: int

