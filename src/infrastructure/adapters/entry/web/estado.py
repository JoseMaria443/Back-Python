from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.application.dtos.estado import (
	EstadoRequestDTO,
	EstadoResponseDTO,
	ListEstadoResponse,
)
from src.application.use_cases.estado import (
	CreateEstadoUseCase,
	DeleteEstadoUseCase,
	GetEstadoUseCase,
	ListEstadoUseCase,
	UpdateEstadoUseCase,
)
from src.domain.exceptions import RecursoNoEncontradoException
from src.infrastructure.adapters.output.repositories.estado_repository import (
	EstadoRepository,
)
from src.infrastructure.config import get_db
from src.infrastructure.config.auth import get_current_empleado

router = APIRouter(prefix="/api/estado", tags=["estado"])


def _to_response(entity) -> EstadoResponseDTO:
	return EstadoResponseDTO(
		id_estado=entity.id_estado,
		nombre_estado=entity.nombre_estado,
	)


@router.post("/", response_model=EstadoResponseDTO, status_code=status.HTTP_201_CREATED)
def crear(
	request: EstadoRequestDTO,
	db: Session = Depends(get_db),
	_current_empleado: dict = Depends(get_current_empleado),
):
	repo = EstadoRepository(db)
	use_case = CreateEstadoUseCase(repo)
	entity = use_case.ejecutar(request.nombre_estado)
	return _to_response(entity)


@router.get("/{id_estado}", response_model=EstadoResponseDTO)
def obtener(
	id_estado: int,
	db: Session = Depends(get_db),
	_current_empleado: dict = Depends(get_current_empleado),
):
	try:
		repo = EstadoRepository(db)
		use_case = GetEstadoUseCase(repo)
		entity = use_case.ejecutar(id_estado)
		return _to_response(entity)
	except RecursoNoEncontradoException as e:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/", response_model=ListEstadoResponse)
def listar(
	skip: int = 0,
	limit: int = 50,
	db: Session = Depends(get_db),
	_current_empleado: dict = Depends(get_current_empleado),
):
	repo = EstadoRepository(db)
	use_case = ListEstadoUseCase(repo)
	items = use_case.ejecutar(skip, limit)
	return ListEstadoResponse(
		items=[_to_response(i) for i in items],
		total=repo.contar(),
		skip=skip,
		limit=limit,
	)


@router.put("/{id_estado}", response_model=EstadoResponseDTO)
def actualizar(
	id_estado: int,
	request: EstadoRequestDTO,
	db: Session = Depends(get_db),
	_current_empleado: dict = Depends(get_current_empleado),
):
	try:
		repo = EstadoRepository(db)
		use_case = UpdateEstadoUseCase(repo)
		entity = use_case.ejecutar(id_estado, request.nombre_estado)
		return _to_response(entity)
	except RecursoNoEncontradoException as e:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{id_estado}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar(
	id_estado: int,
	db: Session = Depends(get_db),
	_current_empleado: dict = Depends(get_current_empleado),
):
	try:
		repo = EstadoRepository(db)
		use_case = DeleteEstadoUseCase(repo)
		use_case.ejecutar(id_estado)
	except RecursoNoEncontradoException as e:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))