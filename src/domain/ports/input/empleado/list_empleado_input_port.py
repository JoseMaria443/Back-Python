from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.empleado import Empleado


class ListEmpleadoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, skip: int = 0, limit: int = 50, nombre: str = None) -> List[Empleado]:
        pass