from typing import List
from datetime import date
from src.domain.entities.archivo import Archivo
from src.domain.ports.input.archivo import (
    CreateArchivoInputPort,
    GetArchivoInputPort,
    ListArchivoInputPort,
    UpdateArchivoInputPort,
    DeleteArchivoInputPort,
)
from src.domain.ports.output.archivo import ArchivoRepositoryPort
from src.domain.exceptions.crud_exceptions import RecursoNoEncontradoException


class CreateArchivoUseCase(CreateArchivoInputPort):
    def __init__(self, repository: ArchivoRepositoryPort):
        self.repository = repository

    def ejecutar(
        self,
        doi: str,
        descripcion: str,
        url_archivo: str,
        nombre_original: str,
        id_elaborador: int,
        fecha_registro: date,
    ) -> Archivo:
        entity = Archivo(
            id_archivo=0,
            doi=doi,
            descripcion=descripcion,
            url_archivo=url_archivo,
            nombre_original=nombre_original,
            id_elaborador=id_elaborador,
            fecha_registro=fecha_registro,
        )
        return self.repository.crear(entity)


class GetArchivoUseCase(GetArchivoInputPort):
    def __init__(self, repository: ArchivoRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_archivo: int) -> Archivo:
        resultado = self.repository.obtener_por_id(id_archivo)
        if not resultado:
            raise RecursoNoEncontradoException(f"Archivo {id_archivo} no encontrado.")
        return resultado


class ListArchivoUseCase(ListArchivoInputPort):
    def __init__(self, repository: ArchivoRepositoryPort):
        self.repository = repository

    def ejecutar(self, skip: int = 0, limit: int = 50) -> List[Archivo]:
        return self.repository.listar(skip, limit)


class UpdateArchivoUseCase(UpdateArchivoInputPort):
    def __init__(self, repository: ArchivoRepositoryPort):
        self.repository = repository

    def ejecutar(
        self,
        id_archivo: int,
        doi: str,
        descripcion: str,
        url_archivo: str,
        nombre_original: str,
        id_elaborador: int,
        fecha_registro: date,
    ) -> Archivo:
        existente = self.repository.obtener_por_id(id_archivo)
        if not existente:
            raise RecursoNoEncontradoException(f"Archivo {id_archivo} no encontrado.")
        existente.doi = doi
        existente.descripcion = descripcion
        existente.url_archivo = url_archivo
        existente.nombre_original = nombre_original
        existente.id_elaborador = id_elaborador
        existente.fecha_registro = fecha_registro
        return self.repository.actualizar(existente)


class DeleteArchivoUseCase(DeleteArchivoInputPort):
    def __init__(self, repository: ArchivoRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_archivo: int) -> None:
        existente = self.repository.obtener_por_id(id_archivo)
        if not existente:
            raise RecursoNoEncontradoException(f"Archivo {id_archivo} no encontrado.")
        self.repository.eliminar(id_archivo)
