from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.entities.estado_tarea import EstadoTarea
from src.domain.ports.output.estado_tarea import EstadoTareaRepositoryPort
from src.infrastructure.adapters.output.persistence.estado_tarea import EstadoTareaORM


class EstadoTareaRepository(EstadoTareaRepositoryPort):

    def __init__(self, session: Session):
        self.session = session

    def crear(self, estado_tarea: EstadoTarea) -> EstadoTarea:
        orm = EstadoTareaORM(nombre_estado=estado_tarea.nombre_estado)
        self.session.add(orm)
        self.session.commit()
        self.session.refresh(orm)
        return self._orm_a_dominio(orm)

    def obtener_por_id(self, id_estado_tarea: int) -> Optional[EstadoTarea]:
        orm = self.session.query(EstadoTareaORM).filter(
            EstadoTareaORM.id_estado_tarea == id_estado_tarea
        ).first()
        if not orm:
            return None
        return self._orm_a_dominio(orm)

    def listar(self, skip: int, limit: int) -> List[EstadoTarea]:
        orms = self.session.query(EstadoTareaORM).offset(skip).limit(limit).all()
        return [self._orm_a_dominio(orm) for orm in orms]

    def contar(self) -> int:
        return self.session.query(EstadoTareaORM).count()

    def actualizar(self, estado_tarea: EstadoTarea) -> Optional[EstadoTarea]:
        orm = self.session.query(EstadoTareaORM).filter(
            EstadoTareaORM.id_estado_tarea == estado_tarea.id_estado_tarea
        ).first()
        if not orm:
            return None
        orm.nombre_estado = estado_tarea.nombre_estado
        self.session.commit()
        self.session.refresh(orm)
        return self._orm_a_dominio(orm)

    def eliminar(self, id_estado_tarea: int) -> bool:
        orm = self.session.query(EstadoTareaORM).filter(
            EstadoTareaORM.id_estado_tarea == id_estado_tarea
        ).first()
        if not orm:
            return False
        self.session.delete(orm)
        self.session.commit()
        return True

    def _orm_a_dominio(self, orm: EstadoTareaORM) -> EstadoTarea:
        return EstadoTarea(id_estado_tarea=orm.id_estado_tarea, nombre_estado=orm.nombre_estado)
