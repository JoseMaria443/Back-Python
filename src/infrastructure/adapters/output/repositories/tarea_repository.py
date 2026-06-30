from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.entities.tarea import Tarea
from src.domain.ports.output.tarea import TareaRepositoryPort
from src.infrastructure.adapters.output.persistence.tarea import TareaORM


class TareaRepository(TareaRepositoryPort):

    def __init__(self, session: Session):
        self.session = session

    def crear(self, tarea: Tarea) -> Tarea:
        orm = TareaORM(
            id_comunicado=tarea.id_comunicado,
            descripcion=tarea.descripcion,
            fecha_entrega=tarea.fecha_entrega,
            fecha_registro=tarea.fecha_registro,
            id_estado_tarea=tarea.id_estado_tarea,
        )
        self.session.add(orm)
        self.session.commit()
        self.session.refresh(orm)
        return self._orm_a_dominio(orm)

    def obtener_por_id(self, id_tarea: int) -> Optional[Tarea]:
        orm = self.session.query(TareaORM).filter(
            TareaORM.id_tarea == id_tarea
        ).first()
        if not orm:
            return None
        return self._orm_a_dominio(orm)

    def listar(self, skip: int, limit: int) -> List[Tarea]:
        orms = self.session.query(TareaORM).offset(skip).limit(limit).all()
        return [self._orm_a_dominio(orm) for orm in orms]

    def contar(self) -> int:
        return self.session.query(TareaORM).count()

    def actualizar(self, tarea: Tarea) -> Optional[Tarea]:
        orm = self.session.query(TareaORM).filter(
            TareaORM.id_tarea == tarea.id_tarea
        ).first()
        if not orm:
            return None
        orm.id_comunicado = tarea.id_comunicado
        orm.descripcion = tarea.descripcion
        orm.fecha_entrega = tarea.fecha_entrega
        orm.fecha_registro = tarea.fecha_registro
        orm.id_estado_tarea = tarea.id_estado_tarea
        self.session.commit()
        self.session.refresh(orm)
        return self._orm_a_dominio(orm)

    def eliminar(self, id_tarea: int) -> bool:
        orm = self.session.query(TareaORM).filter(
            TareaORM.id_tarea == id_tarea
        ).first()
        if not orm:
            return False
        self.session.delete(orm)
        self.session.commit()
        return True

    def _orm_a_dominio(self, orm: TareaORM) -> Tarea:
        return Tarea(
            id_tarea=orm.id_tarea,
            id_comunicado=orm.id_comunicado,
            descripcion=orm.descripcion,
            fecha_entrega=orm.fecha_entrega,
            fecha_registro=orm.fecha_registro,
            id_estado_tarea=orm.id_estado_tarea,
        )
