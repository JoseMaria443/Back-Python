from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.tarea import Tarea


class TareaRepositoryPort(ABC):

    @abstractmethod
    def crear(self, tarea: Tarea) -> Tarea:
        pass

    @abstractmethod
    def obtener_por_id(self, id_tarea: int) -> Optional[Tarea]:
        pass

    @abstractmethod
    def listar(self, skip: int, limit: int) -> List[Tarea]:
        pass

    @abstractmethod
    def actualizar(self, tarea: Tarea) -> Optional[Tarea]:
        pass

    @abstractmethod
    def eliminar(self, id_tarea: int) -> bool:
        pass
