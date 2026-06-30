from typing import List
from src.domain.entities.emp_cargo import EmpCargo
from src.domain.ports.input.emp_cargo import (
    CreateEmpCargoInputPort,
    GetEmpCargoInputPort,
    ListEmpCargoInputPort,
    UpdateEmpCargoInputPort,
    DeleteEmpCargoInputPort,
)
from src.domain.ports.output.emp_cargo import EmpCargoRepositoryPort
from src.domain.exceptions.crud_exceptions import RecursoNoEncontradoException


class CreateEmpCargoUseCase(CreateEmpCargoInputPort):
    def __init__(self, repository: EmpCargoRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_empleado: int, id_cargo: int, fecha_inicio: str, fecha_termina: str, id_registro_modificacion: int) -> EmpCargo:
        from datetime import datetime
        emp_cargo = EmpCargo(
            id_empleado=id_empleado,
            id_cargo=id_cargo,
            fecha_inicio=datetime.strptime(fecha_inicio, "%Y-%m-%d").date(),
            fecha_termina=datetime.strptime(fecha_termina, "%Y-%m-%d").date(),
            id_registro_modificacion=id_registro_modificacion,
        )
        return self.repository.crear(emp_cargo)


class GetEmpCargoUseCase(GetEmpCargoInputPort):
    def __init__(self, repository: EmpCargoRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_empleado: int, id_cargo: int) -> EmpCargo:
        resultado = self.repository.obtener_por_id(id_empleado, id_cargo)
        if not resultado:
            raise RecursoNoEncontradoException(f"EmpCargo {id_empleado}-{id_cargo} no encontrado.")
        return resultado


class ListEmpCargoUseCase(ListEmpCargoInputPort):
    def __init__(self, repository: EmpCargoRepositoryPort):
        self.repository = repository

    def ejecutar(self, skip: int = 0, limit: int = 50) -> List[EmpCargo]:
        return self.repository.listar(skip, limit)


class UpdateEmpCargoUseCase(UpdateEmpCargoInputPort):
    def __init__(self, repository: EmpCargoRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_empleado: int, id_cargo: int, fecha_inicio: str, fecha_termina: str, id_registro_modificacion: int) -> EmpCargo:
        from datetime import datetime
        existente = self.repository.obtener_por_id(id_empleado, id_cargo)
        if not existente:
            raise RecursoNoEncontradoException(f"EmpCargo {id_empleado}-{id_cargo} no encontrado.")
        existente.fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
        existente.fecha_termina = datetime.strptime(fecha_termina, "%Y-%m-%d").date()
        existente.id_registro_modificacion = id_registro_modificacion
        actualizado = self.repository.actualizar(existente)
        return actualizado


class DeleteEmpCargoUseCase(DeleteEmpCargoInputPort):
    def __init__(self, repository: EmpCargoRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_empleado: int, id_cargo: int) -> None:
        existente = self.repository.obtener_por_id(id_empleado, id_cargo)
        if not existente:
            raise RecursoNoEncontradoException(f"EmpCargo {id_empleado}-{id_cargo} no encontrado.")
        self.repository.eliminar(id_empleado, id_cargo)