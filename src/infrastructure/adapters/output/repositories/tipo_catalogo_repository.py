from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.entities.tipo_catalogo import TipoCatalogo
from src.domain.ports.output.tipo_catalogo import TipoCatalogoRepositoryPort
from src.infrastructure.adapters.output.persistence.tipo_catalogo import TipoCatalogoORM


class TipoCatalogoRepository(TipoCatalogoRepositoryPort):

    def __init__(self, session: Session):
        self.session = session

    def crear(self, tipo_catalogo: TipoCatalogo) -> TipoCatalogo:
        orm = TipoCatalogoORM(nombre_tipo_catalogo=tipo_catalogo.nombre_tipo_catalogo)
        self.session.add(orm)
        self.session.commit()
        self.session.refresh(orm)
        return self._orm_a_dominio(orm)

    def obtener_por_id(self, id_tipo_catalogo: int) -> Optional[TipoCatalogo]:
        orm = self.session.query(TipoCatalogoORM).filter(
            TipoCatalogoORM.id_tipo_catalogo == id_tipo_catalogo
        ).first()
        if not orm:
            return None
        return self._orm_a_dominio(orm)

    def listar(self, skip: int, limit: int) -> List[TipoCatalogo]:
        orms = self.session.query(TipoCatalogoORM).offset(skip).limit(limit).all()
        return [self._orm_a_dominio(orm) for orm in orms]

    def contar(self) -> int:
        return self.session.query(TipoCatalogoORM).count()

    def actualizar(self, tipo_catalogo: TipoCatalogo) -> Optional[TipoCatalogo]:
        orm = self.session.query(TipoCatalogoORM).filter(
            TipoCatalogoORM.id_tipo_catalogo == tipo_catalogo.id_tipo_catalogo
        ).first()
        if not orm:
            return None
        orm.nombre_tipo_catalogo = tipo_catalogo.nombre_tipo_catalogo
        self.session.commit()
        self.session.refresh(orm)
        return self._orm_a_dominio(orm)

    def eliminar(self, id_tipo_catalogo: int) -> bool:
        orm = self.session.query(TipoCatalogoORM).filter(
            TipoCatalogoORM.id_tipo_catalogo == id_tipo_catalogo
        ).first()
        if not orm:
            return False
        self.session.delete(orm)
        self.session.commit()
        return True

    def _orm_a_dominio(self, orm: TipoCatalogoORM) -> TipoCatalogo:
        return TipoCatalogo(
            id_tipo_catalogo=orm.id_tipo_catalogo,
            nombre_tipo_catalogo=orm.nombre_tipo_catalogo,
        )
