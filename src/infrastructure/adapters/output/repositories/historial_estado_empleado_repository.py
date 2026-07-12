from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.entities.historial_estado_empleado import HistorialEstadoEmpleado
from src.domain.ports.output.historial_estado_empleado import HistorialEstadoEmpleadoRepositoryPort
from src.infrastructure.adapters.output.persistence.historial_estado_empleado import HistorialEstadoEmpleadoORM


class HistorialEstadoEmpleadoRepository(HistorialEstadoEmpleadoRepositoryPort):
    """Implementación del repositorio de HistorialEstadoEmpleado."""

    def __init__(self, session: Session):
        self.session = session

    def crear(self, historial: HistorialEstadoEmpleado) -> HistorialEstadoEmpleado:
        orm = HistorialEstadoEmpleadoORM(
            id_empleado=historial.id_empleado,
            accion=historial.accion,
            id_empleado_ejecutor=historial.id_empleado_ejecutor,
            fecha=historial.fecha,
        )
        self.session.add(orm)
        self.session.commit()
        self.session.refresh(orm)
        return HistorialEstadoEmpleado(
            id_historial=orm.id_historial,
            id_empleado=orm.id_empleado,
            accion=orm.accion,
            id_empleado_ejecutor=orm.id_empleado_ejecutor,
            fecha=orm.fecha,
        )

    def listar_por_empleado(self, id_empleado: int, skip: int = 0, limit: int = 50) -> List[HistorialEstadoEmpleado]:
        orms = self.session.query(HistorialEstadoEmpleadoORM).filter(
            HistorialEstadoEmpleadoORM.id_empleado == id_empleado
        ).order_by(HistorialEstadoEmpleadoORM.fecha.desc()).offset(skip).limit(limit).all()
        return [
            HistorialEstadoEmpleado(
                id_historial=orm.id_historial,
                id_empleado=orm.id_empleado,
                accion=orm.accion,
                id_empleado_ejecutor=orm.id_empleado_ejecutor,
                fecha=orm.fecha,
            )
            for orm in orms
        ]

    def contar_por_empleado(self, id_empleado: int) -> int:
        return self.session.query(HistorialEstadoEmpleadoORM).filter(
            HistorialEstadoEmpleadoORM.id_empleado == id_empleado
        ).count()