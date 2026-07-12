from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.domain.entities.catalogo import Catalogo
from src.domain.ports.output.catalogo import CatalogoRepositoryPort
from src.infrastructure.adapters.output.persistence.catalogo import CatalogoORM
from src.domain.exceptions.crud_exceptions import RecursoEnUsoException


class CatalogoRepository(CatalogoRepositoryPort):

    def __init__(self, session: Session):
        self.session = session

    def crear(self, catalogo: Catalogo) -> Catalogo:
        orm = CatalogoORM(
            id_tipo_catalogo=catalogo.id_tipo_catalogo,
            descripcion=catalogo.descripcion,
        )
        self.session.add(orm)
        self.session.commit()
        self.session.refresh(orm)
        return self._orm_a_dominio(orm)

    def obtener_por_id(self, id_catalogo: int) -> Optional[Catalogo]:
        orm = self.session.query(CatalogoORM).filter(
            CatalogoORM.id_catalogo == id_catalogo
        ).first()
        if not orm:
            return None
        return self._orm_a_dominio(orm)

    def listar(self, skip: int, limit: int) -> List[Catalogo]:
        orms = self.session.query(CatalogoORM).offset(skip).limit(limit).all()
        return [self._orm_a_dominio(orm) for orm in orms]

    def contar(self) -> int:
        return self.session.query(CatalogoORM).count()

    def actualizar(self, catalogo: Catalogo) -> Optional[Catalogo]:
        orm = self.session.query(CatalogoORM).filter(
            CatalogoORM.id_catalogo == catalogo.id_catalogo
        ).first()
        if not orm:
            return None
        orm.id_tipo_catalogo = catalogo.id_tipo_catalogo
        orm.descripcion = catalogo.descripcion
        self.session.commit()
        self.session.refresh(orm)
        return self._orm_a_dominio(orm)

    def eliminar(self, id_catalogo: int) -> bool:
        orm = self.session.query(CatalogoORM).filter(
            CatalogoORM.id_catalogo == id_catalogo
        ).first()
        if not orm:
            return False
        self.session.delete(orm)
        try:
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise RecursoEnUsoException(
                "No se puede eliminar: el registro está en uso"
            )
        return True

    def _orm_a_dominio(self, orm: CatalogoORM) -> Catalogo:
        return Catalogo(
            id_catalogo=orm.id_catalogo,
            id_tipo_catalogo=orm.id_tipo_catalogo,
            descripcion=orm.descripcion,
        )
