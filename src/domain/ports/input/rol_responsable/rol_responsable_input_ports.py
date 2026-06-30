from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.rol_responsable import RolResponsable


class CreateRolResponsableInputPort(ABC):
    @abstractmethod
    def ejecutar(self, nombre_rol: str, descripcion: str = None) -> RolResponsable:
        pass


class GetRolResponsableInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_rol_responsable: int) -> RolResponsable:
        pass


class ListRolResponsableInputPort(ABC):
    @abstractmethod
    def ejecutar(self, skip: int, limit: int) -> List[RolResponsable]:
        pass


class UpdateRolResponsableInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_rol_responsable: int, nombre_rol: str, descripcion: str = None) -> RolResponsable:
        pass


class DeleteRolResponsableInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_rol_responsable: int) -> None:
        pass