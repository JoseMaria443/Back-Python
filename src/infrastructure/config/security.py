"""Configuración de seguridad: JWT y hash de passwords."""

import os
import jwt
from datetime import datetime, timedelta
from typing import Dict, Any
import bcrypt


# Configuración JWT
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "change-me-in-production")
JWT_EXPIRATION_HOURS = int(os.getenv("JWT_EXPIRATION_HOURS", "24"))
JWT_ALGORITHM = "HS256"


def hash_password(password: str) -> str:
    """Hashea una contraseña usando bcrypt.
    
    Args:
        password: Contraseña en texto plano
        
    Returns:
        Hash de la contraseña
    """
    salt = bcrypt.gensalt(rounds=12)
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()


def verify_password(password: str, hashed: str) -> bool:
    """Verifica una contraseña contra su hash.
    
    Args:
        password: Contraseña en texto plano a verificar
        hashed: Hash almacenado
        
    Returns:
        True si coincide, False en caso contrario
    """
    return bcrypt.checkpw(password.encode(), hashed.encode())


def crear_token_jwt(id_empleado: int, email: str, nombre: str) -> str:
    """Crea un JWT con expiración.
    
    Args:
        id_empleado: ID del empleado
        email: Email del empleado
        nombre: Nombre del empleado
        
    Returns:
        Token JWT codificado
    """
    ahora = datetime.utcnow()
    expiracion = ahora + timedelta(hours=JWT_EXPIRATION_HOURS)
    
    payload: Dict[str, Any] = {
        "id_empleado": id_empleado,
        "email": email,
        "nombre": nombre,
        "iat": ahora,
        "exp": expiracion,
    }
    
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return token


def verificar_token_jwt(token: str) -> Dict[str, Any]:
    """Verifica y decodifica un JWT.
    
    Args:
        token: Token JWT a verificar
        
    Returns:
        Payload del token decodificado
        
    Raises:
        jwt.InvalidTokenError: Si el token es inválido o expirado
    """
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise jwt.InvalidTokenError("Token expirado")
    except jwt.InvalidTokenError:
        raise jwt.InvalidTokenError("Token inválido")
