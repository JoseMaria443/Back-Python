from abc import ABC, abstractmethod
from src.domain.entities.comunicado_adjunto import ComunicadoAdjunto


class AsociarComunicadoAdjuntoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_comunicado: int, id_archivo: int) -> ComunicadoAdjunto:
        pass


class DesasociarComunicadoAdjuntoInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_comunicado: int, id_archivo: int) -> None:
        pass
