from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.catalogo import Catalogo


class CatalogoRepositoryPort(ABC):
    @abstractmethod
    def crear(self, catalogo: Catalogo) -> Catalogo:
        pass

    @abstractmethod
    def obtener_por_id(self, id_catalogo: int) -> Optional[Catalogo]:
        pass

    @abstractmethod
    def listar(self, skip: int = 0, limit: int = 50) -> List[Catalogo]:
        pass

    @abstractmethod
    def actualizar(self, catalogo: Catalogo) -> Catalogo:
        pass

    @abstractmethod
    def eliminar(self, id_catalogo: int) -> bool:
        pass