from typing import List
from src.domain.entities.empleado import Empleado
from src.domain.ports.input.empleado import ListEmpleadoInputPort
from src.domain.ports.output.empleado import EmpleadoRepositoryPort


class ListEmpleadoUseCase(ListEmpleadoInputPort):
    def __init__(self, repository: EmpleadoRepositoryPort):
        self.repository = repository

    def ejecutar(self, skip: int = 0, limit: int = 50, nombre: str = None) -> List[Empleado]:
        return self.repository.listar(skip, limit, nombre)