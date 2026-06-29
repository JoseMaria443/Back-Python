from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.infrastructure.config import get_db
from src.domain.exceptions import RecursoNoEncontradoException
from src.application.dtos.tipo_catalogo import (
    CreateTipoCatalogoRequest,
    UpdateTipoCatalogoRequest,
    TipoCatalogoResponse,
    ListTipoCatalogoResponse,
)
from src.application.use_cases.tipo_catalogo import (
    CreateTipoCatalogoUseCase,
    GetTipoCatalogoUseCase,
    ListTipoCatalogoUseCase,
    UpdateTipoCatalogoUseCase,
    DeleteTipoCatalogoUseCase,
)
from src.infrastructure.adapters.output.repositories.tipo_catalogo_repository import (
    TipoCatalogoRepository,
)

router = APIRouter(prefix="/api/tipo-catalogo", tags=["tipo-catalogo"])


def _to_response(entity) -> TipoCatalogoResponse:
    return TipoCatalogoResponse(
        id_tipo_catalogo=entity.id_tipo_catalogo,
        nombre_tipo_catalogo=entity.nombre_tipo_catalogo,
    )


@router.post("/", response_model=TipoCatalogoResponse, status_code=status.HTTP_201_CREATED)
def crear(request: CreateTipoCatalogoRequest, db: Session = Depends(get_db)):
    repo = TipoCatalogoRepository(db)
    use_case = CreateTipoCatalogoUseCase(repo)
    entity = use_case.ejecutar(request.nombre_tipo_catalogo)
    return _to_response(entity)


@router.get("/{id_tipo_catalogo}", response_model=TipoCatalogoResponse)
def obtener(id_tipo_catalogo: int, db: Session = Depends(get_db)):
    try:
        repo = TipoCatalogoRepository(db)
        use_case = GetTipoCatalogoUseCase(repo)
        entity = use_case.ejecutar(id_tipo_catalogo)
        return _to_response(entity)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/", response_model=ListTipoCatalogoResponse)
def listar(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    repo = TipoCatalogoRepository(db)
    use_case = ListTipoCatalogoUseCase(repo)
    items = use_case.ejecutar(skip, limit)
    return ListTipoCatalogoResponse(
        items=[_to_response(i) for i in items],
        total=repo.contar(),
        skip=skip,
        limit=limit,
    )


@router.put("/{id_tipo_catalogo}", response_model=TipoCatalogoResponse)
def actualizar(
    id_tipo_catalogo: int,
    request: UpdateTipoCatalogoRequest,
    db: Session = Depends(get_db),
):
    try:
        repo = TipoCatalogoRepository(db)
        use_case = UpdateTipoCatalogoUseCase(repo)
        entity = use_case.ejecutar(id_tipo_catalogo, request.nombre_tipo_catalogo)
        return _to_response(entity)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{id_tipo_catalogo}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar(id_tipo_catalogo: int, db: Session = Depends(get_db)):
    try:
        repo = TipoCatalogoRepository(db)
        use_case = DeleteTipoCatalogoUseCase(repo)
        use_case.ejecutar(id_tipo_catalogo)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
