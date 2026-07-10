from abc import ABC, abstractmethod
from src.domain.entities.empleado import Empleado


class ActivarEmpleadoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_empleado: int, id_empleado_ejecutor: int) -> Empleado:
        pass
