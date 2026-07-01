from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.infrastructure.config import get_db
from src.infrastructure.config.auth import get_current_empleado
from src.domain.exceptions import RecursoNoEncontradoException
from src.application.dtos.rol_destinatario import (
    CreateRolDestinatarioRequest,
    UpdateRolDestinatarioRequest,
    RolDestinatarioResponse,
    ListRolDestinatarioResponse,
)
from src.application.use_cases.rol_destinatario import (
    CreateRolDestinatarioUseCase,
    GetRolDestinatarioUseCase,
    ListRolDestinatarioUseCase,
    UpdateRolDestinatarioUseCase,
    DeleteRolDestinatarioUseCase,
)
from src.infrastructure.adapters.output.repositories.rol_destinatario_repository import (
    RolDestinatarioRepository,
)

router = APIRouter(prefix="/api/rol-destinatario", tags=["rol-destinatario"])


def _to_response(entity) -> RolDestinatarioResponse:
    return RolDestinatarioResponse(id_rol=entity.id_rol, descripcion=entity.descripcion)


@router.post("/", response_model=RolDestinatarioResponse, status_code=status.HTTP_201_CREATED)
def crear(
    request: CreateRolDestinatarioRequest,
    db: Session = Depends(get_db),
    _current_empleado: dict = Depends(get_current_empleado),
):
    repo = RolDestinatarioRepository(db)
    use_case = CreateRolDestinatarioUseCase(repo)
    entity = use_case.ejecutar(request.descripcion)
    return _to_response(entity)


@router.get("/{id_rol}", response_model=RolDestinatarioResponse)
def obtener(
    id_rol: int,
    db: Session = Depends(get_db),
    _current_empleado: dict = Depends(get_current_empleado),
):
    try:
        repo = RolDestinatarioRepository(db)
        use_case = GetRolDestinatarioUseCase(repo)
        entity = use_case.ejecutar(id_rol)
        return _to_response(entity)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/", response_model=ListRolDestinatarioResponse)
def listar(
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db),
    _current_empleado: dict = Depends(get_current_empleado),
):
    repo = RolDestinatarioRepository(db)
    use_case = ListRolDestinatarioUseCase(repo)
    items = use_case.ejecutar(skip, limit)
    return ListRolDestinatarioResponse(
        items=[_to_response(i) for i in items],
        total=repo.contar(),
        skip=skip,
        limit=limit,
    )


@router.put("/{id_rol}", response_model=RolDestinatarioResponse)
def actualizar(
    id_rol: int,
    request: UpdateRolDestinatarioRequest,
    db: Session = Depends(get_db),
    _current_empleado: dict = Depends(get_current_empleado),
):
    try:
        repo = RolDestinatarioRepository(db)
        use_case = UpdateRolDestinatarioUseCase(repo)
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
        repo = RolDestinatarioRepository(db)
        use_case = DeleteRolDestinatarioUseCase(repo)
        use_case.ejecutar(id_rol)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
