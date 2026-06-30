from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.infrastructure.config import get_db
from src.domain.exceptions import RecursoNoEncontradoException
from src.application.dtos.estado_tarea import (
    CreateEstadoTareaRequest,
    UpdateEstadoTareaRequest,
    EstadoTareaResponse,
    ListEstadoTareaResponse,
)
from src.application.use_cases.estado_tarea import (
    CreateEstadoTareaUseCase,
    GetEstadoTareaUseCase,
    ListEstadoTareaUseCase,
    UpdateEstadoTareaUseCase,
    DeleteEstadoTareaUseCase,
)
from src.infrastructure.adapters.output.repositories.estado_tarea_repository import (
    EstadoTareaRepository,
)

router = APIRouter(prefix="/api/estado-tarea", tags=["estado-tarea"])


def _to_response(entity) -> EstadoTareaResponse:
    return EstadoTareaResponse(
        id_estado_tarea=entity.id_estado_tarea,
        nombre_estado=entity.nombre_estado,
    )


@router.post("/", response_model=EstadoTareaResponse, status_code=status.HTTP_201_CREATED)
def crear(request: CreateEstadoTareaRequest, db: Session = Depends(get_db)):
    repo = EstadoTareaRepository(db)
    use_case = CreateEstadoTareaUseCase(repo)
    entity = use_case.ejecutar(request.nombre_estado)
    return _to_response(entity)


@router.get("/{id_estado_tarea}", response_model=EstadoTareaResponse)
def obtener(id_estado_tarea: int, db: Session = Depends(get_db)):
    try:
        repo = EstadoTareaRepository(db)
        use_case = GetEstadoTareaUseCase(repo)
        entity = use_case.ejecutar(id_estado_tarea)
        return _to_response(entity)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/", response_model=ListEstadoTareaResponse)
def listar(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    repo = EstadoTareaRepository(db)
    use_case = ListEstadoTareaUseCase(repo)
    items = use_case.ejecutar(skip, limit)
    return ListEstadoTareaResponse(
        items=[_to_response(i) for i in items],
        total=repo.contar(),
        skip=skip,
        limit=limit,
    )


@router.put("/{id_estado_tarea}", response_model=EstadoTareaResponse)
def actualizar(
    id_estado_tarea: int,
    request: UpdateEstadoTareaRequest,
    db: Session = Depends(get_db),
):
    try:
        repo = EstadoTareaRepository(db)
        use_case = UpdateEstadoTareaUseCase(repo)
        entity = use_case.ejecutar(id_estado_tarea, request.nombre_estado)
        return _to_response(entity)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{id_estado_tarea}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar(id_estado_tarea: int, db: Session = Depends(get_db)):
    try:
        repo = EstadoTareaRepository(db)
        use_case = DeleteEstadoTareaUseCase(repo)
        use_case.ejecutar(id_estado_tarea)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
