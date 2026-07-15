from datetime import date
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from sqlalchemy.orm import Session

from src.infrastructure.config import get_db
from src.domain.exceptions import RecursoNoEncontradoException
from src.domain.exceptions.crud_exceptions import ErrorAlmacenamientoException
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
from src.infrastructure.adapters.output.almacenamiento.cloudinary_adapter import CloudinaryAdapter
from src.infrastructure.config.auth import get_current_empleado

router = APIRouter(prefix="/api/archivo", tags=["archivo"])

EXTENSIONES_PERMITIDAS = {".pdf", ".docx", ".jpg", ".jpeg", ".png"}
TAMANO_MAXIMO_MB = 50
TAMANO_MAXIMO_BYTES = TAMANO_MAXIMO_MB * 1024 * 1024


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


def _validar_archivo(file: UploadFile) -> None:
    if not file.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El archivo debe tener un nombre"
        )
    
    extension = "." + file.filename.rsplit(".", 1)[-1].lower() if "." in file.filename else ""
    if extension not in EXTENSIONES_PERMITIDAS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Extensión no permitida. Extensiones válidas: {', '.join(EXTENSIONES_PERMITIDAS)}"
        )


def _validar_tamano(contenido: bytes) -> None:
    if len(contenido) > TAMANO_MAXIMO_BYTES:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"Archivo demasiado grande. Tamaño máximo: {TAMANO_MAXIMO_MB} MB"
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


@router.post("/subir", response_model=ArchivoResponse, status_code=status.HTTP_201_CREATED)
def subir_archivo(
    file: UploadFile = File(...),
    doi: str = Form(...),
    descripcion: str = Form(...),
    id_elaborador: int = Form(...),
    fecha_registro: str = Form(...),
    db: Session = Depends(get_db),
    empleado: dict = Depends(get_current_empleado),
):
    _validar_archivo(file)
    
    contenido = file.file.read()
    _validar_tamano(contenido)
    
    adapter = CloudinaryAdapter()
    try:
        url_archivo = adapter.subir(contenido, file.filename)
    except ErrorAlmacenamientoException as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    
    repo = ArchivoRepository(db)
    use_case = CreateArchivoUseCase(repo)
    entity = use_case.ejecutar(
        doi,
        descripcion,
        url_archivo,
        file.filename,
        id_elaborador,
        date.fromisoformat(fecha_registro),
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