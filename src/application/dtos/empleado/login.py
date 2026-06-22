"""DTOs para solicitud de login."""

from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    """Request body para endpoint POST /login."""
    email: EmailStr
    password: str

    class Config:
        example = {
            "email": "usuario@ejemplo.com",
            "password": "contraseña"
        }


class LoginResponse(BaseModel):
    """Response body para endpoint POST /login."""
    token: str
    token_type: str = "bearer"
    id_empleado: int
    email: str
    nombre: str

    class Config:
        example = {
            "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
            "token_type": "bearer",
            "id_empleado": 1,
            "email": "usuario@ejemplo.com",
            "nombre": "Juan Pérez"
        }
