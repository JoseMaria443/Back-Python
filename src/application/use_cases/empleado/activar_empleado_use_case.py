from src.domain.entities.empleado import Empleado
from src.domain.entities.historial_estado_empleado import HistorialEstadoEmpleado
from src.domain.ports.input.empleado import ActivarEmpleadoInputPort
from src.domain.ports.output.empleado import EmpleadoRepositoryPort
from src.domain.ports.output.historial_estado_empleado import HistorialEstadoEmpleadoRepositoryPort
from src.domain.exceptions.crud_exceptions import RecursoNoEncontradoException


class ActivarEmpleadoUseCase(ActivarEmpleadoInputPort):
    def __init__(self, empleado_repository: EmpleadoRepositoryPort, historial_repository: HistorialEstadoEmpleadoRepositoryPort):
        self.empleado_repository = empleado_repository
        self.historial_repository = historial_repository

    def ejecutar(self, id_empleado: int, id_empleado_ejecutor: int) -> Empleado:
        empleado = self.empleado_repository.obtener_por_id(id_empleado)
        if not empleado:
            raise RecursoNoEncontradoException(f"Empleado {id_empleado} no encontrado.")
        empleado.activo = True
        empleado_actualizado = self.empleado_repository.actualizar(empleado)
        
        # Registrar historial
        self.historial_repository.crear(
            HistorialEstadoEmpleado.crear(
                id_empleado=id_empleado,
                accion="activacion",
                id_empleado_ejecutor=id_empleado_ejecutor,
            )
        )
        
        return empleado_actualizado
