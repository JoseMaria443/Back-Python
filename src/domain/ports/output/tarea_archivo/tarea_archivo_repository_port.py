from abc import ABC, abstractmethod
from typing import Optional
from src.domain.entities.tarea_archivo import TareaArchivo


class TareaArchivoRepositoryPort(ABC):

    @abstractmethod
    def crear(self, asociacion: TareaArchivo) -> TareaArchivo:
        pass

    @abstractmethod
    def obtener(self, id_tarea: int, id_archivo: int) -> Optional[TareaArchivo]:
        pass

    @abstractmethod
    def eliminar(self, id_tarea: int, id_archivo: int) -> bool:
        pass
