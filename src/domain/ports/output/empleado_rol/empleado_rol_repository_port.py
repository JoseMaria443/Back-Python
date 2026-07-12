from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.empleado_rol import EmpleadoRol
from src.domain.entities.rol_empleado import RolEmpleado


class EmpleadoRolRepositoryPort(ABC):
    @abstractmethod
    def asignar(self, id_empleado: int, id_rol: int) -> EmpleadoRol:
        pass

    @abstractmethod
    def quitar(self, id_empleado: int, id_rol: int) -> bool:
        pass

    @abstractmethod
    def listar_por_empleado(self, id_empleado: int) -> List[RolEmpleado]:
        pass

    @abstractmethod
    def existe(self, id_empleado: int, id_rol: int) -> bool:
        pass