from abc import ABC, abstractmethod
from typing import List
from datetime import date
from src.domain.entities.archivo import Archivo


class CreateArchivoInputPort(ABC):
    @abstractmethod
    def ejecutar(
        self,
        doi: str,
        descripcion: str,
        url_archivo: str,
        nombre_original: str,
        id_elaborador: int,
        fecha_registro: date,
    ) -> Archivo:
        pass


class GetArchivoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_archivo: int) -> Archivo:
        pass


class ListArchivoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, skip: int, limit: int) -> List[Archivo]:
        pass


class UpdateArchivoInputPort(ABC):
    @abstractmethod
    def ejecutar(
        self,
        id_archivo: int,
        doi: str,
        descripcion: str,
        url_archivo: str,
        nombre_original: str,
        id_elaborador: int,
        fecha_registro: date,
    ) -> Archivo:
        pass


class DeleteArchivoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_archivo: int) -> None:
        pass
