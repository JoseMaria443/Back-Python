from typing import List
from src.domain.entities.historial_estado_empleado import HistorialEstadoEmpleado
from src.domain.ports.input.historial_estado_empleado import ListHistorialEstadoEmpleadoInputPort
from src.domain.ports.output.historial_estado_empleado import HistorialEstadoEmpleadoRepositoryPort


class ListHistorialEstadoEmpleadoUseCase(ListHistorialEstadoEmpleadoInputPort):
    def __init__(self, repository: HistorialEstadoEmpleadoRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_empleado: int, skip: int = 0, limit: int = 50) -> List[HistorialEstadoEmpleado]:
        return self.repository.listar(id_empleado, skip, limit)