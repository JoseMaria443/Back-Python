from abc import ABC, abstractmethod
from datetime import date

from src.domain.entities.emp_cargo import EmpCargo


class AsociarEmpCargoInputPort(ABC):
    @abstractmethod
    def ejecutar(
        self,
        id_empleado: int,
        id_cargo: int,
        fecha_inicio: date,
        fecha_termina: date,
        id_registro_modificacion: int,
    ) -> EmpCargo:
        pass


class DesasociarEmpCargoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_empleado: int, id_cargo: int) -> None:
        pass