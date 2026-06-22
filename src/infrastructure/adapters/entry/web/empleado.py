"""Adaptador FastAPI para endpoints de Empleado."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.infrastructure.config import get_db
from src.domain.exceptions import (
    CredencialesInvalidasException,
    EmailYaExisteException,
)
from src.application.dtos.empleado import (
    LoginRequest,
    LoginResponse,
    CreateEmpleadoRequest,
    CreateEmpleadoResponse,
)
from src.application.use_cases.empleado import LoginUseCase, CreateEmpleadoUseCase
from src.infrastructure.adapters.output.repositories.empleado_repository import (
    EmpleadoRepository,
)

router = APIRouter(prefix="/api/empleado", tags=["empleado"])


@router.post("/login", response_model=LoginResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    """Endpoint de login.
    
    Recibe email y password, retorna JWT si son válidos.
    """
    try:
        # Inyectar dependencias y ejecutar caso de uso
        repositorio = EmpleadoRepository(db)
        use_case = LoginUseCase(repositorio)
        
        token, id_empleado, nombre = use_case.ejecutar(request.email, request.password)
        
        return LoginResponse(
            token=token,
            token_type="bearer",
            id_empleado=id_empleado,
            email=request.email,
            nombre=nombre,
        )
    
    except CredencialesInvalidasException:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Las credenciales proporcionadas son inválidas.",
        )


@router.post("/crear", response_model=CreateEmpleadoResponse)
def crear_empleado(request: CreateEmpleadoRequest, db: Session = Depends(get_db)):
    """Endpoint para crear empleado (admin only en esta fase).
    
    NOTA: En producción, este endpoint debe estar protegido por autenticación
    y autorización de administrador.
    """
    try:
        # Inyectar dependencias y ejecutar caso de uso
        repositorio = EmpleadoRepository(db)
        use_case = CreateEmpleadoUseCase(repositorio)
        
        empleado = use_case.ejecutar(
            nombre=request.nombre,
            email=request.email,
            password=request.password,
            id_area=request.id_area,
            id_cargo=request.id_cargo,
        )
        
        return CreateEmpleadoResponse(
            id_empleado=empleado.id_empleado,
            nombre=empleado.nombre,
            email=empleado.email,
            id_area=empleado.id_area,
            id_cargo=empleado.id_cargo,
        )
    
    except EmailYaExisteException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
