from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.rol_destinatario import RolDestinatario


class CreateRolDestinatarioInputPort(ABC):
    @abstractmethod
    def ejecutar(self, descripcion: str) -> RolDestinatario:
        pass


class GetRolDestinatarioInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_rol: int) -> RolDestinatario:
        pass


class ListRolDestinatarioInputPort(ABC):
    @abstractmethod
    def ejecutar(self, skip: int, limit: int) -> List[RolDestinatario]:
        pass


class UpdateRolDestinatarioInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_rol: int, descripcion: str) -> RolDestinatario:
        pass


class DeleteRolDestinatarioInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_rol: int) -> None:
        pass