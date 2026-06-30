from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.infrastructure.config.database import get_db
from src.application.use_cases.rol_destinatario.rol_destinatario_use_cases import (
    CreateRolDestinatarioUseCase,
    GetRolDestinatarioUseCase,
    ListRolDestinatarioUseCase,
    UpdateRolDestinatarioUseCase,
    DeleteRolDestinatarioUseCase,
)
from src.infrastructure.adapters.output.repositories.rol_destinatario_repository import RolDestinatarioRepository
from src.application.dtos.rol_destinatario.rol_destinatario_dtos import RolDestinatarioRequestDTO, RolDestinatarioResponseDTO

router = APIRouter(prefix="/api/rol-destinatario", tags=["rol-destinatario"])


@router.post("/", response_model=RolDestinatarioResponseDTO, status_code=status.HTTP_201_CREATED)
def crear_rol_destinatario(request: RolDestinatarioRequestDTO, db: Session = Depends(get_db)):
    repository = RolDestinatarioRepository(db)
    use_case = CreateRolDestinatarioUseCase(repository)
    resultado = use_case.ejecutar(request.nombre_rol, request.descripcion)
    return RolDestinatarioResponseDTO(
        id_rol_destinatario=resultado.id_rol_destinatario,
        nombre_rol=resultado.nombre_rol,
        descripcion=resultado.descripcion,
    )


@router.get("/{id_rol_destinatario}", response_model=RolDestinatarioResponseDTO)
def obtener_rol_destinatario(id_rol_destinatario: int, db: Session = Depends(get_db)):
    repository = RolDestinatarioRepository(db)
    use_case = GetRolDestinatarioUseCase(repository)
    resultado = use_case.ejecutar(id_rol_destinatario)
    return RolDestinatarioResponseDTO(
        id_rol_destinatario=resultado.id_rol_destinatario,
        nombre_rol=resultado.nombre_rol,
        descripcion=resultado.descripcion,
    )


@router.get("/", response_model=list[RolDestinatarioResponseDTO])
def listar_roles_destinatario(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    repository = RolDestinatarioRepository(db)
    use_case = ListRolDestinatarioUseCase(repository)
    resultados = use_case.ejecutar(skip, limit)
    return [
        RolDestinatarioResponseDTO(
            id_rol_destinatario=r.id_rol_destinatario,
            nombre_rol=r.nombre_rol,
            descripcion=r.descripcion,
        )
        for r in resultados
    ]


@router.put("/{id_rol_destinatario}", response_model=RolDestinatarioResponseDTO)
def actualizar_rol_destinatario(id_rol_destinatario: int, request: RolDestinatarioRequestDTO, db: Session = Depends(get_db)):
    repository = RolDestinatarioRepository(db)
    use_case = UpdateRolDestinatarioUseCase(repository)
    resultado = use_case.ejecutar(id_rol_destinatario, request.nombre_rol, request.descripcion)
    return RolDestinatarioResponseDTO(
        id_rol_destinatario=resultado.id_rol_destinatario,
        nombre_rol=resultado.nombre_rol,
        descripcion=resultado.descripcion,
    )


@router.delete("/{id_rol_destinatario}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_rol_destinatario(id_rol_destinatario: int, db: Session = Depends(get_db)):
    repository = RolDestinatarioRepository(db)
    use_case = DeleteRolDestinatarioUseCase(repository)
    use_case.ejecutar(id_rol_destinatario)
    return None