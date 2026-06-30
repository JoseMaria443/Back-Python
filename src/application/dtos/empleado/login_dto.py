from pydantic import BaseModel, EmailStr


class LoginRequestDTO(BaseModel):
    email: EmailStr
    password: str


class LoginResponseDTO(BaseModel):
    access_token: str
    token_type: str = "bearer"
    id_empleado: int
    nombre: str
    email: EmailStr