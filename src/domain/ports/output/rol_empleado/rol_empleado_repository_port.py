from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.rol_empleado import RolEmpleado


class RolEmpleadoRepositoryPort(ABC):
    """Interfaz (puerto) para persistencia de RolEmpleado."""

    @abstractmethod
    def crear(self, rol: RolEmpleado) -> RolEmpleado:
        """Crea un nuevo rol."""
        pass

    @abstractmethod
    def obtener_por_id(self, id_rol: int) -> Optional[RolEmpleado]:
        """Obtiene un rol por ID."""
        pass

    @abstractmethod
    def listar(self, skip: int = 0, limit: int = 50) -> List[RolEmpleado]:
        """Lista roles."""
        pass

    @abstractmethod
    def contar(self) -> int:
        """Cuenta roles."""
        pass

    @abstractmethod
    def actualizar(self, rol: RolEmpleado) -> Optional[RolEmpleado]:
        """Actualiza un rol."""
        pass

    @abstractmethod
    def eliminar(self, id_rol: int) -> bool:
        """Elimina un rol."""
        pass