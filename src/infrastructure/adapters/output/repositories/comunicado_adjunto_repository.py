from typing import Optional
from sqlalchemy.orm import Session
from src.domain.entities.comunicado_adjunto import ComunicadoAdjunto
from src.domain.ports.output.comunicado_adjunto import ComunicadoAdjuntoRepositoryPort
from src.infrastructure.adapters.output.persistence.comunicado_adjunto import ComunicadoAdjuntoORM


class ComunicadoAdjuntoRepository(ComunicadoAdjuntoRepositoryPort):

    def __init__(self, session: Session):
        self.session = session

    def crear(self, asociacion: ComunicadoAdjunto) -> ComunicadoAdjunto:
        orm = ComunicadoAdjuntoORM(
            id_comunicado=asociacion.id_comunicado,
            id_archivo=asociacion.id_archivo,
        )
        self.session.add(orm)
        self.session.commit()
        return asociacion

    def obtener(self, id_comunicado: int, id_archivo: int) -> Optional[ComunicadoAdjunto]:
        orm = self.session.query(ComunicadoAdjuntoORM).filter(
            ComunicadoAdjuntoORM.id_comunicado == id_comunicado,
            ComunicadoAdjuntoORM.id_archivo == id_archivo,
        ).first()
        if not orm:
            return None
        return ComunicadoAdjunto(id_comunicado=orm.id_comunicado, id_archivo=orm.id_archivo)

    def eliminar(self, id_comunicado: int, id_archivo: int) -> bool:
        orm = self.session.query(ComunicadoAdjuntoORM).filter(
            ComunicadoAdjuntoORM.id_comunicado == id_comunicado,
            ComunicadoAdjuntoORM.id_archivo == id_archivo,
        ).first()
        if not orm:
            return False
        self.session.delete(orm)
        self.session.commit()
        return True
