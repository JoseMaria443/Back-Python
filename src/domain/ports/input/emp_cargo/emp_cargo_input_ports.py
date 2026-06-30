from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.emp_cargo import EmpCargo


class CreateEmpCargoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_empleado: int, id_cargo: int, fecha_inicio: str, fecha_termina: str, id_registro_modificacion: int) -> EmpCargo:
        pass


class GetEmpCargoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_empleado: int, id_cargo: int) -> EmpCargo:
        pass


class ListEmpCargoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, skip: int, limit: int) -> List[EmpCargo]:
        pass


class UpdateEmpCargoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_empleado: int, id_cargo: int, fecha_inicio: str, fecha_termina: str, id_registro_modificacion: int) -> EmpCargo:
        pass


class DeleteEmpCargoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_empleado: int, id_cargo: int) -> None:
        pass