"""Caso de uso: Login de Empleado."""

from typing import Tuple
from src.domain.ports.input.empleado import LoginInputPort
from src.domain.ports.output.empleado import EmpleadoRepositoryPort
from src.domain.exceptions import CredencialesInvalidasException
from src.infrastructure.config.security import (
    verify_password,
    crear_token_jwt,
)


class LoginUseCase(LoginInputPort):
    """Caso de uso para autenticación de empleado (login).
    
    Sin dependencias directas de FastAPI ni ORM.
    Solo depende de las interfaces del dominio (puertos).
    """

    def __init__(self, empleado_repository: EmpleadoRepositoryPort):
        """
        Args:
            empleado_repository: Implementación del puerto de repositorio
        """
        self.empleado_repository = empleado_repository

    def ejecutar(self, email: str, password: str) -> Tuple[str, int, str]:
        """Ejecuta la lógica de login.
        
        Args:
            email: Email del empleado
            password: Contraseña en texto plano
            
        Returns:
            Tupla (token_jwt, id_empleado, nombre_empleado)
            
        Raises:
            CredencialesInvalidasException: Si las credenciales son inválidas
        """
        # Buscar empleado por email
        empleado = self.empleado_repository.obtener_por_email(email)
        
        if not empleado:
            # No revelar si el email existe o no (por seguridad)
            raise CredencialesInvalidasException(
                "Las credenciales proporcionadas son inválidas."
            )
        
        # Verificar contraseña
        if not verify_password(password, empleado.password_hash):
            raise CredencialesInvalidasException(
                "Las credenciales proporcionadas son inválidas."
            )
        
        # Crear JWT
        token = crear_token_jwt(empleado.id_empleado, empleado.email, empleado.nombre)
        
        return token, empleado.id_empleado, empleado.nombre
