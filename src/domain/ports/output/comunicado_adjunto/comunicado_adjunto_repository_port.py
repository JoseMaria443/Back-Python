from abc import ABC, abstractmethod
from typing import Optional
from src.domain.entities.comunicado_adjunto import ComunicadoAdjunto


class ComunicadoAdjuntoRepositoryPort(ABC):

    @abstractmethod
    def crear(self, asociacion: ComunicadoAdjunto) -> ComunicadoAdjunto:
        pass

    @abstractmethod
    def obtener(self, id_comunicado: int, id_archivo: int) -> Optional[ComunicadoAdjunto]:
        pass

    @abstractmethod
    def eliminar(self, id_comunicado: int, id_archivo: int) -> bool:
        pass
