from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.historial_estado_empleado import HistorialEstadoEmpleado


class HistorialEstadoEmpleadoRepositoryPort(ABC):
    """Interfaz (puerto) para persistencia de HistorialEstadoEmpleado."""

    @abstractmethod
    def crear(self, historial: HistorialEstadoEmpleado) -> HistorialEstadoEmpleado:
        """Crea una nueva entrada de historial."""
        pass

    @abstractmethod
    def listar_por_empleado(self, id_empleado: int, skip: int = 0, limit: int = 50) -> List[HistorialEstadoEmpleado]:
        """Lista el historial de un empleado."""
        pass

    @abstractmethod
    def contar_por_empleado(self, id_empleado: int) -> int:
        """Cuenta entradas de historial de un empleado."""
        pass