from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.rol_destinatario import RolDestinatario


class RolDestinatarioRepositoryPort(ABC):
    @abstractmethod
    def crear(self, rol_destinatario: RolDestinatario) -> RolDestinatario:
        pass

    @abstractmethod
    def obtener_por_id(self, id_rol_destinatario: int) -> Optional[RolDestinatario]:
        pass

    @abstractmethod
    def listar(self, skip: int = 0, limit: int = 50) -> List[RolDestinatario]:
        pass

    @abstractmethod
    def actualizar(self, rol_destinatario: RolDestinatario) -> RolDestinatario:
        pass

    @abstractmethod
    def eliminar(self, id_rol_destinatario: int) -> bool:
        pass