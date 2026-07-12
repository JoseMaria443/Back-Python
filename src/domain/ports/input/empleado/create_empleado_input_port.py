"""Puerto de entrada (input) para caso de uso de creación de Empleado."""

from abc import ABC, abstractmethod
from src.domain.entities.empleado import Empleado


class CreateEmpleadoInputPort(ABC):
    """Interfaz (puerto) para caso de uso de creación de Empleado."""

    @abstractmethod
    def ejecutar(
        self,
        nombre: str,
        email: str,
        password: str,
        id_area: int,
        id_cargo: int,
        id_empleado_ejecutor: int,
    ) -> Empleado:
        """Crea un nuevo empleado.
        
        Args:
            nombre: Nombre del empleado
            email: Email único del empleado
            password: Contraseña en texto plano (se hasheará)
            id_area: ID del área
            id_cargo: ID del cargo
            id_empleado_ejecutor: ID del empleado que ejecuta la acción
            
        Returns:
            Empleado creado
            
        Raises:
            EmailYaExisteException: Si el email ya está registrado
        """
        pass
