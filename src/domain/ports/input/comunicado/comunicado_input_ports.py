from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import date
from src.domain.entities.comunicado import Comunicado


class CreateComunicadoInputPort(ABC):
    @abstractmethod
    def ejecutar(
        self,
        doi: str,
        num_comunicado: str,
        id_emisor: int,
        fecha_recepcion: date,
        id_destinatario: int,
        fecha_registro: date,
        id_registro: int,
        id_metodo_recepcion: int,
        tema: str,
        id_tipo_comunicado: int,
        observaciones: Optional[str],
    ) -> Comunicado:
        pass


class GetComunicadoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_comunicado: int) -> Comunicado:
        pass


class ListComunicadoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, skip: int, limit: int) -> List[Comunicado]:
        pass


class UpdateComunicadoInputPort(ABC):
    @abstractmethod
    def ejecutar(
        self,
        id_comunicado: int,
        doi: str,
        num_comunicado: str,
        id_emisor: int,
        fecha_recepcion: date,
        id_destinatario: int,
        fecha_registro: date,
        id_registro: int,
        id_metodo_recepcion: int,
        tema: str,
        id_tipo_comunicado: int,
        observaciones: Optional[str],
    ) -> Comunicado:
        pass


class DeleteComunicadoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_comunicado: int) -> None:
        pass
