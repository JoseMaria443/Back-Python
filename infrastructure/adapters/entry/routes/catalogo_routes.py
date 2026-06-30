from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.infrastructure.config.database import get_db
from src.application.use_cases.catalogo.catalogo_use_cases import (
    CreateCatalogoUseCase,
    GetCatalogoUseCase,
    ListCatalogoUseCase,
    UpdateCatalogoUseCase,
    DeleteCatalogoUseCase,
)
from src.infrastructure.adapters.output.repositories.catalogo_repository import CatalogoRepository
from src.application.dtos.catalogo.catalogo_dtos import CatalogoRequestDTO, CatalogoResponseDTO

router = APIRouter(prefix="/api/catalogo", tags=["catalogo"])


@router.post("/", response_model=CatalogoResponseDTO, status_code=status.HTTP_201_CREATED)
def crear_catalogo(request: CatalogoRequestDTO, db: Session = Depends(get_db)):
    repository = CatalogoRepository(db)
    use_case = CreateCatalogoUseCase(repository)
    resultado = use_case.ejecutar(
        nombre_catalogo=request.nombre_catalogo,
        id_tipo_catalogo=request.id_tipo_catalogo,
        descripcion=request.descripcion,
    )
    return CatalogoResponseDTO(
        id_catalogo=resultado.id_catalogo,
        nombre_catalogo=resultado.nombre_catalogo,
        id_tipo_catalogo=resultado.id_tipo_catalogo,
        descripcion=resultado.descripcion,
    )


@router.get("/{id_catalogo}", response_model=CatalogoResponseDTO)
def obtener_catalogo(id_catalogo: int, db: Session = Depends(get_db)):
    repository = CatalogoRepository(db)
    use_case = GetCatalogoUseCase(repository)
    resultado = use_case.ejecutar(id_catalogo)
    return CatalogoResponseDTO(
        id_catalogo=resultado.id_catalogo,
        nombre_catalogo=resultado.nombre_catalogo,
        id_tipo_catalogo=resultado.id_tipo_catalogo,
        descripcion=resultado.descripcion,
    )


@router.get("/", response_model=list[CatalogoResponseDTO])
def listar_catalogos(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    repository = CatalogoRepository(db)
    use_case = ListCatalogoUseCase(repository)
    resultados = use_case.ejecutar(skip, limit)
    return [
        CatalogoResponseDTO(
            id_catalogo=r.id_catalogo,
            nombre_catalogo=r.nombre_catalogo,
            id_tipo_catalogo=r.id_tipo_catalogo,
            descripcion=r.descripcion,
        )
        for r in resultados
    ]


@router.put("/{id_catalogo}", response_model=CatalogoResponseDTO)
def actualizar_catalogo(id_catalogo: int, request: CatalogoRequestDTO, db: Session = Depends(get_db)):
    repository = CatalogoRepository(db)
    use_case = UpdateCatalogoUseCase(repository)
    resultado = use_case.ejecutar(id_catalogo, request.nombre_catalogo, request.descripcion)
    return CatalogoResponseDTO(
        id_catalogo=resultado.id_catalogo,
        nombre_catalogo=resultado.nombre_catalogo,
        id_tipo_catalogo=resultado.id_tipo_catalogo,
        descripcion=resultado.descripcion,
    )


@router.delete("/{id_catalogo}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_catalogo(id_catalogo: int, db: Session = Depends(get_db)):
    repository = CatalogoRepository(db)
    use_case = DeleteCatalogoUseCase(repository)
    use_case.ejecutar(id_catalogo)
    return None