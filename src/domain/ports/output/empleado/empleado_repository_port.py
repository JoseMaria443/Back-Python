"""Puerto de salida (output) para repositorio de Empleado."""

from abc import ABC, abstractmethod
from typing import Optional
from src.domain.entities.empleado import Empleado


class EmpleadoRepositoryPort(ABC):
    """Interfaz (puerto) para persistencia de Empleado.
    
    Define las operaciones que debe implementar el adaptador de persistencia.
    """

    @abstractmethod
    def obtener_por_email(self, email: str) -> Optional[Empleado]:
        """Busca un empleado por email.
        
        Args:
            email: Email del empleado
            
        Returns:
            Empleado si existe, None en caso contrario
        """
        pass

    @abstractmethod
    def obtener_por_id(self, id_empleado: int) -> Optional[Empleado]:
        """Busca un empleado por ID.
        
        Args:
            id_empleado: ID del empleado
            
        Returns:
            Empleado si existe, None en caso contrario
        """
        pass

    @abstractmethod
    def crear(self, empleado: Empleado) -> Empleado:
        """Crea un nuevo empleado.
        
        Args:
            empleado: Instancia de Empleado con datos a guardar
            
        Returns:
            Empleado guardado con ID asignado
        """
        pass

    @abstractmethod
    def existe_email(self, email: str) -> bool:
        """Verifica si un email ya está registrado.
        
        Args:
            email: Email a verificar
            
        Returns:
            True si existe, False en caso contrario
        """
        pass
