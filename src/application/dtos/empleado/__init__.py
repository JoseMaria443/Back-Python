"""DTOs del módulo Empleado."""

from .login import LoginRequest, LoginResponse
from .create import CreateEmpleadoRequest, CreateEmpleadoResponse

__all__ = [
    "LoginRequest",
    "LoginResponse",
    "CreateEmpleadoRequest",
    "CreateEmpleadoResponse",
]
