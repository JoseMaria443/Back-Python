from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.historial_estado_empleado import HistorialEstadoEmpleado


class ListHistorialEstadoEmpleadoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_empleado: int, skip: int = 0, limit: int = 50) -> List[HistorialEstadoEmpleado]:
        pass