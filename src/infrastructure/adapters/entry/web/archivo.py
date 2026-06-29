from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.infrastructure.config import get_db
from src.domain.exceptions import RecursoNoEncontradoException
from src.application.dtos.archivo import (
    CreateArchivoRequest,
    UpdateArchivoRequest,
    ArchivoResponse,
    ListArchivoResponse,
)
from src.application.use_cases.archivo import (
    CreateArchivoUseCase,
    GetArchivoUseCase,
    ListArchivoUseCase,
    UpdateArchivoUseCase,
    DeleteArchivoUseCase,
)
from src.infrastructure.adapters.output.repositories.archivo_repository import ArchivoRepository

router = APIRouter(prefix="/api/archivo", tags=["archivo"])


def _to_response(entity) -> ArchivoResponse:
    return ArchivoResponse(
        id_archivo=entity.id_archivo,
        doi=entity.doi,
        descripcion=entity.descripcion,
        url_archivo=entity.url_archivo,
        nombre_original=entity.nombre_original,
        id_elaborador=entity.id_elaborador,
        fecha_registro=entity.fecha_registro,
    )


@router.post("/", response_model=ArchivoResponse, status_code=status.HTTP_201_CREATED)
def crear(request: CreateArchivoRequest, db: Session = Depends(get_db)):
    repo = ArchivoRepository(db)
    use_case = CreateArchivoUseCase(repo)
    entity = use_case.ejecutar(
        request.doi,
        request.descripcion,
        request.url_archivo,
        request.nombre_original,
        request.id_elaborador,
        request.fecha_registro,
    )
    return _to_response(entity)


@router.get("/{id_archivo}", response_model=ArchivoResponse)
def obtener(id_archivo: int, db: Session = Depends(get_db)):
    try:
        repo = ArchivoRepository(db)
        use_case = GetArchivoUseCase(repo)
        entity = use_case.ejecutar(id_archivo)
        return _to_response(entity)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/", response_model=ListArchivoResponse)
def listar(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    repo = ArchivoRepository(db)
    use_case = ListArchivoUseCase(repo)
    items = use_case.ejecutar(skip, limit)
    return ListArchivoResponse(
        items=[_to_response(i) for i in items],
        total=repo.contar(),
        skip=skip,
        limit=limit,
    )


@router.put("/{id_archivo}", response_model=ArchivoResponse)
def actualizar(id_archivo: int, request: UpdateArchivoRequest, db: Session = Depends(get_db)):
    try:
        repo = ArchivoRepository(db)
        use_case = UpdateArchivoUseCase(repo)
        entity = use_case.ejecutar(
            id_archivo,
            request.doi,
            request.descripcion,
            request.url_archivo,
            request.nombre_original,
            request.id_elaborador,
            request.fecha_registro,
        )
        return _to_response(entity)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{id_archivo}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar(id_archivo: int, db: Session = Depends(get_db)):
    try:
        repo = ArchivoRepository(db)
        use_case = DeleteArchivoUseCase(repo)
        use_case.ejecutar(id_archivo)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
