from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.entities.comunicado import Comunicado
from src.domain.ports.output.comunicado import ComunicadoRepositoryPort
from src.infrastructure.adapters.output.persistence.comunicado import ComunicadoORM


class ComunicadoRepository(ComunicadoRepositoryPort):

    def __init__(self, session: Session):
        self.session = session

    def crear(self, comunicado: Comunicado) -> Comunicado:
        orm = ComunicadoORM(
            doi=comunicado.doi,
            num_comunicado=comunicado.num_comunicado,
            id_emisor=comunicado.id_emisor,
            fecha_recepcion=comunicado.fecha_recepcion,
            id_destinatario=comunicado.id_destinatario,
            fecha_registro=comunicado.fecha_registro,
            id_registro=comunicado.id_registro,
            id_metodo_recepcion=comunicado.id_metodo_recepcion,
            tema=comunicado.tema,
            observaciones=comunicado.observaciones,
            id_tipo_comunicado=comunicado.id_tipo_comunicado,
        )
        self.session.add(orm)
        self.session.commit()
        self.session.refresh(orm)
        return self._orm_a_dominio(orm)

    def obtener_por_id(self, id_comunicado: int) -> Optional[Comunicado]:
        orm = self.session.query(ComunicadoORM).filter(
            ComunicadoORM.id_comunicado == id_comunicado
        ).first()
        if not orm:
            return None
        return self._orm_a_dominio(orm)

    def listar(self, skip: int, limit: int) -> List[Comunicado]:
        orms = self.session.query(ComunicadoORM).offset(skip).limit(limit).all()
        return [self._orm_a_dominio(orm) for orm in orms]

    def contar(self) -> int:
        return self.session.query(ComunicadoORM).count()

    def actualizar(self, comunicado: Comunicado) -> Optional[Comunicado]:
        orm = self.session.query(ComunicadoORM).filter(
            ComunicadoORM.id_comunicado == comunicado.id_comunicado
        ).first()
        if not orm:
            return None
        orm.doi = comunicado.doi
        orm.num_comunicado = comunicado.num_comunicado
        orm.id_emisor = comunicado.id_emisor
        orm.fecha_recepcion = comunicado.fecha_recepcion
        orm.id_destinatario = comunicado.id_destinatario
        orm.fecha_registro = comunicado.fecha_registro
        orm.id_registro = comunicado.id_registro
        orm.id_metodo_recepcion = comunicado.id_metodo_recepcion
        orm.tema = comunicado.tema
        orm.observaciones = comunicado.observaciones
        orm.id_tipo_comunicado = comunicado.id_tipo_comunicado
        self.session.commit()
        self.session.refresh(orm)
        return self._orm_a_dominio(orm)

    def eliminar(self, id_comunicado: int) -> bool:
        orm = self.session.query(ComunicadoORM).filter(
            ComunicadoORM.id_comunicado == id_comunicado
        ).first()
        if not orm:
            return False
        self.session.delete(orm)
        self.session.commit()
        return True

    def _orm_a_dominio(self, orm: ComunicadoORM) -> Comunicado:
        return Comunicado(
            id_comunicado=orm.id_comunicado,
            doi=orm.doi,
            num_comunicado=orm.num_comunicado,
            id_emisor=orm.id_emisor,
            fecha_recepcion=orm.fecha_recepcion,
            id_destinatario=orm.id_destinatario,
            fecha_registro=orm.fecha_registro,
            id_registro=orm.id_registro,
            id_metodo_recepcion=orm.id_metodo_recepcion,
            tema=orm.tema,
            id_tipo_comunicado=orm.id_tipo_comunicado,
            observaciones=orm.observaciones,
        )
