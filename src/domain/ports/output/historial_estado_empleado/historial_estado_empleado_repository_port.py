from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.historial_estado_empleado import HistorialEstadoEmpleado


class HistorialEstadoEmpleadoRepositoryPort(ABC):
    @abstractmethod
    def crear(self, historial: HistorialEstadoEmpleado) -> HistorialEstadoEmpleado:
        pass

    @abstractmethod
    def listar(self, id_empleado: int, skip: int = 0, limit: int = 50) -> List[HistorialEstadoEmpleado]:
        pass

    @abstractmethod
    def contar(self, id_empleado: int) -> int:
        pass