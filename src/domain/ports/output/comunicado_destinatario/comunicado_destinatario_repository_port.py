from abc import ABC, abstractmethod
from typing import Optional
from src.domain.entities.comunicado_destinatario import ComunicadoDestinatario


class ComunicadoDestinatarioRepositoryPort(ABC):

    @abstractmethod
    def crear(self, asociacion: ComunicadoDestinatario) -> ComunicadoDestinatario:
        pass

    @abstractmethod
    def obtener(
        self, id_comunicado: int, id_destinatario: int
    ) -> Optional[ComunicadoDestinatario]:
        pass

    @abstractmethod
    def eliminar(self, id_comunicado: int, id_destinatario: int) -> bool:
        pass
