from typing import Optional
from sqlalchemy.orm import Session
from src.domain.entities.comunicado_destinatario import ComunicadoDestinatario
from src.domain.ports.output.comunicado_destinatario import ComunicadoDestinatarioRepositoryPort
from src.infrastructure.adapters.output.persistence.comunicado_destinatario import ComunicadoDestinatarioORM


class ComunicadoDestinatarioRepository(ComunicadoDestinatarioRepositoryPort):

    def __init__(self, session: Session):
        self.session = session

    def crear(self, asociacion: ComunicadoDestinatario) -> ComunicadoDestinatario:
        orm = ComunicadoDestinatarioORM(
            id_comunicado=asociacion.id_comunicado,
            id_destinatario=asociacion.id_destinatario,
            id_rol_destinatario=asociacion.id_rol_destinatario,
        )
        self.session.add(orm)
        self.session.commit()
        return asociacion

    def obtener(
        self, id_comunicado: int, id_destinatario: int
    ) -> Optional[ComunicadoDestinatario]:
        orm = self.session.query(ComunicadoDestinatarioORM).filter(
            ComunicadoDestinatarioORM.id_comunicado == id_comunicado,
            ComunicadoDestinatarioORM.id_destinatario == id_destinatario,
        ).first()
        if not orm:
            return None
        return ComunicadoDestinatario(
            id_comunicado=orm.id_comunicado,
            id_destinatario=orm.id_destinatario,
            id_rol_destinatario=orm.id_rol_destinatario,
        )

    def eliminar(self, id_comunicado: int, id_destinatario: int) -> bool:
        orm = self.session.query(ComunicadoDestinatarioORM).filter(
            ComunicadoDestinatarioORM.id_comunicado == id_comunicado,
            ComunicadoDestinatarioORM.id_destinatario == id_destinatario,
        ).first()
        if not orm:
            return False
        self.session.delete(orm)
        self.session.commit()
        return True
