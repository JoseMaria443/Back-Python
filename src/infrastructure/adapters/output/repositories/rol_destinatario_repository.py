from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.entities.rol_destinatario import RolDestinatario
from src.domain.ports.output.rol_destinatario import RolDestinatarioRepositoryPort
from src.infrastructure.adapters.output.persistence.rol_destinatario import RolDestinatarioORM


class RolDestinatarioRepository(RolDestinatarioRepositoryPort):

    def __init__(self, session: Session):
        self.session = session

    def crear(self, rol_destinatario: RolDestinatario) -> RolDestinatario:
        orm = RolDestinatarioORM(descripcion=rol_destinatario.descripcion)
        self.session.add(orm)
        self.session.commit()
        self.session.refresh(orm)
        return self._orm_a_dominio(orm)

    def obtener_por_id(self, id_rol: int) -> Optional[RolDestinatario]:
        orm = self.session.query(RolDestinatarioORM).filter(
            RolDestinatarioORM.id_rol == id_rol
        ).first()
        if not orm:
            return None
        return self._orm_a_dominio(orm)

    def listar(self, skip: int, limit: int) -> List[RolDestinatario]:
        orms = self.session.query(RolDestinatarioORM).offset(skip).limit(limit).all()
        return [self._orm_a_dominio(orm) for orm in orms]

    def contar(self) -> int:
        return self.session.query(RolDestinatarioORM).count()

    def actualizar(self, rol_destinatario: RolDestinatario) -> Optional[RolDestinatario]:
        orm = self.session.query(RolDestinatarioORM).filter(
            RolDestinatarioORM.id_rol == rol_destinatario.id_rol
        ).first()
        if not orm:
            return None
        orm.descripcion = rol_destinatario.descripcion
        self.session.commit()
        self.session.refresh(orm)
        return self._orm_a_dominio(orm)

    def eliminar(self, id_rol: int) -> bool:
        orm = self.session.query(RolDestinatarioORM).filter(
            RolDestinatarioORM.id_rol == id_rol
        ).first()
        if not orm:
            return False
        self.session.delete(orm)
        self.session.commit()
        return True

    def _orm_a_dominio(self, orm: RolDestinatarioORM) -> RolDestinatario:
        return RolDestinatario(id_rol=orm.id_rol, descripcion=orm.descripcion)
