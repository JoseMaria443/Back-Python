from src.domain.entities.tarea_archivo import TareaArchivo
from src.domain.ports.input.tarea_archivo import (
    AsociarTareaArchivoInputPort,
    DesasociarTareaArchivoInputPort,
)
from src.domain.ports.output.tarea_archivo import TareaArchivoRepositoryPort
from src.domain.ports.output.tarea import TareaRepositoryPort
from src.domain.ports.output.archivo import ArchivoRepositoryPort
from src.domain.exceptions.crud_exceptions import (
    RecursoNoEncontradoException,
    AsociacionYaExisteException,
)


class AsociarTareaArchivoUseCase(AsociarTareaArchivoInputPort):
    def __init__(
        self,
        repository: TareaArchivoRepositoryPort,
        tarea_repository: TareaRepositoryPort,
        archivo_repository: ArchivoRepositoryPort,
    ):
        self.repository = repository
        self.tarea_repository = tarea_repository
        self.archivo_repository = archivo_repository

    def ejecutar(self, id_tarea: int, id_archivo: int) -> TareaArchivo:
        if not self.tarea_repository.obtener_por_id(id_tarea):
            raise RecursoNoEncontradoException(f"Tarea {id_tarea} no encontrada.")
        if not self.archivo_repository.obtener_por_id(id_archivo):
            raise RecursoNoEncontradoException(f"Archivo {id_archivo} no encontrado.")
        if self.repository.obtener(id_tarea, id_archivo):
            raise AsociacionYaExisteException(
                f"Archivo {id_archivo} ya asociado a la tarea {id_tarea}."
            )
        asociacion = TareaArchivo(id_tarea=id_tarea, id_archivo=id_archivo)
        return self.repository.crear(asociacion)


class DesasociarTareaArchivoUseCase(DesasociarTareaArchivoInputPort):
    def __init__(self, repository: TareaArchivoRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_tarea: int, id_archivo: int) -> None:
        if not self.repository.obtener(id_tarea, id_archivo):
            raise RecursoNoEncontradoException(
                f"Asociacion tarea {id_tarea} - archivo {id_archivo} no encontrada."
            )
        self.repository.eliminar(id_tarea, id_archivo)
