"""Caso de uso: Crear Empleado (por administrador)."""

from src.domain.ports.input.empleado import CreateEmpleadoInputPort
from src.domain.ports.output.empleado import EmpleadoRepositoryPort
from src.domain.ports.output.historial_estado_empleado import HistorialEstadoEmpleadoRepositoryPort
from src.domain.entities.empleado import Empleado
from src.domain.entities.historial_estado_empleado import HistorialEstadoEmpleado
from src.domain.exceptions import EmailYaExisteException
from src.infrastructure.config.security import hash_password


class CreateEmpleadoUseCase(CreateEmpleadoInputPort):
    """Caso de uso para crear un nuevo empleado.
    
    Solo para administrador en esta fase.
    Sin dependencias directas de FastAPI ni ORM.
    """

    def __init__(
        self,
        empleado_repository: EmpleadoRepositoryPort,
        historial_repository: HistorialEstadoEmpleadoRepositoryPort,
    ):
        """
        Args:
            empleado_repository: Implementación del puerto de repositorio
            historial_repository: Implementación del puerto de historial
        """
        self.empleado_repository = empleado_repository
        self.historial_repository = historial_repository

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
            email: Email único
            password: Contraseña en texto plano
            id_area: ID del área
            id_cargo: ID del cargo
            id_empleado_ejecutor: ID del empleado que ejecuta la acción
            
        Returns:
            Empleado creado
            
        Raises:
            EmailYaExisteException: Si el email ya existe
        """
        # Verificar que el email no exista
        if self.empleado_repository.existe_email(email):
            raise EmailYaExisteException(f"El email {email} ya está registrado.")
        
        # Hashear contraseña
        password_hash = hash_password(password)
        
        # Crear instancia de Empleado (sin ID, será asignado por BD)
        empleado = Empleado.crear(
            nombre=nombre,
            email=email,
            password_hash=password_hash,
            id_area=id_area,
            id_cargo=id_cargo,
        )
        
        # Guardar en repositorio
        empleado_guardado = self.empleado_repository.crear(empleado)
        
        # Registrar en historial usando el factory
        historial = HistorialEstadoEmpleado.crear(
            id_empleado=empleado_guardado.id_empleado,
            accion="alta",
            id_empleado_ejecutor=id_empleado_ejecutor,
        )
        self.historial_repository.crear(historial)
        
        return empleado_guardado
