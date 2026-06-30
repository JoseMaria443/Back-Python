from abc import ABC, abstractmethod
from src.domain.entities.tarea_responsable import TareaResponsable


class AsociarTareaResponsableInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_tarea: int, id_responsable: int, id_rol: int) -> TareaResponsable:
        pass


class DesasociarTareaResponsableInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_tarea: int, id_responsable: int) -> None:
        pass
