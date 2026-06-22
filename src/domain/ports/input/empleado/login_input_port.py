"""Puerto de entrada (input) para caso de uso de login."""

from abc import ABC, abstractmethod
from typing import Optional, Tuple


class LoginInputPort(ABC):
    """Interfaz (puerto) para caso de uso de login.
    
    Define las operaciones de autenticación que expone el sistema.
    """

    @abstractmethod
    def ejecutar(self, email: str, password: str) -> Tuple[str, int, str]:
        """Ejecuta el login y retorna JWT.
        
        Args:
            email: Email del empleado
            password: Contraseña en texto plano
            
        Returns:
            Tupla (token_jwt, id_empleado, nombre_empleado)
            
        Raises:
            CredencialesInvalidasException: Si email o password son incorrectos
        """
        pass
