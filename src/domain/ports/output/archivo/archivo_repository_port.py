from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.archivo import Archivo


class ArchivoRepositoryPort(ABC):

    @abstractmethod
    def crear(self, archivo: Archivo) -> Archivo:
        pass

    @abstractmethod
    def obtener_por_id(self, id_archivo: int) -> Optional[Archivo]:
        pass

    @abstractmethod
    def listar(self, skip: int, limit: int) -> List[Archivo]:
        pass

    @abstractmethod
    def actualizar(self, archivo: Archivo) -> Optional[Archivo]:
        pass

    @abstractmethod
    def eliminar(self, id_archivo: int) -> bool:
        pass
