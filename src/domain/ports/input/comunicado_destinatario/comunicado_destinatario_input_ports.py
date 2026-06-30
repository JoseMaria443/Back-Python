from abc import ABC, abstractmethod
from src.domain.entities.comunicado_destinatario import ComunicadoDestinatario


class AsociarComunicadoDestinatarioInputPort(ABC):
    @abstractmethod
    def ejecutar(
        self,
        id_comunicado: int,
        id_destinatario: int,
        id_rol_destinatario: int,
    ) -> ComunicadoDestinatario:
        pass


class DesasociarComunicadoDestinatarioInputPort(ABC):
    @abstractmethod
    def ejecutar(self, id_comunicado: int, id_destinatario: int) -> None:
        pass
