from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.infrastructure.config import get_db
from src.infrastructure.config.auth import get_current_empleado
from src.domain.exceptions import RecursoNoEncontradoException
from src.application.dtos.rol_responsable import (
    CreateRolResponsableRequest,
    UpdateRolResponsableRequest,
    RolResponsableResponse,
    ListRolResponsableResponse,
)
from src.application.use_cases.rol_responsable import (
    CreateRolResponsableUseCase,
    GetRolResponsableUseCase,
    ListRolResponsableUseCase,
    UpdateRolResponsableUseCase,
    DeleteRolResponsableUseCase,
)
from src.infrastructure.adapters.output.repositories.rol_responsable_repository import (
    RolResponsableRepository,
)

router = APIRouter(prefix="/api/rol-responsable", tags=["rol-responsable"])


def _to_response(entity) -> RolResponsableResponse:
    return RolResponsableResponse(id_rol=entity.id_rol, descripcion_rol=entity.descripcion_rol)


@router.post("/", response_model=RolResponsableResponse, status_code=status.HTTP_201_CREATED)
def crear(
    request: CreateRolResponsableRequest,
    db: Session = Depends(get_db),
    _current_empleado: dict = Depends(get_current_empleado),
):
    repo = RolResponsableRepository(db)
    use_case = CreateRolResponsableUseCase(repo)
    entity = use_case.ejecutar(request.descripcion_rol)
    return _to_response(entity)


@router.get("/{id_rol}", response_model=RolResponsableResponse)
def obtener(
    id_rol: int,
    db: Session = Depends(get_db),
    _current_empleado: dict = Depends(get_current_empleado),
):
    try:
        repo = RolResponsableRepository(db)
        use_case = GetRolResponsableUseCase(repo)
        entity = use_case.ejecutar(id_rol)
        return _to_response(entity)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/", response_model=ListRolResponsableResponse)
def listar(
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db),
    _current_empleado: dict = Depends(get_current_empleado),
):
    repo = RolResponsableRepository(db)
    use_case = ListRolResponsableUseCase(repo)
    items = use_case.ejecutar(skip, limit)
    return ListRolResponsableResponse(
        items=[_to_response(i) for i in items],
        total=repo.contar(),
        skip=skip,
        limit=limit,
    )


@router.put("/{id_rol}", response_model=RolResponsableResponse)
def actualizar(
    id_rol: int,
    request: UpdateRolResponsableRequest,
    db: Session = Depends(get_db),
    _current_empleado: dict = Depends(get_current_empleado),
):
    try:
        repo = RolResponsableRepository(db)
        use_case = UpdateRolResponsableUseCase(repo)
        entity = use_case.ejecutar(id_rol, request.descripcion_rol)
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
        repo = RolResponsableRepository(db)
        use_case = DeleteRolResponsableUseCase(repo)
        use_case.ejecutar(id_rol)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
