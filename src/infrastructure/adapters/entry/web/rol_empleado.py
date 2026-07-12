from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.infrastructure.config import get_db
from src.infrastructure.config.auth import get_current_empleado
from src.domain.exceptions import RecursoNoEncontradoException, AsociacionYaExisteException, RecursoEnUsoException
from src.application.dtos.rol_empleado import (
    CreateRolEmpleadoRequest,
    UpdateRolEmpleadoRequest,
    RolEmpleadoResponse,
    ListRolEmpleadoResponse,
    AsignarRolRequest,
)
from src.application.use_cases.rol_empleado import (
    CreateRolEmpleadoUseCase,
    ListRolEmpleadoUseCase,
    UpdateRolEmpleadoUseCase,
    DeleteRolEmpleadoUseCase,
    AsignarRolEmpleadoUseCase,
    QuitarRolEmpleadoUseCase,
    ListarRolesEmpleadoUseCase,
)
from src.infrastructure.adapters.output.repositories.rol_empleado_repository import (
    RolEmpleadoRepository,
)
from src.infrastructure.adapters.output.repositories.empleado_rol_repository import (
    EmpleadoRolRepository,
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
    except AsociacionYaExisteException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except RecursoEnUsoException as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


@router.post("/empleado/{id_empleado}/roles", response_model=RolEmpleadoResponse)
def asignar_rol(
    id_empleado: int,
    request: AsignarRolRequest,
    db: Session = Depends(get_db),
    _current_empleado: dict = Depends(get_current_empleado),
):
    try:
        empleado_rol_repo = EmpleadoRolRepository(db)
        rol_repo = RolEmpleadoRepository(db)
        use_case = AsignarRolEmpleadoUseCase(empleado_rol_repo, rol_repo)
        entity = use_case.ejecutar(id_empleado, request.id_rol)
        return _to_response(entity)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except AsociacionYaExisteException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/empleado/{id_empleado}/roles/{id_rol}", status_code=status.HTTP_204_NO_CONTENT)
def quitar_rol(
    id_empleado: int,
    id_rol: int,
    db: Session = Depends(get_db),
    _current_empleado: dict = Depends(get_current_empleado),
):
    try:
        empleado_rol_repo = EmpleadoRolRepository(db)
        use_case = QuitarRolEmpleadoUseCase(empleado_rol_repo)
        use_case.ejecutar(id_empleado, id_rol)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/empleado/{id_empleado}/roles", response_model=ListRolEmpleadoResponse)
def listar_roles_empleado(
    id_empleado: int,
    db: Session = Depends(get_db),
    _current_empleado: dict = Depends(get_current_empleado),
):
    empleado_rol_repo = EmpleadoRolRepository(db)
    use_case = ListarRolesEmpleadoUseCase(empleado_rol_repo)
    items = use_case.ejecutar(id_empleado)
    return ListRolEmpleadoResponse(
        items=[_to_response(i) for i in items],
        total=len(items),
        skip=0,
        limit=len(items),
    )