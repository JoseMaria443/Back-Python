from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.infrastructure.config import get_db
from src.infrastructure.config.auth import get_current_empleado
from src.domain.exceptions import RecursoNoEncontradoException
from src.application.dtos.rol_empleado import (
    CreateRolEmpleadoRequest,
    UpdateRolEmpleadoRequest,
    RolEmpleadoResponse,
    ListRolEmpleadoResponse,
)
from src.application.use_cases.rol_empleado import (
    CreateRolEmpleadoUseCase,
    GetRolEmpleadoUseCase,
    ListRolEmpleadoUseCase,
    UpdateRolEmpleadoUseCase,
    DeleteRolEmpleadoUseCase,
)
from src.infrastructure.adapters.output.repositories.rol_empleado_repository import (
    RolEmpleadoRepository,
)

router = APIRouter(prefix="/api/rol-empleado", tags=["rol-empleado"])


def _to_response(entity) -> RolEmpleadoResponse:
    return RolEmpleadoResponse(
        id_rol=entity.id_rol,
        descripcion=entity.descripcion,
    )


@router.post("/", response_model=RolEmpleadoResponse, status_code=status.HTTP_201_CREATED)
def crear(
    request: CreateRolEmpleadoRequest,
    db: Session = Depends(get_db),
    _current_empleado: dict = Depends(get_current_empleado),
):
    repo = RolEmpleadoRepository(db)
    use_case = CreateRolEmpleadoUseCase(repo)
    entity = use_case.ejecutar(request.descripcion)
    return _to_response(entity)


@router.get("/{id_rol}", response_model=RolEmpleadoResponse)
def obtener(
    id_rol: int,
    db: Session = Depends(get_db),
    _current_empleado: dict = Depends(get_current_empleado),
):
    try:
        repo = RolEmpleadoRepository(db)
        use_case = GetRolEmpleadoUseCase(repo)
        entity = use_case.ejecutar(id_rol)
        return _to_response(entity)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/", response_model=ListRolEmpleadoResponse)
def listar(
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db),
    _current_empleado: dict = Depends(get_current_empleado),
):
    repo = RolEmpleadoRepository(db)
    use_case = ListRolEmpleadoUseCase(repo)
    items = use_case.ejecutar(skip, limit)
    return ListRolEmpleadoResponse(
        items=[_to_response(i) for i in items],
        total=repo.contar(),
        skip=skip,
        limit=limit,
    )


@router.put("/{id_rol}", response_model=RolEmpleadoResponse)
def actualizar(
    id_rol: int,
    request: UpdateRolEmpleadoRequest,
    db: Session = Depends(get_db),
    _current_empleado: dict = Depends(get_current_empleado),
):
    try:
        repo = RolEmpleadoRepository(db)
        use_case = UpdateRolEmpleadoUseCase(repo)
        entity = use_case.ejecutar(id_rol, request.descripcion)
        return _to_response(entity)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{id_rol}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar(
    id_rol: int,
    db: Session = Depends(get_db),
    _current_empleado: dict = Depends(get_current_empleado),
):
    try:
        repo = RolEmpleadoRepository(db)
        use_case = DeleteRolEmpleadoUseCase(repo)
        use_case.ejecutar(id_rol)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))