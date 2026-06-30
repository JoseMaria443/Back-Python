from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import date
from src.domain.entities.tarea import Tarea


class CreateTareaInputPort(ABC):
    @abstractmethod
    def ejecutar(
        self,
        id_comunicado: int,
        descripcion: str,
        fecha_entrega: date,
        fecha_registro: date,
        id_estado_tarea: Optional[int],
    ) -> Tarea:
        pass


class GetTareaInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_tarea: int) -> Tarea:
        pass


class ListTareaInputPort(ABC):
    @abstractmethod
    def ejecutar(self, skip: int, limit: int) -> List[Tarea]:
        pass


class UpdateTareaInputPort(ABC):
    @abstractmethod
    def ejecutar(
        self,
        id_tarea: int,
        id_comunicado: int,
        descripcion: str,
        fecha_entrega: date,
        fecha_registro: date,
        id_estado_tarea: Optional[int],
    ) -> Tarea:
        pass


class DeleteTareaInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_tarea: int) -> None:
        pass
