from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.tipo_catalogo import TipoCatalogo


class CreateTipoCatalogoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, nombre_tipo_catalogo: str) -> TipoCatalogo:
        pass


class GetTipoCatalogoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_tipo_catalogo: int) -> TipoCatalogo:
        pass


class ListTipoCatalogoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, skip: int, limit: int) -> List[TipoCatalogo]:
        pass


class UpdateTipoCatalogoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_tipo_catalogo: int, nombre_tipo_catalogo: str) -> TipoCatalogo:
        pass


class DeleteTipoCatalogoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_tipo_catalogo: int) -> None:
        pass