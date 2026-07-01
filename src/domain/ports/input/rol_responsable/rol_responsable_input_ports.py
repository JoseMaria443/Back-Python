from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.rol_responsable import RolResponsable


class CreateRolResponsableInputPort(ABC):
    @abstractmethod
    def ejecutar(self, descripcion_rol: str) -> RolResponsable:
        pass


class GetRolResponsableInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_rol: int) -> RolResponsable:
        pass


class ListRolResponsableInputPort(ABC):
    @abstractmethod
    def ejecutar(self, skip: int, limit: int) -> List[RolResponsable]:
        pass


class UpdateRolResponsableInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_rol: int, descripcion_rol: str) -> RolResponsable:
        pass


class DeleteRolResponsableInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_rol: int) -> None:
        pass