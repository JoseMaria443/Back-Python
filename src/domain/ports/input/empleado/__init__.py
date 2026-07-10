"""Puertos de entrada para Empleado."""

from .login_input_port import LoginInputPort
from .create_empleado_input_port import CreateEmpleadoInputPort
from .get_empleado_input_port import GetEmpleadoInputPort
from .list_empleado_input_port import ListEmpleadoInputPort
from .desactivar_empleado_input_port import DesactivarEmpleadoInputPort
from .activar_empleado_input_port import ActivarEmpleadoInputPort

__all__ = [
    "LoginInputPort",
    "CreateEmpleadoInputPort",
    "GetEmpleadoInputPort",
    "ListEmpleadoInputPort",
    "DesactivarEmpleadoInputPort",
    "ActivarEmpleadoInputPort",
]
