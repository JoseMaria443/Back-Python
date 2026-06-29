from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.infrastructure.config import get_db
from src.domain.exceptions import RecursoNoEncontradoException, AsociacionYaExisteException
from src.application.dtos.emp_cargo import AsociarEmpCargoRequest, EmpCargoResponse
from src.application.use_cases.emp_cargo import AsociarEmpCargoUseCase, DesasociarEmpCargoUseCase
from src.infrastructure.adapters.output.repositories.emp_cargo_repository import EmpCargoRepository
from src.infrastructure.adapters.output.repositories.empleado_repository import EmpleadoRepository

router = APIRouter(prefix="/api/emp-cargo", tags=["emp-cargo"])


@router.post("/", response_model=EmpCargoResponse, status_code=status.HTTP_201_CREATED)
def asociar(request: AsociarEmpCargoRequest, db: Session = Depends(get_db)):
    try:
        repo = EmpCargoRepository(db)
        empleado_repo = EmpleadoRepository(db)
        use_case = AsociarEmpCargoUseCase(repo, empleado_repo)
        entity = use_case.ejecutar(
            request.id_empleado,
            request.id_cargo,
            request.fecha_inicio,
            request.fecha_termina,
            request.id_registro_modificacion,
        )
        return EmpCargoResponse(
            id_empleado=entity.id_empleado,
            id_cargo=entity.id_cargo,
            fecha_inicio=entity.fecha_inicio,
            fecha_termina=entity.fecha_termina,
            id_registro_modificacion=entity.id_registro_modificacion,
        )
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except AsociacionYaExisteException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{id_empleado}/{id_cargo}", status_code=status.HTTP_204_NO_CONTENT)
def desasociar(id_empleado: int, id_cargo: int, db: Session = Depends(get_db)):
    try:
        repo = EmpCargoRepository(db)
        use_case = DesasociarEmpCargoUseCase(repo)
        use_case.ejecutar(id_empleado, id_cargo)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
