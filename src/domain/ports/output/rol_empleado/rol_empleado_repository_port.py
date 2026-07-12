from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.rol_empleado import RolEmpleado


class RolEmpleadoRepositoryPort(ABC):
    @abstractmethod
    def crear(self, rol: RolEmpleado) -> RolEmpleado:
        pass

    @abstractmethod
    def obtener_por_id(self, id_rol: int) -> Optional[RolEmpleado]:
        pass

    @abstractmethod
    def listar(self, skip: int = 0, limit: int = 50) -> List[RolEmpleado]:
        pass

    @abstractmethod
    def contar(self) -> int:
        pass

    @abstractmethod
    def actualizar(self, rol: RolEmpleado) -> Optional[RolEmpleado]:
        pass

    @abstractmethod
    def eliminar(self, id_rol: int) -> bool:
        pass

    @abstractmethod
    def existe_asignado(self, id_rol: int) -> bool:
        pass