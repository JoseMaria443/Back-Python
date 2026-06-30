from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.estado import Estado


class EstadoRepositoryPort(ABC):
    @abstractmethod
    def crear(self, estado: Estado) -> Estado:
        pass

    @abstractmethod
    def obtener_por_id(self, id_estado: int) -> Optional[Estado]:
        pass

    @abstractmethod
    def listar(self, skip: int = 0, limit: int = 50) -> List[Estado]:
        pass

    @abstractmethod
    def actualizar(self, estado: Estado) -> Estado:
        pass

    @abstractmethod
    def eliminar(self, id_estado: int) -> bool:
        pass