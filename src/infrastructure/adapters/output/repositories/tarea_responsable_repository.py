from typing import Optional
from sqlalchemy.orm import Session
from src.domain.entities.tarea_responsable import TareaResponsable
from src.domain.ports.output.tarea_responsable import TareaResponsableRepositoryPort
from src.infrastructure.adapters.output.persistence.tarea_responsable import TareaResponsableORM


class TareaResponsableRepository(TareaResponsableRepositoryPort):

    def __init__(self, session: Session):
        self.session = session

    def crear(self, asociacion: TareaResponsable) -> TareaResponsable:
        orm = TareaResponsableORM(
            id_tarea=asociacion.id_tarea,
            id_responsable=asociacion.id_responsable,
            id_rol=asociacion.id_rol,
        )
        self.session.add(orm)
        self.session.commit()
        return asociacion

    def obtener(self, id_tarea: int, id_responsable: int) -> Optional[TareaResponsable]:
        orm = self.session.query(TareaResponsableORM).filter(
            TareaResponsableORM.id_tarea == id_tarea,
            TareaResponsableORM.id_responsable == id_responsable,
        ).first()
        if not orm:
            return None
        return TareaResponsable(
            id_tarea=orm.id_tarea,
            id_responsable=orm.id_responsable,
            id_rol=orm.id_rol,
        )

    def eliminar(self, id_tarea: int, id_responsable: int) -> bool:
        orm = self.session.query(TareaResponsableORM).filter(
            TareaResponsableORM.id_tarea == id_tarea,
            TareaResponsableORM.id_responsable == id_responsable,
        ).first()
        if not orm:
            return False
        self.session.delete(orm)
        self.session.commit()
        return True
