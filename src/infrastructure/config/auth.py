from typing import Any, Dict

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from src.infrastructure.config.security import verificar_token_jwt


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/empleado/login", auto_error=False)


def get_current_empleado(token: str | None = Depends(oauth2_scheme)) -> Dict[str, Any]:
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No autenticado",
            headers={"WWW-Authenticate": "Bearer"},
        )

    try:
        payload = verificar_token_jwt(token)
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return {
        "id_empleado": payload.get("id_empleado"),
        "email": payload.get("email"),
        "nombre": payload.get("nombre"),
    }