"""DTOs para creación de Empleado."""

from pydantic import BaseModel, EmailStr


class CreateEmpleadoRequest(BaseModel):
    """Request body para crear Empleado (solo admin en esta fase)."""
    nombre: str
    email: EmailStr
    password: str  # Se recibirá en texto plano y se hasheará antes de guardar
    id_area: int
    id_cargo: int

    class Config:
        example = {
            "nombre": "Juan Pérez",
            "email": "juan.perez@ejemplo.com",
            "password": "password_segura",
            "id_area": 1,
            "id_cargo": 2
        }


class CreateEmpleadoResponse(BaseModel):
    """Response body para creación de Empleado."""
    id_empleado: int
    nombre: str
    email: str
    id_area: int
    id_cargo: int
    activo: bool = True

    class Config:
        example = {
            "id_empleado": 1,
            "nombre": "Juan Pérez",
            "email": "juan.perez@ejemplo.com",
            "id_area": 1,
            "id_cargo": 2,
            "activo": True
        }
