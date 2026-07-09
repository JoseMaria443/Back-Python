from typing import List, Optional
from sqlalchemy.orm import Session

from src.domain.entities.estado import Estado
from src.domain.ports.output.estado import EstadoRepositoryPort
from src.infrastructure.adapters.output.persistence.estado import EstadoORM


class EstadoRepository(EstadoRepositoryPort):

    def __init__(self, session: Session):
        self.session = session

    def crear(self, estado: Estado) -> Estado:
        orm = EstadoORM(nombre_estado=estado.nombre_estado)
        self.session.add(orm)
        self.session.commit()
        self.session.refresh(orm)
        return Estado(
            id_estado=orm.id_estado,
            nombre_estado=orm.nombre_estado,
        )

    def obtener_por_id(self, id_estado: int) -> Optional[Estado]:
        orm = self.session.query(EstadoORM).filter(
            EstadoORM.id_estado == id_estado
        ).first()
        if not orm:
            return None
        return Estado(
            id_estado=orm.id_estado,
            nombre_estado=orm.nombre_estado,
        )

    def listar(self, skip: int, limit: int) -> List[Estado]:
        orms = self.session.query(EstadoORM).offset(skip).limit(limit).all()
        return [
            Estado(
                id_estado=orm.id_estado,
                nombre_estado=orm.nombre_estado,
            )
            for orm in orms
        ]

    def contar(self) -> int:
        return self.session.query(EstadoORM).count()

    def actualizar(self, estado: Estado) -> Optional[Estado]:
        orm = self.session.query(EstadoORM).filter(
            EstadoORM.id_estado == estado.id_estado
        ).first()
        if not orm:
            return None
        orm.nombre_estado = estado.nombre_estado
        self.session.commit()
        self.session.refresh(orm)
        return Estado(
            id_estado=orm.id_estado,
            nombre_estado=orm.nombre_estado,
        )

    def eliminar(self, id_estado: int) -> bool:
        orm = self.session.query(EstadoORM).filter(
            EstadoORM.id_estado == id_estado
        ).first()
        if not orm:
            return False
        self.session.delete(orm)
        self.session.commit()
        return True