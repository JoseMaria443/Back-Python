from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.rol_destinatario import RolDestinatario


class CreateRolDestinatarioInputPort(ABC):
    @abstractmethod
    def ejecutar(self, nombre_rol: str, descripcion: str = None) -> RolDestinatario:
        pass


class GetRolDestinatarioInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_rol_destinatario: int) -> RolDestinatario:
        pass


class ListRolDestinatarioInputPort(ABC):
    @abstractmethod
    def ejecutar(self, skip: int, limit: int) -> List[RolDestinatario]:
        pass


class UpdateRolDestinatarioInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_rol_destinatario: int, nombre_rol: str, descripcion: str = None) -> RolDestinatario:
        pass


class DeleteRolDestinatarioInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_rol_destinatario: int) -> None:
        pass