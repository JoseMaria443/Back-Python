from datetime import date

from src.domain.entities.emp_cargo import EmpCargo
from src.domain.ports.input.emp_cargo import (
    AsociarEmpCargoInputPort,
    DesasociarEmpCargoInputPort,
)
from src.domain.ports.output.emp_cargo import EmpCargoRepositoryPort
from src.domain.exceptions.crud_exceptions import RecursoNoEncontradoException
from src.domain.exceptions.crud_exceptions import AsociacionYaExisteException
from src.domain.ports.output.empleado import EmpleadoRepositoryPort


class AsociarEmpCargoUseCase(AsociarEmpCargoInputPort):
    def __init__(
        self,
        repository: EmpCargoRepositoryPort,
        empleado_repository: EmpleadoRepositoryPort,
    ):
        self.repository = repository
        self.empleado_repository = empleado_repository

    def ejecutar(
        self,
        id_empleado: int,
        id_cargo: int,
        fecha_inicio: date,
        fecha_termina: date,
        id_registro_modificacion: int,
    ) -> EmpCargo:
        empleado = self.empleado_repository.obtener_por_id(id_empleado)
        if not empleado:
            raise RecursoNoEncontradoException(f"Empleado {id_empleado} no encontrado.")

        existente = self.repository.obtener_por_id(id_empleado, id_cargo)
        if existente:
            raise AsociacionYaExisteException(
                f"La asociación empleado-cargo {id_empleado}-{id_cargo} ya existe."
            )

        emp_cargo = EmpCargo(
            id_empleado=id_empleado,
            id_cargo=id_cargo,
            fecha_inicio=fecha_inicio,
            fecha_termina=fecha_termina,
            id_registro_modificacion=id_registro_modificacion,
        )
        return self.repository.crear(emp_cargo)


class DesasociarEmpCargoUseCase(DesasociarEmpCargoInputPort):
    def __init__(self, repository: EmpCargoRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_empleado: int, id_cargo: int) -> None:
        existente = self.repository.obtener_por_id(id_empleado, id_cargo)
        if not existente:
            raise RecursoNoEncontradoException(f"EmpCargo {id_empleado}-{id_cargo} no encontrado.")
        self.repository.eliminar(id_empleado, id_cargo)