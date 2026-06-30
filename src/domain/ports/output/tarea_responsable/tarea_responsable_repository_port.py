from abc import ABC, abstractmethod
from typing import Optional
from src.domain.entities.tarea_responsable import TareaResponsable


class TareaResponsableRepositoryPort(ABC):

    @abstractmethod
    def crear(self, asociacion: TareaResponsable) -> TareaResponsable:
        pass

    @abstractmethod
    def obtener(self, id_tarea: int, id_responsable: int) -> Optional[TareaResponsable]:
        pass

    @abstractmethod
    def eliminar(self, id_tarea: int, id_responsable: int) -> bool:
        pass
