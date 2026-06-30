from typing import List
from src.domain.entities.tipo_catalogo import TipoCatalogo
from src.domain.ports.input.tipo_catalogo import (
    CreateTipoCatalogoInputPort,
    GetTipoCatalogoInputPort,
    ListTipoCatalogoInputPort,
    UpdateTipoCatalogoInputPort,
    DeleteTipoCatalogoInputPort,
)
from src.domain.ports.output.tipo_catalogo import TipoCatalogoRepositoryPort
from src.domain.exceptions.crud_exceptions import RecursoNoEncontradoException


class CreateTipoCatalogoUseCase(CreateTipoCatalogoInputPort):
    def __init__(self, repository: TipoCatalogoRepositoryPort):
        self.repository = repository

    def ejecutar(self, nombre_tipo_catalogo: str) -> TipoCatalogo:
        tipo_catalogo = TipoCatalogo(id_tipo_catalogo=0, nombre_tipo_catalogo=nombre_tipo_catalogo)
        return self.repository.crear(tipo_catalogo)


class GetTipoCatalogoUseCase(GetTipoCatalogoInputPort):
    def __init__(self, repository: TipoCatalogoRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_tipo_catalogo: int) -> TipoCatalogo:
        resultado = self.repository.obtener_por_id(id_tipo_catalogo)
        if not resultado:
            raise RecursoNoEncontradoException(f"TipoCatalogo {id_tipo_catalogo} no encontrado.")
        return resultado


class ListTipoCatalogoUseCase(ListTipoCatalogoInputPort):
    def __init__(self, repository: TipoCatalogoRepositoryPort):
        self.repository = repository

    def ejecutar(self, skip: int = 0, limit: int = 50) -> List[TipoCatalogo]:
        return self.repository.listar(skip, limit)


class UpdateTipoCatalogoUseCase(UpdateTipoCatalogoInputPort):
    def __init__(self, repository: TipoCatalogoRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_tipo_catalogo: int, nombre_tipo_catalogo: str) -> TipoCatalogo:
        existente = self.repository.obtener_por_id(id_tipo_catalogo)
        if not existente:
            raise RecursoNoEncontradoException(f"TipoCatalogo {id_tipo_catalogo} no encontrado.")
        existente.nombre_tipo_catalogo = nombre_tipo_catalogo
        actualizado = self.repository.actualizar(existente)
        return actualizado


class DeleteTipoCatalogoUseCase(DeleteTipoCatalogoInputPort):
    def __init__(self, repository: TipoCatalogoRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_tipo_catalogo: int) -> None:
        existente = self.repository.obtener_por_id(id_tipo_catalogo)
        if not existente:
            raise RecursoNoEncontradoException(f"TipoCatalogo {id_tipo_catalogo} no encontrado.")
        self.repository.eliminar(id_tipo_catalogo)