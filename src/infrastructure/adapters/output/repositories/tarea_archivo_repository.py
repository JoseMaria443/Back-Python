from typing import Optional
from sqlalchemy.orm import Session
from src.domain.entities.tarea_archivo import TareaArchivo
from src.domain.ports.output.tarea_archivo import TareaArchivoRepositoryPort
from src.infrastructure.adapters.output.persistence.tarea_archivo import TareaArchivoORM


class TareaArchivoRepository(TareaArchivoRepositoryPort):

    def __init__(self, session: Session):
        self.session = session

    def crear(self, asociacion: TareaArchivo) -> TareaArchivo:
        orm = TareaArchivoORM(
            id_tarea=asociacion.id_tarea,
            id_archivo=asociacion.id_archivo,
        )
        self.session.add(orm)
        self.session.commit()
        return asociacion

    def obtener(self, id_tarea: int, id_archivo: int) -> Optional[TareaArchivo]:
        orm = self.session.query(TareaArchivoORM).filter(
            TareaArchivoORM.id_tarea == id_tarea,
            TareaArchivoORM.id_archivo == id_archivo,
        ).first()
        if not orm:
            return None
        return TareaArchivo(id_tarea=orm.id_tarea, id_archivo=orm.id_archivo)

    def eliminar(self, id_tarea: int, id_archivo: int) -> bool:
        orm = self.session.query(TareaArchivoORM).filter(
            TareaArchivoORM.id_tarea == id_tarea,
            TareaArchivoORM.id_archivo == id_archivo,
        ).first()
        if not orm:
            return False
        self.session.delete(orm)
        self.session.commit()
        return True
