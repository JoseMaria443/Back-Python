from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.catalogo import Catalogo


class CreateCatalogoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_tipo_catalogo: int, descripcion: str = None) -> Catalogo:
        pass


class GetCatalogoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_catalogo: int) -> Catalogo:
        pass


class ListCatalogoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, skip: int, limit: int) -> List[Catalogo]:
        pass


class UpdateCatalogoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_catalogo: int, id_tipo_catalogo: int, descripcion: str = None) -> Catalogo:
        pass


class DeleteCatalogoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_catalogo: int) -> None:
        pass