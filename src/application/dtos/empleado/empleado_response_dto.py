from pydantic import BaseModel, EmailStr


class EmpleadoResponseDTO(BaseModel):
    id_empleado: int
    nombre: str
    email: EmailStr
    id_area: int
    id_cargo: int