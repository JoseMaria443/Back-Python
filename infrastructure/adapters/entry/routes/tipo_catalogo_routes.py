from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.infrastructure.config.database import get_db
from src.application.use_cases.tipo_catalogo.tipo_catalogo_use_cases import (
    CreateTipoCatalogoUseCase,
    GetTipoCatalogoUseCase,
    ListTipoCatalogoUseCase,
    UpdateTipoCatalogoUseCase,
    DeleteTipoCatalogoUseCase,
)
from src.infrastructure.adapters.output.repositories.tipo_catalogo_repository import TipoCatalogoRepository
from src.application.dtos.tipo_catalogo.tipo_catalogo_dtos import TipoCatalogoRequestDTO, TipoCatalogoResponseDTO

router = APIRouter(prefix="/api/tipo-catalogo", tags=["tipo-catalogo"])


@router.post("/", response_model=TipoCatalogoResponseDTO, status_code=status.HTTP_201_CREATED)
def crear_tipo_catalogo(request: TipoCatalogoRequestDTO, db: Session = Depends(get_db)):
    repository = TipoCatalogoRepository(db)
    use_case = CreateTipoCatalogoUseCase(repository)
    resultado = use_case.ejecutar(request.nombre_tipo_catalogo)
    return TipoCatalogoResponseDTO(
        id_tipo_catalogo=resultado.id_tipo_catalogo,
        nombre_tipo_catalogo=resultado.nombre_tipo_catalogo,
    )


@router.get("/{id_tipo_catalogo}", response_model=TipoCatalogoResponseDTO)
def obtener_tipo_catalogo(id_tipo_catalogo: int, db: Session = Depends(get_db)):
    repository = TipoCatalogoRepository(db)
    use_case = GetTipoCatalogoUseCase(repository)
    resultado = use_case.ejecutar(id_tipo_catalogo)
    return TipoCatalogoResponseDTO(
        id_tipo_catalogo=resultado.id_tipo_catalogo,
        nombre_tipo_catalogo=resultado.nombre_tipo_catalogo,
    )


@router.get("/", response_model=list[TipoCatalogoResponseDTO])
def listar_tipos_catalogo(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    repository = TipoCatalogoRepository(db)
    use_case = ListTipoCatalogoUseCase(repository)
    resultados = use_case.ejecutar(skip, limit)
    return [
        TipoCatalogoResponseDTO(
            id_tipo_catalogo=r.id_tipo_catalogo,
            nombre_tipo_catalogo=r.nombre_tipo_catalogo,
        )
        for r in resultados
    ]


@router.put("/{id_tipo_catalogo}", response_model=TipoCatalogoResponseDTO)
def actualizar_tipo_catalogo(id_tipo_catalogo: int, request: TipoCatalogoRequestDTO, db: Session = Depends(get_db)):
    repository = TipoCatalogoRepository(db)
    use_case = UpdateTipoCatalogoUseCase(repository)
    resultado = use_case.ejecutar(id_tipo_catalogo, request.nombre_tipo_catalogo)
    return TipoCatalogoResponseDTO(
        id_tipo_catalogo=resultado.id_tipo_catalogo,
        nombre_tipo_catalogo=resultado.nombre_tipo_catalogo,
    )


@router.delete("/{id_tipo_catalogo}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_tipo_catalogo(id_tipo_catalogo: int, db: Session = Depends(get_db)):
    repository = TipoCatalogoRepository(db)
    use_case = DeleteTipoCatalogoUseCase(repository)
    use_case.ejecutar(id_tipo_catalogo)
    return None