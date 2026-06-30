from typing import List
from src.domain.entities.catalogo import Catalogo
from src.domain.ports.input.catalogo import (
    CreateCatalogoInputPort,
    GetCatalogoInputPort,
    ListCatalogoInputPort,
    UpdateCatalogoInputPort,
    DeleteCatalogoInputPort,
)
from src.domain.ports.output.catalogo import CatalogoRepositoryPort
from src.domain.exceptions.crud_exceptions import RecursoNoEncontradoException


class CreateCatalogoUseCase(CreateCatalogoInputPort):
    def __init__(self, repository: CatalogoRepositoryPort):
        self.repository = repository

    def ejecutar(self, nombre_catalogo: str, id_tipo_catalogo: int, descripcion: str = None) -> Catalogo:
        catalogo = Catalogo(
            id_catalogo=0,
            nombre_catalogo=nombre_catalogo,
            id_tipo_catalogo=id_tipo_catalogo,
            descripcion=descripcion,
        )
        return self.repository.crear(catalogo)


class GetCatalogoUseCase(GetCatalogoInputPort):
    def __init__(self, repository: CatalogoRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_catalogo: int) -> Catalogo:
        resultado = self.repository.obtener_por_id(id_catalogo)
        if not resultado:
            raise RecursoNoEncontradoException(f"Catalogo {id_catalogo} no encontrado.")
        return resultado


class ListCatalogoUseCase(ListCatalogoInputPort):
    def __init__(self, repository: CatalogoRepositoryPort):
        self.repository = repository

    def ejecutar(self, skip: int = 0, limit: int = 50) -> List[Catalogo]:
        return self.repository.listar(skip, limit)


class UpdateCatalogoUseCase(UpdateCatalogoInputPort):
    def __init__(self, repository: CatalogoRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_catalogo: int, nombre_catalogo: str, descripcion: str = None) -> Catalogo:
        existente = self.repository.obtener_por_id(id_catalogo)
        if not existente:
            raise RecursoNoEncontradoException(f"Catalogo {id_catalogo} no encontrado.")
        existente.nombre_catalogo = nombre_catalogo
        existente.descripcion = descripcion
        actualizado = self.repository.actualizar(existente)
        return actualizado


class DeleteCatalogoUseCase(DeleteCatalogoInputPort):
    def __init__(self, repository: CatalogoRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_catalogo: int) -> None:
        existente = self.repository.obtener_por_id(id_catalogo)
        if not existente:
            raise RecursoNoEncontradoException(f"Catalogo {id_catalogo} no encontrado.")
        self.repository.eliminar(id_catalogo)