from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.estado_tarea import EstadoTarea


class EstadoTareaRepositoryPort(ABC):

    @abstractmethod
    def crear(self, estado_tarea: EstadoTarea) -> EstadoTarea:
        pass

    @abstractmethod
    def obtener_por_id(self, id_estado_tarea: int) -> Optional[EstadoTarea]:
        pass

    @abstractmethod
    def listar(self, skip: int, limit: int) -> List[EstadoTarea]:
        pass

    @abstractmethod
    def actualizar(self, estado_tarea: EstadoTarea) -> Optional[EstadoTarea]:
        pass

    @abstractmethod
    def eliminar(self, id_estado_tarea: int) -> bool:
        pass
