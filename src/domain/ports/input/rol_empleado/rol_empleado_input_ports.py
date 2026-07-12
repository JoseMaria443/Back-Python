from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.rol_empleado import RolEmpleado


class CreateRolEmpleadoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, descripcion: str) -> RolEmpleado:
        pass


class GetRolEmpleadoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_rol: int) -> RolEmpleado:
        pass


class ListRolEmpleadoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, skip: int = 0, limit: int = 50) -> List[RolEmpleado]:
        pass


class UpdateRolEmpleadoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_rol: int, descripcion: str) -> RolEmpleado:
        pass


class DeleteRolEmpleadoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_rol: int) -> None:
        pass