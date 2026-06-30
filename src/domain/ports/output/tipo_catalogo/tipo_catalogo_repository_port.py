from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.tipo_catalogo import TipoCatalogo


class TipoCatalogoRepositoryPort(ABC):

    @abstractmethod
    def crear(self, tipo_catalogo: TipoCatalogo) -> TipoCatalogo:
        pass

    @abstractmethod
    def obtener_por_id(self, id_tipo_catalogo: int) -> Optional[TipoCatalogo]:
        pass

    @abstractmethod
    def listar(self, skip: int, limit: int) -> List[TipoCatalogo]:
        pass

    @abstractmethod
    def actualizar(self, tipo_catalogo: TipoCatalogo) -> Optional[TipoCatalogo]:
        pass

    @abstractmethod
    def eliminar(self, id_tipo_catalogo: int) -> bool:
        pass