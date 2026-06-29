from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.infrastructure.config import get_db
from src.domain.exceptions import RecursoNoEncontradoException
from src.application.dtos.catalogo import (
    CreateCatalogoRequest,
    UpdateCatalogoRequest,
    CatalogoResponse,
    ListCatalogoResponse,
)
from src.application.use_cases.catalogo import (
    CreateCatalogoUseCase,
    GetCatalogoUseCase,
    ListCatalogoUseCase,
    UpdateCatalogoUseCase,
    DeleteCatalogoUseCase,
)
from src.infrastructure.adapters.output.repositories.catalogo_repository import CatalogoRepository

router = APIRouter(prefix="/api/catalogo", tags=["catalogo"])


def _to_response(entity) -> CatalogoResponse:
    return CatalogoResponse(
        id_catalogo=entity.id_catalogo,
        id_tipo_catalogo=entity.id_tipo_catalogo,
        descripcion=entity.descripcion,
    )


@router.post("/", response_model=CatalogoResponse, status_code=status.HTTP_201_CREATED)
def crear(request: CreateCatalogoRequest, db: Session = Depends(get_db)):
    repo = CatalogoRepository(db)
    use_case = CreateCatalogoUseCase(repo)
    entity = use_case.ejecutar(request.id_tipo_catalogo, request.descripcion)
    return _to_response(entity)


@router.get("/{id_catalogo}", response_model=CatalogoResponse)
def obtener(id_catalogo: int, db: Session = Depends(get_db)):
    try:
        repo = CatalogoRepository(db)
        use_case = GetCatalogoUseCase(repo)
        entity = use_case.ejecutar(id_catalogo)
        return _to_response(entity)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/", response_model=ListCatalogoResponse)
def listar(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    repo = CatalogoRepository(db)
    use_case = ListCatalogoUseCase(repo)
    items = use_case.ejecutar(skip, limit)
    return ListCatalogoResponse(
        items=[_to_response(i) for i in items],
        total=repo.contar(),
        skip=skip,
        limit=limit,
    )


@router.put("/{id_catalogo}", response_model=CatalogoResponse)
def actualizar(
    id_catalogo: int,
    request: UpdateCatalogoRequest,
    db: Session = Depends(get_db),
):
    try:
        repo = CatalogoRepository(db)
        use_case = UpdateCatalogoUseCase(repo)
        entity = use_case.ejecutar(id_catalogo, request.id_tipo_catalogo, request.descripcion)
        return _to_response(entity)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{id_catalogo}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar(id_catalogo: int, db: Session = Depends(get_db)):
    try:
        repo = CatalogoRepository(db)
        use_case = DeleteCatalogoUseCase(repo)
        use_case.ejecutar(id_catalogo)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
