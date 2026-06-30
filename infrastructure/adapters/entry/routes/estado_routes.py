from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.infrastructure.config.database import get_db
from src.application.use_cases.estado.estado_use_cases import (
    CreateEstadoUseCase,
    GetEstadoUseCase,
    ListEstadoUseCase,
    UpdateEstadoUseCase,
    DeleteEstadoUseCase,
)
from src.infrastructure.adapters.output.repositories.estado_repository import EstadoRepository
from src.application.dtos.estado.estado_dtos import EstadoRequestDTO, EstadoResponseDTO

router = APIRouter(prefix="/api/estado", tags=["estado"])

//ugy
@router.post("/", response_model=EstadoResponseDTO, status_code=status.HTTP_201_CREATED)
def crear_estado(request: EstadoRequestDTO, db: Session = Depends(get_db)):
    repository = EstadoRepository(db)
    use_case = CreateEstadoUseCase(repository)
    resultado = use_case.ejecutar(request.nombre_estado, request.descripcion)
    return EstadoResponseDTO(
        id_estado=resultado.id_estado,
        nombre_estado=resultado.nombre_estado,
        descripcion=resultado.descripcion,
    )


@router.get("/{id_estado}", response_model=EstadoResponseDTO)
def obtener_estado(id_estado: int, db: Session = Depends(get_db)):
    repository = EstadoRepository(db)
    use_case = GetEstadoUseCase(repository)
    resultado = use_case.ejecutar(id_estado)
    return EstadoResponseDTO(
        id_estado=resultado.id_estado,
        nombre_estado=resultado.nombre_estado,
        descripcion=resultado.descripcion,
    )


@router.get("/", response_model=list[EstadoResponseDTO])
def listar_estados(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    repository = EstadoRepository(db)
    use_case = ListEstadoUseCase(repository)
    resultados = use_case.ejecutar(skip, limit)
    return [
        EstadoResponseDTO(
            id_estado=r.id_estado,
            nombre_estado=r.nombre_estado,
            descripcion=r.descripcion,
        )
        for r in resultados
    ]


@router.put("/{id_estado}", response_model=EstadoResponseDTO)
def actualizar_estado(id_estado: int, request: EstadoRequestDTO, db: Session = Depends(get_db)):
    repository = EstadoRepository(db)
    use_case = UpdateEstadoUseCase(repository)
    resultado = use_case.ejecutar(id_estado, request.nombre_estado, request.descripcion)
    return EstadoResponseDTO(
        id_estado=resultado.id_estado,
        nombre_estado=resultado.nombre_estado,
        descripcion=resultado.descripcion,
    )


@router.delete("/{id_estado}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_estado(id_estado: int, db: Session = Depends(get_db)):
    repository = EstadoRepository(db)
    use_case = DeleteEstadoUseCase(repository)
    use_case.ejecutar(id_estado)
    return None