from typing import List, Optional
from datetime import date
from src.domain.entities.tarea import Tarea
from src.domain.ports.input.tarea import (
    CreateTareaInputPort,
    GetTareaInputPort,
    ListTareaInputPort,
    UpdateTareaInputPort,
    DeleteTareaInputPort,
)
from src.domain.ports.output.tarea import TareaRepositoryPort
from src.domain.exceptions.crud_exceptions import RecursoNoEncontradoException


class CreateTareaUseCase(CreateTareaInputPort):
    def __init__(self, repository: TareaRepositoryPort):
        self.repository = repository

    def ejecutar(
        self,
        id_comunicado: int,
        descripcion: str,
        fecha_entrega: date,
        fecha_registro: date,
        id_estado_tarea: Optional[int],
    ) -> Tarea:
        entity = Tarea(
            id_tarea=0,
            id_comunicado=id_comunicado,
            descripcion=descripcion,
            fecha_entrega=fecha_entrega,
            fecha_registro=fecha_registro,
            id_estado_tarea=id_estado_tarea,
        )
        return self.repository.crear(entity)


class GetTareaUseCase(GetTareaInputPort):
    def __init__(self, repository: TareaRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_tarea: int) -> Tarea:
        resultado = self.repository.obtener_por_id(id_tarea)
        if not resultado:
            raise RecursoNoEncontradoException(f"Tarea {id_tarea} no encontrada.")
        return resultado


class ListTareaUseCase(ListTareaInputPort):
    def __init__(self, repository: TareaRepositoryPort):
        self.repository = repository

    def ejecutar(self, skip: int = 0, limit: int = 50) -> List[Tarea]:
        return self.repository.listar(skip, limit)


class UpdateTareaUseCase(UpdateTareaInputPort):
    def __init__(self, repository: TareaRepositoryPort):
        self.repository = repository

    def ejecutar(
        self,
        id_tarea: int,
        id_comunicado: int,
        descripcion: str,
        fecha_entrega: date,
        fecha_registro: date,
        id_estado_tarea: Optional[int],
    ) -> Tarea:
        existente = self.repository.obtener_por_id(id_tarea)
        if not existente:
            raise RecursoNoEncontradoException(f"Tarea {id_tarea} no encontrada.")
        existente.id_comunicado = id_comunicado
        existente.descripcion = descripcion
        existente.fecha_entrega = fecha_entrega
        existente.fecha_registro = fecha_registro
        existente.id_estado_tarea = id_estado_tarea
        return self.repository.actualizar(existente)


class DeleteTareaUseCase(DeleteTareaInputPort):
    def __init__(self, repository: TareaRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_tarea: int) -> None:
        existente = self.repository.obtener_por_id(id_tarea)
        if not existente:
            raise RecursoNoEncontradoException(f"Tarea {id_tarea} no encontrada.")
        self.repository.eliminar(id_tarea)
