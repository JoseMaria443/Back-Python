from typing import List, Optional
from datetime import date
from src.domain.entities.comunicado import Comunicado
from src.domain.ports.input.comunicado import (
    CreateComunicadoInputPort,
    GetComunicadoInputPort,
    ListComunicadoInputPort,
    UpdateComunicadoInputPort,
    DeleteComunicadoInputPort,
)
from src.domain.ports.output.comunicado import ComunicadoRepositoryPort
from src.domain.exceptions.crud_exceptions import RecursoNoEncontradoException


class CreateComunicadoUseCase(CreateComunicadoInputPort):
    def __init__(self, repository: ComunicadoRepositoryPort):
        self.repository = repository

    def ejecutar(
        self,
        doi: str,
        num_comunicado: str,
        id_emisor: int,
        fecha_recepcion: date,
        id_destinatario: int,
        fecha_registro: date,
        id_registro: int,
        id_metodo_recepcion: int,
        tema: str,
        id_tipo_comunicado: int,
        observaciones: Optional[str],
    ) -> Comunicado:
        entity = Comunicado(
            id_comunicado=0,
            doi=doi,
            num_comunicado=num_comunicado,
            id_emisor=id_emisor,
            fecha_recepcion=fecha_recepcion,
            id_destinatario=id_destinatario,
            fecha_registro=fecha_registro,
            id_registro=id_registro,
            id_metodo_recepcion=id_metodo_recepcion,
            tema=tema,
            id_tipo_comunicado=id_tipo_comunicado,
            observaciones=observaciones,
        )
        return self.repository.crear(entity)


class GetComunicadoUseCase(GetComunicadoInputPort):
    def __init__(self, repository: ComunicadoRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_comunicado: int) -> Comunicado:
        resultado = self.repository.obtener_por_id(id_comunicado)
        if not resultado:
            raise RecursoNoEncontradoException(f"Comunicado {id_comunicado} no encontrado.")
        return resultado


class ListComunicadoUseCase(ListComunicadoInputPort):
    def __init__(self, repository: ComunicadoRepositoryPort):
        self.repository = repository

    def ejecutar(self, skip: int = 0, limit: int = 50) -> List[Comunicado]:
        return self.repository.listar(skip, limit)


class UpdateComunicadoUseCase(UpdateComunicadoInputPort):
    def __init__(self, repository: ComunicadoRepositoryPort):
        self.repository = repository

    def ejecutar(
        self,
        id_comunicado: int,
        doi: str,
        num_comunicado: str,
        id_emisor: int,
        fecha_recepcion: date,
        id_destinatario: int,
        fecha_registro: date,
        id_registro: int,
        id_metodo_recepcion: int,
        tema: str,
        id_tipo_comunicado: int,
        observaciones: Optional[str],
    ) -> Comunicado:
        existente = self.repository.obtener_por_id(id_comunicado)
        if not existente:
            raise RecursoNoEncontradoException(f"Comunicado {id_comunicado} no encontrado.")
        existente.doi = doi
        existente.num_comunicado = num_comunicado
        existente.id_emisor = id_emisor
        existente.fecha_recepcion = fecha_recepcion
        existente.id_destinatario = id_destinatario
        existente.fecha_registro = fecha_registro
        existente.id_registro = id_registro
        existente.id_metodo_recepcion = id_metodo_recepcion
        existente.tema = tema
        existente.id_tipo_comunicado = id_tipo_comunicado
        existente.observaciones = observaciones
        return self.repository.actualizar(existente)


class DeleteComunicadoUseCase(DeleteComunicadoInputPort):
    def __init__(self, repository: ComunicadoRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_comunicado: int) -> None:
        existente = self.repository.obtener_por_id(id_comunicado)
        if not existente:
            raise RecursoNoEncontradoException(f"Comunicado {id_comunicado} no encontrado.")
        self.repository.eliminar(id_comunicado)
