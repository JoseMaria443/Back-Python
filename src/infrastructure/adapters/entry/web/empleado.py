"""Adaptador FastAPI para endpoints de Empleado."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.infrastructure.config import get_db
from src.infrastructure.config.auth import get_current_empleado
from src.domain.exceptions import (
    CredencialesInvalidasException,
    EmailYaExisteException,
    RecursoNoEncontradoException,
)
from src.application.dtos.empleado import (
    LoginRequest,
    LoginResponse,
    CreateEmpleadoRequest,
    CreateEmpleadoResponse,
    EmpleadoResponse,
    ListEmpleadoResponse,
)
from src.application.dtos.historial_estado_empleado import (
    HistorialEstadoEmpleadoResponse,
    ListHistorialEstadoEmpleadoResponse,
)
from src.application.use_cases.empleado import (
    LoginUseCase,
    CreateEmpleadoUseCase,
    GetEmpleadoUseCase,
    ListEmpleadoUseCase,
    DesactivarEmpleadoUseCase,
    ActivarEmpleadoUseCase,
)
from src.application.use_cases.historial_estado_empleado import (
    ListHistorialEstadoEmpleadoUseCase,
)
from src.infrastructure.adapters.output.repositories.empleado_repository import (
    EmpleadoRepository,
)
from src.infrastructure.adapters.output.repositories.historial_estado_empleado_repository import (
    HistorialEstadoEmpleadoRepository,
)
from src.domain.entities.historial_estado_empleado import HistorialEstadoEmpleado

router = APIRouter(prefix="/api/empleado", tags=["empleado"])


def _to_response(entity) -> EmpleadoResponse:
    return EmpleadoResponse(
        id_empleado=entity.id_empleado,
        nombre=entity.nombre,
        email=entity.email,
        id_area=entity.id_area,
        id_cargo=entity.id_cargo,
        activo=entity.activo,
    )


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
def crear_empleado(
    request: CreateEmpleadoRequest,
    db: Session = Depends(get_db),
    current_empleado: dict = Depends(get_current_empleado),
):
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
        
        # Registrar historial de alta
        historial_repo = HistorialEstadoEmpleadoRepository(db)
        historial_repo.crear(
            HistorialEstadoEmpleado(
                id_historial=0,
                id_empleado=empleado.id_empleado,
                accion="alta",
                id_empleado_ejecutor=current_empleado.get("id_empleado"),
                fecha=None,
            )
        )
        
        return CreateEmpleadoResponse(
            id_empleado=empleado.id_empleado,
            nombre=empleado.nombre,
            email=empleado.email,
            id_area=empleado.id_area,
            id_cargo=empleado.id_cargo,
            activo=empleado.activo,
        )
    
    except EmailYaExisteException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.get("/", response_model=ListEmpleadoResponse)
def listar_empleados(
    skip: int = 0,
    limit: int = 50,
    nombre: str = None,
    db: Session = Depends(get_db),
    _current_empleado: dict = Depends(get_current_empleado),
):
    repo = EmpleadoRepository(db)
    use_case = ListEmpleadoUseCase(repo)
    items = use_case.ejecutar(skip, limit, nombre)
    return ListEmpleadoResponse(
        items=[_to_response(i) for i in items],
        total=repo.contar(nombre),
        skip=skip,
        limit=limit,
    )


@router.get("/{id_empleado}", response_model=EmpleadoResponse)
def obtener_empleado(
    id_empleado: int,
    db: Session = Depends(get_db),
    _current_empleado: dict = Depends(get_current_empleado),
):
    try:
        repo = EmpleadoRepository(db)
        use_case = GetEmpleadoUseCase(repo)
        entity = use_case.ejecutar(id_empleado)
        return _to_response(entity)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.patch("/{id_empleado}/desactivar", response_model=EmpleadoResponse)
def desactivar_empleado(
    id_empleado: int,
    db: Session = Depends(get_db),
    current_empleado: dict = Depends(get_current_empleado),
):
    try:
        empleado_repo = EmpleadoRepository(db)
        historial_repo = HistorialEstadoEmpleadoRepository(db)
        use_case = DesactivarEmpleadoUseCase(empleado_repo, historial_repo)
        entity = use_case.ejecutar(id_empleado, current_empleado.get("id_empleado"))
        return _to_response(entity)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.patch("/{id_empleado}/activar", response_model=EmpleadoResponse)
def activar_empleado(
    id_empleado: int,
    db: Session = Depends(get_db),
    current_empleado: dict = Depends(get_current_empleado),
):
    try:
        empleado_repo = EmpleadoRepository(db)
        historial_repo = HistorialEstadoEmpleadoRepository(db)
        use_case = ActivarEmpleadoUseCase(empleado_repo, historial_repo)
        entity = use_case.ejecutar(id_empleado, current_empleado.get("id_empleado"))
        return _to_response(entity)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


def _to_historial_response(entity) -> HistorialEstadoEmpleadoResponse:
    return HistorialEstadoEmpleadoResponse(
        id_historial=entity.id_historial,
        id_empleado=entity.id_empleado,
        accion=entity.accion,
        id_empleado_ejecutor=entity.id_empleado_ejecutor,
        fecha=entity.fecha,
    )


@router.get("/{id_empleado}/historial", response_model=ListHistorialEstadoEmpleadoResponse)
def listar_historial(
    id_empleado: int,
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db),
    _current_empleado: dict = Depends(get_current_empleado),
):
    repo = HistorialEstadoEmpleadoRepository(db)
    use_case = ListHistorialEstadoEmpleadoUseCase(repo)
    items = use_case.ejecutar(id_empleado, skip, limit)
    return ListHistorialEstadoEmpleadoResponse(
        items=[_to_historial_response(i) for i in items],
        total=repo.contar(id_empleado),
        skip=skip,
        limit=limit,
    )
