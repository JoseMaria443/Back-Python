from src.domain.entities.comunicado_adjunto import ComunicadoAdjunto
from src.domain.ports.input.comunicado_adjunto import (
    AsociarComunicadoAdjuntoInputPort,
    DesasociarComunicadoAdjuntoInputPort,
)
from src.domain.ports.output.comunicado_adjunto import ComunicadoAdjuntoRepositoryPort
from src.domain.ports.output.comunicado import ComunicadoRepositoryPort
from src.domain.ports.output.archivo import ArchivoRepositoryPort
from src.domain.exceptions.crud_exceptions import (
    RecursoNoEncontradoException,
    AsociacionYaExisteException,
)


class AsociarComunicadoAdjuntoUseCase(AsociarComunicadoAdjuntoInputPort):
    def __init__(
        self,
        repository: ComunicadoAdjuntoRepositoryPort,
        comunicado_repository: ComunicadoRepositoryPort,
        archivo_repository: ArchivoRepositoryPort,
    ):
        self.repository = repository
        self.comunicado_repository = comunicado_repository
        self.archivo_repository = archivo_repository

    def ejecutar(self, id_comunicado: int, id_archivo: int) -> ComunicadoAdjunto:
        if not self.comunicado_repository.obtener_por_id(id_comunicado):
            raise RecursoNoEncontradoException(f"Comunicado {id_comunicado} no encontrado.")
        if not self.archivo_repository.obtener_por_id(id_archivo):
            raise RecursoNoEncontradoException(f"Archivo {id_archivo} no encontrado.")
        if self.repository.obtener(id_comunicado, id_archivo):
            raise AsociacionYaExisteException(
                f"Archivo {id_archivo} ya asociado al comunicado {id_comunicado}."
            )
        asociacion = ComunicadoAdjunto(id_comunicado=id_comunicado, id_archivo=id_archivo)
        return self.repository.crear(asociacion)


class DesasociarComunicadoAdjuntoUseCase(DesasociarComunicadoAdjuntoInputPort):
    def __init__(self, repository: ComunicadoAdjuntoRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_comunicado: int, id_archivo: int) -> None:
        if not self.repository.obtener(id_comunicado, id_archivo):
            raise RecursoNoEncontradoException(
                f"Asociacion comunicado {id_comunicado} - archivo {id_archivo} no encontrada."
            )
        self.repository.eliminar(id_comunicado, id_archivo)
