from abc import ABC, abstractmethod


class AlmacenamientoPort(ABC):

    @abstractmethod
    def subir(self, contenido: bytes, nombre_archivo: str) -> str:
        pass