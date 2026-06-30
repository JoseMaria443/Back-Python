from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.infrastructure.config.database import get_db
from src.application.use_cases.rol_responsable.rol_responsable_use_cases import (
    CreateRolResponsableUseCase,
    GetRolResponsableUseCase,
    ListRolResponsableUseCase,
    UpdateRolResponsableUseCase,
    DeleteRolResponsableUseCase,
)
from src.infrastructure.adapters.output.repositories.rol_responsable_repository import RolResponsableRepository
from src.application.dtos.rol_responsable.rol_responsable_dtos import RolResponsableRequestDTO, RolResponsableResponseDTO

router = APIRouter(prefix="/api/rol-responsable", tags=["rol-responsable"])


@router.post("/", response_model=RolResponsableResponseDTO, status_code=status.HTTP_201_CREATED)
def crear_rol_responsable(request: RolResponsableRequestDTO, db: Session = Depends(get_db)):
    repository = RolResponsableRepository(db)
    use_case = CreateRolResponsableUseCase(repository)
    resultado = use_case.ejecutar(request.nombre_rol, request.descripcion)
    return RolResponsableResponseDTO(
        id_rol_responsable=resultado.id_rol_responsable,
        nombre_rol=resultado.nombre_rol,
        descripcion=resultado.descripcion,
    )


@router.get("/{id_rol_responsable}", response_model=RolResponsableResponseDTO)
def obtener_rol_responsable(id_rol_responsable: int, db: Session = Depends(get_db)):
    repository = RolResponsableRepository(db)
    use_case = GetRolResponsableUseCase(repository)
    resultado = use_case.ejecutar(id_rol_responsable)
    return RolResponsableResponseDTO(
        id_rol_responsable=resultado.id_rol_responsable,
        nombre_rol=resultado.nombre_rol,
        descripcion=resultado.descripcion,
    )


@router.get("/", response_model=list[RolResponsableResponseDTO])
def listar_roles_responsable(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    repository = RolResponsableRepository(db)
    use_case = ListRolResponsableUseCase(repository)
    resultados = use_case.ejecutar(skip, limit)
    return [
        RolResponsableResponseDTO(
            id_rol_responsable=r.id_rol_responsable,
            nombre_rol=r.nombre_rol,
            descripcion=r.descripcion,
        )
        for r in resultados
    ]


@router.put("/{id_rol_responsable}", response_model=RolResponsableResponseDTO)
def actualizar_rol_responsable(id_rol_responsable: int, request: RolResponsableRequestDTO, db: Session = Depends(get_db)):
    repository = RolResponsableRepository(db)
    use_case = UpdateRolResponsableUseCase(repository)
    resultado = use_case.ejecutar(id_rol_responsable, request.nombre_rol, request.descripcion)
    return RolResponsableResponseDTO(
        id_rol_responsable=resultado.id_rol_responsable,
        nombre_rol=resultado.nombre_rol,
        descripcion=resultado.descripcion,
    )


@router.delete("/{id_rol_responsable}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_rol_responsable(id_rol_responsable: int, db: Session = Depends(get_db)):
    repository = RolResponsableRepository(db)
    use_case = DeleteRolResponsableUseCase(repository)
    use_case.ejecutar(id_rol_responsable)
    return None