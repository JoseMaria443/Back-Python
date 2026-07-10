from src.domain.entities.empleado import Empleado
from src.domain.ports.input.empleado import GetEmpleadoInputPort
from src.domain.ports.output.empleado import EmpleadoRepositoryPort
from src.domain.exceptions.crud_exceptions import RecursoNoEncontradoException


class GetEmpleadoUseCase(GetEmpleadoInputPort):
    def __init__(self, repository: EmpleadoRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_empleado: int) -> Empleado:
        resultado = self.repository.obtener_por_id(id_empleado)
        if not resultado:
            raise RecursoNoEncontradoException(f"Empleado {id_empleado} no encontrado.")
        return resultado