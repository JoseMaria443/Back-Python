from src.domain.entities.comunicado_destinatario import ComunicadoDestinatario
from src.domain.ports.input.comunicado_destinatario import (
    AsociarComunicadoDestinatarioInputPort,
    DesasociarComunicadoDestinatarioInputPort,
)
from src.domain.ports.output.comunicado_destinatario import ComunicadoDestinatarioRepositoryPort
from src.domain.ports.output.comunicado import ComunicadoRepositoryPort
from src.domain.exceptions.crud_exceptions import (
    RecursoNoEncontradoException,
    AsociacionYaExisteException,
)


class AsociarComunicadoDestinatarioUseCase(AsociarComunicadoDestinatarioInputPort):
    def __init__(
        self,
        repository: ComunicadoDestinatarioRepositoryPort,
        comunicado_repository: ComunicadoRepositoryPort,
    ):
        self.repository = repository
        self.comunicado_repository = comunicado_repository

    def ejecutar(
        self,
        id_comunicado: int,
        id_destinatario: int,
        id_rol_destinatario: int,
    ) -> ComunicadoDestinatario:
        if not self.comunicado_repository.obtener_por_id(id_comunicado):
            raise RecursoNoEncontradoException(f"Comunicado {id_comunicado} no encontrado.")
        if self.repository.obtener(id_comunicado, id_destinatario):
            raise AsociacionYaExisteException(
                f"Destinatario {id_destinatario} ya asociado al comunicado {id_comunicado}."
            )
        asociacion = ComunicadoDestinatario(
            id_comunicado=id_comunicado,
            id_destinatario=id_destinatario,
            id_rol_destinatario=id_rol_destinatario,
        )
        return self.repository.crear(asociacion)


class DesasociarComunicadoDestinatarioUseCase(DesasociarComunicadoDestinatarioInputPort):
    def __init__(self, repository: ComunicadoDestinatarioRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_comunicado: int, id_destinatario: int) -> None:
        if not self.repository.obtener(id_comunicado, id_destinatario):
            raise RecursoNoEncontradoException(
                f"Asociacion comunicado {id_comunicado} - destinatario {id_destinatario} no encontrada."
            )
        self.repository.eliminar(id_comunicado, id_destinatario)
