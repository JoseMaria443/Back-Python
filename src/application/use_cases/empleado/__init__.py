"""Casos de uso del módulo Empleado."""

from .login_use_case import LoginUseCase
from .create_empleado_use_case import CreateEmpleadoUseCase

__all__ = ["LoginUseCase", "CreateEmpleadoUseCase"]
