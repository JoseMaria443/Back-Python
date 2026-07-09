from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.estado import Estado


class CreateEstadoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, nombre_estado: str) -> Estado:
        pass


class GetEstadoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_estado: int) -> Estado:
        pass


class ListEstadoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, skip: int, limit: int) -> List[Estado]:
        pass


class UpdateEstadoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_estado: int, nombre_estado: str) -> Estado:
        pass


class DeleteEstadoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_estado: int) -> None:
        pass