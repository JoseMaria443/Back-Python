from abc import ABC, abstractmethod
from src.domain.entities.tarea_archivo import TareaArchivo


class AsociarTareaArchivoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_tarea: int, id_archivo: int) -> TareaArchivo:
        pass


class DesasociarTareaArchivoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_tarea: int, id_archivo: int) -> None:
        pass
