"""Configuración de seguridad: JWT, hashing de contraseñas y autenticación."""

from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv

from src.infrastructure.config.database import get_db

# Cargar variables de entorno
load_dotenv()

# Configuración de JWT
SECRET_KEY = os.getenv("SECRET_KEY", "tu_clave_secreta_super_segura_cambiar_en_produccion")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

# Configuración de hashing de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme para extraer token del header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/empleado/login")


def hash_password(password: str) -> str:
    """Hashea una contraseña en texto plano.
    
    Args:
        password: Contraseña en texto plano
        
    Returns:
        str: Hash de la contraseña
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica si una contraseña coincide con su hash.
    
    Args:
        plain_password: Contraseña en texto plano
        hashed_password: Hash almacenado
        
    Returns:
        bool: True si coinciden, False si no
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Crea un token JWT de acceso.
    
    Args:
        data: Datos a incluir en el token (ej: {"sub": email, "id_empleado": 1})
        expires_delta: Tiempo de expiración opcional
        
    Returns:
        str: Token JWT codificado
    """
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt


def decode_token(token: str) -> Optional[dict]:
    """Decodifica y valida un token JWT.
    
    Args:
        token: Token JWT a decodificar
        
    Returns:
        dict: Payload del token si es válido, None si no
        
    Raises:
        JWTError: Si el token es inválido o ha expirado
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> dict:
    """Dependency de FastAPI para obtener el usuario actual desde el token JWT.
    
    Args:
        token: Token JWT del header Authorization
        db: Sesión de base de datos
        
    Returns:
        dict: Información del usuario autenticado
        
    Raises:
        HTTPException: Si el token es inválido o el usuario no existe
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # Decodificar token
    payload = decode_token(token)
    if payload is None:
        raise credentials_exception
    
    # Obtener email del token
    email: str = payload.get("sub")
    if email is None:
        raise credentials_exception
    
    # Aquí deberías buscar el usuario en la base de datos
    # Por ahora retornamos el payload, pero lo ideal es:
    # from src.infrastructure.adapters.output.repositories.empleado_repository import EmpleadoRepository
    # repository = EmpleadoRepository(db)
    # empleado = repository.obtener_por_email(email)
    # if empleado is None:
    #     raise credentials_exception
    # return empleado
    
    return payload


def get_current_active_user(current_user: dict = Depends(get_current_user)) -> dict:
    """Dependency para verificar que el usuario esté activo.
    
    Args:
        current_user: Usuario obtenido del token
        
    Returns:
        dict: Usuario activo
        
    Raises:
        HTTPException: Si el usuario está inactivo
    """
    # Aquí podrías verificar si el empleado está activo
    # Por ahora solo retorna el usuario
    return current_user


def require_role(required_roles: list[str]):
    """Middleware para verificar roles de usuario.
    
    Args:
        required_roles: Lista de roles permitidos
        
    Returns:
        function: Dependency de FastAPI
        
    Example:
        @app.get("/admin-only")
        def admin_endpoint(user = Depends(require_role(["admin"]))):
            return {"message": "Acceso concedido"}
    """
    def role_checker(current_user: dict = Depends(get_current_active_user)):
        user_role = current_user.get("rol")
        
        if user_role not in required_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Acceso denegado. Se requiere uno de estos roles: {required_roles}"
            )
        
        return current_user
    
    return role_checker