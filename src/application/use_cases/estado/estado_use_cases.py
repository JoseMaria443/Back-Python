from typing import List
from src.domain.entities.estado import Estado
from src.domain.ports.input.estado import (
    CreateEstadoInputPort,
    GetEstadoInputPort,
    ListEstadoInputPort,
    UpdateEstadoInputPort,
    DeleteEstadoInputPort,
)
from src.domain.ports.output.estado import EstadoRepositoryPort
from src.domain.exceptions.crud_exceptions import RecursoNoEncontradoException


class CreateEstadoUseCase(CreateEstadoInputPort):
    def __init__(self, repository: EstadoRepositoryPort):
        self.repository = repository

    def ejecutar(self, nombre_estado: str) -> Estado:
        estado = Estado(
            id_estado=0,
            nombre_estado=nombre_estado,
        )
        return self.repository.crear(estado)


class GetEstadoUseCase(GetEstadoInputPort):
    def __init__(self, repository: EstadoRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_estado: int) -> Estado:
        resultado = self.repository.obtener_por_id(id_estado)
        if not resultado:
            raise RecursoNoEncontradoException(f"Estado {id_estado} no encontrado.")
        return resultado


class ListEstadoUseCase(ListEstadoInputPort):
    def __init__(self, repository: EstadoRepositoryPort):
        self.repository = repository

    def ejecutar(self, skip: int = 0, limit: int = 50) -> List[Estado]:
        return self.repository.listar(skip, limit)


class UpdateEstadoUseCase(UpdateEstadoInputPort):
    def __init__(self, repository: EstadoRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_estado: int, nombre_estado: str) -> Estado:
        existente = self.repository.obtener_por_id(id_estado)
        if not existente:
            raise RecursoNoEncontradoException(f"Estado {id_estado} no encontrado.")
        existente.nombre_estado = nombre_estado
        actualizado = self.repository.actualizar(existente)
        return actualizado


class DeleteEstadoUseCase(DeleteEstadoInputPort):
    def __init__(self, repository: EstadoRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_estado: int) -> None:
        existente = self.repository.obtener_por_id(id_estado)
        if not existente:
            raise RecursoNoEncontradoException(f"Estado {id_estado} no encontrado.")
        self.repository.eliminar(id_estado)