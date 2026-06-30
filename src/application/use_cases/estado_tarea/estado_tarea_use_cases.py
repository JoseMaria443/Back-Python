from typing import List
from src.domain.entities.estado_tarea import EstadoTarea
from src.domain.ports.input.estado_tarea import (
    CreateEstadoTareaInputPort,
    GetEstadoTareaInputPort,
    ListEstadoTareaInputPort,
    UpdateEstadoTareaInputPort,
    DeleteEstadoTareaInputPort,
)
from src.domain.ports.output.estado_tarea import EstadoTareaRepositoryPort
from src.domain.exceptions.crud_exceptions import RecursoNoEncontradoException


class CreateEstadoTareaUseCase(CreateEstadoTareaInputPort):
    def __init__(self, repository: EstadoTareaRepositoryPort):
        self.repository = repository

    def ejecutar(self, nombre_estado: str) -> EstadoTarea:
        entity = EstadoTarea(id_estado_tarea=0, nombre_estado=nombre_estado)
        return self.repository.crear(entity)


class GetEstadoTareaUseCase(GetEstadoTareaInputPort):
    def __init__(self, repository: EstadoTareaRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_estado_tarea: int) -> EstadoTarea:
        resultado = self.repository.obtener_por_id(id_estado_tarea)
        if not resultado:
            raise RecursoNoEncontradoException(f"EstadoTarea {id_estado_tarea} no encontrado.")
        return resultado


class ListEstadoTareaUseCase(ListEstadoTareaInputPort):
    def __init__(self, repository: EstadoTareaRepositoryPort):
        self.repository = repository

    def ejecutar(self, skip: int = 0, limit: int = 50) -> List[EstadoTarea]:
        return self.repository.listar(skip, limit)


class UpdateEstadoTareaUseCase(UpdateEstadoTareaInputPort):
    def __init__(self, repository: EstadoTareaRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_estado_tarea: int, nombre_estado: str) -> EstadoTarea:
        existente = self.repository.obtener_por_id(id_estado_tarea)
        if not existente:
            raise RecursoNoEncontradoException(f"EstadoTarea {id_estado_tarea} no encontrado.")
        existente.nombre_estado = nombre_estado
        return self.repository.actualizar(existente)


class DeleteEstadoTareaUseCase(DeleteEstadoTareaInputPort):
    def __init__(self, repository: EstadoTareaRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_estado_tarea: int) -> None:
        existente = self.repository.obtener_por_id(id_estado_tarea)
        if not existente:
            raise RecursoNoEncontradoException(f"EstadoTarea {id_estado_tarea} no encontrado.")
        self.repository.eliminar(id_estado_tarea)
