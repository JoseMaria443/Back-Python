from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.entities.rol_responsable import RolResponsable
from src.domain.ports.output.rol_responsable import RolResponsableRepositoryPort
from src.infrastructure.adapters.output.persistence.rol_responsable import RolResponsableORM


class RolResponsableRepository(RolResponsableRepositoryPort):

    def __init__(self, session: Session):
        self.session = session

    def crear(self, rol_responsable: RolResponsable) -> RolResponsable:
        orm = RolResponsableORM(descripcion_rol=rol_responsable.descripcion_rol)
        self.session.add(orm)
        self.session.commit()
        self.session.refresh(orm)
        return self._orm_a_dominio(orm)

    def obtener_por_id(self, id_rol: int) -> Optional[RolResponsable]:
        orm = self.session.query(RolResponsableORM).filter(
            RolResponsableORM.id_rol == id_rol
        ).first()
        if not orm:
            return None
        return self._orm_a_dominio(orm)

    def listar(self, skip: int, limit: int) -> List[RolResponsable]:
        orms = self.session.query(RolResponsableORM).offset(skip).limit(limit).all()
        return [self._orm_a_dominio(orm) for orm in orms]

    def contar(self) -> int:
        return self.session.query(RolResponsableORM).count()

    def actualizar(self, rol_responsable: RolResponsable) -> Optional[RolResponsable]:
        orm = self.session.query(RolResponsableORM).filter(
            RolResponsableORM.id_rol == rol_responsable.id_rol
        ).first()
        if not orm:
            return None
        orm.descripcion_rol = rol_responsable.descripcion_rol
        self.session.commit()
        self.session.refresh(orm)
        return self._orm_a_dominio(orm)

    def eliminar(self, id_rol: int) -> bool:
        orm = self.session.query(RolResponsableORM).filter(
            RolResponsableORM.id_rol == id_rol
        ).first()
        if not orm:
            return False
        self.session.delete(orm)
        self.session.commit()
        return True

    def _orm_a_dominio(self, orm: RolResponsableORM) -> RolResponsable:
        return RolResponsable(id_rol=orm.id_rol, descripcion_rol=orm.descripcion_rol)
