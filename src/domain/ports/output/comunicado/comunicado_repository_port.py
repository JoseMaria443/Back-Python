from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.comunicado import Comunicado


class ComunicadoRepositoryPort(ABC):

    @abstractmethod
    def crear(self, comunicado: Comunicado) -> Comunicado:
        pass

    @abstractmethod
    def obtener_por_id(self, id_comunicado: int) -> Optional[Comunicado]:
        pass

    @abstractmethod
    def listar(self, skip: int, limit: int) -> List[Comunicado]:
        pass

    @abstractmethod
    def actualizar(self, comunicado: Comunicado) -> Optional[Comunicado]:
        pass

    @abstractmethod
    def eliminar(self, id_comunicado: int) -> bool:
        pass
