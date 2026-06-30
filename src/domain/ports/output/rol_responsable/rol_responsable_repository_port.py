from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.rol_responsable import RolResponsable


class RolResponsableRepositoryPort(ABC):

    @abstractmethod
    def crear(self, rol_responsable: RolResponsable) -> RolResponsable:
        pass

    @abstractmethod
    def obtener_por_id(self, id_rol: int) -> Optional[RolResponsable]:
        pass

    @abstractmethod
    def listar(self, skip: int, limit: int) -> List[RolResponsable]:
        pass

    @abstractmethod
    def actualizar(self, rol_responsable: RolResponsable) -> Optional[RolResponsable]:
        pass

    @abstractmethod
    def eliminar(self, id_rol: int) -> bool:
        pass
