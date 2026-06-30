from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.estado_tarea import EstadoTarea


class CreateEstadoTareaInputPort(ABC):
    @abstractmethod
    def ejecutar(self, nombre_estado: str) -> EstadoTarea:
        pass


class GetEstadoTareaInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_estado_tarea: int) -> EstadoTarea:
        pass


class ListEstadoTareaInputPort(ABC):
    @abstractmethod
    def ejecutar(self, skip: int, limit: int) -> List[EstadoTarea]:
        pass


class UpdateEstadoTareaInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_estado_tarea: int, nombre_estado: str) -> EstadoTarea:
        pass


class DeleteEstadoTareaInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_estado_tarea: int) -> None:
        pass
