from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.infrastructure.config import get_db
from src.domain.exceptions import RecursoNoEncontradoException, AsociacionYaExisteException
from src.application.dtos.comunicado import (
    CreateComunicadoRequest,
    UpdateComunicadoRequest,
    ComunicadoResponse,
    ListComunicadoResponse,
)
from src.application.dtos.comunicado_destinatario import (
    AsociarComunicadoDestinatarioRequest,
    ComunicadoDestinatarioResponse,
)
from src.application.dtos.comunicado_adjunto import (
    AsociarComunicadoAdjuntoRequest,
    ComunicadoAdjuntoResponse,
)
from src.application.use_cases.comunicado import (
    CreateComunicadoUseCase,
    GetComunicadoUseCase,
    ListComunicadoUseCase,
    UpdateComunicadoUseCase,
    DeleteComunicadoUseCase,
)
from src.application.use_cases.comunicado_destinatario import (
    AsociarComunicadoDestinatarioUseCase,
    DesasociarComunicadoDestinatarioUseCase,
)
from src.application.use_cases.comunicado_adjunto import (
    AsociarComunicadoAdjuntoUseCase,
    DesasociarComunicadoAdjuntoUseCase,
)
from src.infrastructure.adapters.output.repositories.comunicado_repository import ComunicadoRepository
from src.infrastructure.adapters.output.repositories.comunicado_destinatario_repository import (
    ComunicadoDestinatarioRepository,
)
from src.infrastructure.adapters.output.repositories.comunicado_adjunto_repository import (
    ComunicadoAdjuntoRepository,
)
from src.infrastructure.adapters.output.repositories.archivo_repository import ArchivoRepository

router = APIRouter(prefix="/api/comunicado", tags=["comunicado"])


def _to_response(entity) -> ComunicadoResponse:
    return ComunicadoResponse(
        id_comunicado=entity.id_comunicado,
        doi=entity.doi,
        num_comunicado=entity.num_comunicado,
        id_emisor=entity.id_emisor,
        fecha_recepcion=entity.fecha_recepcion,
        id_destinatario=entity.id_destinatario,
        fecha_registro=entity.fecha_registro,
        id_registro=entity.id_registro,
        id_metodo_recepcion=entity.id_metodo_recepcion,
        tema=entity.tema,
        id_tipo_comunicado=entity.id_tipo_comunicado,
        observaciones=entity.observaciones,
    )


@router.post("/", response_model=ComunicadoResponse, status_code=status.HTTP_201_CREATED)
def crear(request: CreateComunicadoRequest, db: Session = Depends(get_db)):
    repo = ComunicadoRepository(db)
    use_case = CreateComunicadoUseCase(repo)
    entity = use_case.ejecutar(
        request.doi,
        request.num_comunicado,
        request.id_emisor,
        request.fecha_recepcion,
        request.id_destinatario,
        request.fecha_registro,
        request.id_registro,
        request.id_metodo_recepcion,
        request.tema,
        request.id_tipo_comunicado,
        request.observaciones,
    )
    return _to_response(entity)


@router.get("/{id_comunicado}", response_model=ComunicadoResponse)
def obtener(id_comunicado: int, db: Session = Depends(get_db)):
    try:
        repo = ComunicadoRepository(db)
        use_case = GetComunicadoUseCase(repo)
        entity = use_case.ejecutar(id_comunicado)
        return _to_response(entity)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/", response_model=ListComunicadoResponse)
def listar(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    repo = ComunicadoRepository(db)
    use_case = ListComunicadoUseCase(repo)
    items = use_case.ejecutar(skip, limit)
    return ListComunicadoResponse(
        items=[_to_response(i) for i in items],
        total=repo.contar(),
        skip=skip,
        limit=limit,
    )


@router.put("/{id_comunicado}", response_model=ComunicadoResponse)
def actualizar(
    id_comunicado: int,
    request: UpdateComunicadoRequest,
    db: Session = Depends(get_db),
):
    try:
        repo = ComunicadoRepository(db)
        use_case = UpdateComunicadoUseCase(repo)
        entity = use_case.ejecutar(
            id_comunicado,
            request.doi,
            request.num_comunicado,
            request.id_emisor,
            request.fecha_recepcion,
            request.id_destinatario,
            request.fecha_registro,
            request.id_registro,
            request.id_metodo_recepcion,
            request.tema,
            request.id_tipo_comunicado,
            request.observaciones,
        )
        return _to_response(entity)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{id_comunicado}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar(id_comunicado: int, db: Session = Depends(get_db)):
    try:
        repo = ComunicadoRepository(db)
        use_case = DeleteComunicadoUseCase(repo)
        use_case.ejecutar(id_comunicado)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post(
    "/{id_comunicado}/destinatarios",
    response_model=ComunicadoDestinatarioResponse,
    status_code=status.HTTP_201_CREATED,
)
def asociar_destinatario(
    id_comunicado: int,
    request: AsociarComunicadoDestinatarioRequest,
    db: Session = Depends(get_db),
):
    try:
        repo = ComunicadoDestinatarioRepository(db)
        comunicado_repo = ComunicadoRepository(db)
        use_case = AsociarComunicadoDestinatarioUseCase(repo, comunicado_repo)
        entity = use_case.ejecutar(
            id_comunicado,
            request.id_destinatario,
            request.id_rol_destinatario,
        )
        return ComunicadoDestinatarioResponse(
            id_comunicado=entity.id_comunicado,
            id_destinatario=entity.id_destinatario,
            id_rol_destinatario=entity.id_rol_destinatario,
        )
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except AsociacionYaExisteException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{id_comunicado}/destinatarios/{id_destinatario}", status_code=status.HTTP_204_NO_CONTENT)
def desasociar_destinatario(
    id_comunicado: int,
    id_destinatario: int,
    db: Session = Depends(get_db),
):
    try:
        repo = ComunicadoDestinatarioRepository(db)
        use_case = DesasociarComunicadoDestinatarioUseCase(repo)
        use_case.ejecutar(id_comunicado, id_destinatario)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post(
    "/{id_comunicado}/adjuntos",
    response_model=ComunicadoAdjuntoResponse,
    status_code=status.HTTP_201_CREATED,
)
def asociar_adjunto(
    id_comunicado: int,
    request: AsociarComunicadoAdjuntoRequest,
    db: Session = Depends(get_db),
):
    try:
        repo = ComunicadoAdjuntoRepository(db)
        comunicado_repo = ComunicadoRepository(db)
        archivo_repo = ArchivoRepository(db)
        use_case = AsociarComunicadoAdjuntoUseCase(repo, comunicado_repo, archivo_repo)
        entity = use_case.ejecutar(id_comunicado, request.id_archivo)
        return ComunicadoAdjuntoResponse(
            id_comunicado=entity.id_comunicado,
            id_archivo=entity.id_archivo,
        )
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except AsociacionYaExisteException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{id_comunicado}/adjuntos/{id_archivo}", status_code=status.HTTP_204_NO_CONTENT)
def desasociar_adjunto(
    id_comunicado: int,
    id_archivo: int,
    db: Session = Depends(get_db),
):
    try:
        repo = ComunicadoAdjuntoRepository(db)
        use_case = DesasociarComunicadoAdjuntoUseCase(repo)
        use_case.ejecutar(id_comunicado, id_archivo)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
