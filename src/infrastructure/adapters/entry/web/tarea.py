from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.infrastructure.config import get_db
from src.domain.exceptions import RecursoNoEncontradoException, AsociacionYaExisteException
from src.application.dtos.tarea import (
    CreateTareaRequest,
    UpdateTareaRequest,
    TareaResponse,
    ListTareaResponse,
)
from src.application.dtos.tarea_responsable import (
    AsociarTareaResponsableRequest,
    TareaResponsableResponse,
)
from src.application.dtos.tarea_archivo import (
    AsociarTareaArchivoRequest,
    TareaArchivoResponse,
)
from src.application.use_cases.tarea import (
    CreateTareaUseCase,
    GetTareaUseCase,
    ListTareaUseCase,
    UpdateTareaUseCase,
    DeleteTareaUseCase,
)
from src.application.use_cases.tarea_responsable import (
    AsociarTareaResponsableUseCase,
    DesasociarTareaResponsableUseCase,
)
from src.application.use_cases.tarea_archivo import (
    AsociarTareaArchivoUseCase,
    DesasociarTareaArchivoUseCase,
)
from src.infrastructure.adapters.output.repositories.tarea_repository import TareaRepository
from src.infrastructure.adapters.output.repositories.tarea_responsable_repository import (
    TareaResponsableRepository,
)
from src.infrastructure.adapters.output.repositories.tarea_archivo_repository import (
    TareaArchivoRepository,
)
from src.infrastructure.adapters.output.repositories.empleado_repository import EmpleadoRepository
from src.infrastructure.adapters.output.repositories.archivo_repository import ArchivoRepository

router = APIRouter(prefix="/api/tarea", tags=["tarea"])


def _to_response(entity) -> TareaResponse:
    return TareaResponse(
        id_tarea=entity.id_tarea,
        id_comunicado=entity.id_comunicado,
        descripcion=entity.descripcion,
        fecha_entrega=entity.fecha_entrega,
        fecha_registro=entity.fecha_registro,
        id_estado_tarea=entity.id_estado_tarea,
    )


@router.post("/", response_model=TareaResponse, status_code=status.HTTP_201_CREATED)
def crear(request: CreateTareaRequest, db: Session = Depends(get_db)):
    repo = TareaRepository(db)
    use_case = CreateTareaUseCase(repo)
    entity = use_case.ejecutar(
        request.id_comunicado,
        request.descripcion,
        request.fecha_entrega,
        request.fecha_registro,
        request.id_estado_tarea,
    )
    return _to_response(entity)


@router.get("/{id_tarea}", response_model=TareaResponse)
def obtener(id_tarea: int, db: Session = Depends(get_db)):
    try:
        repo = TareaRepository(db)
        use_case = GetTareaUseCase(repo)
        entity = use_case.ejecutar(id_tarea)
        return _to_response(entity)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/", response_model=ListTareaResponse)
def listar(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    repo = TareaRepository(db)
    use_case = ListTareaUseCase(repo)
    items = use_case.ejecutar(skip, limit)
    return ListTareaResponse(
        items=[_to_response(i) for i in items],
        total=repo.contar(),
        skip=skip,
        limit=limit,
    )


@router.put("/{id_tarea}", response_model=TareaResponse)
def actualizar(id_tarea: int, request: UpdateTareaRequest, db: Session = Depends(get_db)):
    try:
        repo = TareaRepository(db)
        use_case = UpdateTareaUseCase(repo)
        entity = use_case.ejecutar(
            id_tarea,
            request.id_comunicado,
            request.descripcion,
            request.fecha_entrega,
            request.fecha_registro,
            request.id_estado_tarea,
        )
        return _to_response(entity)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{id_tarea}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar(id_tarea: int, db: Session = Depends(get_db)):
    try:
        repo = TareaRepository(db)
        use_case = DeleteTareaUseCase(repo)
        use_case.ejecutar(id_tarea)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post(
    "/{id_tarea}/responsables",
    response_model=TareaResponsableResponse,
    status_code=status.HTTP_201_CREATED,
)
def asociar_responsable(
    id_tarea: int,
    request: AsociarTareaResponsableRequest,
    db: Session = Depends(get_db),
):
    try:
        repo = TareaResponsableRepository(db)
        tarea_repo = TareaRepository(db)
        empleado_repo = EmpleadoRepository(db)
        use_case = AsociarTareaResponsableUseCase(repo, tarea_repo, empleado_repo)
        entity = use_case.ejecutar(id_tarea, request.id_responsable, request.id_rol)
        return TareaResponsableResponse(
            id_tarea=entity.id_tarea,
            id_responsable=entity.id_responsable,
            id_rol=entity.id_rol,
        )
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except AsociacionYaExisteException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{id_tarea}/responsables/{id_responsable}", status_code=status.HTTP_204_NO_CONTENT)
def desasociar_responsable(id_tarea: int, id_responsable: int, db: Session = Depends(get_db)):
    try:
        repo = TareaResponsableRepository(db)
        use_case = DesasociarTareaResponsableUseCase(repo)
        use_case.ejecutar(id_tarea, id_responsable)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post(
    "/{id_tarea}/archivos",
    response_model=TareaArchivoResponse,
    status_code=status.HTTP_201_CREATED,
)
def asociar_archivo(
    id_tarea: int,
    request: AsociarTareaArchivoRequest,
    db: Session = Depends(get_db),
):
    try:
        repo = TareaArchivoRepository(db)
        tarea_repo = TareaRepository(db)
        archivo_repo = ArchivoRepository(db)
        use_case = AsociarTareaArchivoUseCase(repo, tarea_repo, archivo_repo)
        entity = use_case.ejecutar(id_tarea, request.id_archivo)
        return TareaArchivoResponse(id_tarea=entity.id_tarea, id_archivo=entity.id_archivo)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except AsociacionYaExisteException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{id_tarea}/archivos/{id_archivo}", status_code=status.HTTP_204_NO_CONTENT)
def desasociar_archivo(id_tarea: int, id_archivo: int, db: Session = Depends(get_db)):
    try:
        repo = TareaArchivoRepository(db)
        use_case = DesasociarTareaArchivoUseCase(repo)
        use_case.ejecutar(id_tarea, id_archivo)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
