from abc import ABC, abstractmethod
from src.domain.entities.empleado import Empleado


class GetEmpleadoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_empleado: int) -> Empleado:
        pass