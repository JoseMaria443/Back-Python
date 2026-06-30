from src.domain.entities.tarea_responsable import TareaResponsable
from src.domain.ports.input.tarea_responsable import (
    AsociarTareaResponsableInputPort,
    DesasociarTareaResponsableInputPort,
)
from src.domain.ports.output.tarea_responsable import TareaResponsableRepositoryPort
from src.domain.ports.output.tarea import TareaRepositoryPort
from src.domain.ports.output.empleado import EmpleadoRepositoryPort
from src.domain.exceptions.crud_exceptions import (
    RecursoNoEncontradoException,
    AsociacionYaExisteException,
)


class AsociarTareaResponsableUseCase(AsociarTareaResponsableInputPort):
    def __init__(
        self,
        repository: TareaResponsableRepositoryPort,
        tarea_repository: TareaRepositoryPort,
        empleado_repository: EmpleadoRepositoryPort,
    ):
        self.repository = repository
        self.tarea_repository = tarea_repository
        self.empleado_repository = empleado_repository

    def ejecutar(self, id_tarea: int, id_responsable: int, id_rol: int) -> TareaResponsable:
        if not self.tarea_repository.obtener_por_id(id_tarea):
            raise RecursoNoEncontradoException(f"Tarea {id_tarea} no encontrada.")
        if not self.empleado_repository.obtener_por_id(id_responsable):
            raise RecursoNoEncontradoException(f"Empleado {id_responsable} no encontrado.")
        if self.repository.obtener(id_tarea, id_responsable):
            raise AsociacionYaExisteException(
                f"Responsable {id_responsable} ya asociado a la tarea {id_tarea}."
            )
        asociacion = TareaResponsable(
            id_tarea=id_tarea,
            id_responsable=id_responsable,
            id_rol=id_rol,
        )
        return self.repository.crear(asociacion)


class DesasociarTareaResponsableUseCase(DesasociarTareaResponsableInputPort):
    def __init__(self, repository: TareaResponsableRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_tarea: int, id_responsable: int) -> None:
        if not self.repository.obtener(id_tarea, id_responsable):
            raise RecursoNoEncontradoException(
                f"Asociacion tarea {id_tarea} - responsable {id_responsable} no encontrada."
            )
        self.repository.eliminar(id_tarea, id_responsable)
